import json
import pathlib
import requests


QUERY = """
SELECT ?item ?itemLabel ?description WHERE {
  VALUES ?item {
    wd:Q13649246    # неизвестность 
    wd:Q44619       # страх 
    wd:Q154430      # тревога 
    wd:Q18614415    # избегание 
    wd:Q58998540    # личный рост 
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
    "User-Agent": "teenbook (educational project)"
  }

  response = requests.get(
    URL,
    params={"query": query, "format": "json"},
    headers=headers,
    timeout=30,
  )
  response.raise_for_status()
  return response.json()


def save_result(data: dict, output_path: pathlib.Path) -> None:
  output_path.parent.mkdir(parents=True, exist_ok=True)
  with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


def convert_format(data: dict, project_name: str) -> dict:
  concepts = []
  for binding in data["results"]["bindings"]:
    concepts.append({
      "concept": binding["item"]["value"],
      "conceptLabel": binding["itemLabel"]["value"],
      "description": binding.get("description", {}).get("value", "")
    })

  return {
    "project": project_name,
    "source": "WikiData SPARQL endpoint",
    "concepts": concepts
  }


def main() -> None:
  output_path = pathlib.Path("wikidata_export.json")

  data = run_query(QUERY)
  converted = convert_format(data, "Я и будущее (выбор пути): Страх неизвестности")
  save_result(converted, output_path)

  print(f"Готово: результат сохранён в {output_path}")


if __name__ == "__main__":
  main()
