default: fmt install test build

ci: install example test build

install:
    pdm install

test: install
    pdm run pytest

build:
    pdm build

example:
    for p in $(ls examples/*/main.py);do pdm run python $p; done

fmt:
    just --fmt --unstable
    dprint fmt
    pre-commit run -a
