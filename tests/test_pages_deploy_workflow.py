from pathlib import Path

import yaml


DEPLOY_WORKFLOW = Path(".github/workflows/deploy-pages.yml")


def test_pages_workflow_requests_oidc_permissions():
    workflow = yaml.safe_load(DEPLOY_WORKFLOW.read_text(encoding="utf-8")) or {}
    permissions = workflow.get("permissions") or {}

    assert permissions.get("pages") == "write"
    assert permissions.get("id-token") == "write"


def test_pages_workflow_deploys_docs_with_deploy_pages_action():
    workflow = yaml.safe_load(DEPLOY_WORKFLOW.read_text(encoding="utf-8")) or {}
    jobs = workflow.get("jobs") or {}
    deploy = jobs.get("deploy") or {}
    steps = deploy.get("steps") or []

    assert any(step.get("uses") == "actions/upload-pages-artifact@v4" for step in steps)
    assert any(
        step.get("uses") == "actions/upload-pages-artifact@v4" and (step.get("with") or {}).get("path") == "docs"
        for step in steps
    )
    assert any(step.get("uses") == "actions/deploy-pages@v5" for step in steps)
