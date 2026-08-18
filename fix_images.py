import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Restore original Arabic filenames in the src attributes
html = html.replace('src="cert/AI for Community Service-1.png"', 'src="cert/الذكاء الاصطناعي في خدمة المجتمع-1.png"')
html = html.replace('src="cert/Generative AI-1.png"', 'src="cert/الذكاء التوليدي-1.png"')
html = html.replace('src="cert/AI Applications-1.png"', 'src="cert/تطبيقات الذكاء االصطناعي-1.png"')
html = html.replace('src="cert/Introduction to AI-1.png"', 'src="cert/مقدمة في الذكاء الاصطناعي-1.png"')

with open('/home/rexkov/Documents/myPortfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored original Arabic image filenames.")
