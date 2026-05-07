import re

file_path = r'c:\Users\91708\Downloads\FInal-dccb-site\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace grid
old_grid = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;">'
new_grid = '<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:24px;">'
content = content.replace(old_grid, new_grid)

# Replace padding
old_padding = 'border-radius:var(--r-md);padding:20px 22px;'
new_padding = 'border-radius:var(--r-md);padding:32px 28px;'
content = content.replace(old_padding, new_padding)

# Replace font styles
old_font_w = "font-size:22px;font-weight:800;font-family:'Syne',sans-serif;color:white;letter-spacing:-0.5px;white-space:nowrap;"
new_font_w = "font-size:32px;font-weight:800;font-family:'Syne',sans-serif;color:white;letter-spacing:-1px;"
content = content.replace(old_font_w, new_font_w)

old_font_o = "font-size:22px;font-weight:800;font-family:'Syne',sans-serif;color:#ff9955;letter-spacing:-0.5px;white-space:nowrap;"
new_font_o = "font-size:32px;font-weight:800;font-family:'Syne',sans-serif;color:#ff9955;letter-spacing:-1px;"
content = content.replace(old_font_o, new_font_o)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI formatting updated")
