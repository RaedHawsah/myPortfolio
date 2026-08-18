import re

with open('/home/rexkov/Documents/myPortfolio/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace orange classes with cyan in the filterCerts function
js = js.replace("tab.classList.add('bg-theme-orange/20', 'border-theme-orange/50', 'text-white');", "tab.classList.add('bg-theme-cyan/20', 'border-theme-cyan/50', 'text-white');")
js = js.replace("tab.classList.remove('bg-theme-orange/20', 'border-theme-orange/50', 'text-white');", "tab.classList.remove('bg-theme-cyan/20', 'border-theme-cyan/50', 'text-white');")

with open('/home/rexkov/Documents/myPortfolio/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed script.js")
