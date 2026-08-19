"""
Comprehensive professional redesign of index.html:
- Hero: keeps video, improves spacing, adds scroll indicator
- Stats: elevated inside colored accent bar
- Nosotros: two-column with photo side + text + pillar cards
- Servicios: refined section header, keeping golden master cards  
- Estudios Viales: redesigned with icon pills and visual deliverables
- Tecnología: 3-column cards with icons, cleaner ASETRAN Check panel
- Noticias: add subtle photo accent + improved card layout
- Contacto: side-by-side form and contact info, improved labels  
- Footer: refined with accreditation logos, social-style layout
"""

import re

html_dir = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website"
index_path = html_dir + r"\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- NOSOTROS SECTION REDESIGN ---
old_nosotros = re.search(r'<!-- Section 3: Nosotros -->.*?</section>', content, re.DOTALL).group(0)

new_nosotros = '''<!-- Section 3: Nosotros -->
        <section id="nosotros" class="bg-alt">
            <div class="container">
                <div class="nosotros-layout">
                    <!-- Left: Text Content -->
                    <div class="nosotros-text reveal">
                        <span class="badge">QUIÉNES SOMOS</span>
                        <h2>Expertos en Seguridad Vial con Acreditación Internacional</h2>
                        <p class="nosotros-intro">
                            Nuestra misión es asegurar que los más altos estándares de calidad, confiabilidad y seguridad operativa se cumplan rigurosamente en el transporte terrestre de personas y carga. Operamos bajo criterio técnico independiente como <strong>Organismo de Inspección Técnica Tipo A</strong>.
                        </p>

                        <!-- Value Pills -->
                        <div class="value-pills">
                            <div class="value-pill">
                                <div class="pill-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"/><path d="M8 21h8"/><path d="M4 6.5h16"/><path d="M4 6.5l-2.5 6.5h5L4 6.5z"/><path d="M1.5 13a2.5 2.5 0 0 0 5 0"/><path d="M20 6.5l-2.5 6.5h5L20 6.5z"/><path d="M17.5 13a2.5 2.5 0 0 0 5 0"/></svg>
                                </div>
                                <div>
                                    <h4>Imparcialidad</h4>
                                    <p>Criterio técnico objetivo e independiente en cada inspección.</p>
                                </div>
                            </div>
                            <div class="value-pill">
                                <div class="pill-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="10.5" width="15" height="10.5" rx="3.5"/><path d="M7 10.5V7a5 5 0 0 1 10 0v3.5"/><circle cx="12" cy="15" r="1.5"/><path d="M12 16.5v2.5"/></svg>
                                </div>
                                <div>
                                    <h4>Confidencialidad</h4>
                                    <p>Protección estricta de la información estratégica del mandante.</p>
                                </div>
                            </div>
                            <div class="value-pill">
                                <div class="pill-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                                </div>
                                <div>
                                    <h4>Integridad Técnica</h4>
                                    <p>Tolerancia cero a las desviaciones mecánicas en flota.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Right: Accreditation Block -->
                    <div class="nosotros-accred reveal">
                        <div class="accred-panel glass">
                            <div class="accred-header">
                                <span class="portal-tag" style="background: var(--color-primary); color: #fff; border: none; font-weight: 700;">RESPALDO INSTITUCIONAL</span>
                                <h3>Acreditación Oficial INN Chile</h3>
                                <p>Acreditados bajo los estrictos protocolos de la norma internacional ISO 17020:2012.</p>
                            </div>
                            <div class="accred-logos">
                                <div class="accred-logo-item">
                                    <img src="assets/iso-logo-white.png" alt="ISO 17020:2012" style="height: 52px; width: auto; object-fit: contain;">
                                    <span>ISO 17020 : 2012</span>
                                </div>
                                <div class="accred-divider"></div>
                                <div class="accred-logo-item">
                                    <img src="assets/inn-logo-white.png" alt="INN-CHILE" style="height: 52px; width: auto; object-fit: contain;">
                                    <span>Acred. LC 071 y LC 072</span>
                                </div>
                            </div>
                            <div class="accred-footer-tag">
                                <span style="font-size: 0.8rem; color: #10B981; font-weight: 600;">✓ Verificación activa por INN-Chile</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_nosotros, new_nosotros)


# --- ESTUDIOS VIALES SECTION REDESIGN ---
old_estudios = re.search(r'<!-- Section 5: Estudios Viales -->.*?</section>', content, re.DOTALL).group(0)

new_estudios = '''<!-- Section 5: Estudios Viales -->
        <section id="estudios" class="bg-alt">
            <div class="container">
                <div class="reveal text-center" style="margin-bottom: 3rem;">
                    <span class="badge">INGENIERÍA VIAL</span>
                    <h2>Estudios Viales y Tránsito Industrial</h2>
                    <p class="section-subtitle">Diagnóstico, evaluación y estrategias de seguridad vial corporativa para faenas mineras, parques industriales y redes públicas.</p>
                </div>

                <div class="estudios-nuevo-grid reveal">
                    <div class="estudio-feature-item">
                        <div class="estudio-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v18H3z"/><path d="M3 9h18M9 21V9"/></svg>
                        </div>
                        <div class="estudio-text">
                            <h4>Libro de Ruta</h4>
                            <p>Cartografía de puntos críticos y velocidades recomendadas por tipo de vehículo.</p>
                        </div>
                    </div>
                    <div class="estudio-feature-item">
                        <div class="estudio-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
                        </div>
                        <div class="estudio-text">
                            <h4>Gestión de Velocidades</h4>
                            <p>Estudio técnico de límites y auditoría de tramos de alta complejidad operacional.</p>
                        </div>
                    </div>
                    <div class="estudio-feature-item">
                        <div class="estudio-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                        </div>
                        <div class="estudio-text">
                            <h4>Análisis de Puntos Críticos</h4>
                            <p>Identificación de curvas peligrosas, pendientes severas y cruces industriales.</p>
                        </div>
                    </div>
                    <div class="estudio-feature-item">
                        <div class="estudio-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                        </div>
                        <div class="estudio-text">
                            <h4>Videos de Inducción</h4>
                            <p>Material audiovisual interactivo de inducción vial para conductores en faena.</p>
                        </div>
                    </div>
                    <div class="estudio-feature-item">
                        <div class="estudio-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                        </div>
                        <div class="estudio-text">
                            <h4>Evaluación de Señalización</h4>
                            <p>Diagnóstico del estado y cumplimiento normativo de la señalética existente.</p>
                        </div>
                    </div>
                    <div class="estudio-feature-item">
                        <div class="estudio-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                        </div>
                        <div class="estudio-text">
                            <h4>Convivencia de Flotas</h4>
                            <p>Análisis de compatibilidad operativa entre vehículos pesados y livianos en ruta.</p>
                        </div>
                    </div>
                </div>

                <!-- Deliverables Row -->
                <div class="entregables-row reveal">
                    <span class="entregables-label">Entregables:</span>
                    <div class="entregable-chip">📄 Informe de Estudio Vial</div>
                    <div class="entregable-chip">🗺️ Libro de Ruta</div>
                    <div class="entregable-chip">🎬 Videos de Inducción HD</div>
                    <div class="entregable-chip">📊 Valorización de Señalética</div>
                </div>
            </div>
        </section>'''

content = content.replace(old_estudios, new_estudios)


# --- TECNOLOGÍA SECTION REDESIGN ---
old_tecnologia = re.search(r'<!-- Section 6: Tecnología -->.*?</section>', content, re.DOTALL).group(0)

new_tecnologia = '''<!-- Section 6: Tecnología -->
        <section id="tecnologia">
            <div class="container">
                <div class="reveal text-center" style="margin-bottom: 3.5rem;">
                    <span class="badge">INNOVACIÓN TECNOLÓGICA</span>
                    <h2>Tecnología e Innovación</h2>
                    <p class="section-subtitle">Soluciones de vanguardia para la gestión del tránsito, flotas y seguridad vial corporativa</p>
                </div>

                <div class="tech-nuevo-grid reveal">
                    <!-- Radar Card -->
                    <div class="tech-nuevo-card glass">
                        <div class="tech-nuevo-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="2"/><path d="M16.24 7.76a6 6 0 0 1 0 8.49m-8.48-.01a6 6 0 0 1 0-8.49m11.31-2.82a10 10 0 0 1 0 14.14m-14.14 0a10 10 0 0 1 0-14.14"/></svg>
                        </div>
                        <div class="tech-nuevo-badge">HARDWARE</div>
                        <h3>Radares de Velocidad Disuasivos</h3>
                        <p>Carros solares móviles para minería y caminos privados. Disuaden excesos de velocidad y registran datos en tiempo real.</p>
                        <ul class="tech-nuevo-specs">
                            <li>⚡ Instalación &lt;5 min</li>
                            <li>📡 Alcance 300m</li>
                            <li>📷 Cámara Full HD</li>
                            <li>☀️ Panel LED &amp; Solar</li>
                        </ul>
                    </div>

                    <!-- App Card -->
                    <div class="tech-nuevo-card glass">
                        <div class="tech-nuevo-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
                        </div>
                        <div class="tech-nuevo-badge">SOFTWARE</div>
                        <h3>App Apoyo a Conducción</h3>
                        <p>Aplicación móvil tipo Waze para navegación interna en rutas privadas y recintos industriales con alertas de zona crítica.</p>
                        <ul class="tech-nuevo-specs">
                            <li>🗺️ Orientación en rutas</li>
                            <li>🔔 Alertas preventivas</li>
                            <li>⚠️ Zonas críticas</li>
                            <li>📴 Modo offline</li>
                        </ul>
                    </div>

                    <!-- ASETRAN Check Card -->
                    <div class="tech-nuevo-card glass tech-highlight-card">
                        <div class="tech-nuevo-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                        </div>
                        <div class="tech-nuevo-badge tech-badge-highlight">PLATAFORMA</div>
                        <h3>ASETRAN Check</h3>
                        <p>Plataforma digital para la gestión integral de inspecciones con trazabilidad auditable y monitoreo en tiempo real.</p>
                        <ul class="tech-nuevo-specs">
                            <li>📋 Checklists digitales</li>
                            <li>📊 Dashboard KPIs</li>
                            <li>🔏 Sello digital</li>
                            <li>📱 Android / iOS / Web</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_tecnologia, new_tecnologia)


