default: fmt install test build

ci: install example test build

install:
    pdm install -G=rich

test: install
    pdm run pytest

build:
    pdm build

example:
    #!/usr/bin/env bash
    set -euo pipefail

    for p in $(ls examples/*/main.py);
    do
        echo " * $p * "
        pdm run python $p
        echo ""
    done

fmt:
    just --fmt --unstable
    dprint fmt
    pre-commit run -a
