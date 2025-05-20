# FasthapiX
just a puvdantic fast pyweb appX

## Table of contents

* [Stack](#stack)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [IDE configuration](#ide-configuration)
* [Tests](#tests)
* [CI/CD](#ci/cd)

## Stack

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
<a href="https://www.htmx.org/" style="color: black;font-size:26px;text-decoration:none"><<span style="color:#3366CC">/</span>>htm<span style="color:#3366CC">x</span></a>
<a href=https://ai.pydantic.dev/><img src=https://ai.pydantic.dev/img/pydantic-ai-light.svg#only-light width=120></a>
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

[![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)](https://jinja.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Alpine.js](https://img.shields.io/badge/alpinejs-white.svg?style=for-the-badge&logo=alpinedotjs&logoColor=%238BC0D)](https://alpinejs.dev/)

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

Python project [pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).

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
