# 0x03. Unittests and Integration Tests

> This project focuses on writing unit and integration tests in Python using the `unittest` framework and mocking techniques.

---

## 📚 Learning Objectives

By the end of this project, you should be able to:

- Understand the difference between unit tests and integration tests.
- Write unit tests using `unittest` and `parameterized`.
- Use mocking (`unittest.mock`) to isolate test behavior.
- Test functions, methods, decorators, and classes.
- Mock external API requests using `patch`.
- Apply test-driven development practices.

---

## 🧠 Core Concepts

- **Unit Testing**: Testing individual units of code in isolation.
- **Integration Testing**: Testing the interaction between components.
- **Mocking**: Simulating real objects to test behavior without depending on external services or data.
- **Test Automation**: Ensuring code correctness and reliability through repeatable, automated tests.

---

## 🛠️ Project Structure

```bash
alx-backend-python/
└── 0x03-Unittests_and_integration_tests/
    ├── client.py              # GitHubOrgClient implementation
    ├── utils.py               # Utility functions (nested access, memoization, etc.)
    ├── fixtures.py            # Predefined sample data for testing
    ├── test_client.py         # Tests for GitHubOrgClient class
    ├── test_utils.py          # Tests for utility functions
    └── README.md              # This file
