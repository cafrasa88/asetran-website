import os, re

def upgrade_estudios_viales():
    path = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website\servicio-estudios-viales.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_block = r'''<div class="entregables-grid">.*?</div>\s*</div>'''
    new_block = '''<div class="bento-grid-talleres" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.8rem;">
    <div class="phase-card glass" style="padding: 0; overflow: hidden; border-radius: 1.1rem; display: flex; flex-direction: column; border: 1px solid rgba(242, 53, 14, 0.35); background: rgba(255,255,255,0.03); box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
        <div style="width: 100%; aspect-ratio: 1 / 1; overflow: hidden; position: relative; margin: 0; padding: 0; background: #000;">
            <img src="assets/cat-estudios-ruta.jpg" alt="Informe de Estudio Vial" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; border: none; outline: none; margin: 0; padding: 0;">
        </div>
        <div style="padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; background: rgba(10, 14, 23, 0.95);">
            <span class="portal-tag" style="background: var(--color-primary); color: #fff; border: none; align-self: flex-start; margin-bottom: 0.6rem; font-weight: 700;">INFORME VIAL · DIAGNÓSTICO</span>
            <h3 style="font-size: 1.15rem; color: #fff; font-weight: 700; margin-bottom: 0.4rem;">1. Informe de Estudio Vial & Tránsito</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 1rem;">Levantamiento completo en terreno de flujos vehiculares, puntos ciegos y diseño geométrico seguro.</p>
            <span class="equip-tag" style="margin-top: auto; align-self: flex-start; background: rgba(242, 53, 14, 0.18); color: var(--color-primary); border: 1px solid rgba(242, 53, 14, 0.35); font-weight: 600;">Ingeniería de Tránsito HD</span>
        </div>
    </div>
    <div class="phase-card glass" style="padding: 0; overflow: hidden; border-radius: 1.1rem; display: flex; flex-direction: column; border: 1px solid rgba(242, 53, 14, 0.35); background: rgba(255,255,255,0.03); box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
        <div style="width: 100%; aspect-ratio: 1 / 1; overflow: hidden; position: relative; margin: 0; padding: 0; background: #000;">
            <img src="assets/cat-conductores.jpg" alt="Libro de Ruta Profesional" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; border: none; outline: none; margin: 0; padding: 0;">
        </div>
        <div style="padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; background: rgba(10, 14, 23, 0.95);">
            <span class="portal-tag" style="background: var(--color-primary); color: #fff; border: none; align-self: flex-start; margin-bottom: 0.6rem; font-weight: 700;">NUEVO · LIBRO DE RUTA</span>
            <h3 style="font-size: 1.15rem; color: #fff; font-weight: 700; margin-bottom: 0.4rem;">2. Libro de Ruta por Tipo de Vehículo</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 1rem;">Manual preventivo detallado de conducción por tramo, velocidades máximas y zonas de alto riesgo.</p>
            <span class="equip-tag" style="margin-top: auto; align-self: flex-start; background: rgba(242, 53, 14, 0.18); color: var(--color-primary); border: 1px solid rgba(242, 53, 14, 0.35); font-weight: 600;">Manual de Ruta Digital</span>
        </div>
    </div>
    <div class="phase-card glass" style="padding: 0; overflow: hidden; border-radius: 1.1rem; display: flex; flex-direction: column; border: 1px solid rgba(242, 53, 14, 0.35); background: rgba(255,255,255,0.03); box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
        <div style="width: 100%; aspect-ratio: 1 / 1; overflow: hidden; position: relative; margin: 0; padding: 0; background: #000;">
            <img src="assets/fleet-trucks.jpg" alt="Videos de Inducción Vial" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; border: none; outline: none; margin: 0; padding: 0;">
        </div>
        <div style="padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; background: rgba(10, 14, 23, 0.95);">
            <span class="portal-tag" style="background: var(--color-primary); color: #fff; border: none; align-self: flex-start; margin-bottom: 0.6rem; font-weight: 700;">MULTIMEDIA · INDUCCIÓN</span>
            <h3 style="font-size: 1.15rem; color: #fff; font-weight: 700; margin-bottom: 0.4rem;">3. Videos de Inducción Vial en Ruta</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 1rem;">Cápsulas audiovisuales de capacitación preventiva para conductores sobre tramos críticos de faena.</p>
            <span class="equip-tag" style="margin-top: auto; align-self: flex-start; background: rgba(242, 53, 14, 0.18); color: var(--color-primary); border: 1px solid rgba(242, 53, 14, 0.35); font-weight: 600;">Cápsulas HD 4K</span>
        </div>
    </div>
    <div class="phase-card glass" style="padding: 0; overflow: hidden; border-radius: 1.1rem; display: flex; flex-direction: column; border: 1px solid rgba(242, 53, 14, 0.35); background: rgba(255,255,255,0.03); box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
        <div style="width: 100%; aspect-ratio: 1 / 1; overflow: hidden; position: relative; margin: 0; padding: 0; background: #000;">
            <img src="assets/cat-senalizacion.jpg" alt="Valorización de Señalética" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; border: none; outline: none; margin: 0; padding: 0;">
        </div>
        <div style="padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; background: rgba(10, 14, 23, 0.95);">
            <span class="portal-tag" style="background: var(--color-primary); color: #fff; border: none; align-self: flex-start; margin-bottom: 0.6rem; font-weight: 700;">PRESUPUESTO · SEÑALÉICA</span>
            <h3 style="font-size: 1.15rem; color: #fff; font-weight: 700; margin-bottom: 0.4rem;">4. Valorización y Planimetría de Señalética</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 1rem;">Cálculo de presupuestos, planimetría CAD y especificaciones MOP para señalización reglamentaria.</p>
            <span class="equip-tag" style="margin-top: auto; align-self: flex-start; background: rgba(242, 53, 14, 0.18); color: var(--color-primary); border: 1px solid rgba(242, 53, 14, 0.35); font-weight: 600;">Presupuesto & CAD</span>
        </div>
    </div>
</div>'''
    content = re.sub(old_block, new_block, content, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Upgraded estudios viales cards!")

upgrade_estudios_viales()
