---
id: 1
title: Create Todo App Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app
branch: main
user: Claude User
command: sp.constitution
labels: [constitution, todo-app, python]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

You are an expert Python architect and CLI application designer.

Create a Spec-Kit Plus Constitution for the project "Todo In-Memory Python Console App".

Project Objective:
Build a command-line todo application that stores tasks in memory (no database, no file persistence).

Technology Constraints:
- Python 3.13+
- UV for environment management
- Console-based interaction only
- No external databases
- No frameworks

Development Rules:
- Follow spec-driven development strictly
- Follow clean code principles
- Use clear separation of concerns
- Use meaningful variable and function names
- Keep logic simple and readable
- Follow Python best practices (PEP8)

Application Rules:
- Tasks must have: id, title, description, completed status
- Data must remain in memory during runtime only
- IDs must be unique and auto-incremented
- User interacts through numbered menu options

Repository Rules:
- /src contains all Python code
- /specs/history contains all specification files
- README.md must explain setup and usage
- CLAUDE.md must contain Claude Code instructions

Do NOT write any code.
Only generate the Constitution file content.

## Response snapshot

Created a comprehensive constitution file for the Todo In-Memory Python Console App with the following sections:
- Core Principles (Spec-Driven Development, Clean Code, In-Memory Persistence, Console Interaction, Task Data Integrity, Technology Constraints)
- Application Constraints (Technology Stack, Data Requirements, Repository Structure)
- Development Workflow (Spec Compliance, Code Quality, Testing Requirements)
- Governance (Constitutional authority and amendment process)

## Outcome

- ✅ Impact: Created initial constitution file at .specify/memory/constitution.md
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with project-specific constitution
- 🔁 Next prompts: Continue with spec creation using sp.specify
- 🧠 Reflection: Constitution properly captures all specified requirements and constraints

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create feature specification