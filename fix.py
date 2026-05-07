import re

with open(r'c:\Users\91708\Downloads\FInal-dccb-site\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the sections to be moved
ai_sections_pattern = r'(\s*<!-- ══════════════════════════════════════════════════════\n     NEW SECTION: AI READINESS.*?)(?=<!-- ══════════════════════════════════════════════════════\n     FOOTER)'
match = re.search(ai_sections_pattern, content, re.DOTALL)
if not match:
    print('AI sections not found at bottom.')
    exit(1)

ai_sections_str = match.group(1)

# Remove them from the bottom
content = content.replace(ai_sections_str, '\n    ')

# 2. Find insertion point (after verified-data section)
# Looking for "    </section>\n\n    <!-- ══════════════════════════════════════════════════════\n     SECTION 2: LANDSCAPE"
insertion_marker_pattern = r'(    </section>\s*<!-- ══════════════════════════════════════════════════════\n     SECTION 2: LANDSCAPE)'
match_insertion = re.search(insertion_marker_pattern, content)
if not match_insertion:
    print('Insertion marker not found.')
    exit(1)

content = content.replace(match_insertion.group(1), ai_sections_str + match_insertion.group(1))

# 3. Fix the font sizes and wrapping in the verified-data grid boxes
old_style_white = r"font-size:28px;font-weight:800;font-family:'Syne',sans-serif;color:white;"
new_style_white = r"font-size:22px;font-weight:800;font-family:'Syne',sans-serif;color:white;letter-spacing:-0.5px;white-space:nowrap;"
content = content.replace(old_style_white, new_style_white)

old_style_orange = r"font-size:28px;font-weight:800;font-family:'Syne',sans-serif;color:#ff9955;"
new_style_orange = r"font-size:22px;font-weight:800;font-family:'Syne',sans-serif;color:#ff9955;letter-spacing:-0.5px;white-space:nowrap;"
content = content.replace(old_style_orange, new_style_orange)

with open(r'c:\Users\91708\Downloads\FInal-dccb-site\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully moved AI sections and updated UI formatting.')
