[EN](https://github.com/Dendroculus/Daily-Heartbeats/blob/main/README.md) | CN

# 💓 每日心跳 (Daily Heartbeats)

[![Actions Status](https://github.com/Dendroculus/Daily-Heartbeats/actions/workflows/daily-commit.yml/badge.svg)](https://github.com/Dendroculus/Daily-Heartbeats/actions/workflows/daily-commit.yml) 
[![License: MIT](https://img.shields.io/github/license/Dendroculus/Daily-Heartbeats)](LICENSE)

一个自动、精简且可靠的每日提交工具，让你的 GitHub 贡献图保持常绿。由 GitHub Actions 和一个小型 Python 脚本驱动。

## 🧭 概览

“每日心跳”通过一个预定的 GitHub Actions 工作流，每天向 `log.txt` 文件追加一个时间戳。每一次提交都像一次“心跳”，帮助你保持稳定、可审查的提交记录。

项目保持小巧且易于上手：将其复制为模板，调整少量设置即可完成。

理想用途：
- 让你需要保持活跃的账户或演示账户的贡献图保持可见
- 在仓库历史中生成轻量级的定时活动（cron-like）
- 作为 GitHub Actions + 简单自动化的教学示例

## ✨ 特性

- 自动每日提交（支持 cron 定时触发和手动触发）
- 精简的 Python 脚本，无需第三方依赖
- 在 `log.txt` 中记录人类可读的时间戳条目
- 易于自定义时间表、提交信息与提交作者

## 🚀 快速设置

1. 使用此仓库作为模板：点击 “Use this template（使用此模板）” 创建一个新仓库。
2. 在新仓库中启用 Actions：Settings → Actions → General → 选择 “Allow all actions and reusable workflows（允许所有 actions 和可重用工作流）” → Save。
3. （可选）提供自定义提交作者：
   - Settings → Secrets and variables → Actions → New repository secret
   - 添加 `COMMIT_NAME = "你的名字"`
   - 添加 `COMMIT_EMAIL = "your-email@example.com"`
   - 如果未提供，工作流将默认使用 `GITHUB_ACTOR`（你的 GitHub 用户名）。
4. 立即测试工作流：
   - 前往 Actions 标签页 → 选择 "Daily Commit" → Run workflow → 选择分支（通常是 `main`）。
5. 完成！工作流将按照 workflow 文件中定义的时间表自动运行。

## ⚙️ 工作原理

- 工作流通过 `on: schedule:`（定时触发）和 `workflow_dispatch`（手动触发）来运行。
- 运行器会检出仓库并执行 `daily_commit.py`。
- `daily_commit.py` 会将当前 UTC 时间戳（和可选信息）追加到 `log.txt`。
- 工作流会设置 git 作者（从 secrets 或 `GITHUB_ACTOR` 获取），然后提交并推送更改。

## 📁 文件结构

```
.
├── .github/workflows/daily-commit.yml
├── daily_commit.py
└── log.txt
```

- `.github/workflows/daily-commit.yml` — 计划任务工作流定义
- `daily_commit.py` — 将时间戳写入 `log.txt` 的脚本
- `log.txt` — 存储心跳时间戳

## 🔧 配置与自定义

- 更改时间表：编辑 `.github/workflows/daily-commit.yml` 并更新 cron 表达式。注意：GitHub Actions 的 cron 使用 UTC。
  示例：每天午夜 UTC 运行
  ```yaml
  on:
    schedule:
      - cron: '0 0 * * *' # 每日 00:00 UTC
    workflow_dispatch: {}
  ```
- 更改提交信息：修改工作流中的 commit 步骤，或更新 `daily_commit.py` 来自定义条目格式。
- 覆盖提交作者：添加仓库 secret `COMMIT_NAME` 和 `COMMIT_EMAIL` 来指定提交作者。
- 本地运行：
  ```bash
  python3 daily_commit.py
  ```
  这将在本地副本中向 `log.txt` 追加一个时间戳，便于测试。

建议的提交信息示例（工作流或脚本可使用）：
```
chore: heartbeat 2025-10-27 00:00:00 UTC
```

## 🛠️ 故障排查

- 在 Actions 标签页中看不到工作流：
  - 确保 `.github/workflows/daily-commit.yml` 文件位于仓库默认分支（如 `main`）上。
  - 在仓库设置中启用 Actions。
- 预定的运行没有发生：
  - Cron 表达式基于 UTC 时间，请确保转换正确。
  - 只有默认分支上的工作流文件才会被安排运行。
- 工作流显示没有创建提交：
  - 检查 Actions 运行日志中的脚本错误。
  - 如果 `daily_commit.py` 没有产生任何更改，通常会看到类似 `git commit -m ... || echo "No changes"` 的容错处理。
- 需要更多权限（罕见）：
  - 标准的 `GITHUB_TOKEN` 通常足够提交。如果需要更广泛权限，可创建 PAT（个人访问令牌）并保存为 secret，但请谨慎使用。

## 📝 日志条目示例

```
Daily heartbeat: 2025-10-27T00:57:51.172795+00:00
```

## 🤝 贡献

欢迎贡献——小而清晰的改进最理想。建议流程：
1. Fork 仓库。
2. 创建主题分支（例如 `feat/custom-format`）。
3. 做出更改并通过 Actions 或本地测试。
4. 针对 `main` 分支发起 Pull Request，并附上简洁描述。

如果你有关于功能（例如可配置的格式、时区或保留策略）的想法，建议先开一个 issue 讨论范围。

## 📜 许可证

MIT — 详情请参阅仓库中的 LICENSE 文件。
