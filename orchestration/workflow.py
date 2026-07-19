from orchestration.builder import build_graph


class AgentWorkflow:
    def __init__(self):
        self.graph = build_graph()

    def execute(self, requirement: str):
        return self.graph.invoke({
            "requirement": requirement,
        })
