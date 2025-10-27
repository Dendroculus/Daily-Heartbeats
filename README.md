EN | [中文](https://github.com/Dendroculus/Daily-Heartbeats/blob/main/docs/readmeCN.md)

# 💓 Daily Heartbeats

[![Actions Status](https://github.com/Dendroculus/Daily-Heartbeats/actions/workflows/daily-commit.yml/badge.svg)](https://github.com/Dendroculus/Daily-Heartbeats/actions/workflows/daily-commit.yml) [![License: MIT](https://img.shields.io/github/license/Dendroculus/Daily-Heartbeats)](LICENSE)

Automated, minimal, and reliable daily commits to keep your GitHub contribution graph active — powered by GitHub Actions and a tiny Python script.



## 🧭 Overview

Daily Heartbeats appends a timestamp to `log.txt` once per day via a scheduled GitHub Actions workflow. Each commit acts as a "heartbeat" that preserves a steady, auditable commit history. The project is intentionally small and easy to adopt: copy as a template, adjust one or two settings, and you're done.

Ideal uses:
- Maintain an always-active contribution graph for demos or accounts you want to keep active.
- Lightweight cron-like activity that’s visible in the repository history.
- Educational example for GitHub Actions + simple automation.



## ✨ Features

- Automated daily commits using GitHub Actions (cron + manual trigger).
- Minimal Python script with no external dependencies.
- Human-readable timestamp entries in `log.txt`.
- Easy to customize schedule, commit message, and commit author.



## 🚀 Quick setup

1. Use this repository as a template: click **Use this template** and create a new repository.
2. Enable Actions in your new repo: Settings → Actions → General → Allow all actions and reusable workflows → Save.
3. (Optional) Provide a custom commit author:
   - Settings → Secrets and variables → Actions → New repository secret
   - Add `COMMIT_NAME` = "Your Name"
   - Add `COMMIT_EMAIL` = "your-email@example.com"
   If not provided, the workflow will use `GITHUB_ACTOR`.

4. Test the workflow immediately:
   - Go to the Actions tab → select "Daily Commit" → Run workflow → choose branch (usually `main`).

That’s it — the workflow will run automatically on the schedule defined in the workflow file.



## ⚙️ How it works

1. The workflow triggers on a schedule (`on: schedule:`) and supports `workflow_dispatch` for manual runs.
2. The runner checks out the repo and runs `daily_commit.py`.
3. `daily_commit.py` appends the current UTC timestamp (and optional message) to `log.txt`.
4. The workflow sets the git author (from secrets or `GITHUB_ACTOR`), commits, and pushes the change.



## 📁 File structure

- `.github/workflows/daily-commit.yml` — Scheduled workflow definition
- `daily_commit.py` — Writes a timestamp entry to `log.txt`
- `log.txt` — Stores the heartbeat timestamps

Example tree:
```
.
├── .github/workflows/daily-commit.yml
├── daily_commit.py
└── log.txt
```



## 🔧 Configuration & customization

Change the schedule
- Edit `.github/workflows/daily-commit.yml` and update the `cron` expression. GitHub Actions cron expressions use UTC.

Example: run every day at midnight UTC
```yaml
on:
  schedule:
    - cron: '0 0 * * *' # 00:00 UTC daily
  workflow_dispatch: {}
```

Change the commit message
- Modify the commit step in the workflow, or update `daily_commit.py` to format entries as you prefer.

Override commit author
- Add repository secrets `COMMIT_NAME` and `COMMIT_EMAIL` to use a custom author for these commits.

Run locally
```bash
python3 daily_commit.py
```
This appends one timestamp to `log.txt` in your local copy (useful for testing).

Suggested commit message example (used by the workflow or script)
```
chore: heartbeat 2025-10-27 00:00:00 UTC
```



## 🛠️ Troubleshooting

- Workflow does not appear in Actions tab:
  - Ensure `.github/workflows/daily-commit.yml` is on the repository default branch (e.g., `main`).
  - Confirm Actions are allowed in repository settings.

- Scheduled runs not happening:
  - Cron expressions are evaluated in UTC. Convert local times to UTC when editing the cron.
  - Workflows are only scheduled for workflow files on the default branch.

- Workflow shows no commit created:
  - Check the Actions run logs for script errors.
  - If `daily_commit.py` produced no change, the commit step should be resilient (common pattern: `git commit -m ... || echo "No changes"`).

- Need more permissions (rare):
  - The standard `GITHUB_TOKEN` is sufficient for commits. If you need broader permissions, create a PAT and store it as a secret — use carefully.



## 📝 Example log entry

```
Daily heartbeat: 2025-10-27T00:57:51.172795+00:00
```



## 🤝 Contributing

Contributions welcome — small, clear improvements are ideal here.

Suggested workflow:
1. Fork the repository.
2. Create a topic branch (e.g., `feat/custom-format`).
3. Make changes and test locally or via Actions.
4. Open a pull request against `main` with a concise description.

If you have ideas for features (e.g., configurable formats, timezones, or retention policies), open an issue first so we can discuss scope.



## 📜 License

MIT — see the LICENSE file for details.

