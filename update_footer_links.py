"""
Task 3: Update footer Privacy and Terms links across ALL .html files.
- Privacy link: href="#" -> href="privacy.html"
- Terms link: href="#" -> href="terms.html"
"""
import os
import glob

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

updated = 0
privacy_fixed = 0
terms_fixed = 0

for filepath in html_files:
    filename = os.path.basename(filepath)
    
    # Skip the newly created files (they already have correct links)
    if filename in ("privacy.html", "terms.html"):
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix Privacy link: href="#">Privacy -> href="privacy.html">Privacy
        old_privacy = 'href="#">Privacy</a>'
        new_privacy = 'href="privacy.html">Privacy</a>'
        if old_privacy in content:
            content = content.replace(old_privacy, new_privacy)
            privacy_fixed += 1
        
        # Fix Terms link: href="#">Terms -> href="terms.html">Terms
        old_terms = 'href="#">Terms</a>'
        new_terms = 'href="terms.html">Terms</a>'
        if old_terms in content:
            content = content.replace(old_terms, new_terms)
            terms_fixed += 1
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
    
    except Exception as e:
        print(f"ERROR in {filename}: {e}")

print(f"Total HTML files scanned: {len(html_files)}")
print(f"Files with footer updated: {updated}")
print(f"Privacy links fixed: {privacy_fixed}")
print(f"Terms links fixed: {terms_fixed}")
