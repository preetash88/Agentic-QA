from pydantic import BaseModel, Field


class TestPlan(BaseModel):
    positive_scenarios: list[str] = Field(default_factory=list)
    negative_scenarios: list[str] = Field(default_factory=list)
    edge_cases: list[str] = Field(default_factory=list)

    api_test_ideas: list[str] = Field(default_factory=list)
    ui_test_ideas: list[str] = Field(default_factory=list)

    security_test_ideas: list[str] = Field(default_factory=list)
    performance_test_ideas: list[str] = Field(default_factory=list)


class BugReport(BaseModel):
    severity: str = Field(description="Critical, High, Medium or Low")
    probable_owner: str = Field(description="Owner responsible")
    owning_team: str = Field(description="Team or component responsible")
    root_cause: str
    failure_category: str = Field(
        description="Authentication, UI, API, Infrastructure, Performance, Network, Test Data etc")
    confidence_score: float = Field(
        ge=0,
        le=100,
        description="Confidence percentage between 0 and 100"
    )
    next_steps: list[str]
    similar_incidents: list[str] = Field(default_factory=list)
    recommended_runbooks: list[str] = Field(default_factory=list)
    github_duplicates: list[str] = Field(default_factory=list)
    is_duplicate: bool = False


class GithubIssue(BaseModel):
    title: str
    body: str
    labels: list[str] = []
    assignees: list[str] = []


class UITriageReport(BaseModel):
    root_cause: str
    probable_owner: str
    confidence_score: int


class SecurityFinding(BaseModel):
    severity: str
    category: str
    description: str
    recommendation: str


class SecurityReport(BaseModel):
    findings: list[SecurityFinding]
    risk_score: int
    summary: str


class PerformanceFinding(BaseModel):
    severity: str
    metric: str
    observation: str
    recommendation: str


class PerformanceReport(BaseModel):
    findings: list[PerformanceFinding]
    bottlenecks: list[str]
    summary: str
