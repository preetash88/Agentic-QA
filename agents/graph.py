from typing import TypedDict

from langgraph.constants import END
from langgraph.graph import StateGraph

from agents.api_agent import generate_api_tests
from agents.models import TestPlan
from agents.performance_agent import generate_performance_tests
from agents.planner_agent import generate_test_plan
from agents.security_agent import generate_security_tests
from agents.ui_agent import generate_ui_tests


class AgentState(TypedDict):
    requirement: str
    planner_output: TestPlan
    api_output: str
    ui_output: str
    security_output: str
    performance_output: str


def planner_node(state: AgentState):
    return {
        "planner_output": generate_test_plan(state["requirement"])
    }


def api_node(state: AgentState):
    return {
        "api_output": generate_api_tests(state["planner_output"].api_test_ideas)
    }


def ui_node(state: AgentState):
    return {
        "ui_output": generate_ui_tests(state["planner_output"].ui_test_ideas)
    }


def security_node(state: AgentState):
    return {
        "security_output": generate_security_tests(state["planner_output"].security_test_ideas)
    }


def performance_node(state: AgentState):
    return {
        "performance_output": generate_performance_tests(state["planner_output"].performance_test_ideas)
    }


graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("api", api_node)
graph.add_node("ui", ui_node)
graph.add_node("security", security_node)
graph.add_node("performance_tests", performance_node)

graph.set_entry_point("planner")
graph.add_edge("planner", "api")
graph.add_edge("planner", "ui")
graph.add_edge("planner", "security")
graph.add_edge("planner", "performance_tests")

graph.add_edge("api", END)
graph.add_edge("ui", END)
graph.add_edge("security", END)
graph.add_edge("performance_tests", END)

workflow = graph.compile()
