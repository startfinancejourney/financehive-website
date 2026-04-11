import re
import glob

workspace_dir = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
html_files = glob.glob(fr"{workspace_dir}\*.html")

count = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="mobile-menu-btn"' in content:
        continue

    # Replacement logic: finding the LAST </div></nav> tag in the file.
    # Since we verified earlier that every file has exactly exactly 1 `</nav>`, and it is preceded by `</div>`.
    
    hamburger_btn_and_menu = '''
        <!-- Mobile Hamburger Button -->
        <button id="mobile-menu-btn" class="md:hidden text-[#383833] hover:text-secondary focus:outline-none flex items-center justify-center ml-2 p-1 transition-colors">
            <span class="material-symbols-outlined text-4xl font-black">menu</span>
        </button>
    </div>
    </nav>
    
    <!-- Mobile Menu -->
    <div id="mobile-menu" class="hidden md:hidden bg-surface border-b-4 border-stone-800 flex-col items-center py-4 w-full shadow-lg fixed left-0 right-0 z-40 transition-all font-marker" style="top: 86px;">
        <a class="text-on-surface hover:text-secondary font-black text-xl w-full text-center py-3 border-b-2 border-stone-800/10" href="learn-finance.html">Concepts</a>
        <a class="text-on-surface hover:text-secondary font-black text-xl w-full text-center py-3 border-b-2 border-stone-800/10" href="sectors.html">Sectors</a>
        <a class="text-on-surface hover:text-secondary font-black text-xl w-full text-center py-3 border-b-2 border-stone-800/10" href="request-topic.html">Request a Topic</a>
        <a class="text-on-surface hover:text-secondary font-black text-xl w-full text-center py-3" href="about.html">About</a>
    </div>

    <!-- Mobile Menu Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            const nav = document.querySelector('nav');
            
            if (btn && menu && nav) {
                btn.addEventListener('click', () => {
                    // Position menu strictly below navbar
                    menu.style.top = nav.getBoundingClientRect().bottom + 'px';
                    menu.classList.toggle('hidden');
                    menu.classList.toggle('flex');
                    
                    // Change icon based on menu state
                    const icon = btn.querySelector('.material-symbols-outlined');
                    if (icon) {
                        icon.textContent = menu.classList.contains('hidden') ? 'menu' : 'close';
                    }
                });
                
                // Close menu when a link is tapped
                menu.querySelectorAll('a').forEach(link => {
                    link.addEventListener('click', () => {
                        menu.classList.add('hidden');
                        menu.classList.remove('flex');
                        const icon = btn.querySelector('.material-symbols-outlined');
                        if (icon) icon.textContent = 'menu';
                    });
                });
            }
        });
    </script>
    '''
    
    # We use re.sub with count=1
    new_content = re.sub(r'</div>\s*</nav>', hamburger_btn_and_menu, content, count=1)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
    
print(f"Successfully processed {count} HTML files.")
