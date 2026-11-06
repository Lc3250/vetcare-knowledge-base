---
type: component
created: 2026-11-06
tags: [component]
path: api/
layer: api
status: planned
implements: ["ADR-002 Три шари архітектури"]
depends_on: ["Модуль прострочених вакцинацій", "Репозиторій SQLite", "Експорт історії"]
---

# HTTP API

REST-інтерфейс на FastAPI: маршрути для [[Власник|власників]], [[Тварина|тварин]] і звітів. Не містить бізнес-логіки, викликає шар core. Рішення: [[ADR-002 Три шари архітектури]].
