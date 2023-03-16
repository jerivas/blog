pip-compile:
	python -m piptools compile --extra dev --output-file requirements.txt pyproject.toml

pip-sync:
	python -m piptools sync requirements.txt

serve:
	pelican --autoreload --listen --ignore-cache

build:
	pelican -s publishconf.py

lint:
	black --check .
	ruff check .

format:
	black .
	ruff check --fix .
