# 💓 Daily Heartbeats

Automated daily commits that keep your GitHub contribution graph alive and consistent — powered by GitHub Actions and Python.

## ⚙️ Overview

This repository runs a scheduled GitHub Actions workflow every 24 hours to append a timestamp entry to `log.txt`. Each commit acts as a "heartbeat," maintaining an active commit history and reflecting continuous project activity.

## 🕒 Workflow Summary

- **Trigger:** Runs daily at **00:00 UTC**
- **Environment:** Ubuntu runner with **Python 3.x**
- **Process:**
  1. Executes `daily_commit.py`
  2. Appends a new timestamp to `log.txt`
  3. Commits and pushes the change automatically

## 📁 File Structure

| File | Description |
|------|-------------|
| `.github/workflows/daily-commit.yml` | Defines the automated workflow and schedule |
| `daily_commit.py` | Generates a new timestamp entry |
| `log.txt` | Stores all recorded heartbeat timestamps |

## 🚀 Usage

To trigger the workflow manually:
1. Navigate to the **Actions** tab in your repository.
2. Select **Daily Commit** from the workflow list.
3. Click **Run workflow** and choose the branch (usually `main`).

A new heartbeat entry will be committed instantly when run manually, or automatically at the scheduled time.

## 🧾 Example Log Entry

```
2025-10-25 00:00:00 - Heartbeat executed successfully
```

## ⚙️ Customization

- To change the schedule, edit `.github/workflows/daily-commit.yml` and update the `cron` expression under `on: schedule:`.
- Cron times are interpreted in UTC by GitHub Actions.
- Ensure the workflow file is on the repository's default branch (e.g., `main`) for scheduled runs to be registered.

## 📜 License

Licensed under the **MIT License**.  
You are free to use, modify, and distribute this project for personal or educational purposes.
