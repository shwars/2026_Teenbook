# Блок «Навыки и знания»

## Ответственный: Участник 2

О том, из чего складывается мастерство: что такое навык, чем гибкие навыки (soft skills) отличаются от профессиональных, какую роль играют образование и талант.

## Понятия блока

- `concepts/navyk.md` — Навык
- `concepts/gibkie_navyki.md` — Гибкие навыки
- `concepts/obrazovanie.md` — Образование
- `concepts/talant.md` — Талант

Список понятий и файлов — в [`concepts.json`](concepts.json).

## Данные из WikiData

Запрос: [`scripts/query.py`](scripts/query.py) → выгрузка: [`data/wikidata_export.json`](data/wikidata_export.json).

| Сущность WikiData | Описание (ru) |
|-------------------|---------------|
| [умение](http://www.wikidata.org/entity/Q205961) | опытное знание, условие для деятельности |
| [образование](http://www.wikidata.org/entity/Q8434) | система обучения и приобретённые знания |
| [одарённость](http://www.wikidata.org/entity/Q467677) | — |
| [гибкие навыки](http://www.wikidata.org/entity/Q15910354) | — |

## Как воспроизвести

```bash
pip install requests
python scripts/query.py    # перезапишет data/wikidata_export.json
```

## Финальные тексты

Сгенерированные «детские» статьи блока — в `WEB/my_future_profession/skills_and_knowledge/concepts/`.
