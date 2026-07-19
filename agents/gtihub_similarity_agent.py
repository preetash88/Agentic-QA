import asyncio

from mcp_integration.github_search import search_issues


def find_duplicates(query: str):
    result = asyncio.run(
        search_issues(
            owner="preetash88",
            repo="github-mcp-test",
            query=query,
        )
    )

    if result.isError:
        return []

    duplicates = []

    for item in result.content:
        duplicates.append(item.text[:500])

    return duplicates
