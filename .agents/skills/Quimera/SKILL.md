```markdown
# Quimera Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the Quimera Python codebase. It covers file organization, import/export styles, commit message patterns, and testing conventions. This guide is intended to help contributors maintain consistency and quality across the project.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - **Example:**  
    `data_processor.py`  
    `utils/helpers.py`

### Import Style
- Use **relative imports** within the package.
  - **Example:**
    ```python
    from .utils import helper_function
    from ..models import DataModel
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - **Example:**
    ```python
    def process_data(data):
        ...

    def clean_data(data):
        ...

    __all__ = ['process_data', 'clean_data']
    ```

### Commit Messages
- Freeform style, no strict prefixes.
- Average commit message length: ~61 characters.
  - **Example:**  
    `Fix bug in data normalization step for edge cases`

## Workflows

### Adding a New Module
**Trigger:** When you need to add new functionality to the project  
**Command:** `/add-module`

1. Create a new Python file using snake_case naming.
2. Implement your functions/classes.
3. Use relative imports for internal dependencies.
4. Define `__all__` to specify exported functions/classes.
5. Write corresponding tests in a `*.test.*` file.
6. Commit changes with a descriptive message.

### Updating an Existing Module
**Trigger:** When modifying or extending existing code  
**Command:** `/update-module`

1. Locate the relevant module (use snake_case).
2. Make necessary changes, maintaining code style.
3. Update `__all__` if new exports are added.
4. Update or add tests as needed.
5. Commit with a clear, descriptive message.

### Running Tests
**Trigger:** To verify code correctness after changes  
**Command:** `/run-tests`

1. Identify all test files matching `*.test.*`.
2. Run tests using the project's preferred method (framework unknown; use `python` or your test runner).
   - **Example:**  
     ```bash
     python my_module.test.py
     ```
3. Review test results and fix any failures.

## Testing Patterns

- Test files follow the pattern: `*.test.*` (e.g., `data_processor.test.py`).
- The testing framework is not specified; use standard Python testing practices.
- Place tests alongside or near the modules they cover.
- Write clear, concise test cases for each function or class.

  **Example:**
  ```python
  # data_processor.test.py
  from .data_processor import process_data

  def test_process_data_valid():
      assert process_data([1, 2, 3]) == [2, 3, 4]
  ```

## Commands
| Command        | Purpose                                         |
|----------------|-------------------------------------------------|
| /add-module    | Add a new module following project conventions  |
| /update-module | Update an existing module                       |
| /run-tests     | Run all tests in the codebase                   |
```
