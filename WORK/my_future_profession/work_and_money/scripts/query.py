import json
import pathlib
import requests

# SPARQL-запрос к WikiData: берём ключевые понятия блока «Работа и деньги»
QUERY = """
SELECT ?item ?itemLabel ?description WHERE {
  VALUES ?item {
    wd:Q268378    # труд
    wd:Q2266417    # занятость
    wd:Q6821213    # заработная плата
    wd:Q282049    # карьера
    wd:Q950511    # резюме
    wd:Q850171    # собеседование
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
        "project": "Я и будущая профессия: Работа и деньги",
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
