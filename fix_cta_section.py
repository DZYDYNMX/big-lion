import os
import glob

old_string = '<section class="section" style="padding-top: 4rem; padding-bottom: 4rem; text-align: center; background: var(--navy-mid);">'
new_string = '<section class="section section-mid" style="padding-top: 4rem; padding-bottom: 4rem; text-align: center;">'

files = glob.glob("*.html") + ["generate_services.py"]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    if old_string in content:
        content = content.replace(old_string, new_string)
        with open(file, "w") as f:
            f.write(content)
        print(f"Fixed {file}")

