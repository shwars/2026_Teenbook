import json
import pathlib
import requests

# SPARQL-запрос к WikiData: берём ключевые понятия блока «Профессии будущего»
QUERY = """
SELECT ?item ?itemLabel ?description WHERE {
  VALUES ?item {
    wd:Q3908516    # предпринимательство
    wd:Q215279    # фрилансер
    wd:Q11660    # искусственный интеллект
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru,en". }
  OPTIONAL {
    ?item schema:description ?description .
    FILTER(LANG(?description) = "ru")
  }
}
"""

URL = "https://query.wikidata.org/sparql"


def run_query(query: str) -> dict:
    headers = {
        "Accept": "application/sparql-results+json",
        "User-Agent": "teenbook (educational project)",
    }
    resp = requests.get(URL, params={"query": query, "format": "json"},
                        headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def convert(data: dict) -> dict:
    concepts = []
    for b in data["results"]["bindings"]:
        concepts.append({
            "concept": b["item"]["value"],
            "conceptLabel": b["itemLabel"]["value"],
            "description": b.get("description", {}).get("value", ""),
        })
    return {
        "project": "Я и будущая профессия: Профессии будущего",
        "source": "WikiData SPARQL endpoint",
        "concepts": concepts,
    }


def main() -> None:
    out = pathlib.Path(__file__).resolve().parent.parent / "data" / "wikidata_export.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = convert(run_query(QUERY))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Готово: {out}")


if __name__ == "__main__":
    main()
