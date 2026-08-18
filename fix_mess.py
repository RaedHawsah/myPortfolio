import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Skills Cards
# Card 3 to be pure Cyan
card3_target = """            <!-- Skill 3: AI & Cyber-Physical Security -->
            <div
                class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-all duration-500 group border border-gray-800 hover:border-theme-purple hover:shadow-[0_0_30px_rgba(168,85,247,0.4)]">
                <div
                    class="w-14 h-14 rounded-full bg-black/60 border border-theme-cyan/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(0,229,255,0.3)] group-hover:shadow-[0_0_40px_rgba(0,229,255,0.6)] transition-all">
                    <i class="fas fa-brain text-theme-purple text-xl"></i>"""

card3_replace = """            <!-- Skill 3: AI & Cyber-Physical Security -->
            <div
                class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-all duration-500 group border border-gray-800 hover:border-theme-cyan hover:shadow-[0_0_30px_rgba(0,229,255,0.4)]">
                <div
                    class="w-14 h-14 rounded-full bg-black/60 border border-theme-cyan/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(0,229,255,0.3)] group-hover:shadow-[0_0_40px_rgba(0,229,255,0.6)] transition-all">
                    <i class="fas fa-brain text-theme-cyan text-xl"></i>"""
html = html.replace(card3_target, card3_replace)

# Card 4 to be pure Purple
card4_target = """            <!-- Skill 4: Enterprise & Cloud Architecture -->
            <div
                class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-all duration-500 group border border-gray-800 hover:border-theme-purple hover:shadow-[0_0_30px_rgba(0,229,255,0.4)]">
                <div
                    class="w-14 h-14 rounded-full bg-black/60 border border-theme-purple/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(168,85,247,0.3)] group-hover:shadow-[0_0_40px_rgba(168,85,247,0.6)] transition-all">
                    <i class="fas fa-network-wired text-theme-purple text-xl"></i>"""

card4_replace = """            <!-- Skill 4: Enterprise & Cloud Architecture -->
            <div
                class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-all duration-500 group border border-gray-800 hover:border-theme-purple hover:shadow-[0_0_30px_rgba(168,85,247,0.4)]">
                <div
                    class="w-14 h-14 rounded-full bg-black/60 border border-theme-purple/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(168,85,247,0.3)] group-hover:shadow-[0_0_40px_rgba(168,85,247,0.6)] transition-all">
                    <i class="fas fa-network-wired text-theme-purple text-xl"></i>"""
html = html.replace(card4_target, card4_replace)

# 2. Fix the Tabs in Wall of Achievements (in index.html)
tabs_target = """                <button onclick="filterCerts('all')" id="tab-all" class="cert-tab active-tab px-6 py-2 rounded-lg text-sm font-medium transition-all text-white bg-theme-orange/20 border border-theme-orange/50">All</button>"""
tabs_replace = """                <button onclick="filterCerts('all')" id="tab-all" class="cert-tab active-tab px-6 py-2 rounded-lg text-sm font-medium transition-all text-white bg-theme-cyan/20 border border-theme-cyan/50">All</button>"""
html = html.replace(tabs_target, tabs_replace)

# 3. Replace the Featured Project content with a video placeholder
# We need to find the terminal content which is after <!-- Terminal Header --> ... </div>
# Let's use regex to replace everything inside <div class="p-6 md:p-10 flex flex-col md:flex-row gap-8"> ... </section> (no, up to the end of the terminal window)

project_start = html.find('<!-- Terminal Header -->')
if project_start != -1:
    terminal_header_end = html.find('</div>', project_start)
    # The header ends after a few nested divs, let's just find the inner content div
    inner_start = html.find('<div class="p-6 md:p-10 flex flex-col md:flex-row gap-8">', terminal_header_end)
    if inner_start != -1:
        # Find the end of the terminal window (which is before </section>)
        terminal_end = html.find('</section>', inner_start)
        # We need to preserve the ending tag of the terminal window which is the div before </section>
        
        # A safer way: replace the content inside the terminal explicitly
        new_inner = """            <!-- Terminal Content (Video Area) -->
            <div class="p-0">
                <video controls autoplay loop muted class="w-full h-auto object-cover rounded-b-xl max-h-[70vh] outline-none">
                    <source src="project_video.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        </div>
    </section>"""
        
        # Let's slice everything from inner_start to </section> and replace
        html = html[:inner_start] + new_inner + html[terminal_end + 10:] # 10 is length of </section>

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed HTML issues.")
