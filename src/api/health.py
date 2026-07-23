from fastapi import APIRouter

from src.infra.infra_manager import InfraManager

router = APIRouter(tags=['Health'])


def dependency_status(obj):
    return "UP" if obj else "DOWN"


@router.get('/health')
async def health():
    return {
        "status": "UP",
        "dependencies": {
            "kafka": dependency_status(InfraManager.kafka()),
            "redis": dependency_status(InfraManager.redis()),
            "qdrant": dependency_status(InfraManager.qdrant())
        }
    }
