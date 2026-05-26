import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r"RBI Financial Inclusion Index \(March 2023\)", "RBI Financial Inclusion Index (March 2025)"),
    (r"primarily March 2023 for RBI data", "primarily 2025-2026 for RBI data"),
    (r"RRB gross NPA ratio: 7\.3% \(March 2023\)", "RRB gross NPA ratio: 7.3% (March 2025)")
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Remaining data replacements completed.")
