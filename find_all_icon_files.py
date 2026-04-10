import os, glob

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

target_files = []
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    if "draw" in content and "ink_pen" in content and "bar_chart" in content:
        target_files.append(os.path.basename(fp))

print(f"Files containing all 3 icons: {target_files}")
