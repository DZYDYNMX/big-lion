import glob

files = glob.glob("*.html") + ["generate_services.py"]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    # Facebook
    if 'href="#" aria-label="Facebook"' in content:
        content = content.replace(
            'href="#" aria-label="Facebook"',
            'href="https://web.facebook.com/p/Biglion-plumbing-services-61584886455564/?_rdc=1&_rdr" target="_blank" rel="noopener noreferrer" aria-label="Facebook"'
        )
    
    # Instagram
    if 'href="#" aria-label="Instagram"' in content:
        content = content.replace(
            'href="#" aria-label="Instagram"',
            'href="https://www.instagram.com/biglionplumbingservice" target="_blank" rel="noopener noreferrer" aria-label="Instagram"'
        )
        
    with open(file, "w") as f:
        f.write(content)

print("Updated social links")
