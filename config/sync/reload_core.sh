curl -s -X POST \
    -H "Authorization: Bearer $(cat ../../ha_secrets.json | grep -o '"token"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)" \
    -H "Content-Type: application/json" \
    -d '{}' \
    "http://$(cat ../../ha_secrets.json | grep -o '"host"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4):$(cat ../../ha_secrets.json | grep -o '"port"[[:space:]]*:[[:space:]]*[0-9]*' | cut -d':' -f2 | tr -d ' ')/api/services/homeassistant/reload_core_config" > /dev/null
