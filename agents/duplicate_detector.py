from agents.gtihub_similarity_agent import find_duplicates


def detect_duplicates(report):
    query = f"""
    {report.root_cause}

    {report.failure_category}

    {report.probable_owner}
    """

    results = find_duplicates(query)

    duplicates = []

    for item in results.content:
        text = item.text

        if "JWT" in text:
            duplicates.append(text)

    report.github_duplicates = duplicates
    report.is_duplicate = len(duplicates) > 0

    return report