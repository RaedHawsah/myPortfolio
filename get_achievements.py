import re

transcript_path = '/home/rexkov/.gemini/antigravity-ide/brain/74b21002-0cd2-4dfc-9a03-4e5a13b1fb0e/.system_generated/logs/transcript_full.jsonl'
with open(transcript_path, 'r') as f:
    text = f.read()

# The output from view_file includes lines formatted as:
# \n304:     <!-- Achievements Section -->\n305:     <section id=\"achievements\" class=\"relative py-20 px-6 md:px-16 w-full max-w-[1400px] mx-auto z-20\">\n
# I will find all lines matching the format "\d+: .*" and reconstruct the file

lines_dict = {}
for match in re.finditer(r'\\n(\d+): (.*?)(?=\\n\d+: |\\n)', text):
    line_num = int(match.group(1))
    content = match.group(2)
    # the json encoding might have escaped quotes
    content = content.replace('\\"', '"').replace('\\/', '/').replace('\\\\', '\\')
    
    # store it
    if line_num not in lines_dict:
        lines_dict[line_num] = content

# reconstruct 304 to 646
out_lines = []
for i in range(304, 647):
    if i in lines_dict:
        out_lines.append(lines_dict[i])
    else:
        print(f"Missing line {i}")

if len(out_lines) > 300:
    with open('original_achievements.html', 'w') as f:
        f.write('\n'.join(out_lines))
    print("Success")
else:
    print(f"Failed, found only {len(out_lines)} lines.")
