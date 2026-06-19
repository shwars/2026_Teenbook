# -*- coding: utf-8 -*-
"""SPARQL-запросы для подтемы "Время".

Запросы собирают не только физическое понятие времени, но и связанные с
подростковой темой узлы: прошлое, настоящее, будущее, память, планирование,
прокрастинацию, детство, подростковый возраст и отношения.
"""

from textwrap import dedent


SEED_ENTITIES = {
    "time": "Q11471",
    "past": "Q192630",
    "present": "Q193168",
    "future": "Q344",
    "memory": "Q492",
    "childhood": "Q276258",
    "adolescence": "Q131774",
    "planning": "Q309100",
    "time management": "Q355217",
    "procrastination": "Q330104",
    "interpersonal relationship": "Q223642",
}

QUERY_SEED_ENTITIES = dedent("""
SELECT DISTINCT ?item ?itemLabel ?itemDescription WHERE {
  VALUES ?item {
    wd:Q11471
    wd:Q192630
    wd:Q193168
    wd:Q344
    wd:Q492
    wd:Q276258
    wd:Q131774
    wd:Q309100
    wd:Q355217
    wd:Q330104
    wd:Q223642
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru,en". }
}
ORDER BY ?itemLabel
""")

QUERY_EXPAND_CLASS_TREE = dedent("""
SELECT DISTINCT ?seed ?seedLabel ?related ?relatedLabel ?relation WHERE {
  VALUES ?seed {
    wd:Q11471
    wd:Q192630
    wd:Q193168
    wd:Q344
    wd:Q492
    wd:Q276258
    wd:Q131774
    wd:Q309100
    wd:Q355217
    wd:Q330104
    wd:Q223642
  }

  {
    ?related wdt:P31 ?seed.
    BIND("instance of" AS ?relation)
  }
  UNION
  {
    ?related wdt:P279 ?seed.
    BIND("subclass of" AS ?relation)
  }

  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru,en". }
}
LIMIT 150
""")

QUERY_LOCAL_GRAPH = dedent("""
SELECT DISTINCT ?item1 ?item1Label ?p ?propLabel ?item2 ?item2Label WHERE {
  VALUES ?item1 {
    wd:Q11471
    wd:Q192630
    wd:Q193168
    wd:Q344
    wd:Q492
    wd:Q276258
    wd:Q131774
    wd:Q309100
    wd:Q355217
    wd:Q330104
    wd:Q223642
  }

  ?item1 ?p ?item2.
  FILTER(STRSTARTS(STR(?item2), "http://www.wikidata.org/entity/"))
  ?prop wikibase:directClaim ?p.

  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru,en". }
}
LIMIT 200
""")

QUERY_REVERSE_GRAPH = dedent("""
SELECT DISTINCT ?item1 ?item1Label ?p ?propLabel ?item2 ?item2Label WHERE {
  VALUES ?item2 {
    wd:Q11471
    wd:Q192630
    wd:Q193168
    wd:Q344
    wd:Q492
    wd:Q276258
    wd:Q131774
    wd:Q309100
    wd:Q355217
    wd:Q330104
    wd:Q223642
  }

  ?item1 ?p ?item2.
  FILTER(STRSTARTS(STR(?item1), "http://www.wikidata.org/entity/"))
  ?prop wikibase:directClaim ?p.

  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru,en". }
}
LIMIT 200
""")


if __name__ == "__main__":
    for name in [
        "QUERY_SEED_ENTITIES",
        "QUERY_EXPAND_CLASS_TREE",
        "QUERY_LOCAL_GRAPH",
        "QUERY_REVERSE_GRAPH",
    ]:
        print(f"=== {name} ===")
        print(globals()[name].strip())
        print()
