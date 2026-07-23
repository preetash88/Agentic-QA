from src.agents.performance_agent import generate_performance_tests
from src.agents.api_agent import generate_api_tests
from src.agents.planner_agent import generate_test_plan
from src.agents.security_agent import generate_security_tests
from src.agents.ui_agent import generate_ui_tests
from src.messaging.event_bus import event_bus
from src.messaging.topics import AGENT_EVENTS
from src.observability.langsmith import tracer
from src.orchestration.state import WorkflowState


def planner_node(state: WorkflowState):
    test_plan = tracer.wrap(
        "planner_agent",
        generate_test_plan,
        state["requirement"],
    )

    event_bus.publish(
        AGENT_EVENTS,
        {
            "agent": "planner",
            "status": "completed",
            "requirement": state["requirement"],
            "test_plan": test_plan.model_dump(),
        }
    )

    return {
        "test_plan": test_plan
    }


def api_node(state: WorkflowState):
    api_tests = tracer.wrap(
        "api_agent",
        generate_api_tests,
        state["test_plan"],
    )

    event_bus.publish(
        AGENT_EVENTS,
        {
            "agent": "api",
            "status": "completed",
            "requirement": state["requirement"],
            "api_tests": api_tests
        }
    )

    return {
        "api_tests": api_tests
    }


def ui_node(state: WorkflowState):
    ui_tests = tracer.wrap(
        "ui_agent",
        generate_ui_tests,
        state["test_plan"],
    )
    event_bus.publish(
        AGENT_EVENTS, {
            "agent": "ui",
            "status": "completed",
            "requirement": state["requirement"],
            "ui_tests": ui_tests
        }
    )

    return {
        "ui_tests": ui_tests
    }


def security_node(state: WorkflowState):
    security_tests = tracer.wrap(
        "security_agent",
        generate_security_tests,
        state["test_plan"],
    )
    event_bus.publish(
        AGENT_EVENTS,
        {
            "agent": "security",
            "status": "completed",
            "requirement": state["requirement"],
            "security_tests": security_tests
        }
    )
    return {
        "security_tests": security_tests
    }


def performance_node(state: WorkflowState):
    performance_tests = tracer.wrap(
        "performance_agent",
        generate_performance_tests,
        state["test_plan"],
    )
    event_bus.publish(
        AGENT_EVENTS,
        {
            "agent": "performance",
            "status": "completed",
            "requirement": state["requirement"],
            "performance_tests": performance_tests
        }
    )

    return {
        "performance_tests": performance_tests
    }
