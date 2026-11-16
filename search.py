# 외부 검색 기능을 담당한다.
import requests


def search_web(query: str, max_results: int = 5) -> list[dict]:
    response = requests.get(
        "https://ko.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "generator": "search",
            "gsrsearch": query,
            "gsrlimit": max_results,
            "gsrnamespace": 0,
            "prop": "extracts|info",
            "exintro": 1,
            "explaintext": 1,
            "inprop": "url",
            "format": "json",
            "formatversion": 2,
        },
        headers={
            "User-Agent": "AnswerCheckingAPI/0.1 (Educational Project)"
        },
        timeout=20,
    )

    response.raise_for_status()

    data = response.json()

    if "error" in data:
        raise ValueError("Search API error")

    pages = data.get("query", {}).get("pages", [])

    return [
        {
            "id": index,
            "title": page["title"],
            "url": page["fullurl"],
            "content": page["extract"][:3000],
        }
        for index, page in enumerate(pages, start=1)
        if page.get("extract") and page.get("fullurl")
    ]


if __name__ == "__main__":
    from pprint import pprint

    pprint(search_web("목성"))
