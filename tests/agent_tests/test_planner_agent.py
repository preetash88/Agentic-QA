from src.agents.planner_agent import generate_test_plan


def test_planner_agent():

    story= """
    As as user,
    I want to login using email and password,
    so that I can access my dashboard.
    """

    result = generate_test_plan(story)

    print(result)

    assert result is not None
    assert len(result) > 0