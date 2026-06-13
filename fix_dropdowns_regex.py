import os
import glob
import re

new_dropdown = """<div class="dropdown-menu" style="max-height: 400px; overflow-y: auto;">
                        <a href="areas.html">View All Areas</a>
                        <a href="area-richmond-city.html">Richmond City</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-short-pump.html">Short Pump</a>
                        <a href="area-glen-allen.html">Glen Allen</a>
                        <a href="area-ashland.html">Ashland</a>
                        <a href="area-sandston.html">Sandston</a>
                        <a href="area-highland-springs.html">Highland Springs</a>
                        <a href="area-bon-air.html">Bon Air</a>
                        <a href="area-powhatan.html">Powhatan</a>
                        <a href="area-petersburg.html">Petersburg</a>
                        <a href="area-hopewell.html">Hopewell</a>
                        <a href="area-chester.html">Chester</a>
                        <a href="area-tuckahoe.html">Tuckahoe</a>
                        <a href="area-varina.html">Varina</a>
                        <a href="area-goochland.html">Goochland</a>
                        <a href="area-hanover.html">Hanover</a>
                    </div>"""

for file in glob.glob("area-*.html"):
    with open(file, "r") as f:
        content = f.read()

    # The area files might have different contents. We can just replace the <div class="dropdown-menu">...</div>
    # block after "Service Areas".
    # Find the Service Areas link
    pattern = re.compile(r'(<a href="areas\.html"[^>]*>Service Areas <span class="desktop-only-arrow">▾</span></a>\s*)<div class="dropdown-menu">.*?</div>', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(r'\1' + new_dropdown, content)
        with open(file, "w") as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file}")
print("Done")
