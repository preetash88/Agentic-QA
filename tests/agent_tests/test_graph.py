from src.agents import workflow


def test_graph():
    result = workflow.invoke({
        "requirement": """
        As a user,
        I want to login using email and password
        so that I can access my dashboard.
        """
    })
    print(result["planner_output"])

    print(result["api_output"])

    print(result["ui_output"])

    print(result["security_output"])

    print(result["performance_output"])
