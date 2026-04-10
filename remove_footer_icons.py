import os, glob, re

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

# Patterns to look for
icon_patterns = [
    r'draw',
    r'ink_pen',
    r'bar_chart'
]

container_regex = re.compile(r'<div[^>]*opacity-(?:10|20)[^>]*>.*?<span[^>]*material-symbols-outlined[^>]*>.*?</div>', re.DOTALL)

removed_count = 0

for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We are looking for the cluster specifically
    # Let's search for the icons in sequence
    new_content = re.sub(r'<!-- Illustration Spacer -->\s*<div[^>]*>.*?draw.*?ink_pen.*?bar_chart.*?</div>', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed icon cluster from {os.path.basename(fp)}")
        removed_count += 1

print(f"Total files updated: {removed_count}")
