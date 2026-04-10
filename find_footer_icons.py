import os, glob

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

icons = ["draw", "ink_pen", "bar_chart", "assignment", "edit", "analytics", "trending_up"]

found = []
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Check the last 100 lines (footer area is usually near the end)
    footer_area = "".join(lines[-150:])
    for icon in icons: 
        pass
    
    match_count = sum(1 for icon in icons if icon in footer_area)
    if match_count >= 2:
        found.append((os.path.basename(fp), match_count))

print(found)
