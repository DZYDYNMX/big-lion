import re

with open("index.html", "r") as f:
    content = f.read()

# Remove the review avatars
content = re.sub(r'[ \t]*<div class="review-avatar[^>]*>.*?</div>\n*', '', content)

# Bump cache to v=62
content = content.replace("styles.css?v=61", "styles.css?v=62")
content = content.replace("script.js?v=61", "script.js?v=62")

with open("index.html", "w") as f:
    f.write(content)

print("Stripped avatars and bumped index cache to v=62")
