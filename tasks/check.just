# run check tasks
[group('check')]
check: check-code check-type check-format check-security check-coverage

# check code quality
[group('check')]
check-code:
    uv run ruff check {{SOURCES}} {{TESTS}}

# check code coverage
[group('check')]
check-coverage nbproc="auto" cov_fail_under="80":
    uv run pytest --numprocesses={{nbproc}} --cov={{SOURCES}} --cov-fail-under={{cov_fail_under}} {{TESTS}}

# check code format
[group('check')]
check-format:
    uv run ruff format --check {{SOURCES}} {{TESTS}}

# check code security
[group('check')]
check-security:
    uv run bandit --recursive --configfile=pyproject.toml {{SOURCES}}

# check unit tests
[group('check')]
check-test nbproc="auto":
    uv run pytest --numprocesses={{nbproc}} {{TESTS}}

# check code typing
[group('check')]
check-type:
    uv run mypy {{SOURCES}} {{TESTS}}
