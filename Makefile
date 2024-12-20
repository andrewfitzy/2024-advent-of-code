all: install

compile-dependencies:
	@uv pip compile requirements.in -o requirements.txt

compile-dependencies-dev:
	@uv pip compile requirements-dev.in -o requirements-dev.txt

compile-dependencies-all: compile-dependencies compile-dependencies-dev

install: compile-dependencies-all
	@uv pip install -r requirements-dev.txt

.PHONY: test
test:
	TEST_ENV=local pytest --cov-fail-under=80 --cov=src/ --cov-report=term-missing --cov-report=xml

test-file:
	TEST_ENV=local pytest $(file)