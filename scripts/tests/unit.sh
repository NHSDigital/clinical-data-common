#!/bin/bash

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"


mkdir -p test-artefacts

echo "Running unit tests..."
poetry run pytest src/ -v \
  --junit-xml="test-artefacts/unit-tests.xml" \
  --html="test-artefacts/unit-tests.html" --self-contained-html
