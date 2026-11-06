---
type: component
created: 2026-11-06
tags: [component]
path: storage/repository.py
layer: storage
status: planned
implements: ["ADR-001 Використання SQLite", "ADR-009 Дати як ISO-текст і пошук без регістру в SQLite"]
---

# Репозиторій SQLite

Єдине місце доступу до бази: збереження й читання [[Власник|власників]], [[Тварина|тварин]], [[Візит|візитів]], [[Вакцинація|вакцинацій]]. Лише параметризовані запити. Рішення: [[ADR-001 Використання SQLite]].
