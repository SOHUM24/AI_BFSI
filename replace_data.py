import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # FI-Index
    (r"60\.1", "67.0"),
    (r"FI-Index score March 2023", "FI-Index score March 2025"),
    (r"Financial Inclusion Index reached 60\.1 in March 2023", "Financial Inclusion Index reached 67.0 in March 2025"),
    
    # Global Findex
    (r"Global Findex Database 2021", "Global Findex Database 2025"),
    (r"~78% of Indian adults", "~89% of Indian adults"),
    (r"78%</span> Indian adults", "89%</span> Indian adults"),
    (r"78%Indian adults", "89%Indian adults"),
    (r"78% Indian adults", "89% Indian adults"),
    
    # PMJDY
    (r"48\.65 Cr", "57.78 Cr"),
    
    # KCC
    (r"7 Cr\+", "7.72 Cr"),
    
    # BC Agents
    (r"14L\+", "13.1L+"),
    (r"14 lakh\+", "13.1 lakh+"),
    
    # RRB
    (r"₹4\.56L Cr</span> RRB credit outstanding", "₹12L Cr+</span> RRB total business"),
    (r"₹4\.56L Cr", "₹12L Cr+"),
    (r"RRB credit outstanding", "RRB total business"),
    
    # Citations
    (r"2022-23", "2024-25"),
    (r"2017–2023", "2017–2025")
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Data replacements completed.")
