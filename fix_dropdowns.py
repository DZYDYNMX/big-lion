import os
import glob

old_dropdown = """                        <a href="areas.html">View All Areas</a>
                        <a href="area-houston.html">Richmond</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>"""

new_dropdown = """                        <a href="areas.html">View All Areas</a>
                        <a href="area-richmond-city.html">Richmond City</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>"""

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    if old_dropdown in content:
        content = content.replace(old_dropdown, new_dropdown)
        with open(file, "w") as f:
            f.write(content)
        print(f"Updated {file}")

print("Done")
