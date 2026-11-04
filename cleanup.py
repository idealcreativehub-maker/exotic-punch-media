"""Deletes post videos 7 days after their post time.
delete_list.json: {"file.mp4": {"posted_at": "...", "delete_after": "YYYY-MM-DDTHH:MM:SS+00:00"}}
Claude adds an entry when it uploads a video (delete_after = post time + 7 days).
To keep a video longer, change its delete_after date or remove its entry."""
import datetime as dt
import json
import os

LIST = "delete_list.json"
now = dt.datetime.now(dt.timezone.utc)
data = json.load(open(LIST)) if os.path.exists(LIST) else {}
keep = {}
for name, info in data.items():
    when = dt.datetime.fromisoformat(info["delete_after"])
    if when <= now:
        if os.path.exists(name):
            os.remove(name)
            print(f"deleted {name}")
    else:
        keep[name] = info
        print(f"keeping {name} until {info['delete_after']}")
with open(LIST, "w") as f:
    json.dump(keep, f, indent=2)
