---
type: moc
created: 2026-11-06
tags: [moc, ontology]
---

# Онтологія VetCare

Онтологія застосунку виражена типами нотаток, тегами, папками та типізованими зв'язками. Докладний опис: `docs/ontology.md` у репозиторії застосунку.

## Типи сутностей
- concept (Concepts/): [[Власник]], [[Тварина]], [[Візит]], [[Вакцинація]], [[Ревакцинація]], [[Довідник вакцин]]
- component (Components/): [[Модуль графіка ревакцинації]], [[HTTP API]]
- decision (Decisions/): [[ADR-001 Використання SQLite]]
- glossary (Glossary/): [[Пацієнт]]

## Типи зв'язків
Записуються в frontmatter нотатки-джерела списком назв.

| Зв'язок | Від → до |
|---------|----------|
| depends_on | component → component |
| implements | component → concept, decision, glossary |
| supersedes | decision → decision |
| belongs_to | concept → concept |

## Приклади
- [[Модуль прострочених вакцинацій]] depends_on [[Модуль графіка ревакцинації]]
- [[Візит]] belongs_to [[Тварина]]

Навігація: [[MOC-Застосунок]]; правила оформлення: [[Конвенції vault]].
