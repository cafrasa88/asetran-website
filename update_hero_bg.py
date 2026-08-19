import shutil, os

src = r"C:\Users\camil\.gemini\antigravity\brain\2e1d1b8b-a3b6-423b-b4ee-183e3f53b5c3\asetran_master_hero_bg_1785605646153.jpg"
dest_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website\assets"

shutil.copy(src, os.path.join(dest_dir, "hero-bg.jpg"))
shutil.copy(src, os.path.join(dest_dir, "asetran_master_hero_bg.jpg"))

print("Successfully updated hero-bg.jpg with the generated fleet inspection photo!")
