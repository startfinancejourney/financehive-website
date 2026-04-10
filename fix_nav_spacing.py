"""
Fix nav link spacing after search bar removal.
Adds 'ml-auto' to the nav links container div to push it rightward,
creating visual balance between the Logo (left) and Start Learning button (right).
Skips learn-finance.html which still has its search bar.
"""
import os
import glob

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

updated = 0
skipped = 0
already_done = 0

for filepath in html_files:
    filename = os.path.basename(filepath)
    
    # Skip learn-finance.html completely
    if filename == "learn-finance.html":
        skipped += 1
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Target: the nav links div that holds Concepts/Sectors/Request a Topic/About
        # Current:  <div class="hidden md:flex gap-6 items-center">
        # Goal:     <div class="hidden md:flex gap-6 items-center ml-auto">
        
        old_class = 'class="hidden md:flex gap-6 items-center"'
        new_class = 'class="hidden md:flex gap-6 items-center ml-auto"'
        
        if old_class in content:
            content = content.replace(old_class, new_class, 1)  # Only first occurrence (nav)
            updated += 1
        elif new_class in content:
            already_done += 1
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    
    except Exception as e:
        print(f"ERROR in {filename}: {e}")

print(f"Total HTML files: {len(html_files)}")
print(f"Updated with ml-auto: {updated}")
print(f"Skipped (learn-finance): {skipped}")
print(f"Already had fix: {already_done}")
