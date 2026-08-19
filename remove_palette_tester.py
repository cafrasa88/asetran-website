import os, glob, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

for filepath in glob.glob(os.path.join(html_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove theme switcher markup
    content = re.sub(
        r'<div class="theme-switcher-wrapper">.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="theme-switcher-wrapper">.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully removed theme switcher HTML from all pages!")
