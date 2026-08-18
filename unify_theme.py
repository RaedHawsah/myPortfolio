import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Colors mappings
# Hero Section
html = html.replace('text-theme-orange font-bold font-mono', 'text-theme-purple font-bold font-mono')
html = html.replace('bg-theme-orange text-[#0F0A1A]', 'bg-theme-purple text-white')
html = html.replace('hover:bg-[#ff8533]', 'hover:bg-[#b975f8]')
html = html.replace('hover:shadow-[0_0_20px_rgba(255,107,0,0.4)]', 'hover:shadow-[0_0_20px_rgba(168,85,247,0.6)]')
html = html.replace('hover:border-theme-orange', 'hover:border-theme-purple')
html = html.replace('hover:text-theme-orange', 'hover:text-theme-purple')
html = html.replace('border-theme-orange/20', 'border-theme-cyan/20')
html = html.replace('text-theme-orange/30', 'text-theme-cyan/30')
html = html.replace('border-theme-orange/50', 'border-theme-cyan/50')
html = html.replace('text-theme-orange filter drop-shadow-[0_0_20px_#FF6B00]', 'text-theme-cyan filter drop-shadow-[0_0_20px_#00E5FF]')

# Specific icons that were orange
html = html.replace('fas fa-trophy text-theme-orange text-xl', 'fas fa-trophy text-theme-cyan text-xl')
html = html.replace('text-theme-orange', 'text-theme-purple') # catch any remaining orange

# Skills Section - Make sure they alternate
html = html.replace('text-theme-orange/60', 'text-theme-cyan/60')
html = html.replace('border-theme-orange/60', 'border-theme-cyan/60')
html = html.replace('shadow-[0_0_20px_rgba(255,107,0,0.3)]', 'shadow-[0_0_20px_rgba(0,229,255,0.3)]')
html = html.replace('group-hover:shadow-[0_0_40px_rgba(255,107,0,0.6)]', 'group-hover:shadow-[0_0_40px_rgba(0,229,255,0.6)]')

html = html.replace('hover:border-blue-500', 'hover:border-theme-purple')
html = html.replace('border-blue-500/60', 'border-theme-purple/60')
html = html.replace('shadow-[0_0_20px_rgba(59,130,246,0.3)]', 'shadow-[0_0_20px_rgba(168,85,247,0.3)]')
html = html.replace('group-hover:shadow-[0_0_40px_rgba(59,130,246,0.6)]', 'group-hover:shadow-[0_0_40px_rgba(168,85,247,0.6)]')
html = html.replace('text-blue-500', 'text-theme-purple')

# SOC Dashboard - Neutralize other colors
html = html.replace('bg-red-500', 'bg-theme-purple')
html = html.replace('bg-yellow-500', 'bg-gray-600')
html = html.replace('bg-green-500', 'bg-theme-cyan')
html = html.replace('text-yellow-500', 'text-theme-purple')
html = html.replace('border-yellow-900/50', 'border-theme-purple/30')
html = html.replace('bg-yellow-950/30', 'bg-theme-purple/10')
html = html.replace('text-red-400', 'text-theme-cyan')
html = html.replace('border-red-900/50', 'border-theme-cyan/30')
html = html.replace('bg-red-950/30', 'bg-theme-cyan/10')
html = html.replace('border-orange-900/50', 'border-theme-purple/30')
html = html.replace('bg-orange-950/30', 'bg-theme-purple/10')

# Achievements Wall (Restored version)
# We will just replace all instances of text-yellow-500, text-red-500 etc.

# Yellow -> Purple
html = html.replace('hover:border-yellow-500', 'hover:border-theme-purple')
html = html.replace('hover:shadow-[0_0_30px_rgba(234,179,8,0.3)]', 'hover:shadow-[0_0_30px_rgba(168,85,247,0.3)]')
html = html.replace('from-yellow-500/10', 'from-theme-purple/10')
html = html.replace('border-yellow-500/50', 'border-theme-purple/50')
html = html.replace('shadow-[0_0_15px_rgba(234,179,8,0.4)]', 'shadow-[0_0_15px_rgba(168,85,247,0.4)]')
html = html.replace('text-yellow-500', 'text-theme-purple')
html = html.replace('group-hover:text-yellow-400', 'group-hover:text-theme-purple')

