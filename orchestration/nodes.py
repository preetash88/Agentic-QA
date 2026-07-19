from agents.api_agent import generate_api_tests
from agents.performance_analysis_agent import analyze_performance
from agents.planner_agent import generate_test_plan
from agents.security_analysis_agent import analyze_security
from agents.ui_agent import generate_ui_tests
from orchestration.state import WorkflowState


def planner_node(state: WorkflowState):
    state["test_plan"] = generate_test_plan(state["requirement"])

    return state


def api_node(state: WorkflowState):
    state["api_tests"] = generate_api_tests(state["test_plan"])
    return state


def ui_node(state: WorkflowState):
    state["ui_tests"] = generate_ui_tests(state["test_plan"])
    return state


def security_node(state: WorkflowState):
    state["security_report"] = analyze_security(state["test_plan"])
    return state


# def performance_node(state: WorkflowState):
#     state["performance_report"] = analyze_performance()
#     return state
