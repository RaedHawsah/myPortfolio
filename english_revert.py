import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert HTML tag
content = content.replace('<html lang="ar" dir="rtl">', '<html lang="en">')

# 2. Update Title
content = re.sub(
    r'<title>0xRexKov \| خبير الأمن السيبراني والهندسة العكسية</title>',
    r'<title>0xRexKov | Cyber Security & Reverse Engineering Expert</title>',
    content
)

# 3. Revert Navbar Links
nav_links_ar = """            <a href="#home" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الرئيسية</a>
            <a href="#skills" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الترسانة والمهارات</a>
            <a href="#projects" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">المشاريع</a>
            <a href="#experience" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الخبرات</a>
            <a href="#achievements" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الإنجازات</a>
            <a href="#contact" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">تواصل معي</a>"""

nav_links_en = """            <a href="#home" class="text-gray-300 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Home</a>
            <a href="#skills" class="text-gray-300 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Skills / Arsenal</a>
            <a href="#projects" class="text-gray-300 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Projects</a>
            <a href="#experience" class="text-gray-300 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Experience</a>
            <a href="#achievements" class="text-gray-300 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Achievements</a>
            <a href="#contact" class="text-gray-300 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Contact</a>"""

content = content.replace(nav_links_ar, nav_links_en)

# 4. Revert Resume Button
content = content.replace('تحميل السيرة الذاتية', 'Download Resume')

# 5. Revert Hero Text
hero_ar = """                <h3 class="text-gray-300 font-sans text-xl md:text-2xl mb-2 font-medium tracking-wide">
                    أهلاً بك في المساحة المظلمة، أنا <span class="text-theme-orange font-bold font-mono">0xRexKov</span>
                </h3>
                <h1 class="text-5xl md:text-7xl lg:text-[5.5rem] font-bold text-white tracking-tight leading-[1.1] mb-6">
                    مختص بالأمن الهجومي<br/><span class="text-gray-200 text-4xl md:text-5xl lg:text-[4.0rem]">والهندسة العكسية</span>
                </h1>
                <p class="text-gray-400 text-base md:text-lg max-w-lg mb-10 leading-relaxed">
                    أقوم بتفكيك الأنظمة المعقدة واستغلال الثغرات العميقة. أمتلك خبرة متقدمة تمتد من اختراق الشبكات والأنظمة إلى تحليل البرمجيات الخبيثة والهندسة العكسية.
                </p>"""

hero_en = """                <h3 class="text-gray-300 font-sans text-2xl md:text-3xl mb-3 font-semibold tracking-widest uppercase">
                    Welcome to the dark space, I am <span class="text-theme-orange font-bold font-mono">0xRexKov</span>
                </h3>
                <h1 class="text-5xl md:text-7xl lg:text-[6rem] font-extrabold text-white tracking-tighter leading-[1.05] mb-8 drop-shadow-lg">
                    Offensive Security<br/><span class="text-gray-200 text-4xl md:text-6xl lg:text-[4.5rem] tracking-tight">& Reverse Engineer</span>
                </h1>
                <p class="text-gray-300 text-lg md:text-xl max-w-2xl mb-12 leading-relaxed font-medium">
                    I deconstruct complex systems and exploit deep-seated vulnerabilities. My advanced expertise ranges from network and system penetration to malware analysis and low-level reverse engineering.
                </p>"""
content = content.replace(hero_ar, hero_en)

# 6. Revert Hire Me
content = content.replace('وظفني', 'Hire Me')
content = content.replace('text-[#0F0A1A] font-bold', 'text-[#0F0A1A] font-extrabold text-lg tracking-wider')

# 7. Revert Guinness Card
guinness_ar = """                            <div class="text-white text-base font-bold">موسوعة غينيس للأرقام القياسية</div>
                            <div class="text-gray-400 text-sm">أكبر درس في الذكاء الاصطناعي</div>"""

guinness_en = """                            <div class="text-white text-lg font-extrabold tracking-wide">Guinness World Record Holder</div>
                            <div class="text-gray-300 text-base font-medium">Largest AI Tech Lesson</div>"""
content = content.replace(guinness_ar, guinness_en)

# 8. Footer Links
footer_links_ar = """                    <a href="#home" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الرئيسية</a>
                    <a href="#skills" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الترسانة والمهارات</a>
                    <a href="#projects" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">المشاريع</a>
                    <a href="#experience" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الخبرات</a>
                    <a href="#achievements" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الإنجازات</a>"""

footer_links_en = """                    <a href="#home" class="text-gray-400 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Home</a>
                    <a href="#skills" class="text-gray-400 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Skills / Arsenal</a>
                    <a href="#projects" class="text-gray-400 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Projects</a>
                    <a href="#experience" class="text-gray-400 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Experience</a>
                    <a href="#achievements" class="text-gray-400 hover:text-theme-cyan transition-colors text-base font-semibold tracking-wide">Achievements</a>"""
content = content.replace(footer_links_ar, footer_links_en)

# 9. Copyright
content = content.replace('جميع الحقوق محفوظة.', 'All rights reserved.')

# Make headings generally bolder and larger across the site
# Skills
content = content.replace('<h2 class="text-3xl md:text-5xl font-bold text-white mb-4">', '<h2 class="text-4xl md:text-6xl font-extrabold text-white mb-4 tracking-tight">')
content = content.replace('text-lg font-bold text-white', 'text-xl font-extrabold text-white tracking-wide')
content = content.replace('text-gray-400 text-sm leading-relaxed', 'text-gray-300 text-base leading-relaxed font-medium')

# Project Title
content = content.replace('<h3 class="text-2xl md:text-3xl font-bold text-white mb-2 font-sans">', '<h3 class="text-3xl md:text-4xl font-extrabold text-white mb-3 tracking-tight font-sans">')
content = content.replace('text-gray-400 text-sm md:text-base leading-relaxed mb-8 font-sans', 'text-gray-300 text-base md:text-lg leading-relaxed mb-8 font-sans font-medium')

# Experience
content = content.replace('<h3 class="text-2xl font-bold text-white">', '<h3 class="text-3xl font-extrabold text-white tracking-tight">')

# Achievements cards
content = content.replace('text-white font-bold text-xl md:text-2xl', 'text-white font-extrabold text-2xl md:text-3xl tracking-tight')
content = content.replace('text-gray-400 text-sm md:text-base', 'text-gray-300 text-base md:text-lg font-medium')

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted to English and enhanced fonts successfully.")
