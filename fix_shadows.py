import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any lingering orange RGBA
html = html.replace('rgba(255,107,0,', 'rgba(168,85,247,')
html = html.replace('rgba(249,115,22,', 'rgba(168,85,247,')
# Replace red RGBA
html = html.replace('rgba(239,68,68,', 'rgba(0,229,255,')
# Replace yellow RGBA
html = html.replace('rgba(234,179,8,', 'rgba(168,85,247,')
# Replace blue RGBA
html = html.replace('rgba(59,130,246,', 'rgba(0,229,255,')

# Add font-mono to some key headers
html = html.replace('class="text-3xl font-extrabold text-white tracking-tight"', 'class="text-3xl font-extrabold text-white tracking-tight font-mono"')
html = html.replace('class="text-5xl md:text-7xl lg:text-[5.5rem] font-bold text-white tracking-tight leading-[1.1] mb-6"', 'class="text-5xl md:text-7xl lg:text-[5.5rem] font-bold text-white tracking-tight leading-[1.1] mb-6 font-mono"')
html = html.replace('class="text-white font-extrabold mb-2 text-2xl md:text-3xl tracking-tight"', 'class="text-white font-extrabold mb-2 text-2xl md:text-3xl tracking-tight font-mono"')
html = html.replace('class="text-white text-lg font-extrabold tracking-wide"', 'class="text-white text-lg font-extrabold tracking-wide font-mono"')
html = html.replace('class="text-xl font-extrabold text-white tracking-wide"', 'class="text-xl font-extrabold text-white tracking-wide font-mono"')

# Replace hover:-translate-y-1 with stronger hover and more drop-shadow
html = html.replace('hover:-translate-y-1 ', 'hover:-translate-y-2 hover:drop-shadow-[0_0_15px_rgba(0,229,255,0.4)] ')

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed RGBA shadows and applied font-mono to headers.")
