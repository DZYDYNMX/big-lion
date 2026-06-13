import glob

NEW_V = "63"
for file in glob.glob("*.html") + ["generate_biglion_areas.py"]:
    with open(file, "r") as f:
        content = f.read()
    
    content = content.replace("styles.css?v=62", f"styles.css?v={NEW_V}")
    content = content.replace("script.js?v=62", f"script.js?v={NEW_V}")
    content = content.replace("v=62", f"v={NEW_V}")
    
    with open(file, "w") as f:
        f.write(content)

print(f"Bumped cache to v={NEW_V}")
