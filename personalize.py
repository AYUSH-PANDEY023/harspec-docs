"""Replace the placeholders with your details.   python scripts/personalize.py YOUR_GITHUB_NAME "Your Name" you@email.com"""
import os
import sys

if len(sys.argv) != 4:
    sys.exit(__doc__)
user, name, email = sys.argv[1:]
changed = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
    for f in files:
        if f == "personalize.py" or not f.endswith((".md", ".toml", ".yml", ".html", ".xml", ".txt", ".json", ".svg", ".js", ".css", ".py")):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding="utf-8").read()
        t = s.replace("YOUR_USERNAME", user).replace("YOUR_NAME", name).replace("YOUR_EMAIL", email)
        if t != s:
            open(p, "w", encoding="utf-8").write(t)
            changed += 1
print(f"Updated {changed} files for {user}.")
