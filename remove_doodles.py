"""
Remove the decorative doodles background overlay div from ALL .html files.
The block looks like:
<!-- Decorative Doodles Background Overlay (Reduced noise) -->
<div class="fixed inset-0 pointer-events-none opacity-[0.015] z-[-1] overflow-hidden">
<span ...>currency_rupee</span>
<span ...>lightbulb</span>
</div>
"""
import os, glob, re

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

# Regex pattern to match the comment + div block
# Handles both \r\n and \n line endings, variable whitespace
pattern = re.compile(
    r'<!--\s*Decorative Doodles Background Overlay.*?-->\s*\r?\n'
    r'\s*<div class="fixed inset-0 pointer-events-none opacity-\[0\.015\] z-\[-1\] overflow-hidden">\s*\r?\n'
    r'.*?</div>',
    re.DOTALL
)

removed = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        removed += 1

print(f"Total files scanned: {len(html_files)}")
print(f"Files with decorative overlay removed: {removed}")
