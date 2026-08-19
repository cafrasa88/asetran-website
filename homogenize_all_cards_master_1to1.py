import os, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

# Enforce 1:1 aspect-ratio in all photo containers across all HTML files
for fname in os.listdir(html_dir):
    if not fname.endswith(".html"):
        continue
    filepath = os.path.join(html_dir, fname)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace aspect-ratio: 16 / 10 with aspect-ratio: 1 / 1
    content = content.replace("aspect-ratio: 16 / 10", "aspect-ratio: 1 / 1")
    content = content.replace("aspect-ratio: 16/10", "aspect-ratio: 1 / 1")
    
    # Ensure all image containers have aspect-ratio: 1 / 1
    content = re.sub(
        r'style="width:\s*100%;\s*aspect-ratio:[^;]*;',
        'style="width: 100%; aspect-ratio: 1 / 1;',
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully updated all HTML files to 1:1 aspect ratio!")
