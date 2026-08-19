import os

assets_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website\assets"
files = sorted(os.listdir(assets_dir))

print("All asset files:")
for f in files:
    if f.endswith(('.jpg', '.png', '.mp4', '.webp')):
        size_kb = os.path.getsize(os.path.join(assets_dir, f)) / 1024
        print(f" - {f} ({size_kb:.1f} KB)")
