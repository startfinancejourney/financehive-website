import os, glob, re

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

found_files = []

for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find SVG tags
    svgs = re.findall(r'<svg.*?</svg>', content, re.DOTALL)
    if len(svgs) >= 3:
        for i in range(len(svgs) - 2):
            # Check proximity
            start_idx = content.find(svgs[i])
            end_idx = content.find(svgs[i+2]) + len(svgs[i+2])
            if end_idx - start_idx < 1000:
                # Potential cluster
                cluster = content[start_idx:end_idx]
                if "opacity" in cluster or "gray" in cluster or "stone" in cluster:
                    found_files.append((os.path.basename(fp), cluster[:100]))
                    break

print(found_files)
