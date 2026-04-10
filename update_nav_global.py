"""
Global Navigation Update Script
- Task 1: Rename "Learn Finance" nav link text to "Concepts" in ALL .html files
- Task 2: Remove search bar from ALL .html files EXCEPT learn-finance.html
- Does NOT touch the "Start Learning" button
- Does NOT change any href paths
"""
import os
import re
import glob

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"

# Get all .html files
html_files = glob.glob(os.path.join(workspace, "*.html"))

task1_count = 0  # Files where "Learn Finance" link text was renamed
task2_count = 0  # Files where search bar was removed
skipped_search = []  # Files where search bar was intentionally kept
errors = []

for filepath in html_files:
    filename = os.path.basename(filepath)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # ===== TASK 1: Rename "Learn Finance" to "Concepts" =====
        # Match the nav link with href="learn-finance.html" and text "Learn Finance"
        # Be careful NOT to match the "Start Learning" button
        # Pattern: the nav link text ">Learn Finance</a>" (not touching href)
        old_nav = 'href="learn-finance.html">Learn Finance</a>'
        new_nav = 'href="learn-finance.html">Concepts</a>'
        
        if old_nav in content:
            content = content.replace(old_nav, new_nav)
            task1_count += 1
        
        # ===== TASK 2: Remove search bar (EXCEPT learn-finance.html) =====
        if filename != "learn-finance.html":
            # The search bar is a div containing input + search icon span
            # Pattern varies slightly but structure is consistent:
            # <div class="relative group flex items-center">
            # <input ... placeholder="Search concepts..." .../>
            # <span ...>search</span>
            # </div>
            #
            # We need to remove this entire div block
            
            # Use regex to match the search container div
            # Match from '<div class="relative group flex items-center">' to the closing '</div>'
            # that contains the search input
            search_pattern = r'<div class="relative group flex items-center">\s*\n?\s*<input[^>]*placeholder="Search concepts\.\.\."[^>]*/>\s*\n?\s*<span[^>]*>search</span>\s*\n?\s*</div>'
            
            match = re.search(search_pattern, content)
            if match:
                content = content[:match.start()] + content[match.end():]
                task2_count += 1
            else:
                # Try alternate pattern with \r\n
                search_pattern2 = r'<div class="relative group flex items-center">\r?\n\s*<input[^>]*placeholder="Search concepts\.\.\."[^>]*/>\r?\n\s*<span[^>]*>search</span>\r?\n\s*</div>'
                match2 = re.search(search_pattern2, content)
                if match2:
                    content = content[:match2.start()] + content[match2.end():]
                    task2_count += 1
        else:
            skipped_search.append(filename)
        
        # Write back only if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    
    except Exception as e:
        errors.append(f"{filename}: {str(e)}")

print(f"Total HTML files processed: {len(html_files)}")
print(f"Task 1 - 'Learn Finance' renamed to 'Concepts': {task1_count} files")
print(f"Task 2 - Search bar removed: {task2_count} files")
print(f"Search bar intentionally kept in: {skipped_search}")
if errors:
    print(f"Errors: {errors}")
else:
    print("No errors encountered.")