# Red -> Cyan
html = html.replace('hover:border-red-500', 'hover:border-theme-cyan')
html = html.replace('hover:shadow-[0_0_30px_rgba(239,68,68,0.3)]', 'hover:shadow-[0_0_30px_rgba(0,229,255,0.3)]')
html = html.replace('from-red-500/10', 'from-theme-cyan/10')
html = html.replace('border-red-500/50', 'border-theme-cyan/50')
html = html.replace('shadow-[0_0_15px_rgba(239,68,68,0.4)]', 'shadow-[0_0_15px_rgba(0,229,255,0.4)]')
html = html.replace('text-red-500', 'text-theme-cyan')
html = html.replace('group-hover:text-red-400', 'group-hover:text-theme-cyan')

# Orange -> Purple
html = html.replace('hover:border-orange-500', 'hover:border-theme-purple')
html = html.replace('hover:shadow-[0_0_30px_rgba(249,115,22,0.3)]', 'hover:shadow-[0_0_30px_rgba(168,85,247,0.3)]')
html = html.replace('from-orange-500/10', 'from-theme-purple/10')
html = html.replace('border-orange-500/50', 'border-theme-purple/50')
html = html.replace('shadow-[0_0_15px_rgba(249,115,22,0.4)]', 'shadow-[0_0_15px_rgba(168,85,247,0.4)]')
html = html.replace('text-orange-500', 'text-theme-purple')
html = html.replace('group-hover:text-orange-400', 'group-hover:text-theme-purple')

# Blue -> Cyan
html = html.replace('hover:border-blue-500', 'hover:border-theme-cyan')
html = html.replace('hover:shadow-[0_0_30px_rgba(59,130,246,0.3)]', 'hover:shadow-[0_0_30px_rgba(0,229,255,0.3)]')
html = html.replace('from-blue-500/10', 'from-theme-cyan/10')
html = html.replace('border-blue-500/50', 'border-theme-cyan/50')
html = html.replace('shadow-[0_0_15px_rgba(59,130,246,0.4)]', 'shadow-[0_0_15px_rgba(0,229,255,0.4)]')
html = html.replace('text-blue-500', 'text-theme-cyan')
html = html.replace('group-hover:text-blue-400', 'group-hover:text-theme-cyan')

# Fix font classes (Hacker vibe)
# We make section headers font-mono
html = html.replace('<h2 class="text-4xl md:text-6xl font-extrabold text-white mb-4 tracking-tight">', '<h2 class="text-4xl md:text-5xl font-extrabold text-white mb-4 tracking-tighter font-mono">')
html = html.replace('<h2 class="text-3xl md:text-5xl font-bold text-white mb-4">', '<h2 class="text-4xl md:text-5xl font-extrabold text-white mb-4 tracking-tighter font-mono">')

# Enhance Hovers across all cards
html = html.replace('glass-card rounded-2xl p-6 hover:-translate-y-2 transition-transform duration-300 group', 'glass-card rounded-2xl p-6 hover:-translate-y-2 transition-all duration-500 group')
html = html.replace('hover:text-theme-cyan transition-colors', 'hover:text-theme-cyan hover:drop-shadow-[0_0_10px_rgba(0,229,255,0.8)] transition-all duration-300')
html = html.replace('hover:text-theme-purple transition-colors', 'hover:text-theme-purple hover:drop-shadow-[0_0_10px_rgba(168,85,247,0.8)] transition-all duration-300')

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Unified colors to 50% cyan and 50% purple, updated fonts to modern hacker vibe, and enhanced hovers.")
