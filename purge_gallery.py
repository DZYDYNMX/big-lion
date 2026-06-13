import os
import glob
import re

files = glob.glob("*.html") + glob.glob("*.py") + ["sitemap.xml"]

for file in files:
    if not os.path.exists(file):
        continue
        
    with open(file, "r") as f:
        content = f.read()

    # 1. Remove nav links to gallery.html (any label)
    content = re.sub(r'[ \t]*<li><a href="gallery\.html"[^>]*>.*?</a></li>\n?', '', content)

    # 2. In index.html, remove the entire Gallery Marquee section
    if file == "index.html":
        content = re.sub(r'[ \t]*<!-- GALLERY MARQUEE -->\s*<section class="section section-mid">.*?</section>\n*', '', content, flags=re.DOTALL)
        
    # 3. In sitemap files, remove the URL block for gallery
    if file == "sitemap.xml":
        content = re.sub(r'[ \t]*<url>\s*<loc>https://biglionplumbing\.com/gallery\.html</loc>.*?</url>\n*', '', content, flags=re.DOTALL)

    # 4. In Python generators, remove gallery from sitemap generator if present
    if file == "generate_sitemap.py":
        content = re.sub(r'[^\\n]*"gallery\.html"[^\\n]*\n', '', content)

    with open(file, "w") as f:
        f.write(content)

# Delete the actual file
if os.path.exists("gallery.html"):
    os.remove("gallery.html")

# Delete the assets/gallery folder to clean up space
os.system("rm -rf assets/gallery")

print("Gallery purged successfully.")
