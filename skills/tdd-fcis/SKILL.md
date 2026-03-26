---
name: tdd-fcis
description: Coding methodology combining TDD (Red-Green-Refactor) with Functional Core / Imperative Shell, SOLID, types, and refactoring. Use when writing, designing, or reviewing any code.
---

# TDD + Functional Core, Imperative Shell

Apply this methodology to every coding task. The five practices work as a system — don't skip steps.

## The System

| Practice | Answers | Rule |
|---|---|---|
| **FCIS** | WHERE to put code | Pure logic → core. Side effects (I/O, DB, network, files) → shell |
| **TDD** | HOW to write code | Never write code without a failing test first |
| **Single Responsibility** | HOW to structure code | Each function does exactly one thing |
| **Types** | HOW to catch errors early | Every function has typed inputs and outputs |
| **Refactoring** | HOW to improve code | Clean up after every green test |

## Step-by-Step Process

### 1. Separate Core from Shell (FCIS)

Before writing any code, identify:

- **Functional Core** — Pure functions: take input, return output, NO side effects
  - No DB calls, no file I/O, no network, no global state, no `datetime.now()`
  - Deterministic: same input = same output, always
- **Imperative Shell** — Thin glue: fetches data, calls core, applies side effects
  - Should be so simple it barely needs testing

```python
# CORE: pure, testable, reusable
def get_expired_users(users: list[User], cutoff: datetime) -> list[User]:
    return [u for u in users if u.end_date <= cutoff and not u.is_trial]

# SHELL: thin, wires things together
expired = get_expired_users(db.get_users(), datetime.now())
email.bulk_send(generate_emails(expired))
```

### 2. Write a Failing Test First (🔴 Red)

Write a test for ONE behavior of a core function. The test must fail.

```python
def test_filters_expired_non_trial_users():
    users = [
        User("Ali", end_date=PAST, is_trial=False),   # expired
        User("Bob", end_date=FUTURE, is_trial=False),  # active
        User("Cat", end_date=PAST, is_trial=True),     # trial
    ]
    result = get_expired_users(users, NOW)
    assert result == [users[0]]  # Only Ali
```

Rules:
- Test the core, not the shell
- No mocks needed — pure functions don't need them
- Test one behavior per test
- Use descriptive test names that read like specifications

### 3. Write Minimum Code (🟢 Green)

Write just enough code to make the test pass. Nothing more.

- Don't optimize
- Don't handle edge cases you haven't tested yet
- Don't add features "just in case"

### 4. Refactor (🔵 Refactor)

With tests passing, clean up:

- **Extract Function** — Pull repeated logic into reusable pure functions
- **Rename** — Names should explain intent, not implementation
- **Remove Duplication** — Shared logic → shared function
- **Simplify** — If a function does two things, split it

Run tests after every change. If they pass, your refactoring is safe.

### 5. Repeat

Go back to step 2 for the next behavior. Continue until the core is complete, then write the shell.

## Checklist for Every Function

- [ ] Is it pure? (no side effects)
- [ ] Does it have typed inputs and outputs?
- [ ] Does it do exactly one thing?
- [ ] Was a failing test written before the implementation?
- [ ] Is the name descriptive?

## Checklist for Every Shell

- [ ] Is it thin? (just wiring, minimal logic)
- [ ] Does all logic live in the core?
- [ ] Are side effects (DB, files, network) only here?

## Common Mistakes

| Mistake | Fix |
|---|---|
| Testing the shell with mocks | Move logic to core, test core directly |
| `datetime.now()` inside core function | Pass `cutoff: datetime` as parameter |
| Function does filtering AND sending email | Split into two functions |
| No types on function signature | Add type hints — they catch bugs at write time |
| Writing code before tests | Stop. Write the failing test first |
| Testing implementation details | Test behavior (input → output), not internals |

## When to Use This Skill

- Writing any new function or class
- Refactoring existing code
- Reviewing code (check: is logic separated from side effects?)
- Designing a module or feature before implementation

