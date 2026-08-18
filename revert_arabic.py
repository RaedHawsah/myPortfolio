import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'الرئيسية': 'Home',
    r'الترسانة\s*والمهارات': 'Skills / Arsenal',
    r'المشاريع': 'Projects',
    r'الخبرات': 'Experience',
    r'الإنجازات': 'Achievements',
    r'تواصل\s*معي': 'Contact',
    r'أهلاً بك في المساحة المظلمة، أنا': 'Welcome to the dark space, I am',
    r'مختص بالأمن الهجومي': 'Offensive Security',
    r'والهندسة\s*العكسية': '& Reverse Engineer',
    r'أقوم بتفكيك الأنظمة المعقدة واستغلال الثغرات العميقة\.\s*أمتلك خبرة متقدمة تمتد من اختراق الشبكات\s*والأنظمة إلى تحليل البرمجيات الخبيثة والهندسة العكسية\.': 'I deconstruct complex systems and exploit deep-seated vulnerabilities. My advanced expertise ranges from network and system penetration to malware analysis and low-level reverse engineering.',
    r'جميع الحقوق محفوظة\.': 'All rights reserved.',
    r'Raed Hawsah': '0xRexKov',
    r'تحميل السيرة الذاتية': 'Download Resume',
    r'وظفني': 'Hire Me'
}

for ar, en in replacements.items():
    content = re.sub(ar, en, content)

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Arabic text replaced.")
