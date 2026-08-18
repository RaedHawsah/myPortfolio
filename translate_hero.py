import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title
content = re.sub(
    r'<title>Raed Hawsah \| Cyber Security Professional</title>',
    r'<title>0xRexKov | خبير الأمن السيبراني والهندسة العكسية</title>',
    content
)
content = re.sub(r'lang="en"', r'lang="ar" dir="rtl"', content)

# 2. Update Navbar Logo
content = re.sub(
    r'raed<span class="text-theme-cyan">\.</span>',
    r'0xRexKov<span class="text-theme-cyan">.</span>',
    content
)

# 3. Update Navbar Links
nav_links_old = """            <a href="#home" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">Home</a>
            <a href="#skills" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">Skills / Arsenal</a>
            <a href="#projects" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">Projects</a>
            <a href="#experience" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">Experience</a>
            <a href="#achievements" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">Achievements</a>
            <a href="#contact" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">Contact</a>"""

nav_links_new = """            <a href="#home" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الرئيسية</a>
            <a href="#skills" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الترسانة والمهارات</a>
            <a href="#projects" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">المشاريع</a>
            <a href="#experience" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الخبرات</a>
            <a href="#achievements" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">الإنجازات</a>
            <a href="#contact" class="text-gray-300 hover:text-theme-cyan transition-colors text-sm font-medium">تواصل معي</a>"""

content = content.replace(nav_links_old, nav_links_new)

# 4. Update Resume Button
content = content.replace('Download Resume', 'تحميل السيرة الذاتية')

# 5. Update Hero Text
hero_old = """                <h3 class="text-gray-300 font-sans text-xl md:text-2xl mb-2 font-medium tracking-wide">
                    Hey, I am <span class="text-theme-orange font-bold">Raed Hawsah</span>
                </h3>
                <h1 class="text-5xl md:text-7xl lg:text-[5.5rem] font-bold text-white tracking-tight leading-[1.1] mb-6">
                    Offensive Security<br/><span class="text-gray-200 text-4xl md:text-5xl lg:text-[4.5rem]">& Full-Stack Developer</span>
                </h1>
                <p class="text-gray-400 text-base md:text-lg max-w-lg mb-10 leading-relaxed">
                    I deconstruct complex systems to identify deep-seated vulnerabilities, from standard network assessments to low-level assembly analysis.
                </p>"""

hero_new = """                <h3 class="text-gray-300 font-sans text-xl md:text-2xl mb-2 font-medium tracking-wide">
                    أهلاً بك في المساحة المظلمة، أنا <span class="text-theme-orange font-bold font-mono">0xRexKov</span>
                </h3>
                <h1 class="text-5xl md:text-7xl lg:text-[5.5rem] font-bold text-white tracking-tight leading-[1.1] mb-6">
                    مختص بالأمن الهجومي<br/><span class="text-gray-200 text-4xl md:text-5xl lg:text-[4.0rem]">والهندسة العكسية</span>
                </h1>
                <p class="text-gray-400 text-base md:text-lg max-w-lg mb-10 leading-relaxed">
                    أقوم بتفكيك الأنظمة المعقدة واستغلال الثغرات العميقة. أمتلك خبرة متقدمة تمتد من اختراق الشبكات والأنظمة إلى تحليل البرمجيات الخبيثة والهندسة العكسية.
                </p>"""
content = content.replace(hero_old, hero_new)

# 6. Update Hire Me
content = content.replace('Hire me', 'وظفني')

# 7. Update Guinness Card
guinness_old = """                            <div class="text-white text-base font-bold">Guinness World Record Holder</div>
                            <div class="text-gray-400 text-sm">AI & Tech Innovation</div>"""

guinness_new = """                            <div class="text-white text-base font-bold">موسوعة غينيس للأرقام القياسية</div>
                            <div class="text-gray-400 text-sm">أكبر درس في الذكاء الاصطناعي</div>"""
content = content.replace(guinness_old, guinness_new)

# 8. Update avatar alt
content = content.replace('alt="Raed Hawsah 3D Avatar"', 'alt="0xRexKov 3D Avatar"')

# 9. Update footer links text too!
footer_links_old = """                    <a href="#home" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">Home</a>
                    <a href="#skills" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">Skills / Arsenal</a>
                    <a href="#projects" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">Projects</a>
                    <a href="#experience" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">Experience</a>
                    <a href="#achievements" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">Achievements</a>"""

footer_links_new = """                    <a href="#home" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الرئيسية</a>
                    <a href="#skills" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الترسانة والمهارات</a>
                    <a href="#projects" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">المشاريع</a>
                    <a href="#experience" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الخبرات</a>
                    <a href="#achievements" class="text-gray-500 hover:text-theme-cyan transition-colors text-sm font-medium">الإنجازات</a>"""

content = content.replace(footer_links_old, footer_links_new)

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translations and updates applied successfully.")
