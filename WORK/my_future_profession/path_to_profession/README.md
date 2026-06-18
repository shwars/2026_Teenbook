# Блок «Путь к профессии»

## Ответственный: Участник 3

Дорога от «не знаю, кем быть» до первой работы: профориентация, профессиональное образование (колледж и вуз), стажировка и роль наставника.

## Понятия блока

- `concepts/proforientaciya.md` — Профориентация
- `concepts/professionalnoe_obrazovanie.md` — Профессиональное образование
- `concepts/stazhirovka.md` — Стажировка
- `concepts/nastavnik.md` — Наставник

Список понятий и файлов — в [`concepts.json`](concepts.json).

## Данные из WikiData

Запрос: [`scripts/query.py`](scripts/query.py) → выгрузка: [`data/wikidata_export.json`](data/wikidata_export.json).

| Сущность WikiData | Описание (ru) |
|-------------------|---------------|
| [наставничество](http://www.wikidata.org/entity/Q967647) | отношения, в которых опытный или более сведущий человек помогает менее опытному или менее сведущему усвоить определенные компетенции |
| [стажировка](http://www.wikidata.org/entity/Q4439145) | деятельность по приобретению опыта работы или повышение квалификации по специальности, а также работа по специальности |
| [профессиональная ориентация](http://www.wikidata.org/entity/Q741939) | — |
| [профессионально-техническое образование](http://www.wikidata.org/entity/Q6869278) | — |

## Как воспроизвести

```bash
pip install requests
python scripts/query.py    # перезапишет data/wikidata_export.json
```

## Финальные тексты

Сгенерированные «детские» статьи блока — в `WEB/my_future_profession/path_to_profession/concepts/`.
