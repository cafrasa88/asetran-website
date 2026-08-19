with open(r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website\css\styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if ".hero" in line or "hero-video" in line or "hero-overlay" in line:
        print(f"Line {i+1}: {line.strip()}")
