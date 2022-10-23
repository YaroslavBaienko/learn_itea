import json

import requests
import sys


def search(title):
    url = "http://archive.org/advancedsearch.php"
    params = {"q": f"title:({title})",
              "output": "json",
              "fields": "identifier,title",
              "rows": 50,
              "page": 1, }
    resp = requests.get(url, params=params)
    return resp.json()


if __name__ == "__main__":
    title = sys.argv[1]
    data = search(title)
    docs = data["response"]["docs"]
    print(f"Found {len(docs)} items, showing first 50")
    print("identifier\ttitle")
    for row in docs[:50]:
        print(row["identifier"], row["title"], sep="\t")
