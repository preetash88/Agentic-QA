from agents.performance_analysis_agent import analyze_performance


def test_performance_analysis():
    with open("performance/results.txt", encoding="utf-16") as file:
        results = file.read()

    report = analyze_performance(results)

    print(report.model_dump_json(indent=4))

    assert len(report.findings) > 0
