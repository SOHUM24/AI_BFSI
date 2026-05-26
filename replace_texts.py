import re

replacements = {
    "A DCCB attempting a standalone equivalent would be institutionally destroyed by the attempt.": "A DCCB attempting a standalone equivalent would face severe financial and operational strain.",
    "Skip it = failed deployment of every subsequent technology investment.": "Skipping it significantly increases the risk of suboptimal deployment for subsequent technology investments.",
    "A uniform AI prescription across all 351 DCCBs would be analytically irresponsible.": "A uniform AI prescription across all 351 DCCBs would be analytically suboptimal and practically ineffective.",
    "Zero PACS-CBS integration in most UP DCCBs.": "Limited PACS-CBS integration in most UP DCCBs.",
    "CBS = data entry tool, not intelligence platform.": "CBS is currently utilized primarily as a system of record rather than an intelligence platform.",
    "PMFBY auto-enrolment via AIDE portal is non-negotiable for all PD+ DCCBs.": "PMFBY auto-enrolment via AIDE portal is highly recommended as a baseline capability for all PD+ DCCBs.",
    "Implementation below these thresholds produces zero operational return on subsequent AI investment.": "Implementation below these thresholds yields limited operational return on subsequent AI investments.",
    "last-mile agricultural credit data is effectively \"dark\".": "last-mile agricultural credit data remains largely uncaptured digitally.",
    "Zero marginal cost once AIDE API integration is active.": "Minimal marginal cost once AIDE API integration is active.",
    "Without structured historical credit performance data for agricultural borrowers, supervised ML credit risk models cannot be trained or validated.": "The absence of structured historical credit performance data for agricultural borrowers complicates the training and validation of supervised ML credit risk models.",
    "Post-disbursement credit risk monitoring in most DCCBs is effectively absent.": "Post-disbursement credit risk monitoring in most DCCBs requires significant strengthening.",
    "NPA classification at 90 days past due — by which point recovery probability is structurally compromised.": "NPA classification at 90 days past due — by which point recovery probability is substantially reduced.",
    "Crop failure -> income loss -> KCC NPA cascade": "Crop failure -> income loss -> KCC NPA correlation",
    "Severe Digital Deficit": "Significant Digital Gap",
    "Forcing urban-designed apps on rural borrowers produces dormant accounts — not financial inclusion.": "Deploying urban-designed apps for rural borrowers often results in dormant accounts rather than effective financial inclusion.",
    "Whether digital products work depends entirely on the client segment and delivery channel.": "The effectiveness of digital products depends heavily on the client segment and delivery channel.",
    "BC model is self-sustaining. Scale aggressively as the primary Segment C (remote/tribal) client strategy — no subsidy required at scale.": "The BC model is structurally viable. Expanding its scale can serve as an effective primary strategy for Segment C (remote/tribal) clients with improved cost efficiency."
}

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)
    # Also handle possible HTML formatting issues like newlines
    # For example, what if it's broken across lines?
    
    # We can try a regex replace that ignores whitespace variations
    old_regex = r'\s*'.join([re.escape(w) for w in old.split()])
    content = re.sub(old_regex, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacements completed.")
