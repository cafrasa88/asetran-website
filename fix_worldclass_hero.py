import os, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

# 1. Update index.html Hero
index_path = os.path.join(html_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

old_idx_hero = r'<section id="inicio" class="hero"[^>]*>.*?</section>'
new_idx_hero = '''<section id="inicio" class="hero" style="position: relative; overflow: hidden; min-height: 85vh; display: flex; align-items: center; padding: 9rem 0 4rem 0; background: #0a0e17 url('assets/hero-bg.jpg') center/cover no-repeat;">
    <video class="hero-video" autoplay loop muted playsinline poster="assets/hero-bg.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; opacity: 0.85; filter: brightness(0.9) contrast(1.05);">
        <source src="assets/hero-video.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(10,14,23,0.8) 0%, rgba(10,14,23,0.4) 50%, rgba(10,14,23,0.7) 100%); z-index: 1; pointer-events: none;"></div>
    
    <div class="container hero-content" style="position: relative; z-index: 2; width: 100%; max-width: 880px; margin-left: 0; text-align: left;">
        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.2rem; flex-wrap: wrap;">
            <span class="badge" style="display: inline-block; font-size: 0.78rem; padding: 0.35rem 0.85rem; background: rgba(242, 53, 14, 0.22); color: #fff; border: 1px solid rgba(242, 53, 14, 0.45); font-weight: 700; border-radius: 4px; letter-spacing: 0.5px;">ORGANISMO DE INSPECCIÓN TIPO A · ISO 17020:2012</span>
            <div class="hero-accred-group" style="display: inline-flex; align-items: center; gap: 1rem; padding: 0.35rem 0.9rem; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.18); border-radius: 0.6rem; backdrop-filter: blur(8px);">
                <img src="assets/inn-logo-white.png" alt="INN CHILE OI-323" class="hero-accred-img" style="height: 38px; width: auto; object-fit: contain;">
                <img src="assets/iso-logo-white.png" alt="ISO 17020:2012" class="hero-accred-img" style="height: 38px; width: auto; object-fit: contain;">
            </div>
        </div>
        <h1 style="font-size: clamp(2.2rem, 4.8vw, 3.8rem); color: #ffffff; margin-bottom: 1.1rem; line-height: 1.15; font-weight: 800; text-shadow: 0 4px 20px rgba(0,0,0,0.95);">LA SEGURIDAD VIAL<br><span style="color: var(--color-primary);">NO ES ACCIDENTAL</span></h1>
        <p style="font-size: 1.05rem; color: #f1f5f9; line-height: 1.6; margin-bottom: 2rem; max-width: 720px; text-shadow: 0 2px 10px rgba(0,0,0,0.9);">Empresa líder en seguridad vial y colaboradora especializada en transporte terrestre de personas y carga. Proporcionamos seguridad y confiabilidad operativa mecánica.</p>
        <div class="hero-btns" style="display: flex; gap: 1.2rem; flex-wrap: wrap;">
            <a href="#servicios" class="btn btn-primary" style="padding: 0.95rem 2.4rem; font-weight: 700; font-size: 1.02rem;">Conocer Servicios</a>
            <a href="#contacto" class="btn btn-outline" style="padding: 0.95rem 2.4rem; font-weight: 600; font-size: 1.02rem; border-color: rgba(255,255,255,0.4); color: #ffffff;">Contactar</a>
        </div>
    </div>
</section>'''

idx_content = re.sub(old_idx_hero, new_idx_hero, idx_content, flags=re.DOTALL)
with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Updated Hero in index.html!")

# 2. Update all Service Detail Pages Hero
service_heroes = {
    "servicio-flotas.html": {
        "title": "Acreditación Mecánica de Flotas y Vehículos",
        "desc": "Inspecciones integrales de seguridad operacional para flotas de carga, transporte de personal y maquinaria pesada bajo la norma internacional ISO 17020:2012 por Organismo de Inspección Tipo A.",
        "poster": "assets/servicios/1-flotas/hero.jpg",
        "video": "assets/servicios/1-flotas/hero-video.mp4",
        "btn_text": "Solicitar Acreditación de Flota",
        "crumb": "Acreditación Mecánica de Flotas"
    },
    "servicio-talleres.html": {
        "title": "Certificación de Talleres Mecánicos",
        "desc": "Auditoría integral de infraestructura, instrumental técnico calibrado y nivel de competencia del personal para la certificación de talleres mecánicos de mantención.",
        "poster": "assets/cat-talleres.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Solicitar Certificación de Taller",
        "crumb": "Certificación de Talleres"
    },
    "servicio-conductores.html": {
        "title": "Acreditación & Psicotécnico de Conductores",
        "desc": "Evaluación sensométrica y visomotora de alta precisión para operadores de transporte de personas, carga pesada y vehículos de minería.",
        "poster": "assets/cat-psicotecnico.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Agendar Evaluaciones",
        "crumb": "Acreditación Conductores"
    },
    "servicio-end.html": {
        "title": "Análisis de Fallas & Ensayos No Destructivos (END)",
        "desc": "Diagnóstico de integridad estructural mediante Ultrasonido (UT), Líquidos Penetrantes (PT), Yugo Magnético (MT) y Pruebas de Hermeticidad acústica.",
        "poster": "assets/tech-ultrasound.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Solicitar Servicio END",
        "crumb": "Ensayos No Destructivos"
    },
    "servicio-quinta-rueda.html": {
        "title": "Certificación Técnica de Quinta Rueda",
        "desc": "Inspección rigurosa sin desmontaje que evalúa tolerancia de perno rey, tornamesa, mordazas de acople y plato en tractocamiones.",
        "poster": "assets/tech-fifth-wheel.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Solicitar Inspección Quinta Rueda",
        "crumb": "Certificación Quinta Rueda"
    },
    "servicio-estudios-viales.html": {
        "title": "Estudios de Ruta & Tránsito Industrial",
        "desc": "Levantamiento de campo, auditorías de velocidad, diseño geométrico de caminos y elaboración de Libros de Ruta preventivos.",
        "poster": "assets/cat-estudios-ruta.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Solicitar Estudio Vial",
        "crumb": "Estudios Viales"
    },
    "servicio-senalizacion.html": {
        "title": "Señalización Vial & Elementos de Tránsito",
        "desc": "Fabricación e instalación de señaléctica reflectiva Grado Diamante, pintura termoplástica de calzada y barreras de contención bionda.",
        "poster": "assets/cat-senalizacion.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Cotizar Señalización Vial",
        "crumb": "Señalización Vial"
    },
    "servicio-ito-mop.html": {
        "title": "Inspección Técnica de Obra (ITO MOP)",
        "desc": "Fiscalización técnica independiente de contratos de obra vial, recepción de partidas, ensayos de asfalto y planes de desvío de tránsito.",
        "poster": "assets/cat-ito-mop.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Solicitar Inspección ITO MOP",
        "crumb": "Inspección ITO MOP"
    },
    "servicio-peritajes.html": {
        "title": "Peritajes e Investigación de Siniestros Viales",
        "desc": "Reconstrucción física forense de colisiones, cálculo de velocidad de impacto, análisis metaloquímico de fallas y cartografía de puntos ciegos.",
        "poster": "assets/cat-accidentes.jpg",
        "video": "assets/hero-video.mp4",
        "btn_text": "Solicitar Informe Pericial",
        "crumb": "Peritajes de Siniestros"
    }
}

for fname, data in service_heroes.items():
    filepath = os.path.join(html_dir, fname)
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_hero_html = f'''<section class="service-detail-hero" style="position: relative; overflow: hidden; min-height: 75vh; display: flex; align-items: center; padding: 9rem 0 4rem 0; background: #0a0e17 url('{data['poster']}') center/cover no-repeat;">
            <video autoplay loop muted playsinline poster="{data['poster']}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; opacity: 0.85; filter: brightness(0.9) contrast(1.05);">
                <source src="{data['video']}" type="video/mp4">
            </video>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(10,14,23,0.8) 0%, rgba(10,14,23,0.4) 50%, rgba(10,14,23,0.7) 100%); z-index: 1; pointer-events: none;"></div>
            
            <div class="container hero-content" style="position: relative; z-index: 2; width: 100%; max-width: 880px; margin-left: 0; text-align: left;">
                <div class="breadcrumb" style="font-size: 0.85rem; color: var(--color-primary); margin-bottom: 0.9rem; font-weight: 600;">
                    <a href="index.html" style="color: var(--color-text-muted);">Inicio</a> / <a href="index.html#servicios" style="color: var(--color-text-muted);">Servicios</a> / <span>{data['crumb']}</span>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.2rem; flex-wrap: wrap;">
                    <span class="badge" style="display: inline-block; font-size: 0.78rem; padding: 0.35rem 0.85rem; background: rgba(242, 53, 14, 0.22); color: #fff; border: 1px solid rgba(242, 53, 14, 0.45); font-weight: 700; border-radius: 4px; letter-spacing: 0.5px;">ORGANISMO DE INSPECCIÓN TIPO A · ISO 17020:2012</span>
                    <div class="hero-accred-group" style="display: inline-flex; align-items: center; gap: 1rem; padding: 0.35rem 0.9rem; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.18); border-radius: 0.6rem; backdrop-filter: blur(8px);">
                        <img src="assets/inn-logo-white.png" alt="INN CHILE OI-323" class="hero-accred-img" style="height: 38px; width: auto; object-fit: contain;">
                        <img src="assets/iso-logo-white.png" alt="ISO 17020:2012" class="hero-accred-img" style="height: 38px; width: auto; object-fit: contain;">
                    </div>
                </div>
                <h1 style="font-size: clamp(1.8rem, 3.8vw, 3rem); color: #ffffff; margin-bottom: 0.9rem; line-height: 1.2; font-weight: 800; text-shadow: 0 4px 20px rgba(0,0,0,0.95);">{data['title']}</h1>
                <p style="font-size: 1.02rem; color: #f1f5f9; line-height: 1.55; margin-bottom: 1.8rem; max-width: 720px; text-shadow: 0 2px 10px rgba(0,0,0,0.9);">{data['desc']}</p>
                <div class="hero-btns" style="display: flex; gap: 1.2rem; flex-wrap: wrap;">
                    <a href="#solicitar" class="btn btn-primary" style="padding: 0.9rem 2.2rem; font-weight: 700; font-size: 1rem;">{data['btn_text']}</a>
                    <a href="index.html#servicios" class="btn btn-outline" style="padding: 0.9rem 2.2rem; font-weight: 600; font-size: 1rem; border-color: rgba(255,255,255,0.4); color: #ffffff;">← Volver al Catálogo</a>
                </div>
            </div>
        </section>'''

    content = re.sub(
        r'<section class="service-detail-hero"[^>]*>.*?</section>',
        new_hero_html,
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated Hero in: {fname}")

print("Successfully applied world-class Hero layout across all pages!")
