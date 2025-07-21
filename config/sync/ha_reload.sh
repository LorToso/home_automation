#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SECRETS_FILE="$SCRIPT_DIR/../../ha_secrets.json"

# Check if secrets file exists
if [ ! -f "$SECRETS_FILE" ]; then
    echo "Error: Secrets file not found at $SECRETS_FILE"
    exit 1
fi

# Load Home Assistant configuration from secrets file
HA_TOKEN=$(cat "$SECRETS_FILE" | grep -o '"token"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)
HA_HOST=$(cat "$SECRETS_FILE" | grep -o '"host"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)
HA_PORT=$(cat "$SECRETS_FILE" | grep -o '"port"[[:space:]]*:[[:space:]]*[0-9]*' | cut -d':' -f2 | tr -d ' ')

# Validate that we got the required values
if [ -z "$HA_TOKEN" ] || [ -z "$HA_HOST" ] || [ -z "$HA_PORT" ]; then
    echo "Error: Could not load Home Assistant credentials from secrets file"
    exit 1
fi

# Function to call Home Assistant reload service
ha_reload() {
    local service=$1
    echo "Reloading $service..."
    curl -s -X POST \
        -H "Authorization: Bearer $HA_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{}' \
        "http://$HA_HOST:$HA_PORT/api/services/$service/reload" > /dev/null
    echo "$service reloaded successfully"
}

# Call the function with the provided service
if [ $# -eq 1 ]; then
    ha_reload $1
else
    echo "Usage: $0 <service_name>"
    echo "Examples: $0 scene, $0 script, $0 automation"
fi