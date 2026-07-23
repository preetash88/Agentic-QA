from src.orchestration.workflow import AgentWorkflow
from fastapi import Request


def get_workflow(request: Request) -> AgentWorkflow:
    return request.app.state.workflow
