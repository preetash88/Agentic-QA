from fastapi.concurrency import run_in_threadpool

from src.orchestration.workflow import AgentWorkflow


class WorkflowService:

    @staticmethod
    async def execute(
            workflow: AgentWorkflow,
            requirement: str
    ):
        return await run_in_threadpool(
            workflow.execute,
        requirement
        )
