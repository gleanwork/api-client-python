#!/usr/bin/env bash
set -euo pipefail

FILE="${1:-src/glean/__init__.py}"

# If the lines are already present, exit without modifying.
if grep -Fq "extend_path(__path__, __name__)" "$FILE"; then
  if [[ -n "${OUTPUT:-}" ]]; then
    echo "patched=false" >> "$OUTPUT"
  fi
  exit 0
fi

# Insert the two lines immediately after the first line.
awk 'NR==1 {print $0; print "from pkgutil import extend_path\n"; print "__path__ = extend_path(__path__, __name__)\n"; next} 1' "$FILE" > "$FILE.new"
mv "$FILE.new" "$FILE"

if [[ -n "${OUTPUT:-}" ]]; then
  echo "patched=true" >> "$OUTPUT"
fi 