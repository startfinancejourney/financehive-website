import os
import glob
import re

dir_path = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(dir_path, "*.html*")) 

# New combined script for search and active highlighting
script_content = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Search Filtering & Focus
            const searchInput = document.querySelector('nav input[placeholder="Search concepts..."]');
            if (searchInput) {
                const searchIcon = searchInput.nextElementSibling;
                if (searchIcon && searchIcon.textContent.trim() === 'search') {
                    searchIcon.style.cursor = 'pointer';
                    searchIcon.addEventListener('click', () => searchInput.focus());
                }

                searchInput.addEventListener('input', function() {
                    const query = this.value.toLowerCase().trim();
                    // Target concept cards (article) and sector cards (sketch-border items in grids)
                    const cards = document.querySelectorAll('article, .grid > .sketch-border, .grid > div[onclick*="sector-"]');
                    
                    cards.forEach(card => {
                        const text = card.textContent.toLowerCase();
                        if (text.includes(query)) {
                            card.style.display = ''; // Revert to original layout (flex/block etc)
                        } else {
                            card.style.display = 'none';
                        }
                    });
                });
            }
            
            // Active Navigation Highlighting
            const navLinks = document.querySelectorAll('nav a');
            let currentPath = window.location.pathname.split('/').pop().split('?')[0].split('#')[0];
            if (!currentPath || currentPath === '') {
                currentPath = 'index.html';
            }
            navLinks.forEach(link => {
                const href = link.getAttribute('href');
                if (href && (href === currentPath || (currentPath === 'index.html' && href === 'index.html'))) {
                    link.classList.add('active');
                }
            });
        });
    </script>
"""

# New style content
style_content = """
    <style>
        /* Active Navigation Link Styling */
        nav div a.active:not(.bg-primary-container) {
            color: #776300 !important;
            border-bottom: 3px solid #fdd400;
            padding-bottom: 2px;
        }
    </style>
"""

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # 1. Remove icons (if still present)
    content = re.sub(r'<button[^>]*>\s*<span[^>]*>notifications</span>\s*</button>', '', content)
    content = re.sub(r'<button[^>]*>\s*<span[^>]*>account_circle</span>\s*</button>', '', content)

    # 2. Clean up old injected scripts/styles to avoid duplicates
    # Remove any script that has "Search Filtering & Focus" or "Active Navigation Highlighting"
    content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*// Search Filtering & Focus[\s\S]*?<\/script>', '', content)
    # Also remove the style block if it exists
    content = re.sub(r'<style>\s*\/\* Active Navigation Link Styling \*\/[\s\S]*?<\/style>', '', content)

    # 3. Inject new ones
    if "</body>" in content:
        content = content.replace("</body>", script_content + "\n</body>")
    
    if "</head>" in content:
        content = content.replace("</head>", style_content + "\n</head>")

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

count = 0
for filepath in html_files:
    if filepath.endswith(".html") or filepath.endswith(".html"):
        if process_file(filepath):
            count += 1

print(f"Refreshed {count} HTML files with robust search logic.")
