import os

assets_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website\assets"
files = os.listdir(assets_dir)
hero_files = [f for f in files if "hero" in f.lower() or "bg" in f.lower()]
print("Hero asset files:", hero_files)

for f in hero_files:
    path = os.path.join(assets_dir, f)
    size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"{f}: {size_mb:.2f} MB")
