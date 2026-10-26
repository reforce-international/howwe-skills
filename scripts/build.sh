#!/usr/bin/env bash
# Builds one zip per skill for upload to ChatGPT and Copilot Studio.
# Claude needs no build: the repo itself is the plugin.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for dir in skills/*/; do
  name=$(basename "$dir")
  (cd skills && zip -qr "../dist/${name}.zip" "$name" -x '*.DS_Store')
  echo "dist/${name}.zip"
done
