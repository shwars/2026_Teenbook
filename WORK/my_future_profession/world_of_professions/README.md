# Блок «Мир профессий»

## Ответственный: Участник 1

С чего начинается разговор о работе: что вообще такое профессия, чем она отличается от специальности, что такое внутреннее «призвание» и как устроены большие отрасли.

## Понятия блока

- `concepts/professiya.md` — Профессия
- `concepts/specialnost.md` — Специальность
- `concepts/prizvanie.md` — Призвание
- `concepts/otrasl.md` — Отрасль

Список понятий и файлов — в [`concepts.json`](concepts.json).

## Данные из WikiData

Запрос: [`scripts/query.py`](scripts/query.py) → выгрузка: [`data/wikidata_export.json`](data/wikidata_export.json).

| Сущность WikiData | Описание (ru) |
|-------------------|---------------|
| [профессия](http://www.wikidata.org/entity/Q28640) | род занятий, требующий специальной подготовки |
| [отрасль экономики](http://www.wikidata.org/entity/Q268592) | группа компаний, производящих однородные товары или услуги |
| [призвание](http://www.wikidata.org/entity/Q829183) | внутреннее влечение к какому-нибудь делу, какой-нибудь профессии |
| [специальность](http://www.wikidata.org/entity/Q1047113) | область деятельности в рамках другой области деятельности |

## Как воспроизвести

```bash
pip install requests
python scripts/query.py    # перезапишет data/wikidata_export.json
```

## Финальные тексты

Сгенерированные «детские» статьи блока — в `WEB/my_future_profession/world_of_professions/concepts/`.
