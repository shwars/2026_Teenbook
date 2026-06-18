# Блок «Профессии будущего»

## Ответственный: Участник 5

Как меняется мир труда: своё дело (предпринимательство), свободная работа без офиса (фриланс) и влияние искусственного интеллекта на профессии.

## Понятия блока

- `concepts/predprinimatelstvo.md` — Предпринимательство
- `concepts/frilans.md` — Фриланс
- `concepts/ii_i_rabota.md` — Искусственный интеллект и работа

Список понятий и файлов — в [`concepts.json`](concepts.json).

## Данные из WikiData

Запрос: [`scripts/query.py`](scripts/query.py) → выгрузка: [`data/wikidata_export.json`](data/wikidata_export.json).

| Сущность WikiData | Описание (ru) |
|-------------------|---------------|
| [фрилансер](http://www.wikidata.org/entity/Q215279) | свободный или наёмный работник (работница), чаще всего работающий по Интернету |
| [предпринимательство](http://www.wikidata.org/entity/Q3908516) | экономическая деятельность по удовлетворению потребительского спроса |
| [искусственный интеллект](http://www.wikidata.org/entity/Q11660) | наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ |

## Как воспроизвести

```bash
pip install requests
python scripts/query.py    # перезапишет data/wikidata_export.json
```

## Финальные тексты

Сгенерированные «детские» статьи блока — в `WEB/my_future_profession/professions_of_the_future/concepts/`.
