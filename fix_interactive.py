import re

file_path = r'c:\Users\91708\Downloads\FInal-dccb-site\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS to inject
css_styles = """
    <style>
      .metric-card {
        position: relative;
        overflow: hidden;
        border-radius: var(--r-md);
        transition: all 0.3s ease;
        background: white;
        padding: 32px;
        box-shadow: var(--shadow-sm);
        z-index: 1;
      }
      .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-md);
      }
      .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(135deg, rgba(0,168,107,0.05), rgba(0,184,212,0.05));
        z-index: -1;
        opacity: 0;
        transition: opacity 0.3s ease;
      }
      .metric-card:hover::before {
        opacity: 1;
      }
      .metric-reveal {
        margin-top: 16px;
        padding-top: 16px;
        border-top: 1px dashed var(--sand);
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      .metric-row {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        align-items: center;
      }
      .val-current { color: var(--text-muted); text-decoration: line-through; }
      .val-ai { color: var(--emerald); font-weight: 700; font-size: 14px; }
      .progress-bg { background: var(--sand); height: 6px; border-radius: 3px; width: 100%; overflow: hidden; margin-top:4px; }
      .progress-bar { height: 100%; border-radius: 3px; background: var(--emerald); transition: width 1.5s cubic-bezier(0.22, 1, 0.36, 1); width: 0; }
      .metric-card:hover .progress-bar { width: var(--target-width) !important; }
      .callout-box:hover .progress-bar { width: var(--target-width) !important; }
    </style>
"""

# Inject CSS right before the ai-readiness section
if '<!-- ══════════════════════════════════════════════════════\n     NEW SECTION: AI READINESS & AUTOMATION IN RFI' in content and 'metric-card' not in content:
    content = content.replace('<!-- ══════════════════════════════════════════════════════\n     NEW SECTION: AI READINESS & AUTOMATION IN RFI', css_styles + '\n    <!-- ══════════════════════════════════════════════════════\n     NEW SECTION: AI READINESS & AUTOMATION IN RFI')


# 1. Replace STCB Tier in AI Readiness
old_stcb = """<div class="callout-box cb-emerald reveal">
            <h3 style="font-size:16px;font-family:'Syne',sans-serif;margin-bottom:12px;"><i class="fas fa-building"></i> STCB Tier (High Readiness)</h3>
            <p><strong>100% CBS Adoption:</strong> At the apex level, all 34 STCBs are fully CBS integrated, generating structured financial data. Liquid surplus management and apex-level treasury operations are immediately ready for AI forecasting models.</p>
          </div>"""
new_stcb = """<div class="callout-box cb-emerald reveal" style="position:relative; overflow:hidden; transition:all 0.3s ease;">
            <h3 style="font-size:16px;font-family:'Syne',sans-serif;margin-bottom:12px;"><i class="fas fa-building"></i> STCB Tier (High Readiness)</h3>
            <p style="margin-bottom:16px;"><strong>100% CBS Adoption:</strong> At the apex level, all 34 STCBs are fully CBS integrated. Liquid surplus management and treasury are ready for AI forecasting.</p>
            <div class="metric-reveal" style="border-top-color:rgba(0,168,107,0.2);">
              <div class="metric-row"><span style="color:var(--emerald-bright);">Working Capital Data Lake</span> <strong style="color:white;font-size:14px;">₹4,55,187 Cr</strong></div>
              <div class="metric-row"><span style="color:var(--emerald-bright);">Total Deposits Captured</span> <strong style="color:white;font-size:14px;">₹2,54,937 Cr</strong></div>
              <div class="progress-bg" style="background:rgba(255,255,255,0.1);"><div class="progress-bar" style="--target-width:100%; background:var(--emerald-bright);"></div></div>
              <div style="font-size:10px;color:rgba(255,255,255,0.5);margin-top:2px;">100% Data Structuring Complete (Hover to load)</div>
            </div>
          </div>"""
content = content.replace(old_stcb, new_stcb)

# 2. Replace DCCB Tier in AI Readiness
old_dccb = """<div class="callout-box cb-amber reveal">
            <h3 style="font-size:16px;font-family:'Syne',sans-serif;margin-bottom:12px;"><i class="fas fa-university"></i> DCCB Tier (Moderate Readiness)</h3>
            <p><strong>CBS Operational but Siloed:</strong> While all 351 DCCBs have CBS, data quality is inconsistent. Regulatory reporting (OSS) remains heavily manual. AI Readiness requires intermediary RPA data pipelines to sanitize and structure CBS outputs for ML models.</p>
          </div>"""
