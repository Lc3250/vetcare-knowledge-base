---
type: decision
created: 2026-11-06
tags: [decision, adr, ide]
---

# ADR-004 Claude Code як агентна IDE

## Контекст
Потрібна агентна IDE з MCP, bash, проєктними інструкціями та hooks (коміт 178ce09, ПР1).

## Рішення
Обрано Claude Code; вибір фіксується до кінця курсу.

## Альтернативи
GitHub Copilot, Cursor.

## Наслідки
Конфігурація MCP лежить у `.mcp.json`, guardrails реалізуються hooks Claude Code.

## Зв'язки
- [[ADR-002 Три шари архітектури]]
