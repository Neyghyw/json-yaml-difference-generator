tests:
	poetry run pytest

lint:
	poetry run flake8

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code
