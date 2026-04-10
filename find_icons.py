import os, glob, re

workspace = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))

for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Looking for a div with opacity-20 or similar, containing spans with material-symbols-outlined
    # Or just the cluster of icons.
    if "material-symbols-outlined" in content:
        # Match a container with multiple symbols
        matches = re.findall(r'<span[^>]*material-symbols-outlined[^>]*>.*?</span>', content, re.DOTALL)
        if len(matches) >= 3:
            # Check if they are close together
            # A more robust check: find the container
            container_matches = re.findall(r'<div[^>]*>.*?material-symbols-outlined.*?material-symbols-outlined.*?material-symbols-outlined.*?</div>', content, re.DOTALL)
            if container_matches:
                print(f"Candidate in {os.path.basename(fp)}")
                for m in container_matches:
                    # Filter for those likely to be the "footer icons"
                    if "text-6xl" in m or "opacity-20" in m:
                        print(f"  Matches criteria: {m[:100]}...")
