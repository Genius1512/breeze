mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

sandbox: $(mkfile_dir)sandbox/main.py
	@poetry run python3 $(mkfile_dir)sandbox/main.py

test:
	@poetry run pytest

build-docs: docs
	@cd docs && poetry run sphinx-apidoc -o . ..
	@cd docs && make html

venv:
	@echo "source `poetry env info --path`/bin/activate"

