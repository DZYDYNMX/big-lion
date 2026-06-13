import glob
import re

files = glob.glob("*.html") + ["generate_biglion_areas.py"]
NEW_V = "57"

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    # Update CSS and JS cache versions
    content = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={NEW_V}', content)
    content = re.sub(r'script\.js\?v=\d+', f'script.js?v={NEW_V}', content)
    
    # Add/update cache busters on the hero images
    content = re.sub(r'hero-bg\.jpg(\?v=\d+)?', f'hero-bg.jpg?v={NEW_V}', content)
    content = re.sub(r'areas-hero\.jpg(\?v=\d+)?', f'areas-hero.jpg?v={NEW_V}', content)
    content = re.sub(r'about-team\.jpg(\?v=\d+)?', f'about-team.jpg?v={NEW_V}', content)
    
    with open(file, "w") as f:
        f.write(content)

print(f"Busted all caches to v={NEW_V}")
