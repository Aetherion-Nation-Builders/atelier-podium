# Pulling in upstream work

Upstream is [storytold/deckcraft](https://github.com/storytold/deckcraft). We merge its `main`
into ours; our changes stay a thin layer on top (`docs/brand.md`).

```bash
scripts/sync-upstream.sh            # fetch upstream, merge into a branch, run the checks
```

The script adds the `upstream` remote if it is missing, creates `sync/upstream-<date>` from
`main`, merges `upstream/main`, and leaves the checks to you (`cargo xtask ci`). Open a pull
request from that branch; `main` is protected and is only changed through pull requests.

Conflicts come from the files the brand layer touches. `NOTICE` keeps our version automatically
(`.gitattributes` marks it `merge=ours`; the script enables that merge driver). `README.md` is
our header on top of upstream's feature sections, so upstream README edits merge in below the
line; if the header conflicts, keep ours. For anything else, keep upstream's logic and re-apply
the rename.

CI here is upstream's (`ci.yml` on every pull request, FreeBSD, packaging lint).

`release.yml` builds the macOS DMG only for now, on the standard `macos-15` runner, unsigned until
Apple signing secrets are added; the draft release is `Atelier Podium v<version>`, and publishing
it makes it the release Atelier Gate installs. To cut one without the `release` branch: Actions ›
Release › Run workflow on `main`. Its other platform jobs are kept from upstream and skipped unless
named in the repository variable `ATELIER_RELEASE_PLATFORMS`; the DMG holds `Atelier Podium.app` on
an `Atelier Podium` volume, with the Atelier background (`packaging/macos/dmg/`). When syncing,
keep those lines of ours in `release.yml`, `packaging/macos/package.sh` and `packaging/macos/dmg/`.

Upstream now calls shared workflows from `storytold/craft-common-actions` (`freebsd.yml`,
`packaging-lint.yml`, and its `release.yml`). Here they are pinned to a commit rather than
`@main`; a sync moves the pin on purpose. Our `release.yml` keeps its own jobs instead of the
shared one, which would build every platform on the larger runner as "DeckCraft".
