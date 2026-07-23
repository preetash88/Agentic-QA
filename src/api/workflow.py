from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.api.dependencies import get_workflow
from src.orchestration.workflow import AgentWorkflow
from src.services.workflow_service import WorkflowService

router = APIRouter(tags=["Workflow"])


class WorkflowRequest(BaseModel):
    requirement: str


@router.post("/execute-workflow")
async def execute(
        request: WorkflowRequest,
        workflow: AgentWorkflow = Depends(get_workflow)
):
    result = await WorkflowService.execute(workflow, request.requirement)
    return {
        "status": "completed",
        "result": result
    }