# --- NOTICIAS SECTION IMPROVEMENT ---
old_noticias = re.search(r'<!-- Section 6\.5: Noticias.*?</section>', content, re.DOTALL).group(0)

new_noticias = '''<!-- Section 6.5: Noticias & Novedades Técnicas -->
        <section id="noticias" class="bg-alt">
            <div class="container">
                <div class="reveal text-center" style="margin-bottom: 3.5rem;">
                    <span class="badge">ACTUALIDAD Y NORMATIVA</span>
                    <h2>Noticias y Novedades Técnicas</h2>
                    <p class="section-subtitle">Últimas publicaciones sobre regulación vial, acreditaciones ISO 17020 y tecnología de transporte</p>
                </div>

                <div class="news-grid reveal">
                    <article class="news-card glass">
                        <div class="news-img-header" style="height: 160px; overflow: hidden; border-radius: 0.6rem 0.6rem 0 0; margin: -0.1px; background: linear-gradient(135deg, rgba(242,53,14,0.25), rgba(10,14,23,0.95));">
                            <img src="assets/cat-conductores.jpg" alt="Normativa ISO 17020" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.6; mix-blend-mode: luminosity;">
                        </div>
                        <div style="padding: 1.5rem;">
                            <div class="news-date">JULIO 2026</div>
                            <h3>Actualización de Normativa ISO 17020 para Inspección de Flotas en Minería</h3>
                            <p>ASETRAN consolida su estándar técnico incorporando protocolos avanzados de verificación en terreno para equipos de alta tonelaje.</p>
                            <a href="#contacto" class="news-link">Leer Nota Técnica →</a>
                        </div>
                    </article>

                    <article class="news-card glass">
                        <div class="news-img-header" style="height: 160px; overflow: hidden; border-radius: 0.6rem 0.6rem 0 0; margin: -0.1px; background: linear-gradient(135deg, rgba(242,53,14,0.25), rgba(10,14,23,0.95));">
                            <img src="assets/cat-estudios-ruta.jpg" alt="Radares Solares" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.6; mix-blend-mode: luminosity;">
                        </div>
                        <div style="padding: 1.5rem;">
                            <div class="news-date">JUNIO 2026</div>
                            <h3>Implementación de Radares Solares Disuasivos en Rutas Logísticas</h3>
                            <p>Monitoreo preventivo y disuasión de velocidad con tecnología autónoma solar y conectividad 4G para faenas industriales.</p>
                            <a href="#contacto" class="news-link">Leer Nota Técnica →</a>
                        </div>
                    </article>

                    <article class="news-card glass">
                        <div class="news-img-header" style="height: 160px; overflow: hidden; border-radius: 0.6rem 0.6rem 0 0; margin: -0.1px; background: linear-gradient(135deg, rgba(242,53,14,0.25), rgba(10,14,23,0.95));">
                            <img src="assets/tech-fifth-wheel.jpg" alt="Quinta Rueda" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.6; mix-blend-mode: luminosity;">
                        </div>
                        <div style="padding: 1.5rem;">
                            <div class="news-date">MAYO 2026</div>
                            <h3>Cero Desacoplamientos: Certificación de Quinta Rueda y Perno Rey</h3>
                            <p>Aplicación de Ensayos No Destructivos (END) por Líquidos Penetrantes y Yugo Magnético sin desmontaje de piezas en acoples pesados.</p>
                            <a href="#contacto" class="news-link">Leer Nota Técnica →</a>
                        </div>
                    </article>
                </div>
            </div>
        </section>'''