new_dccb = """<div class="callout-box cb-amber reveal" style="position:relative; overflow:hidden; transition:all 0.3s ease;">
            <h3 style="font-size:16px;font-family:'Syne',sans-serif;margin-bottom:12px;"><i class="fas fa-university"></i> DCCB Tier (Moderate Readiness)</h3>
            <p style="margin-bottom:16px;"><strong>CBS Operational but Siloed:</strong> All 351 DCCBs have CBS, but reporting remains manual. AI Readiness requires RPA data pipelines to sanitize outputs.</p>
            <div class="metric-reveal" style="border-top-color:rgba(212,130,10,0.2);">
              <div class="metric-row"><span style="color:var(--amber-bright);">Total Offices (Data Nodes)</span> <strong style="color:white;font-size:14px;">14,228</strong></div>
              <div class="metric-row"><span style="color:var(--amber-bright);">NPA Burden (Needs Prediction)</span> <strong style="color:white;font-size:14px;">₹35,032 Cr (9.6%)</strong></div>
              <div class="progress-bg" style="background:rgba(255,255,255,0.1);"><div class="progress-bar" style="--target-width:50%; background:var(--amber-bright);"></div></div>
              <div style="font-size:10px;color:rgba(255,255,255,0.5);margin-top:2px;">~50% Data Structuring via Manual Intermediaries</div>
            </div>
          </div>"""
content = content.replace(old_dccb, new_dccb)

# 3. Replace PACS Tier in AI Readiness
old_pacs = """<div class="callout-box cb-dark reveal">
            <h3 style="font-size:16px;font-family:'Syne',sans-serif;margin-bottom:12px;"><i class="fas fa-leaf"></i> PACS Tier (Low Readiness)</h3>
            <p><strong>Severe Digital Deficit:</strong> With <15% CBS connectivity among 1,01,524 PACS, last-mile agricultural credit data is effectively "dark". Strategic priority must be mobile-first OCR digitisation of paper ledgers to build the foundational data lake.</p>
          </div>"""
new_pacs = """<div class="callout-box cb-dark reveal" style="position:relative; overflow:hidden; transition:all 0.3s ease;">
            <h3 style="font-size:16px;font-family:'Syne',sans-serif;margin-bottom:12px;"><i class="fas fa-leaf"></i> PACS Tier (Low Readiness)</h3>
            <p style="margin-bottom:16px;"><strong>Severe Digital Deficit:</strong> Last-mile agricultural credit data is effectively "dark". Strategic priority must be mobile-first OCR digitisation.</p>
            <div class="metric-reveal" style="border-top-color:rgba(255,255,255,0.1);">
              <div class="metric-row"><span style="color:var(--text-muted);">Operational PACS</span> <strong style="color:white;font-size:14px;">1,01,524</strong></div>
              <div class="metric-row"><span style="color:var(--text-muted);">Dark Data Member Base</span> <strong style="color:white;font-size:14px;">~6 Cr</strong></div>
              <div class="progress-bg" style="background:rgba(255,255,255,0.1);"><div class="progress-bar" style="--target-width:15%; background:#ff7070;"></div></div>
              <div style="font-size:10px;color:rgba(255,255,255,0.5);margin-top:2px;">&lt;15% CBS Connectivity</div>
            </div>
          </div>"""
content = content.replace(old_pacs, new_pacs)


# 4. Replace AI Automation Cards
old_card1 = """<div class="reveal" style="background:white;padding:32px;border-radius:var(--r-md);box-shadow:var(--shadow-sm);">
            <div style="width:48px;height:48px;background:rgba(0,168,107,0.1);color:var(--emerald);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-chart-line"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">1. AI Credit Scoring for KCC</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Moving beyond rudimentary land-holding metrics by integrating PMFBY, satellite NDVI data, and historical transaction frequency. Capable of reducing the 14-42 day processing TAT to < 5 days while improving NPA prediction.</p>
          </div>"""
new_card1 = """<div class="metric-card reveal">
            <div style="width:48px;height:48px;background:rgba(0,168,107,0.1);color:var(--emerald);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-chart-line"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">1. AI Credit Scoring for KCC</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Integrating PMFBY and satellite NDVI data to optimize the <strong>₹3,66,708 Cr</strong> DCCB loan portfolio. Predicts NPA prior to SMA classification.</p>
            <div class="metric-reveal">
              <div class="metric-row"><span>Processing TAT</span> <div><span class="val-current">14-42 Days</span> <i class="fas fa-arrow-right" style="color:var(--sand);margin:0 4px;font-size:10px;"></i> <span class="val-ai">&lt; 5 Days</span></div></div>
              <div class="progress-bg"><div class="progress-bar" style="--target-width:85%;"></div></div>
              <div style="font-size:10px;color:var(--emerald);margin-top:2px;text-align:right;">85% Faster Approvals</div>
            </div>
          </div>"""
content = content.replace(old_card1, new_card1)

