import glob
import re

files = glob.glob("*.html") + ["generate_services.py"]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    # Remove YouTube link
    content = re.sub(r'<a href="[^"]*" aria-label="YouTube">.*?</a>\n?', '', content, flags=re.DOTALL)
    
    # Remove LinkedIn link
    content = re.sub(r'<a href="[^"]*" aria-label="LinkedIn">.*?</a>\n?', '', content, flags=re.DOTALL)
        
    with open(file, "w") as f:
        f.write(content)

print("Removed YouTube and LinkedIn links")