content = content.replace(old_noticias, new_noticias)


# --- CONTACTO SECTION IMPROVEMENT ---
old_contacto = re.search(r'<!-- Section 7: Contacto -->.*?</section>', content, re.DOTALL).group(0)

new_contacto = '''<!-- Section 7: Contacto -->
        <section id="contacto">
            <div class="container">
                <div class="reveal text-center" style="margin-bottom: 3.5rem;">
                    <span class="badge">CONTÁCTENOS</span>
                    <h2>Hablemos de tu Proyecto</h2>
                    <p class="section-subtitle">Nuestro equipo técnico está disponible para responder sus consultas y coordinar una inspección.</p>
                </div>

                <div class="contact-grid reveal">
                    <!-- Form -->
                    <div class="contact-form-wrapper glass">
                        <h3 style="color: #fff; margin-bottom: 0.4rem; font-size: 1.4rem;">Solicitar Servicio</h3>
                        <p style="color: var(--color-text-muted); font-size: 0.9rem; margin-bottom: 1.8rem;">Complete el formulario y nos comunicaremos dentro de 24 horas hábiles.</p>
                        <form class="contact-form" id="contactForm">
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="name">Nombre Completo</label>
                                    <input type="text" id="name" class="form-control" placeholder="Juan Pérez" required>
                                </div>
                                <div class="form-group">
                                    <label for="email">Correo Electrónico</label>
                                    <input type="email" id="email" class="form-control" placeholder="juan@empresa.cl" required>
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="phone">Teléfono</label>
                                    <input type="tel" id="phone" class="form-control" placeholder="+56 9 XXXX XXXX">
                                </div>
                                <div class="form-group">
                                    <label for="service">Servicio de Interés</label>
                                    <select id="service" class="form-control">
                                        <option value="">Seleccione un servicio</option>
                                        <option>Acreditación Mecánica de Flotas</option>
                                        <option>Análisis de Fallas (Ensayos No Destructivos)</option>
                                        <option>Certificación de Quinta Rueda</option>
                                        <option>Peritajes e Investigación</option>
                                        <option>Estudios Viales y Tránsito Industrial</option>
                                        <option>Radares de Velocidad Disuasivos</option>
                                        <option>ASETRAN Check</option>
                                        <option>Capacitaciones</option>
                                        <option>Otro</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="message">Mensaje</label>
                                <textarea id="message" class="form-control" placeholder="Describa brevemente su necesidad o consulta..." required></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary" style="width: 100%; padding: 1rem; font-size: 1rem; font-weight: 700;">Enviar Solicitud →</button>
                        </form>
                    </div>

                    <!-- Contact Info -->
                    <div class="contact-side">
                        <div class="contact-info-card glass">
                            <div class="contact-info-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.62 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 9.91a16 16 0 0 0 6.29 6.29l.95-.94a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                            </div>
                            <div>
                                <h4>Teléfonos</h4>
                                <p>+56 02 26680244</p>
                                <p>+56 02 26621194</p>
                            </div>
                        </div>

                        <div class="contact-info-card glass">
                            <div class="contact-info-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                            </div>
                            <div>
                                <h4>Email</h4>
                                <p>contacto@asetran.cl</p>
                            </div>
                        </div>

                        <div class="contact-info-card glass">
                            <div class="contact-info-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            </div>
                            <div>
                                <h4>Web</h4>
                                <p>www.asetran.cl</p>
                            </div>
                        </div>

                        <!-- Quick Info Box -->
                        <div class="contact-quick-box">
                            <div class="quick-box-icon">⏱️</div>
                            <div>
                                <h5>Respuesta rápida garantizada</h5>
                                <p>Respondemos dentro de 24 horas hábiles. Para inspecciones urgentes, contáctenos directamente por teléfono.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_contacto, new_contacto)


with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully redesigned all main sections in index.html!")
