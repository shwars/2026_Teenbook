#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Расстановка перекрёстных ссылок в статьях раздела «Я и будущая профессия».

Для каждого понятия из WORK/my_future_profession/<блок>/concepts.json скрипт
находит в текстах WEB/my_future_profession/<блок>/concepts/*.md упоминания
этого понятия (в разных падежах) и оборачивает первое из них в ссылку
[слово](относительный/путь/concept.md).

Падежи обрабатываются двумя способами:
  1. Список алиасов (aliases) из concepts.json — частые словоформы.
  2. Опционально pymorphy2 — нормализация слов до начальной формы.

Чтобы расставить ссылки и на понятия других групп, запустите с флагом
--cross: тогда дополнительно загружаются все WORK/*/**/concepts.json.

Использование:
    python crosslink.py            # ссылки внутри раздела
    python crosslink.py --check    # ничего не писать, только показать, что найдено
    python crosslink.py --cross    # учитывать понятия других разделов

Зависимости: стандартная библиотека. pymorphy2 — по желанию.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
SECTION = "my_future_profession"
WEB_DIR = BASE / "WEB" / SECTION
WORK_DIR = BASE / "WORK" / SECTION

# ─── pymorphy2 (опционально) ──────────────────────────────────────────────────
try:
    import pymorphy2  # type: ignore
    MORPH = pymorphy2.MorphAnalyzer()
    HAS_MORPH = True
except Exception:
    HAS_MORPH = False


def normal_form(word: str) -> str:
    if HAS_MORPH:
        return MORPH.parse(word)[0].normal_form
    return word.lower()


# ─── Загрузка понятий ─────────────────────────────────────────────────────────
def load_concepts(work_root: Path, web_section: str) -> list[dict]:
    """Возвращает список понятий с id, именем, алиасами и путём к файлу."""
    concepts: list[dict] = []
    for cj in sorted(work_root.glob("*/concepts.json")):
        block = cj.parent.name
        data = json.loads(cj.read_text(encoding="utf-8"))
        for c in data["concepts"]:
            file = c["file"]
            cid = f"{web_section}/{block}/{file}"
            target = BASE / "WEB" / web_section / block / "concepts" / file
            concepts.append({
                "id": cid,
                "name": c["name"],
                "aliases": c.get("aliases", []),
                "block": block,
                "file": file,
                "target": target,
                "norm": normal_form(c["name"].split()[0]),
            })
    return concepts


def build_patterns(concepts: list[dict]) -> list[tuple[dict, re.Pattern]]:
    """Для каждого понятия — регулярка по имени и алиасам (длинные раньше коротких)."""
    patterns = []
    for c in concepts:
        variants = sorted({c["name"], *c["aliases"]}, key=len, reverse=True)
        escaped = [re.escape(v) for v in variants]
        pat = re.compile(r"(?<![\w-])(" + "|".join(escaped) + r")(?![\w-])", re.IGNORECASE)
        patterns.append((c, pat))
    return patterns


# ─── Зоны, которые нельзя трогать (ссылки, код, заголовки) ─────────────────────
def protected_spans(text: str) -> list[tuple[int, int]]:
    spans = []
    for m in re.finditer(r"\[[^\]]*\]\([^)]*\)", text):   # уже готовые ссылки
        spans.append(m.span())
    for m in re.finditer(r"`[^`]*`", text):               # инлайн-код
        spans.append(m.span())
    for m in re.finditer(r"^#{1,6} .*$", text, re.MULTILINE):  # заголовки
        spans.append(m.span())
    return spans


def in_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(a <= pos < b for a, b in spans)


def rel_path(src: Path, dst: Path) -> str:
    import os
    return os.path.relpath(dst, src.parent).replace(os.sep, "/")


def process_file(path: Path, patterns, self_id: str, dry: bool) -> int:
    text = path.read_text(encoding="utf-8")
    linked: set[str] = set()      # одно понятие — одна ссылка на файл
    added = 0
    # Идём по понятиям; внутри файла каждое линкуем максимум один раз.
    for c, pat in patterns:
        if c["id"] == self_id or c["id"] in linked:
            continue
        spans = protected_spans(text)
        m = pat.search(text)
        while m and in_protected(m.start(), spans):
            m = pat.search(text, m.end())
        if not m:
            continue
        word = m.group(1)
        href = rel_path(path, c["target"])
        replacement = f"[{word}]({href})"
        text = text[:m.start()] + replacement + text[m.end():]
        linked.add(c["id"])
        added += 1
    if added and not dry:
        path.write_text(text, encoding="utf-8")
    return added


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="не записывать, только посчитать")
    ap.add_argument("--cross", action="store_true", help="учитывать понятия других разделов")
    args = ap.parse_args()

    concepts = load_concepts(WORK_DIR, SECTION)
    if args.cross:
        for other in sorted((BASE / "WORK").glob("*")):
            if other.name == SECTION or not other.is_dir():
                continue
            # эвристика: имя web-папки совпадает с work-папкой
            web = other.name
            if not (BASE / "WEB" / web).exists():
                continue
            try:
                concepts += load_concepts(other, web)
            except Exception:
                pass

    patterns = build_patterns(concepts)
    total = 0
    files = sorted(WEB_DIR.glob("*/concepts/*.md"))
    for f in files:
        self_id = f"{SECTION}/{f.parent.parent.name}/{f.name}"
        n = process_file(f, patterns, self_id, dry=args.check)
        if n:
            print(f"  {f.relative_to(BASE)}: +{n}")
        total += n

    mode = "морфология: pymorphy2" if HAS_MORPH else "морфология: алиасы"
    print(f"\nПонятий: {len(concepts)} | файлов: {len(files)} | "
          f"ссылок: {total} | {mode}{' | DRY-RUN' if args.check else ''}")


if __name__ == "__main__":
    main()
