from agents.models import BugReport, GithubIssue

TEAM_ASSIGNEES = {
    "backend-auth": ["preetash88"],
    "frontend-ui": ["frontend-lead"],
    "payments": ["payments-lead"],
    "search": ["search-lead"],
    "security": ["security-lead"],
    "platform": ["platform-lead"],
}

MAX_BODY_LENGTH = 50000


def get_assignees(bug_report: BugReport) -> list[str]:
    return TEAM_ASSIGNEES.get(bug_report.owning_team.lower(), [])


def bug_report_github_issue(report: BugReport) -> GithubIssue:
    assignees = get_assignees(report)

    body = f"""
    ## Root Cause
    {report.root_cause}

    ## Probable Owner
    {report.probable_owner}

    ## Confidence Score
    {report.confidence_score}%
    
    # Similar Incidents
    {"\n".join(f"- {incident}" for incident in report.similar_incidents[:10])}

    ## Recommended Runbooks
    {"\n".join(f"- {runbook}" for runbook in report.recommended_runbooks[:10])}    
    
    # Next Steps
    {"\n".join(f"- {step}" for step in report.next_steps[:10])}
    
    ## Github Duplicates
    {"\n".join(f"- {issue}" for issue in report.github_duplicates[:10])}
    """

    if len(body) > MAX_BODY_LENGTH:
        body = body[:MAX_BODY_LENGTH]

    return GithubIssue(
        title=f"[{report.severity}] {report.failure_category}",
        body=body,
        labels=[
            report.severity.lower(),
            report.failure_category.lower().replace(" ", "-")
        ],
        assignees=assignees
    )
