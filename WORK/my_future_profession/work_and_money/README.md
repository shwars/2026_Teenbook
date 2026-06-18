# Блок «Работа и деньги»

## Ответственный: Участник 4

Как устроена сама работа и что с ней связано: труд и занятость, зарплата, карьерный рост, а также резюме и собеседование как способ устроиться.

## Понятия блока

- `concepts/rabota.md` — Работа
- `concepts/zarplata.md` — Зарплата
- `concepts/karera.md` — Карьера
- `concepts/rezyume.md` — Резюме
- `concepts/sobesedovanie.md` — Собеседование

Список понятий и файлов — в [`concepts.json`](concepts.json).

## Данные из WikiData

Запрос: [`scripts/query.py`](scripts/query.py) → выгрузка: [`data/wikidata_export.json`](data/wikidata_export.json).

| Сущность WikiData | Описание (ru) |
|-------------------|---------------|
| [труд](http://www.wikidata.org/entity/Q268378) | целенаправленная созидательная деятельность |
| [карьера](http://www.wikidata.org/entity/Q282049) | успешное продвижение в области служебной, социальной, научной и другой деятельности |
| [собеседование](http://www.wikidata.org/entity/Q850171) | обсуждение поступления на работу |
| [резюме](http://www.wikidata.org/entity/Q950511) | описание жизни и навыков для устройства на работу |
| [занятость](http://www.wikidata.org/entity/Q2266417) | деятельность, связанная с получением дохода |
| [зарплата](http://www.wikidata.org/entity/Q6821213) | вознаграждение за труд в зависимости от квалификации работника, сложности, количества, качества и условий выполняемой работы |

## Как воспроизвести

```bash
pip install requests
python scripts/query.py    # перезапишет data/wikidata_export.json
```

## Финальные тексты

Сгенерированные «детские» статьи блока — в `WEB/my_future_profession/work_and_money/concepts/`.
