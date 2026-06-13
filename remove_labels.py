import glob
import re
import os

files_updated = 0

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()

    # The pattern matches <div class="label">...</div> and possibly trailing whitespace/newlines
    pattern = re.compile(r'<div class="label">.*?</div>\s*', re.IGNORECASE | re.DOTALL)
    
    new_content = pattern.sub('', content)
    
    # Bump cache buster while we're at it
    new_content = new_content.replace("styles.css?v=37", "styles.css?v=38")
    new_content = new_content.replace("script.js?v=35", "script.js?v=38")

    if new_content != content:
        with open(file, "w") as f:
            f.write(new_content)
        files_updated += 1

print(f"Removed labels from {files_updated} files.")
