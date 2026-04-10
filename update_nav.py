import os
import glob
import re

dir_path = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(os.path.join(dir_path, "*.html*")) 

def remove_buttons(html):
    # Regex for button containing notifications
    html = re.sub(r'<button[^>]*>\s*<span[^>]*>notifications</span>\s*</button>', '', html)
    # Regex for button containing account_circle
    html = re.sub(r'<button[^>]*>\s*<span[^>]*>account_circle</span>\s*</button>', '', html)
    return html

script_to_add = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Search Filtering & Focus
            const searchInput = document.querySelector('input[placeholder="Search concepts..."]');
            if (searchInput) {
                const searchIcon = searchInput.nextElementSibling;
                if (searchIcon && searchIcon.textContent.trim() === 'search') {
                    searchIcon.style.cursor = 'pointer';
                    searchIcon.addEventListener('click', () => searchInput.focus());
                }
                searchInput.addEventListener('input', function() {
                    const query = this.value.toLowerCase();
                    const cards = document.querySelectorAll('article, .grid > div.sketch-border');
                    cards.forEach(card => {
                        const text = card.textContent.toLowerCase();
                        card.style.display = text.includes(query) ? '' : 'none';
                    });
                });
            }
            
            // Active Navigation Highlighting
            const navLinks = document.querySelectorAll('nav a');
            // get current page filename, default to index.html if empty
            let currentPath = window.location.pathname.split('/').pop().split('?')[0].split('#')[0];
            if (!currentPath || currentPath === '') {
                currentPath = 'index.html';
            }
            navLinks.forEach(link => {
                const href = link.getAttribute('href');
                if (href && href === currentPath) {
                    link.classList.add('active');
                }
            });
        });
    </script>
</body>
"""

style_to_add = """
    <style>
        /* Active Navigation Link Styling */
        nav div a.active:not(.bg-primary-container) {
            color: #776300 !important;
            border-bottom: 3px solid #fdd400;
            padding-bottom: 2px;
        }
    </style>
</head>
"""

count = 0
for filepath in html_files:
    if not (filepath.endswith(".html") or filepath.endswith(".html")):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    content = remove_buttons(content)

    if "Active Navigation Highlighting" not in content:
        content = content.replace("</body>", script_to_add)

    if "Active Navigation Link Styling" not in content:
        content = content.replace("</head>", style_to_add)

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files.")
