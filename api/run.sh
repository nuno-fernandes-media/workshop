#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src
