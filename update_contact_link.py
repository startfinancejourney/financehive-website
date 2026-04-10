"""
Update the footer "Contact" link href to a mailto: link across ALL .html files.
"""
import os, glob

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

old = 'href="about.html">Contact</a>'
new = 'href="mailto:startfinanacejourney@gmail.com?subject=Inquiry%20from%20FinanceHive">Contact</a>'

updated = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1

print(f"Total files scanned: {len(html_files)}")
print(f"Files updated: {updated}")
