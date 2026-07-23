from typing import TypedDict

from src.agents.models import TestPlan, SecurityReport, PerformanceReport, BugReport


class WorkflowState(TypedDict, total=False):
    requirement: str
    test_plan: TestPlan
    api_tests: str
    ui_tests: str
    security_report: SecurityReport
    performance_report: PerformanceReport
    bug_report: BugReport
    evaluation: dict
    errors: list[str]
