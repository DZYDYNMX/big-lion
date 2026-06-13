import os
import glob

# Identify the old block we want to replace
# We want to replace the entire <div class="dropdown-menu"> under the Service Areas dropdown

old_nav_block = """                    <a href="areas.html">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu">
                        <a href="areas.html">View All Areas</a>
                        <a href="area-richmond-city.html">Richmond City</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>
                        
                    </div>"""

# Note the exact 20 areas we have
new_nav_block = """                    <a href="areas.html" class="active">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu" style="max-height: 400px; overflow-y: auto;">
                        <a href="areas.html">View All Areas</a>
                        <a href="area-richmond-city.html">Richmond City</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>
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

# we should make sure we don't break the "active" class logic if the page is currently on areas.html
for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()

    # The block might have class="active" or not
    block1 = """                    <a href="areas.html">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu">
                        <a href="areas.html">View All Areas</a>
                        <a href="area-richmond-city.html">Richmond City</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>
                        
                    </div>"""
                    
    block2 = """                    <a href="areas.html" class="active">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu">
                        <a href="areas.html">View All Areas</a>
                        <a href="area-richmond-city.html">Richmond City</a>
                        <a href="area-henrico.html">Henrico County</a>
                        <a href="area-chesterfield.html">Chesterfield</a>
                        <a href="area-midlothian.html">Midlothian</a>
                        <a href="area-mechanicsville.html">Mechanicsville</a>
                        <a href="area-colonial-heights.html">Colonial Heights</a>
                        
                    </div>"""
                    
    updated1 = """                    <a href="areas.html">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu" style="max-height: 400px; overflow-y: auto;">
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
                    
    updated2 = """                    <a href="areas.html" class="active">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu" style="max-height: 400px; overflow-y: auto;">
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
                    
    if block1 in content:
        content = content.replace(block1, updated1)
        with open(file, "w") as f:
            f.write(content)
        print(f"Updated {file}")
    elif block2 in content:
        content = content.replace(block2, updated2)
        with open(file, "w") as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file} (pattern not found)")

print("Done")
