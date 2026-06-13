import glob

files = glob.glob("*.html") + glob.glob("*.py") + ["styles.css"]

for file in files:
    if file == "replace_emdash.py":
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '—' in content:
        content = content.replace('—', '-')
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

print("Replaced all em-dashes with standard hyphens")
