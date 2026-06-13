import glob

files = glob.glob("*.html") + ["generate_biglion_areas.py"]
NEW_V = "58"

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    # Fix index.html pointing to old hero-plumber.webp
    content = content.replace("hero-plumber.webp", f"hero-bg.jpg?v={NEW_V}")
    
    # Fix areas.html pointing to .png
    content = content.replace("areas-hero.png", f"areas-hero.jpg?v={NEW_V}")
    
    # Also update cache version to force reload
    content = content.replace("styles.css?v=57", f"styles.css?v={NEW_V}")
    content = content.replace("script.js?v=57", f"script.js?v={NEW_V}")
    
    # Update existing v=57 cache busters
    content = content.replace("v=57", f"v={NEW_V}")
    
    with open(file, "w") as f:
        f.write(content)

print(f"Fixed wrong image references and busted cache to v={NEW_V}")
