import re

with open('original_achievements.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Translations
translations = {
    'الأمن السيبراني': 'Cybersecurity',
    'الذكاء الاصطناعي في خدمة المجتمع': 'AI for Community Service',
    'الذكاء التوليدي': 'Generative AI',
    'تطبيقات الذكاء الاصطناعي': 'AI Applications',
    'ريادة الأعمال التقنية': 'Tech Entrepreneurship',
    'مقدمة في الذكاء الاصطناعي': 'Introduction to AI'
}

for ar, en in translations.items():
    orig = orig.replace(ar, en)
    # Also replace in the alt tag if there are formatting weirdnesses
    orig = orig.replace('تطبيقات الذكاء االصطناعي', 'AI Applications') # specific typo in alt
    
# Font enhancements
orig = orig.replace('text-white font-bold mb-2 text-xl md:text-2xl', 'text-white font-extrabold mb-2 text-2xl md:text-3xl tracking-tight')
orig = orig.replace('text-sm text-gray-400 leading-relaxed max-w-2xl', 'text-base text-gray-300 leading-relaxed max-w-2xl font-medium')

# The original block in index.html starts with <!-- Browser-like Tabs --> and ends before <!-- Footer / Contact -->
with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# We need to replace the entire <section id="achievements"> ... </section> in index.html
# with the orig content which is exactly the <section id="achievements"> ... </section>

start_marker = '<section id="achievements"'
end_marker = '</section>'
# find the start of achievements section
idx_start = index_content.find(start_marker, index_content.find('<!-- Achievements Section -->'))

if idx_start != -1:
    # find the end of achievements section (the next section or footer)
    idx_end = index_content.find('<!-- Footer / Contact -->', idx_start)
    if idx_end != -1:
        # we want to replace up to the start of the footer
        # but wait, orig contains the entire <section> up to </section>
        
        # let's just replace between <!-- Achievements Section --> and <!-- Footer / Contact -->
        
        # Actually orig contains:
        # <!-- Achievements Section -->
        # <section id="achievements" ...>
        # ...
        # </section>
        # 
        
        # Let's cleanly replace
        part1 = index_content[:index_content.find('    <!-- Achievements Section -->')]
        part2 = index_content[index_content.find('    <!-- Footer / Contact -->'):]
        
        # Ensure orig starts properly
        if not orig.strip().startswith('<!-- Achievements Section -->'):
            orig = '    <!-- Achievements Section -->\n' + orig
            
        final_content = part1 + orig + '\n\n' + part2
        
        with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
            f.write(final_content)
        print("Restored successfully.")
    else:
        print("Footer not found.")
else:
    print("Achievements section not found.")
