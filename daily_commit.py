from datetime import datetime, UTC

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"Daily heartbeat: {datetime.now(UTC).isoformat()}\n")