old_card2 = """<div class="reveal" style="background:white;padding:32px;border-radius:var(--r-md);box-shadow:var(--shadow-sm);">
            <div style="width:48px;height:48px;background:rgba(212,130,10,0.1);color:var(--amber);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-exclamation-triangle"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">2. NPA Early Warning Systems (EWS)</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Crucial for addressing the ₹35,032 Cr gross NPA burden. EWS ML models analyze cash-flow velocity and account behavior anomalies to flag potential defaults 60-90 days before formal SMA classification.</p>
          </div>"""
new_card2 = """<div class="metric-card reveal">
            <div style="width:48px;height:48px;background:rgba(212,130,10,0.1);color:var(--amber);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-exclamation-triangle"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">2. NPA Early Warning Systems (EWS)</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Crucial for addressing the <strong>₹35,032 Cr</strong> gross NPA burden. EWS ML models flag potential defaults 60-90 days early via cash-flow anomalies.</p>
            <div class="metric-reveal">
              <div class="metric-row"><span>NPA Reduction Target</span> <div><span class="val-current">9.6% Ratio</span> <i class="fas fa-arrow-right" style="color:var(--sand);margin:0 4px;font-size:10px;"></i> <span class="val-ai" style="color:var(--amber);">~7.5%</span></div></div>
              <div class="progress-bg"><div class="progress-bar" style="--target-width:20%; background:var(--amber);"></div></div>
              <div style="font-size:10px;color:var(--amber);margin-top:2px;text-align:right;">Estimated Asset Value Saved: ₹7,006 Cr</div>
            </div>
          </div>"""
content = content.replace(old_card2, new_card2)

old_card3 = """<div class="reveal" style="background:white;padding:32px;border-radius:var(--r-md);box-shadow:var(--shadow-sm);">
            <div style="width:48px;height:48px;background:rgba(0,184,212,0.1);color:var(--cyan);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-microchip"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">3. RPA Compliance Automation</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Automating XBRL generation and OSS regulatory reporting. Reduces the estimated 780+ person-hours per cycle required by DCCBs to < 90 hours, freeing up operational capacity.</p>
          </div>"""
new_card3 = """<div class="metric-card reveal">
            <div style="width:48px;height:48px;background:rgba(0,184,212,0.1);color:var(--cyan);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-microchip"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">3. RPA Compliance Automation</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Automating XBRL and OSS regulatory reporting across all <strong>14,228</strong> DCCB offices, freeing up massive operational capacity.</p>
            <div class="metric-reveal">
              <div class="metric-row"><span>Compliance Labor</span> <div><span class="val-current">780+ Hrs/Cycle</span> <i class="fas fa-arrow-right" style="color:var(--sand);margin:0 4px;font-size:10px;"></i> <span class="val-ai" style="color:var(--cyan);">&lt; 90 Hrs</span></div></div>
              <div class="progress-bg"><div class="progress-bar" style="--target-width:88%; background:var(--cyan);"></div></div>
              <div style="font-size:10px;color:var(--cyan);margin-top:2px;text-align:right;">88% Automation Efficiency</div>
            </div>
          </div>"""
content = content.replace(old_card3, new_card3)

old_card4 = """<div class="reveal" style="background:white;padding:32px;border-radius:var(--r-md);box-shadow:var(--shadow-sm);">
            <div style="width:48px;height:48px;background:rgba(139,92,246,0.1);color:#8b5cf6;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-microphone-alt"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">4. Multilingual Voice Banking</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Vernacular NLP models integrated with IVR to bridge the digital divide for the 6 Cr predominantly rural PACS members, enabling voice-based balance inquiries and transaction initiation without smartphone reliance.</p>
          </div>"""
new_card4 = """<div class="metric-card reveal">
            <div style="width:48px;height:48px;background:rgba(139,92,246,0.1);color:#8b5cf6;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:20px;"><i class="fas fa-microphone-alt"></i></div>
            <h3 style="font-family:'Syne',sans-serif;font-size:18px;margin-bottom:12px;">4. Multilingual Voice Banking</h3>
            <p style="font-size:13px;color:var(--text-muted);line-height:1.6;">Vernacular NLP integrated with IVR to bridge the digital divide for the <strong>6.76 Lakh</strong> DCCB and <strong>~6 Cr</strong> PACS members.</p>
            <div class="metric-reveal">
              <div class="metric-row"><span>Digital Service Reach</span> <div><span class="val-current">Smartphone Only</span> <i class="fas fa-arrow-right" style="color:var(--sand);margin:0 4px;font-size:10px;"></i> <span class="val-ai" style="color:#8b5cf6;">100% Telecom Reach</span></div></div>
              <div class="progress-bg"><div class="progress-bar" style="--target-width:100%; background:#8b5cf6;"></div></div>
              <div style="font-size:10px;color:#8b5cf6;margin-top:2px;text-align:right;">Universal Inclusion via Feature Phones</div>
            </div>
          </div>"""
content = content.replace(old_card4, new_card4)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated AI sections with real data and interactive CSS hover states.")
