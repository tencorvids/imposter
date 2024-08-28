set shell := ["bash", "-c"]

default:
    @just --list

install:
    poetry install

run REPO_PATH START_DATE=`date -d "30 days ago" +%Y-%m-%d` END_DATE=`date +%Y-%m-%d` PROFILE="workday-andy":
    poetry run imposter --repo-path {{REPO_PATH}} --start-date {{START_DATE}} --end-date {{END_DATE}} --profile {{PROFILE}}

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
