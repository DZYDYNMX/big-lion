import glob
import re

# Fix CSS select appearance
with open("styles.css", "r") as f:
    css = f.read()

hero_select_css = """
.hero-form select {
    appearance: none;
    -webkit-appearance: none;
    background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2300D4FF%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    background-size: 0.8rem auto;
    padding-right: 2.5rem;
    color: #94a3b8; /* Matching placeholder text color initially */
}
.hero-form select:focus {
    color: var(--white);
}
"""
if ".hero-form select {" not in css:
    css += hero_select_css

with open("styles.css", "w") as f:
    f.write(css)

# Fix HTML mobile buttons and bump cache version
NEW_V = "60"
files = glob.glob("*.html") + ["generate_biglion_areas.py"]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    # Change btn-cyan to btn-outline for the hide-on-desktop contact buttons
    content = content.replace('class="btn btn-cyan hide-on-desktop contact-btn"', 'class="btn btn-outline hide-on-desktop contact-btn"')
    
    # Cache bump
    content = content.replace("styles.css?v=59", f"styles.css?v={NEW_V}")
    content = content.replace("script.js?v=59", f"script.js?v={NEW_V}")
    content = content.replace("v=59", f"v={NEW_V}")
    
    with open(file, "w") as f:
        f.write(content)

print(f"Fixed Safari select and changed mobile button to outline. Cache bumped to v={NEW_V}")
