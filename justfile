set shell := ["bash", "-c"]

default:
    @just --list

install:
    poetry install

run REPO_PATH DAYS="30" PROFILE="workday-andy":
    poetry run imposter --repo-path {{REPO_PATH}} --days {{DAYS}} --profile {{PROFILE}}

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type d -name ".pytest_cache" -exec rm -rf {} +
    find . -type d -name ".mypy_cache" -exec rm -rf {} +
    find . -type f -name "*.py[co]" -delete
    find . -type f -name "*.log" -delete

build:
    poetry build

update:
    poetry update
