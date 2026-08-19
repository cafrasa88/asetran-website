import os, glob, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

# 1. Update css/styles.css for hero-video brightness and card styles
css_path = os.path.join(html_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Make hero-video 100% visible and bright
css_content = re.sub(
    r'\.hero-video\s*\{[^}]*\}',
    '''.hero-video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  transform: translate(-50%, -50%);
  object-fit: cover;
  z-index: 0;
  opacity: 1 !important;
  filter: brightness(0.95) contrast(1.05) !important;
}''',
    css_content
)

# Make hero-overlay crystal clear
css_content = re.sub(
    r'\.hero-overlay\s*\{[^}]*\}',
    '''.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(10, 14, 23, 0.35) 0%, rgba(10, 14, 23, 0.15) 50%, rgba(10, 14, 23, 0.75) 100%);
  z-index: 1;
  pointer-events: none;
}''',
    css_content
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print("Updated css/styles.css!")

# 2. Update Hero Overlay in all HTML files
for fname in os.listdir(html_dir):
    if not fname.endswith(".html"):
        continue
    filepath = os.path.join(html_dir, fname)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Clear dark gradient overlays over hero videos
    content = re.sub(
        r'background:\s*linear-gradient\([^)]*\);',
        'background: linear-gradient(180deg, rgba(10, 14, 23, 0.35) 0%, rgba(10, 14, 23, 0.15) 50%, rgba(10, 14, 23, 0.75) 100%);',
        content,
        count=1 # only hero overlay
    )

    # Make all photo containers aspect-ratio: 16 / 10 for clean equal proportions
    content = re.sub(
        r'aspect-ratio:\s*1\s*/\s*1',
        'aspect-ratio: 16 / 10',
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated HTML: {fname}")

print("Successfully updated video overlay and 16:10 aspect ratio in all HTML files!")
