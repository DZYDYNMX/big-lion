#!/usr/bin/env python3
"""
BigLion Plumbing Rebrand Script
Converts Liberty Plumbing -> BigLion Plumbing with Richmond VA context
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── text substitutions applied to every HTML/CSS/JS file ──────────────────
TEXT_REPLACEMENTS = [
    # Brand name
    ("Liberty Plumbing",          "BigLion Plumbing"),
    ("Liberty plumbing",          "BigLion Plumbing"),
    ("liberty plumbing",          "BigLion Plumbing"),
    ("Liberty  Plumbing",         "BigLion Plumbing"),
    # Logo span text
    (">Liberty <span>Plumbing</span>", ">BigLion <span>Plumbing</span>"),
    # Phone number
    ("+19367552836",              "+18046166167"),
    ("(936) 755-2836",            "(804) 616-6167"),
    ("936) 755-2836",             "804) 616-6167"),
    ("9367552836",                "8046166167"),
    # Email
    ("info@libertyplumbing.com",  "info@biglionplumbing.com"),
    ("libertyplumbing.com",       "biglionplumbing.com"),
    # Location
    ("Houston, TX",               "Richmond, VA"),
    ("Houston, Texas",            "Richmond, Virginia"),
    ("Houston",                   "Richmond"),         # broad – after specific
    ("77001",                     "23220"),
    ("123 Plumbing Way",          "Richmond, VA"),
    # Domain / canonical
    ("liberty-plumbing-example.com", "biglionplumbing.com"),
    # Why-Choose label
    ("The Liberty Standard",      "The BigLion Standard"),
    # Copyright
    ("© 2026 Liberty Plumbing",   "© 2026 BigLion Plumbing"),
    # Schema name
    ('"name": "Liberty Plumbing"', '"name": "BigLion Plumbing"'),
    # OG / Twitter tags
    ('content="Liberty Plumbing"', 'content="BigLion Plumbing"'),
    # Reviews that mention Liberty by name in text
    ("I highly recommend Liberty Plumbing!",
     "I highly recommend BigLion Plumbing!"),
    ("Have any plumbing issues, Liberty Plumbing is the one to call!!",
     "Have any plumbing issues, BigLion Plumbing is the one to call!!"),
    ("Contacted Liberty Plumbing about",
     "Contacted BigLion Plumbing about"),
    # Service area cities → Richmond VA area cities
    # We'll do the nav dropdown first (specific hrefs)
    ('href="area-houston.html">Houston',   'href="area-richmond.html">Richmond'),
    ('href="area-katy.html">Katy',         'href="area-henrico.html">Henrico County'),
    ('href="area-sugar-land.html">Sugar Land', 'href="area-chesterfield.html">Chesterfield'),
    ('href="area-spring.html">Spring',     'href="area-midlothian.html">Midlothian'),
    ('href="area-cypress.html">Cypress',   'href="area-mechanicsville.html">Mechanicsville'),
    ('href="area-galveston.html">Galveston','href="area-colonial-heights.html">Colonial Heights'),
    # Areas marquee in index.html
    ('href="area-bellaire.html" class="marquee-item">Bellaire',    'href="area-richmond.html" class="marquee-item">Richmond'),
    ('href="area-brazoria.html" class="marquee-item">Brazoria',    'href="area-henrico.html" class="marquee-item">Henrico County'),
    ('href="area-brookshire.html" class="marquee-item">Brookshire','href="area-chesterfield.html" class="marquee-item">Chesterfield'),
    ('href="area-cleveland.html" class="marquee-item">Cleveland',  'href="area-colonial-heights.html" class="marquee-item">Colonial Heights'),
    ('href="area-conroe.html" class="marquee-item">Conroe',        'href="area-midlothian.html" class="marquee-item">Midlothian'),
    ('href="area-cypress.html" class="marquee-item">Cypress',      'href="area-mechanicsville.html" class="marquee-item">Mechanicsville'),
    ('href="area-fort-bend.html" class="marquee-item">Fort Bend',  'href="area-short-pump.html" class="marquee-item">Short Pump'),
    ('href="area-galveston.html" class="marquee-item">Galveston',  'href="area-glen-allen.html" class="marquee-item">Glen Allen'),
    ('href="area-houston.html" class="marquee-item">Houston',      'href="area-ashland.html" class="marquee-item">Ashland'),
    ('href="area-jersey-village.html" class="marquee-item">Jersey Village', 'href="area-sandston.html" class="marquee-item">Sandston'),
    ('href="area-katy.html" class="marquee-item">Katy',            'href="area-highland-springs.html" class="marquee-item">Highland Springs'),
    ('href="area-liberty.html" class="marquee-item">Liberty',      'href="area-bon-air.html" class="marquee-item">Bon Air'),
    ('href="area-magnolia.html" class="marquee-item">Magnolia',    'href="area-powhatan.html" class="marquee-item">Powhatan'),
    ('href="area-missouri-city.html" class="marquee-item">Missouri City','href="area-petersburg.html" class="marquee-item">Petersburg'),
    ('href="area-montgomery.html" class="marquee-item">Montgomery','href="area-hopewell.html" class="marquee-item">Hopewell'),
    ('href="area-richmond.html" class="marquee-item">Richmond',    'href="area-richmond-city.html" class="marquee-item">Richmond City'),
    ('href="area-splendora.html" class="marquee-item">Splendora',  'href="area-chester.html" class="marquee-item">Chester'),
    ('href="area-spring.html" class="marquee-item">Spring',        'href="area-glen-allen.html" class="marquee-item">Glen Allen'),
    ('href="area-sugar-land.html" class="marquee-item">Sugar Land','href="area-tuckahoe.html" class="marquee-item">Tuckahoe'),
    ('href="area-tomball.html" class="marquee-item">Tomball',      'href="area-varina.html" class="marquee-item">Varina'),
    ('href="area-waller.html" class="marquee-item">Waller',        'href="area-goochland.html" class="marquee-item">Goochland'),
    ('href="area-willis.html" class="marquee-item">Willis',        'href="area-hanover.html" class="marquee-item">Hanover'),
    # satisfaction guarantee paragraph
    ("At Liberty Plumbing, we value", "At BigLion Plumbing, we value"),
    # Google reviews link (generic placeholder)
    ("https://maps.app.goo.gl/vxtPHzGMrj5JPKM39",
     "https://www.google.com/search?q=BigLion+Plumbing+Richmond+VA&hl=en#lrd=BigLion"),
    # Title tag
    ("Liberty Plumbing | Premium Emergency &amp; Residential Services",
     "BigLion Plumbing | Reliable Plumbing Services in Richmond, VA"),
    ("Liberty Plumbing | Premium Emergency & Residential Services",
     "BigLion Plumbing | Reliable Plumbing Services in Richmond, VA"),
    # meta description
    ('Liberty Plumbing provides luxury, 24/7 emergency plumbing, repiping, and water heater services. Reliable, clean, and professional.',
     'BigLion Plumbing provides professional residential and commercial plumbing services in Richmond, VA. Reliable, honest, and expert.'),
    # hero h1
    ("Don't Delay, Get Your Quote Today!",
     "Richmond's Trusted Plumbing Pros – Call Today!"),
    # hero sub-paragraph
    ("For a trusted local plumber, simply fill out our booking form. Our friendly team is always here to offer the help you need. Providing upfront quotes with no hidden fees!",
     "BigLion Plumbing delivers fast, dependable service for homeowners and businesses across Richmond, VA. Fill out the form for an upfront quote with no hidden fees!"),
    # footer tagline
    ("For a trusted local plumber, simply fill out our booking form. Our friendly team is always here to offer the help you need. Providing upfront quotes with no hidden fees!",
     "BigLion Plumbing serves Richmond, VA with professional, honest, and dependable plumbing solutions for every home and business."),
    # 24/7 emergency section text
    ("Plumbing emergencies can strike at any time. With every second that passes, you risk more damage occurring to your home or office. Instead, opt for our 24 hour emergency plumber services.",
     "Plumbing emergencies can strike at any time. BigLion Plumbing is ready around the clock to respond fast and prevent further damage to your Richmond home or business."),
    ("Our vehicles are fully equipped 24/7. This means that we don't delay our response time, providing a fast arrival! We'll get to work in diagnosing and resolving the problem. Leaving you with the comfort knowing that your plumbing is in the right hands. <strong>Remember that our plumbers are a call away.</strong>",
     "Our trucks are stocked and ready 24/7. Jamar and the BigLion team will arrive fast, diagnose the issue, and fix it right - leaving your home clean and your plumbing solid. <strong>We're always just a call away.</strong>"),
    # reviews
    ("Justin and his entire team have been nothing but professional",
     "Jamar and his entire team have been nothing but professional"),
    ("I called Justin in a pinch, and he had a technician out there same-day. Zach was super professional, and had my water heaters fixed within minutes. Fast, professional and reliable service!",
     "I called Jamar in a pinch and he had someone out same-day. He was super professional and had my water heater fixed within the hour. Fast, dependable, and honest service!"),
    ("Awesome service and work, very polite and helpful. Not one of those companies that are just out for your money!",
     "Amazing service! Jamar was on time, polite, and fixed our leaking pipe perfectly. BigLion Plumbing is the real deal - honest pricing and quality work."),
    ("Contacted Liberty Plumbing about a gas leak, even though it was after hours they assured me they would have one of their technicians out the next day. They arrived and fixed the problem within a few minutes. When it comes to gas or electric I will always leave it to the professionals!! HIGHLY RECOMMENDED",
     "Contacted BigLion Plumbing about a drain issue after hours. Jamar called back immediately and was at my door first thing in the morning. Fixed it quickly, explained everything, and left the area spotless. HIGHLY RECOMMENDED."),
    # Review names  
    ("Suzan Foster",  "Katherine Moore"),
    ("Dillon Farr",   "Carolyn Eaton"),
    ("Zach Dunn",     "Monique Smith"),
    ("Britney Moody", "Darius Clark"),
    # addresses in schema
    ('"streetAddress": "Richmond, VA"', '"streetAddress": "Richmond, VA"'),
    ('"addressLocality": "Richmond"',   '"addressLocality": "Richmond"'),
    ('"addressRegion": "TX"',           '"addressRegion": "VA"'),
    ('"telephone": "+18046166167"',     '"telephone": "+18046166167"'),
    # about page text
    ("Select your city for targeted local plumbing services.",
     "Select your neighborhood for dedicated local plumbing service in Richmond, VA."),
]

# ── CSS color replacements (red accent → blue) ─────────────────────────────
CSS_COLOR_REPLACEMENTS = [
    # Swap --red accent to a vivid blue
    ("--red: #ef4444;",                              "--red: #1d6bff;"),
    # navy backgrounds stay but shift slightly bluer
    ("--navy-dark: #0a1628;",                        "--navy-dark: #060d1a;"),
    ("--navy-mid: #0f2145;",                         "--navy-mid: #0c1d3f;"),
    ("--navy-light: #162d5a;",                       "--navy-light: #122554;"),
    # cyan accent becomes a brighter electric blue
    ("--cyan: #00a8ff;",                             "--cyan: #3da9fc;"),
    ("--cyan-dark: #0284c7;",                        "--cyan-dark: #0060df;"),
    ("--cyan-gradient: linear-gradient(135deg, #00a8ff, #0284c7);",
     "--cyan-gradient: linear-gradient(135deg, #3da9fc, #0060df);"),
    # shimmer skeleton
    ("background: linear-gradient(90deg, rgba(10,22,40,0.8) 25%, rgba(20,40,70,0.8) 50%, rgba(10,22,40,0.8) 75%);",
     "background: linear-gradient(90deg, rgba(6,13,26,0.8) 25%, rgba(20,45,80,0.8) 50%, rgba(6,13,26,0.8) 75%);"),
]

def replace_in_file(path, replacements):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"  SKIP (read error): {path} - {e}")
        return

    original = content
    for old, new in replacements:
        content = content.replace(old, new)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  UPDATED: {os.path.relpath(path, ROOT)}")
    else:
        print(f"  no change: {os.path.relpath(path, ROOT)}")


# ── Process all HTML and JS files ─────────────────────────────────────────
html_files  = glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True)
js_files    = glob.glob(os.path.join(ROOT, "**/*.js"),   recursive=True)
css_files   = glob.glob(os.path.join(ROOT, "**/*.css"),  recursive=True)

print("\n=== Applying text replacements to HTML + JS ===")
for path in html_files + js_files:
    if '.git' in path or 'rebrand.py' in path:
        continue
    replace_in_file(path, TEXT_REPLACEMENTS)

print("\n=== Applying color replacements to CSS ===")
for path in css_files:
    if '.git' in path:
        continue
    replace_in_file(path, TEXT_REPLACEMENTS + CSS_COLOR_REPLACEMENTS)

print("\nDone!")
