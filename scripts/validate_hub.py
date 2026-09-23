#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_json(path):
    with (ROOT / path).open("r", encoding="utf-8") as f:
        return json.load(f)

def require_file(path):
    p = ROOT / path
    assert p.is_file(), f"missing required file: {path}"
    assert p.stat().st_size > 0, f"required file is empty: {path}"
    return p

def main():
    required = [
        "README.md",
        "AGENTS.md",
        "RAILWAY_HUB_RULES.md",
        "registry/apps.json",
        "registry/resources.json",
        "registry/api-registry.json",
        "templates/NEW_APP_CHECKLIST.md",
        "templates/DEPLOYMENT_CHECKLIST.md",
        "docs/architecture.md",
        "docs/recovery.md",
        "changes/CHANGELOG.md",
    ]
    for path in required:
        require_file(path)

    readme = require_file("README.md").read_text(encoding="utf-8")
    rules = require_file("RAILWAY_HUB_RULES.md").read_text(encoding="utf-8")
    agents = require_file("AGENTS.md").read_text(encoding="utf-8")

    for phrase in [
        "READ THIS BEFORE ANY RAILWAY WRITE",
        "Treat every registered application as if it belongs to a different customer",
        "No documentation = no Railway project creation",
        "READ THAT APP'S OWN README + AGENTS.md + RAILWAY_HUB_RULES.md",
        "Immutable Safety Invariants",
        "No single artifact automatically overrides another",
        "Current governance version: v1.0 — frozen",
    ]:
        assert phrase in readme, f"README hard-gate phrase missing: {phrase}"

    assert "No new application Railway project may be created until:" in rules
    assert "Immutable Safety Invariants" in rules
    assert "Reconciliation Rule" in rules
    assert "Governance Freeze" in rules
    assert "Before any Railway write:" in agents
    assert "Registry / Live-State Mismatch" in agents
    assert "Governance v1.0 freeze" in agents

    apps_doc = load_json("registry/apps.json")
    resources = load_json("registry/resources.json")
    api_registry = load_json("registry/api-registry.json")

    assert apps_doc.get("governance_version") == "1.0", "governance_version must be 1.0"
    assert apps_doc.get("governance_status") == "frozen", "governance_status must be frozen"
    assert apps_doc.get("reconciliation_policy"), "reconciliation policy missing"

    hub_project = apps_doc.get("railway_hub_runtime_project") or {}
    assert hub_project.get("status") in {"not_provisioned", "active"}, "invalid Hub Railway project status"
    if hub_project.get("status") == "active":
        assert hub_project.get("name") == "Railway Project Hub", "active governance project must use canonical name"
        assert hub_project.get("id"), "active governance project missing project id"
        assert hub_project.get("application_runtime_allowed") is False, "Hub project must forbid app runtime"
        assert hub_project.get("expected_runtime_service_count") == 0, "Hub project expected runtime service count must be zero"
        assert hub_project.get("registry_marker_services_allowed") is True, "Hub project must explicitly govern registry marker services"

    apps = apps_doc["apps"]
    assert apps, "at least one registered app is required"

    numbers = [a["app_number"] for a in apps]
    slugs = [a["slug"] for a in apps]
    assert len(numbers) == len(set(numbers)), "duplicate app_number"
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    assert apps_doc["next_app_number"] > max(numbers), "next_app_number must exceed all registered apps"

    by_slug = {a["slug"]: a for a in apps}
    canonical_services = {}

    for app in apps:
        for field in ["app_number", "slug", "display_name", "status", "repository", "governance_doc"]:
            assert app.get(field) not in (None, ""), f"{app.get('slug', '<unknown>')} missing {field}"

        gov = require_file(app["governance_doc"]).read_text(encoding="utf-8")
        assert app["display_name"] in gov, f"{app['slug']} governance doc does not name the app"
        assert app["repository"] in gov, f"{app['slug']} governance doc does not name its repository"

        assert app["status"] in {"planned", "active", "archived", "deprecated", "retired"}, f"invalid app status: {app['status']}"

        if app["status"] == "active":
            rp = app.get("railway_project") or {}
            env = rp.get("environment") or {}
            assert rp.get("name") and rp.get("id"), f"{app['slug']} active app missing Railway project identity"
            assert env.get("name") and env.get("id"), f"{app['slug']} active app missing environment identity"
            services = app.get("canonical_services") or []
            assert services, f"{app['slug']} active app must register at least one canonical service"
            for service in services:
                assert service not in canonical_services, f"canonical service registered to multiple apps: {service}"
                canonical_services[service] = app["slug"]

        if app["status"] in {"archived", "retired"}:
            assert not app.get("canonical_services"), f"{app['slug']} archived/retired app must not claim canonical services"
            assert not app.get("railway_project"), f"{app['slug']} archived/retired app must not claim an active Railway project"

        assert isinstance(app.get("cross_app_dependencies", []), list)
        assert isinstance(app.get("shared_resources", []), list)

    resource_projects = resources.get("projects", [])
    resource_services = resources.get("services", [])
    governance_projects = resources.get("governance_projects", [])

    if hub_project.get("status") == "active":
        matches = [p for p in governance_projects if p.get("project_id") == hub_project.get("id")]
        assert len(matches) == 1, "active Hub Railway project must appear exactly once in resources.governance_projects"
        gp = matches[0]
        assert gp.get("application_runtime_allowed") is False, "governance project must forbid app runtime"
        assert gp.get("expected_runtime_service_count") == 0, "governance project expected runtime service count must be zero"
        assert gp.get("registry_marker_services_allowed") is True, "governance project marker policy missing"
        active_app_project_ids = {p.get("project_id") for p in resource_projects}
        assert gp.get("project_id") not in active_app_project_ids, "governance project cannot also be an active app project"

    for marker in resources.get("planned_governance_markers", []):
        assert marker.get("status") == "planned", "planned marker must have planned status"
        assert marker.get("marker_only") is True, "planned governance marker must be marker_only"
        assert marker.get("runtime_allowed") is False, "planned governance marker must forbid runtime"
        assert marker.get("owner_app") in by_slug, "planned marker references unknown app"
        assert marker.get("service_name"), "planned marker missing service name"

    for marker in resources.get("governance_marker_services", []):
        assert marker.get("marker_only") is True, "governance marker must be marker_only"
        assert marker.get("runtime_allowed") is False, "governance marker must forbid runtime"
        assert marker.get("owner_app") in by_slug, "governance marker references unknown app"
        assert marker.get("service_id"), "verified governance marker missing service id"
        assert marker.get("source_attached") is False, "governance marker cannot have a source"
        assert marker.get("deployment_present") is False, "governance marker cannot have a deployment"
        assert marker.get("domain_present") is False, "governance marker cannot have a domain"
        assert marker.get("custom_variable_names") == [], "governance marker cannot have custom variables"

    for project in resource_projects:
        assert project["owner_app"] in by_slug, f"unknown project owner_app: {project['owner_app']}"
        assert project.get("canonical") is True, "projects registry should contain canonical active projects only"

    seen_service_names = set()
    for service in resource_services:
        owner = service["owner_app"]
        name = service["service_name"]
        assert owner in by_slug, f"unknown service owner_app: {owner}"
        assert service.get("canonical") is True, f"active services list contains non-canonical service: {name}"
        assert name not in seen_service_names, f"duplicate canonical service entry: {name}"
        seen_service_names.add(name)
        assert canonical_services.get(name) == owner, f"service ownership mismatch for {name}"

    assert set(canonical_services) == seen_service_names, "apps.json canonical_services and resources.json services differ"

    for residue in resources.get("migration_residue", []):
        assert residue.get("canonical") is False, "migration residue must never be canonical"
        assert residue.get("status") in {"removed_verified", "do_not_touch_until_cleanup_approved"}, "invalid residue status"

    for api in api_registry.get("apis", []):
        assert api["used_by_app"] in by_slug, f"API references unknown app: {api['used_by_app']}"
        assert "credential_variable_name" in api, "API entry missing credential variable name"
        assert "value" not in api, "API registry must never store secret values"

    print(f"Hub validation passed: {len(apps)} apps, {len(resource_services)} canonical services.")

if __name__ == "__main__":
    main()
