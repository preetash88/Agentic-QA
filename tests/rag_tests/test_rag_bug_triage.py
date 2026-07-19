from agents.bug_triage_agent import analyze_failure


def test_rag_bug_triage():
    report = analyze_failure(
        logs="""
        JWT validation failed.
        Token expired.
        Authentication service returned 401.
        """,
        console_logs=None,
        playwright_error="""
        locator("#dashboard")
        timeout 30000ms exceeded
        """
    )

    print(report.model_dump_json(indent=4))

    assert report.root_cause is not None
