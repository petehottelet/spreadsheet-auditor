# CLAUDE.md

Guidance for Claude Code sessions working in this repository.

## Working tree

Other sessions may be working in this checkout. Before a command that changes
the working tree (switching branches, merging, resetting), run
`git branch --show-current` and `git status`; if the branch or the changes are
not this session's, work in a separate worktree under `.claude/worktrees/`.

## Pushing and opening pull requests

Commit, push, and open pull requests only when the user asks for it in the
conversation. An approval covers the push it was given for, not later ones.

Before pushing, run what CI runs:

```bash
python -m ruff check --select F,E9 spreadsheet_auditor tests scripts benchmarks examples
python scripts/quick_validate.py .
python -m pytest tests -q
```

Then check that the push publishes no personal data: no local paths and no
email addresses, in the files or in the commit messages.

```bash
git grep -n -i -E "[A-Z]:[\\/]+(Users|Documents and Settings)|[/](Users|home)[/][A-Za-z]|App[D]ata" HEAD
git grep -n -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}" HEAD
git log --format="%an <%ae>%n%B" origin/main..HEAD
```

The only expected hit is the GitHub noreply address (the security contact in
`SECURITY.md`, and commit authors). Fix anything else at its source: record a
path relative to the repository, or remove the value. Files under
`benchmarks/` are committed, and the corpus harness records directories with
`corpuslib.display_path()` for this reason.

If a local check refuses a commit or push, fix what it found. Never route
around it: not another checkout, not the GitHub API, not a disabled hook.
When it still refuses after the checks above are clean, tell the user what
it reported and let them decide.
