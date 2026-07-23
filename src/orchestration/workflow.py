from src.monitoring.metrics import workflow_failed
from src.observability.langsmith import tracer
from src.orchestration.builder import build_graph
from src.monitoring.metrics import workflow_total
from src.messaging.event_bus import event_bus
from src.messaging.topics import WORKFLOW_EVENTS


class AgentWorkflow:
    def __init__(self):
        self.graph = build_graph()

    def execute(self, requirement: str):
        tracer.annotate("workflow_execute", {
            "requirement": requirement,
        })

        workflow_total.inc()

        event_bus.publish(WORKFLOW_EVENTS, {
            "event": "started",
            "requirement": requirement,
        })

        try:
            result = self.graph.invoke({
                "requirement": requirement,
            })
            event_bus.publish(WORKFLOW_EVENTS, {
                "event": "completed",
                "result": result,
            }, )

            return result
        except Exception as e:
            workflow_failed.inc()

            event_bus.publish(
                WORKFLOW_EVENTS,
                {
                    "event": "failed",
                    "requirement": requirement,
                    "error": str(e),
                }, )
            raise