import glob

files = glob.glob("*.html") + ["generate_biglion_areas.py"]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    content = content.replace("areas-hero.webp", "areas-hero.jpg")
    content = content.replace("about-team.webp", "about-team.jpg")
    content = content.replace("styles.css?v=55", "styles.css?v=56")
    
    with open(file, "w") as f:
        f.write(content)

print("Updated image extensions and bumped CSS version to 56")
