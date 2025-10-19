#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Get environment variables with defaults
API_HOST=${API_HOST:-"0.0.0.0"}
API_PORT=${API_PORT:-"8000"}
API_ENV=${API_ENV:-"development"}

echo "🚀 Starting Sensor Workshop API"
echo "Environment: $API_ENV"
echo "Host: $API_HOST"
echo "Port: $API_PORT"
echo "API Title: ${API_TITLE:-Sensor Workshop API}"

uvicorn app.main:app --reload --host "$API_HOST" --port "$API_PORT" --app-dir src
