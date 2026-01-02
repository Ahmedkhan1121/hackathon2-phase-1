# Research: In-Memory Todo Python Console App

## Decision: Python Version Selection
**Rationale**: Using Python 3.8+ for its widespread adoption, extensive standard library, and modern features like f-strings and type hints that improve code readability and maintainability.

**Alternatives considered**:
- Python 2.7 (deprecated, no longer supported)
- Python 3.6/3.7 (still functional but missing some modern features)

## Decision: No External Dependencies
**Rationale**: Keeping the application simple and lightweight using only Python's built-in libraries. This ensures easy installation and portability across different systems without requiring pip installations.

**Alternatives considered**:
- Using Rich library for better CLI formatting (adds dependency)
- Using Click for command-line interface (adds dependency)
- Using Pydantic for data validation (adds dependency)

## Decision: In-Memory Storage Implementation
**Rationale**: Using Python's built-in list and dict data structures for in-memory storage, which provides O(1) access for operations and is sufficient for the specified requirements with no need for persistence.

**Alternatives considered**:
- SQLite in-memory database (overkill for simple requirements)
- JSON file storage (would contradict "no file saving" requirement)
- Custom data structures (unnecessary complexity)

## Decision: Menu Loop Architecture
**Rationale**: Implementing a main loop in main.py that continuously displays menu options and processes user input until exit command is given. This provides a simple, clear user interface that matches the "simple menu-driven CLI" requirement.

**Alternatives considered**:
- One-time command execution (doesn't match menu-driven requirement)
- State machine approach (unnecessary complexity)
- Event-driven architecture (overkill for simple console app)