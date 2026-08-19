import os, re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"

# 1. Update index.html Hero (Clean Centered Video Hero)
index_path = os.path.join(html_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

old_idx_hero = r'<section id="inicio" class="hero"[^>]*>.*?</section>'
new_idx_hero = '''<section id="inicio" class="hero">
    <video class="hero-video" autoplay loop muted playsinline poster="assets/hero-bg.jpg">
        <source src="assets/hero-video.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay"></div>
    
    <div class="container hero-content reveal">
        <div class="hero-accred-group">
            <img src="assets/inn-logo-white.png" alt="INN CHILE OI-323" class="hero-accred-img">
            <img src="assets/iso-logo-white.png" alt="ISO 17020:2012" class="hero-accred-img">
        </div>
        <div>
            <span class="badge">Organismo de Inspección Tipo A · ISO 17020:2012</span>
        </div>
        <h1>LA SEGURIDAD VIAL<br><span style="color: var(--color-primary);">NO ES ACCIDENTAL</span></h1>
        <p>Empresa líder en seguridad vial y colaboradora especializada en transporte terrestre de personas y carga. Proporcionamos seguridad y confiabilidad operativa mecánica.</p>
        <div class="hero-btns">
            <a href="#servicios" class="btn btn-primary">Conocer Servicios</a>
            <a href="#contacto" class="btn btn-outline">Contactar</a>
        </div>
    </div>
</section>'''

idx_content = re.sub(old_idx_hero, new_idx_hero, idx_content, flags=re.DOTALL)
with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Restored clean centered Video Hero in index.html!")

# 2. Update all Service Detail Pages Hero (Clean Video / Photo Hero)
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

    new_hero_html = f'''<section class="service-detail-hero">
            <video class="hero-video" autoplay loop muted playsinline poster="{data['poster']}">
                <source src="{data['video']}" type="video/mp4">
            </video>
            <div class="hero-overlay"></div>
            
            <div class="container hero-content">
                <div class="breadcrumb" style="margin-bottom: 1rem;">
                    <a href="index.html">Inicio</a> / <a href="index.html#servicios">Servicios</a> / <span>{data['crumb']}</span>
                </div>
                <div class="hero-accred-group">
                    <img src="assets/inn-logo-white.png" alt="INN CHILE OI-323" class="hero-accred-img">
                    <img src="assets/iso-logo-white.png" alt="ISO 17020:2012" class="hero-accred-img">
                </div>
                <h1>{data['title']}</h1>
                <p>{data['desc']}</p>
                <div class="hero-btns">
                    <a href="#solicitar" class="btn btn-primary">{data['btn_text']}</a>
                    <a href="index.html#servicios" class="btn btn-outline">← Volver al Catálogo</a>
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
    print(f"Restored clean Hero in: {fname}")

print("Successfully restored clean HTML Hero structure across all 10 pages!")
