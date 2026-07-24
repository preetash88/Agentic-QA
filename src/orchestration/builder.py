from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.orchestration.nodes import planner_node, api_node, security_node, ui_node
from src.orchestration.state import WorkflowState


def build_graph():
    graph = StateGraph(WorkflowState)

    graph.add_node("planner", planner_node)
    graph.add_node("api", api_node)
    graph.add_node("ui", ui_node)
    graph.add_node("security", security_node)
    # graph.add_node("performance", performance_node)

    graph.add_edge(START, "planner")

    graph.add_edge("planner", "api")
    graph.add_edge("planner", "ui")
    graph.add_edge("planner", "security")
    # graph.add_edge("planner", "performance")

    graph.add_edge("api", END)
    graph.add_edge("ui", END)
    graph.add_edge("security", END)
    # graph.add_edge("performance", END)

    return graph.compile()
