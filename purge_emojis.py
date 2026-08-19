import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace featured badge emoji containers
content = re.sub(r'<span class="featured-icon">[^<]+</span>', '', content)

# Remove all unicode emojis completely
emoji_regex = re.compile(r'[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff\u2b50\u2b55\u200d]')
content = emoji_regex.sub('', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("100% of emojis purged from index.html!")
