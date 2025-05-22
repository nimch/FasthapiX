[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/monogram.svg" height="56">](https://www.python.org/)
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/fasthapix.svg" height="56">](https://www.python.org/)
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/fasthapix.png" height="56">](https://www.python.org/)
[![FasthapiX](https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/monogram.svg)](https://github.com/nimch/FasthapiX)
[![FasthapiX](https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/fasthapix.svg)](https://github.com/nimch/FasthapiX)
[![FasthapiX](https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/fasthapix.png)](https://github.com/nimch/FasthapiX)

## Table of contents

* [Stack](#stack)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [IDE configuration](#ide-configuration)
* [Tests](#tests)
* [CI/CD](#ci/cd)

## Stack

[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/python.svg" height="48">](https://www.python.org/)

[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/htmx.svg" height="30">](https://www.htmx.org/)&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/pydantic.svg" height="32">](https://ai.pydantic.dev/)&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/fastapi.svg" height="24">](https://fastapi.tiangolo.com/)

[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/jinja.svg" height="58">](https://jinja.palletsprojects.com/)&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/tailwind.svg" height="28">](https://tailwindcss.com/)&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/alpinejs.svg" height="36">](https://alpinejs.dev/)&nbsp;&nbsp;&nbsp;&nbsp;

[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/just.svg" height="36">](https://just.systems/)&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/uv.svg" height="40">](https://docs.astral.sh/uv/)&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="https://raw.githubusercontent.com/nimch/FasthapiX/refs/heads/main/docs/graphics/stack/docker.svg" height="46">](https://www.docker.com/)

Python project [pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
Temporary use of tailwindcss and alpine.js from cdn.

## Prerequisites

[Install](https://docs.astral.sh/uv/getting-started/installation/) Python package and project manager: [`UV`](https://docs.astral.sh/uv/)

[Install](https://github.com/casey/just) just a command runner (make inspiration): [`just`](https://just.systems/)

## Setup

Install all dependencies:
```bash
just install
```
Launch local server (TODO):
```bash
just project-run
```
List of tasks:
```bash
just --list
```

### Add package

```bash
uv add package-name
```
adds dependency package, while
```bash
uv add --dev package-name
```
adds development dependency package.
Both updates pyproject.toml and uv.lock
```bash
uv add --group groupname package-name
```
See groups in pyproject.toml.

## Architecture

Description of the project's architecture. Diagrams, maps, etc.

TODO

[API](https://fastapi.tiangolo.com/) trying to respect [this](https://www.openapis.org/)

## IDE configuration

vscode workspace file is present.

## Tests

Obviously:
```bash
just check-test
```

## CI/CD

Description of what the CI/CD process looks like and how it works. What is the deployment strategy, etc.

TODO

https://pre-commit.com/

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
