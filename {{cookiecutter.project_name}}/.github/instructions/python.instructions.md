---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## Python Instructions

* Write concise comments for each function.
* Use descriptive function names and full type hints.
* Provide PEP 257-compliant docstrings.
* Use `typing` only for advanced constructs such as `TypedDict`, `Protocol`, and specialized generics.
* Split complex logic into smaller functions.
* Favor list comprehensions or generator expressions for simple transformations.

## General Instructions

* Prioritize clarity and readability.
* For algorithms, document the approach.
* Explain non-obvious design decisions in comments.
* Handle edge cases and implement clear exception flows.
* Comment on the purpose of any external libraries.
* Maintain consistent naming and follow language best practices.
* Write idiomatic, efficient code that remains easy to understand.

## Code Style and Formatting

* Follow **PEP 8**.
* Use 4-space indentation.
* Keep line length under 79 characters.
* Place docstrings immediately after `def` or `class`.
* Use blank lines to separate logical code sections.

## Edge Cases and Testing

* Provide tests for critical paths.
* Cover common edge cases such as empty input, invalid types, and large datasets.
* Document expected behavior for edge cases.
* Write unit tests with docstrings explaining intent.
* Prefer **pytest**, with `unittest` as an alternative.

## Documentation Standards

* Add docstrings to all public modules, classes, functions, and methods.
* Use triple double quotes.

## Example of Proper Documentation

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Parameters:
        radius (float): The circle radius.

    Returns:
        float: π * radius^2.
    """
    import math
    return math.pi * radius ** 2
```

## File and Directory Structure

* Use lowercase with underscores for file and module names.
* Organize code logically into packages and modules.
* Place executable code under `if __name__ == "__main__":`.

## Version Control

* Write clear commit messages.
* Do not commit secrets or large binaries.
