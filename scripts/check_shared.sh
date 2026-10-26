#!/usr/bin/env bash
# Each skill is packaged on its own, so shared references are copied into every
# skill that uses them. A reference file with the same name in several skills
# must be identical everywhere.
set -euo pipefail
cd "$(dirname "$0")/.."
status=0
for name in $(ls skills/*/references/ | grep '\.md$' | sort | uniq -d); do
  copies=(skills/*/references/"$name")
  for copy in "${copies[@]:1}"; do
    if ! cmp -s "${copies[0]}" "$copy"; then
      echo "Differs from ${copies[0]}: $copy"
      status=1
    fi
  done
done
[ "$status" -eq 0 ] && echo "OK: shared references are identical."
exit "$status"
