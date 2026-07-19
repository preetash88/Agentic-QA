from orchestration.workflow import AgentWorkflow


def test_workflow():
    workflow = AgentWorkflow()

    result = workflow.execute(f"""
    User logs into application using email and password.
""")
    assert result["test_plan"] is not None
    assert result["api_tests"] is not None
    assert result["ui_tests"] is not None
    assert result["security_report"] is not None
