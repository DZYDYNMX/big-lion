import os
import glob

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    content = content.replace("styles.css?v=47", "styles.css?v=48")
    with open(file, "w") as f:
        f.write(content)
print("Bumped CSS version to 48")
