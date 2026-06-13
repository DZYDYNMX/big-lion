import os
import glob

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    content = content.replace("styles.css?v=58", "styles.css?v=59")
    content = content.replace("script.js?v=58", "script.js?v=59")
    with open(file, "w") as f:
        f.write(content)
print("Bumped CSS version to 59")
