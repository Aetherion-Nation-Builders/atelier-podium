#!/usr/bin/env bash
# Merge the latest upstream DeckCraft into a branch of this repository. See docs/upstream.md.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
UPSTREAM_URL="https://github.com/storytold/deckcraft"
git remote get-url upstream >/dev/null 2>&1 || git remote add upstream "$UPSTREAM_URL"
git config merge.ours.driver true   # NOTICE keeps our version (see .gitattributes)
git fetch upstream main
BRANCH="sync/upstream-$(date +%Y-%m-%d)"
git checkout -b "$BRANCH" main
if ! git merge --no-edit upstream/main; then
  echo
  echo "Conflicts above. Keep upstream's logic, re-apply the rename (docs/brand.md), then:"
  echo "  git add -A && git commit"
  exit 1
fi
echo "Merged upstream/main into $BRANCH. Now run the checks (cargo test --workspace) and open a pull request."
