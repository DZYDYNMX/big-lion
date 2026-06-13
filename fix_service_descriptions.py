import os
import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()

    # Bump cache busters
    content = content.replace("styles.css?v=34", "styles.css?v=35")
    content = content.replace("script.js?v=33", "script.js?v=35")

    # Only process service-*.html for the paragraph hiding
    if file.startswith("service-") and file.endswith(".html"):
        # The target paragraph
        target_style = 'style="font-size: 1.1rem; color: #e2e8f0; margin-bottom: 2rem; line-height: 1.6;"'
        
        # We need to find the <p> with this style
        pattern = re.compile(rf'(<p {target_style}>)(.*?)(</p>)', re.DOTALL)
        
        def replacer(match):
            p_open = match.group(1)
            text = match.group(2)
            p_close = match.group(3)
            
            # Don't double wrap
            if "hide-on-mobile" in text:
                return match.group(0)
            
            # Find the second or third sentence
            sentences = [s + "." for s in text.split(". ") if s]
            if text.endswith("."):
                sentences[-1] = sentences[-1][:-1] # remove double dot
            else:
                sentences[-1] = sentences[-1][:-1] # might not end with dot, just careful
                
            # A more robust split: find all ". "
            parts = text.split(". ")
            if len(parts) > 3:
                # keep first two sentences visible
                visible = ". ".join(parts[:2]) + ". "
                hidden = ". ".join(parts[2:])
                return f'{p_open}{visible}<span class="hide-on-mobile">{hidden}</span>{p_close}'
            elif len(parts) == 3:
                visible = parts[0] + ". "
                hidden = ". ".join(parts[1:])
                return f'{p_open}{visible}<span class="hide-on-mobile">{hidden}</span>{p_close}'
            else:
                return match.group(0)
        
        content = pattern.sub(replacer, content)

    with open(file, "w") as f:
        f.write(content)

print("Done")
