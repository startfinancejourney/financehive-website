import os, glob, re

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

found_files = []

for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find spans that are material-symbols-outlined
    spans = re.findall(r'<span[^>]*material-symbols-outlined[^>]*>.*?</span>', content, re.DOTALL)
    if len(spans) >= 3:
        # Check if 3 spans are within 200 characters of each other
        # This is a bit rough but works for clustering.
        for i in range(len(spans) - 2):
            text_cluster = content[content.find(spans[i]) : content.find(spans[i+2]) + len(spans[i+2])]
            if len(text_cluster) < 500:
                # Check icons. If they match the "placeholder" ones:
                if any(x in text_cluster for x in ["draw", "ink_pen", "bar_chart", "analytics", "assignment", "edit"]):
                    # Check if it's near the bottom (in the footer area)
                    # For simplicity, just print it for now.
                    found_files.append((os.path.basename(fp), text_cluster[:100]))
                    break

print(found_files)
