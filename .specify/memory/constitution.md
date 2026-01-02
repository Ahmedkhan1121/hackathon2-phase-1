<!--
SYNC IMPACT REPORT:
- Version change: N/A → 1.0.0 (initial constitution)
- Added sections: All principles and sections for Todo In-Memory Python Console App
- Templates requiring updates: N/A (initial creation)
- Follow-up TODOs: None
-->

# Todo In-Memory Python Console App Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must follow spec-driven development methodology: specifications written and approved → tasks defined → implementation follows. No code changes without corresponding spec updates and approvals.

### II. Clean Code and Readability
All code must follow clean code principles with meaningful variable and function names, clear separation of concerns, and Python best practices (PEP8). Code should be self-documenting and maintainable.

### III. In-Memory Data Persistence
All task data must remain in memory during runtime only - no file persistence, databases, or external storage. This ensures simplicity and prevents data leakage between sessions.

### IV. Console-Based Interaction
All user interaction must occur through a numbered menu system in the console. No GUI, web interfaces, or alternative interaction methods. Input/output must be text-based and clear.

### V. Task Data Integrity
Tasks must have id (auto-incremented, unique), title, description, and completed status. All data fields must be properly validated and maintained with integrity throughout the application lifecycle.

### VI. Technology Constraint Adherence


All technology choices must comply with constraints: Python 3.13+, UV for environment management, no external frameworks or databases. Deviations require constitutional amendment.


## Application Constraints

Technology Stack:
- Python 3.13+ required
- UV for environment management
- Console-based interaction only
- No external databases or frameworks
- Memory-only data storage

Data Requirements:
- Tasks must have: id (auto-incremented), title, description, completed status
- IDs must be unique and never reused within a session
- Data exists only in memory during runtime

Repository Structure:
- /src contains all Python code
- /specs/history contains all specification files
- README.md must explain setup and usage
- CLAUDE.md must contain Claude Code instructions


## Development Workflow

Spec Compliance:
- All features must be specified before implementation
- Tasks must be derived from approved specifications
- Implementation must match spec requirements exactly

Code Quality:
- Follow PEP8 Python standards
- Use meaningful names for variables and functions
- Maintain clear separation of concerns
- Keep logic simple and readable

Testing Requirements:
- All functionality must have corresponding tests
- Test-driven development approach preferred
- Both unit and integration tests required


## Governance

This constitution supersedes all other development practices. All code reviews must verify compliance with constitutional principles. Any deviations require formal constitutional amendments with proper justification and approval.

All pull requests must demonstrate compliance with constitutional requirements. New features or changes that conflict with constitutional principles must be accompanied by a constitutional amendment process.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
