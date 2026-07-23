TEAM_MAP = {
    "authentication": "identity-team",
    "payments": "payments-team",
    "checkout": "checkout-team",
    "search": "search-team",
}

def get_assignee(report):
    owner = report.owning_team.lower()

    return TEAM_MAP.get(
        owner,
        None
    )