---
id: 1
title: todo-app-spec
stage: spec
date: 2026-01-02
surface: agent
model: Claude Sonnet 4.5
feature: 1-todo-app
branch: 1-todo-app
user: Claude Code
command: /sp.specify
labels: ["spec", "todo", "console-app"]
links:
  spec: specs/1-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-todo-app/spec.md
 - specs/1-todo-app/checklists/requirements.md
tests:
 - specs/1-todo-app/spec.md
---

## Prompt

```text
You are acting as a product specification writer.

Using the Constitution, create a detailed specification for Phase I:
"In-Memory Todo Python Console App (Basic Level)".

The specification must include:

Features:
1. Add Task
   - User enters title and description
   - Task is stored in memory
   - Task receives auto-incremented ID
   - Default status is incomplete

2. View Tasks
   - Display all tasks
   - Show ID, title, description, and status
   - Status indicator: [✓] completed, [ ] incomplete

3. Update Task
   - Update title and/or description using task ID
   - Handle invalid IDs gracefully

4. Delete Task
   - Delete task by ID
   - Confirm deletion or show error if ID not found

5. Mark Task Complete / Incomplete
   - Toggle task completion status by ID

Non-Functional Requirements:
- Clear console messages
- Simple menu-driven CLI
- No crashes on invalid input

Out of Scope:
- No file saving
- No database
- No authentication
- No GUI

Do NOT generate code.
Output only the specification content.
```

## Response snapshot

Created a detailed specification for the In-Memory Todo Python Console App (Phase I) including user scenarios, functional requirements, key entities, and success criteria. The specification covers all requested features: Add Task, View Tasks, Update Task, Delete Task, and Mark Task Complete/Incomplete. Non-functional requirements for clear console messages and a simple menu-driven CLI are included, with out-of-scope items clearly defined.

## Outcome

- ✅ Impact: Created complete specification document and quality checklist for todo app feature
- 🧪 Tests: Specification validated against quality checklist with all items passing
- 📁 Files: Created spec.md and requirements.md checklist in specs/1-todo-app/
- 🔁 Next prompts: Ready for /sp.clarify or /sp.plan phases
- 🧠 Reflection: Specification covers all required features with clear acceptance criteria and measurable outcomes

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All quality checklist items validated
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to planning phase