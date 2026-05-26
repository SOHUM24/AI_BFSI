import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Fix the dates for FI-Index
    (r"reached <strong>67\.0</strong> in March 2023", "reached <strong>67.0</strong> in March 2025"),
    (r"FI-Index 67\.0 \(March 2023\)", "FI-Index 67.0 (March 2025)"),
    
    # Fix other "March 2023" dates related to these metrics if applicable
    (r"PMJDY accounts opened by March 2023", "PMJDY accounts opened by February 2026"),
    (r"PMJDY deposits mobilised by March 2023", "PMJDY deposits mobilised by February 2026"),
    
    # Fix any other remaining 2023 dates for these metrics
    (r"FI-Index 53\.9 \(March 2021\), Account", "FI-Index 64.2 (March 2024), Account"),
    
    # KCC accounts date
    (r"7\.72 Cr Active KCC accounts", "7.72 Cr Active KCC accounts (as of March 2026)"),
    
    # Make sure we didn't miss PMJDY in 5136: "PMJDY: 53.13 crore" -> this is specific to some context?
    # Let's update PMJDY: 53.13 crore to PMJDY: 57.78 crore
    (r"PMJDY: 53\.13 crore", "PMJDY: 57.78 crore"),
    
    # Update chart data to reflect the new 2025 index point in the FI-Index chart
    # label: 'FI-Index (Actual/Projected)',
    # data: [43.4, 46.0, 48.5, 51.4, 53.9, 56.4, 67.0, null, null, null],
    # Actually the chart data array is: [43.4 (2017), 46.0, 48.5, 51.4, 53.9 (2021), 56.4 (2022), 60.1 (2023), 64.2 (2024), 67.0 (2025)]
    # We should let the dashboard handle it, but wait, it's hardcoded here in `index.html` lines 8726. Let's fix that.
    (r"data: \[43\.4, 46\.0, 48\.5, 51\.4, 53\.9, 56\.4, 67\.0, null, null, null\]", "data: [43.4, 46.0, 48.5, 51.4, 53.9, 56.4, 60.1, 64.2, 67.0, null]"),
    (r"data: \[null, null, null, null, null, null, 67\.0, 62\.0, 63\.5, 65\.0\]", "data: [null, null, null, null, null, null, null, null, 67.0, 69.5]"),
    (r"data: \[null, null, null, null, null, null, 67\.0, 64\.5, 68\.0, 72\.5\]", "data: [null, null, null, null, null, null, null, null, 67.0, 71.5]")
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Refined data replacements completed.")
