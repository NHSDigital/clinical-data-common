#!/bin/bash

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"


mkdir -p test-artefacts

echo "Running unit tests..."
poetry run pytest src/ -v \
  --cov="." \
  --cov-report=html:test-artefacts/coverage-html \
  --cov-report=xml:test-artefacts/coverage.xml \
  --cov-report=term \
  --junit-xml="test-artefacts/unit-tests.xml" \
  --html="test-artefacts/unit-tests.html" --self-contained-html
