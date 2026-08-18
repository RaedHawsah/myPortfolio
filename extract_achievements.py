import json

transcript_path = '/home/rexkov/.gemini/antigravity-ide/brain/74b21002-0cd2-4dfc-9a03-4e5a13b1fb0e/.system_generated/logs/transcript_full.jsonl'

lines_dict = {}

with open(transcript_path, 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('source') == 'SYSTEM' and data.get('type') == 'TOOL_RESPONSE':
                for tool_resp in data.get('tool_responses', []):
                    if tool_resp.get('name') == 'default_api:view_file':
                        output = tool_resp.get('response', {}).get('output', '')
                        # Parse the output which has lines formatted as "130:             <img src=..."
                        for line_str in output.split('\n'):
                            if ':' in line_str:
                                parts = line_str.split(':', 1)
                                if parts[0].strip().isdigit():
                                    line_num = int(parts[0].strip())
                                    content = parts[1]
                                    # Remove leading space that was added by view_file formatter
                                    if content.startswith(' '):
                                        content = content[1:]
                                    lines_dict[line_num] = content
        except Exception as e:
            pass

# We need the Achievements section which started at line 304 and ended at 644
achievements_html = []
for i in range(304, 645):
    if i in lines_dict:
        achievements_html.append(lines_dict[i])
    else:
        print(f"Missing line {i}")

if len(achievements_html) == (645 - 304):
    with open('original_achievements.html', 'w') as out_f:
        out_f.write('\n'.join(achievements_html))
    print("Successfully extracted original achievements to original_achievements.html")
else:
    print(f"Only extracted {len(achievements_html)} lines.")
