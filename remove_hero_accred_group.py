import os, glob, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

for filepath in glob.glob(os.path.join(html_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove hero-accred-group markup from hero section
    content = re.sub(
        r'<div class="hero-accred-group">.*?</div>\s*',
        '',
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Removed hero-accred-group from: {os.path.basename(filepath)}")

print("Successfully removed accreditation logo group from all Hero sections!")
