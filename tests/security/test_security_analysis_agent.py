import requests

from agents.security_analysis_agent import analyze_security


def test_security_analysis():
    response = requests.get("https://reqres.in/api/users/2")

    report = analyze_security(
        url=response.url,
        headers=dict(response.headers),
        response_body=response.text,
        cookies=response.cookies.get_dict()
    )
    print(
        report.model_dump_json(
            indent=4
        )
    )

    assert report.risk_score >= 0
