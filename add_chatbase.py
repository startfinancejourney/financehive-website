import os
import glob

directory = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
script_to_add = """<script>
(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="okRPgozu3doX4vY4MK0UV";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
</script>
"""

html_files = []
for ext in ('*.html', '*.html.html'):
    html_files.extend(glob.glob(os.path.join(directory, ext)))

html_files = list(set(html_files))

count = 0
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "window.chatbase" in content:
            continue
            
        idx = content.rfind("</body>")
        if idx != -1:
            new_content = content[:idx] + script_to_add + content[idx:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Successfully updated {count} HTML files.")
