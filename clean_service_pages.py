import os, glob, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

for filepath in glob.glob(os.path.join(html_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean hero inline padding
    content = re.sub(
        r'<section class="service-detail-hero" style="[^"]*">',
        '<section class="service-detail-hero">',
        content
    )

    # 2. Clean #solicitar container inline styles
    content = re.sub(
        r'<div id="solicitar" class="glass" style="[^"]*">',
        '<div id="solicitar" class="glass solicitar-box">',
        content
    )

    # 3. Clean form inline styles
    content = re.sub(
        r'<form style="display: grid; grid-template-columns: repeat\(2, 1fr\); gap: 1\.5rem;">',
        '<form class="service-inquiry-form">',
        content
    )

    # 4. Clean textarea inline styles
    content = re.sub(
        r'<textarea([^>]*)style="grid-column: span 2;[^"]*"',
        r'<textarea\1class="form-textarea"',
        content
    )

    # 5. Clean form action div inline styles
    content = re.sub(
        r'<div style="grid-column: span 2; display: flex; justify-content: space-between; align-items: center;">',
        '<div class="form-actions-wrapper">',
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully cleaned inline form and hero styles across all HTML files!")
