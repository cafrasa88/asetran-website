import os
import glob
import re

mobile_css = """
<style id="mobile-master-override">
/* 100% PERFECT WORLD CLASS DUAL PC & MOBILE LAYOUT (CACHE BYPASS v12000) */
html, body { 
  overflow-x: hidden !important; 
  max-width: 100vw !important; 
  width: 100% !important; 
  margin: 0 !important; 
  padding: 0 !important; 
}
* { 
  box-sizing: border-box !important; 
}

/* UNIVERSAL HERO VIDEO BRIGHTNESS & OVERLAY */
.hero-video,
video[autoplay] {
  position: absolute !important;
  top: 50% !important;
  left: 50% !important;
  min-width: 100% !important;
  min-height: 100% !important;
  width: auto !important;
  height: auto !important;
  transform: translate(-50%, -50%) !important;
  object-fit: cover !important;
  z-index: 0 !important;
  opacity: 1 !important;
  filter: brightness(0.95) contrast(1.05) !important;
}

.hero-overlay {
  position: absolute !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background: linear-gradient(180deg, rgba(10, 14, 23, 0.45) 0%, rgba(10, 14, 23, 0.65) 60%, rgba(10, 14, 23, 0.95) 100%) !important;
  z-index: 1 !important;
  pointer-events: none !important;
}

/* FIX VERTICAL GAP BETWEEN STATS BAR & QUIÉNES SOMOS */
.stats-section {
  padding: 0 !important;
  margin-top: 1.5rem !important;
  margin-bottom: 0 !important;
}

#nosotros {
  padding-top: 2rem !important;
}

/* UNIVERSAL CARD HOMOGENEITY & EQUAL HEIGHT */
.phase-card,
.service-portal-card,
.catalog-card,
.protocol-step-card,
.fleet-card {
  display: flex !important;
  flex-direction: column !important;
  height: 100% !important;
  border-radius: 1.1rem !important;
  overflow: hidden !important;
  border: 1px solid rgba(242, 53, 14, 0.35) !important;
  background: rgba(10, 14, 23, 0.95) !important;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5) !important;
  box-sizing: border-box !important;
}

.phase-card div[style*="aspect-ratio"],
.service-portal-card div[style*="aspect-ratio"],
.catalog-card div[style*="aspect-ratio"],
.fleet-card div[style*="aspect-ratio"] {
  width: 100% !important;
  aspect-ratio: 16 / 10 !important;
  max-height: none !important;
  overflow: hidden !important;
  flex-shrink: 0 !important;
  position: relative !important;
}

.phase-card img,
.service-portal-card img,
.catalog-card img,
.fleet-card img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
}

.phase-card p,
.service-portal-card p,
.catalog-card p,
.fleet-card p {
  font-size: 0.85rem !important;
  color: #cbd5e1 !important;
  line-height: 1.45 !important;
  margin-bottom: 1rem !important;
  display: -webkit-box !important;
  -webkit-line-clamp: 3 !important;
  -webkit-box-orient: vertical !important;
  overflow: hidden !important;
}

.phase-card .equip-tag,
.service-portal-card .equip-tag,
.catalog-card .equip-tag,
.fleet-card .equip-tag {
  margin-top: auto !important;
  align-self: flex-start !important;
  background: rgba(242, 53, 14, 0.18) !important;
  color: var(--color-primary) !important;
  border: 1px solid rgba(242, 53, 14, 0.35) !important;
  font-weight: 600 !important;
  padding: 0.35rem 0.75rem !important;
  border-radius: 6px !important;
  font-size: 0.78rem !important;
}

/* DESKTOP SPECIFIC RULES (PC SCREEN >= 1024px) */
@media (min-width: 1024px) {
  .hero {
    min-height: 100vh !important;
    padding-top: 6rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }

  .hero-content {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    max-width: 920px !important;
    margin: 0 auto !important;
    position: relative !important;
    z-index: 3 !important;
  }

  .hero-btns {
    display: flex !important;
    gap: 1.2rem !important;
    justify-content: center !important;
    align-items: center !important;
  }

  .service-portal-grid,
  .catalog-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 1.8rem !important;
  }

  .bento-grid-talleres,
  .quinta-phases-grid,
  .protocol-steps-grid,
  .fleet-grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1.8rem !important;
  }
}

/* MOBILE SPECIFIC RULES (TELEPHONE SCREEN <= 768px) */
@media (max-width: 768px) {
  .container { 
    padding: 0 1rem !important; 
    max-width: 100% !important; 
    box-sizing: border-box !important; 
  }

  .hero,
  .service-detail-hero { 
    min-height: auto !important; 
    padding: 6.5rem 1rem 2rem 1rem !important; 
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
  }

  .hero-content {
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 auto !important;
    padding: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
  }

  .service-detail-hero h1,
  .hero h1 { 
    font-size: 1.65rem !important; 
    line-height: 1.25 !important; 
    margin-top: 0.5rem !important;
    margin-bottom: 0.8rem !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.95) !important;
  }

  .service-detail-hero p,
  .hero p { 
    font-size: 0.92rem !important; 
    line-height: 1.5 !important; 
    color: #f1f5f9 !important;
    margin-bottom: 1.4rem !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.9) !important;
  }

  .breadcrumb {
    font-size: 0.78rem !important;
    white-space: normal !important;
    word-wrap: break-word !important;
    margin-bottom: 0.6rem !important;
  }

  .hero-btns {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.75rem !important;
    width: 100% !important;
    margin-top: 1rem !important;
    align-items: center !important;
  }

  .hero-btns .btn,
  .hero-btns a {
    width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    text-align: center !important;
    justify-content: center !important;
    display: flex !important;
    align-items: center !important;
    box-sizing: border-box !important;
    white-space: nowrap !important;
    font-size: 0.95rem !important;
    padding: 0.85rem 1rem !important;
  }

  .stats-bar { 
    margin-top: 1.5rem !important;
    margin-bottom: 0.5rem !important;
    grid-template-columns: 1fr 1fr !important; 
    gap: 0.8rem !important; 
    padding: 0.85rem !important; 
    position: relative !important;
    z-index: 2 !important;
    clear: both !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .stat-item h3 { 
    font-size: 1.6rem !important; 
  }

  .stat-item p { 
    font-size: 0.72rem !important; 
  }

  #nosotros {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
  }

  .solicitar-box,
  #solicitar {
    padding: 1.25rem 1rem !important;
    margin-top: 2rem !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    border-radius: 1rem !important;
  }

  .solicitar-box h3,
  #solicitar h3 {
    font-size: 1.35rem !important;
    margin-bottom: 0.5rem !important;
  }

  .solicitar-box p,
  #solicitar p {
    font-size: 0.88rem !important;
    margin-bottom: 1.2rem !important;
  }

  .service-inquiry-form,
  form,
  #solicitar form { 
    display: grid !important; 
    grid-template-columns: 1fr !important; 
    gap: 0.85rem !important; 
    width: 100% !important; 
    max-width: 100% !important;
    box-sizing: border-box !important; 
  }

  form input, 
  form select, 
  form textarea, 
  form button, 
  form div,
  .form-textarea,
  .form-actions-wrapper { 
    grid-column: span 1 !important; 
    grid-column: 1 / -1 !important;
    width: 100% !important; 
    max-width: 100% !important; 
    box-sizing: border-box !important; 
    margin: 0 !important;
  }

  .form-actions-wrapper,
  form div[style*="display: flex"],
  #solicitar form div {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.75rem !important;
    width: 100% !important;
    align-items: stretch !important;
    margin-top: 0.5rem !important;
  }

  .form-actions-wrapper .btn,
  .form-actions-wrapper a,
  form div .btn,
  form div a.btn,
  #solicitar form div .btn,
  #solicitar form div a {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    white-space: nowrap !important;
    font-size: 0.92rem !important;
    padding: 0.85rem 1rem !important;
  }

  .accreditation-block {
    padding: 1.25rem 1rem !important;
    max-width: 100% !important;
    width: 100% !important;
    margin: 2rem 0 !important;
    box-sizing: border-box !important;
  }

  .accreditation-header h3 {
    font-size: 1.3rem !important;
    line-height: 1.3 !important;
  }

  .accreditation-logos {
    display: flex !important;
    flex-direction: column !important;
    gap: 1rem !important;
    width: 100% !important;
  }

  .accreditation-card {
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .strategy-banner {
    flex-direction: column !important;
    text-align: center !important;
    padding: 0.8rem 0.9rem !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .strategy-banner span {
    white-space: normal !important;
    word-wrap: break-word !important;
  }
  
  .catalog-grid, 
  .service-portal-grid, 
  .bento-grid-talleres, 
  .quinta-phases-grid, 
  .protocol-steps-grid, 
  .protocol-grid, 
  .protocol-grid-photo, 
  .news-grid, 
  .services-secondary-grid, 
  .pillars-grid, 
  .entregables-grid, 
  .fleet-grid,
  .values-grid {
    display: grid !important; 
    grid-template-columns: 1fr !important; 
    gap: 1.25rem !important; 
    width: 100% !important; 
    box-sizing: border-box !important;
  }

  .service-portal-card, 
  .catalog-card, 
  .phase-card, 
  .protocol-step-card,
  .fleet-card {
    grid-column: span 1 !important; 
    grid-column: 1 / -1 !important;
    width: 100% !important; 
    max-width: 100% !important; 
    height: auto !important; 
    min-height: auto !important; 
    box-sizing: border-box !important;
    margin: 0 !important;
  }

  .workflow-section {
    padding: 1.25rem 1rem !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .workflow-steps {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
    width: 100% !important;
  }

  .workflow-step {
    width: 100% !important;
    box-sizing: border-box !important;
    text-align: left !important;
    display: flex !important;
    align-items: center !important;
    gap: 1rem !important;
    padding: 0.9rem 1rem !important;
  }

  .workflow-arrow {
    display: none !important;
  }

  .master-photo-banner { 
    height: auto !important; 
    min-height: 240px !important; 
    width: 100% !important; 
    border-radius: 0.9rem !important; 
    overflow: hidden !important; 
  }

  .master-banner-overlay { 
    padding: 1.2rem !important; 
    display: flex !important; 
    flex-direction: column !important; 
    justify-content: flex-end !important; 
    align-items: flex-start !important; 
    text-align: left !important; 
    background: linear-gradient(to top, rgba(10, 14, 23, 0.96) 0%, rgba(10, 14, 23, 0.65) 60%, rgba(10, 14, 23, 0.2) 100%) !important; 
  }

  .master-banner-tag { 
    font-size: 0.68rem !important; 
    padding: 0.35rem 0.75rem !important; 
    margin-bottom: 0.6rem !important; 
    display: inline-block !important; 
    max-width: 100% !important; 
    white-space: normal !important; 
    line-height: 1.3 !important; 
  }

  .master-banner-overlay h4 { 
    font-size: 1.15rem !important; 
    line-height: 1.35 !important; 
    margin: 0 !important; 
  }
}

@media (max-width: 480px) {
  .service-detail-hero h1,
  .hero h1 { 
    font-size: 1.45rem !important; 
  }
  .master-banner-overlay h4 { 
    font-size: 1.05rem !important; 
  }
}
</style>
"""

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"
count = 0
for filepath in glob.glob(os.path.join(html_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Cache buster for styles.css
    content = re.sub(
        r'href=["\']css/styles\.css(\?v=[^\'\"]*)?["\']',
        'href="css/styles.css?v=20260801_v12000"',
        content
    )

    # Remove old inline style override if present
    content = re.sub(
        r'<style id="mobile-master-override">.*?</style>',
        '',
        content,
        flags=re.DOTALL
    )

    # Inject before </head>
    if "</head>" in content:
        content = content.replace("</head>", f"{mobile_css}\n</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1
    print(f"Updated: {os.path.basename(filepath)}")

print(f"Successfully updated {count} HTML files with v12000 cache buster and gap fix!")
