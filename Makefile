PEP_IGNORE_ERRORS="C901 E501 W503 E203 E231 E266 F403"

test: FORCE ## Run tests using pytest
	python -m pytest -v --disable-pytest-warnings -rsx

docs: FORCE ## Build docs using Sphinx.
	rm -rf docs/_build
	sphinx-apidoc -fo docs starter
	sphinx-build -b html docs docs/_build

install: FORCE
	pip install -e .

all: install docs test

.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

FORCE: