#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para actualizar el aviso en preview.html, preview_avisos.html y previews/avisos.html
con la versión compacta de 3 puntos (Acreditaciones, Pósters y Mesas Redondas/Orales),
usando tags <p> para garantizar compatibilidad total con querySelector('p').
"""

import os
import re
import shutil

BASE_DIR = r"g:\Mi unidad\Inv\2026\pruebas_Congreso_SETAC\d_LittleLink"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
PREVIEW_PATH = os.path.join(BASE_DIR, "preview.html")
PREVIEW_AVISOS_PATH = os.path.join(BASE_DIR, "preview_avisos.html")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews")
PREVIEWS_AVISOS_PATH = os.path.join(PREVIEWS_DIR, "avisos.html")
PREVIEW_SEDES_PATH = os.path.join(BASE_DIR, "preview_sedes_miercoles.html")

AVISO_COMPACTO_HTML = """    <!-- BANNER DE ALERTA / AVISOS EN VIVO (COMPACTO: 3 PUNTOS CLAVE) -->
    <aside id="liveAlert" class="live-alert-card" role="alert" style="border-left: 5px solid #d97706; background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); padding: 10px 14px; margin-bottom: 14px;">
      <svg class="live-alert-icon" width="20" height="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="margin-top: 1px; min-width: 20px;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line>
        <line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div class="live-alert-content">
        <h4 style="color:#92400e; font-weight:800; font-size:12px; margin: 0 0 5px 0; text-transform: uppercase; letter-spacing:.03em;">Avisos Importantes</h4>
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <p style="margin: 0; font-size: 12px; line-height: 1.35; color: #78350f;">
            <strong>• Acreditaciones:</strong> Habilitadas a partir de las 08:30 hs en el Hall Central (2do Subsuelo).
          </p>
          <p style="margin: 0; font-size: 12px; line-height: 1.35; color: #78350f;">
            <strong>• Pósters:</strong> Deben permanecer colocados toda la jornada del día de su presentación.
          </p>
          <p style="margin: 0; font-size: 12px; line-height: 1.35; color: #78350f;">
            <strong>• Mesas Redondas y Sesiones Orales:</strong> Acercar previamente el archivo de su presentación a los encargados de la sala asignada.
          </p>
        </div>
      </div>
    </aside>"""

def replace_live_alert(content, new_alert):
    pattern = re.compile(r'<!-- BANNER DE ALERTA.*?-->\s*<aside id="liveAlert".*?</aside>', re.DOTALL)
    if pattern.search(content):
        return pattern.sub(new_alert, content, count=1)
    # Fallback to matching just <aside id="liveAlert"...</aside>
    pattern2 = re.compile(r'<aside id="liveAlert".*?</aside>', re.DOTALL)
    if pattern2.search(content):
        return pattern2.sub(new_alert, content, count=1)
    return None

def main():
    print("Iniciando actualización compacta de avisos con tags <p>...")

    # 1. Actualizar preview.html
    if os.path.exists(PREVIEW_PATH):
        with open(PREVIEW_PATH, "r", encoding="utf-8") as f:
            prev_content = f.read()
        updated_prev = replace_live_alert(prev_content, AVISO_COMPACTO_HTML)
        if updated_prev:
            with open(PREVIEW_PATH, "w", encoding="utf-8") as f:
                f.write(updated_prev)
            print("  [OK] preview.html actualizado.")
        else:
            print("  [WARN] No se pudo encontrar el bloque liveAlert en preview.html.")

    # 2. Generar/actualizar preview_avisos.html
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            index_content = f.read()

        preview_indicator = """
  <!-- BARRA SUPERIOR INDICADORA DE MODO PREVIEW -->
  <div style="background: linear-gradient(90deg, #1e3a8a 0%, #0369a1 100%); color: #ffffff; text-align: center; padding: 7px 12px; font-size: 12px; font-weight: 700; position: sticky; top: 0; z-index: 9999; box-shadow: 0 2px 8px rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; gap: 8px;">
    <span>👁️ MODO PREVIEW • Aviso Compacto (Acreditaciones, Pósters y Presentaciones)</span>
    <span style="opacity: 0.6;">|</span>
    <a href="index.html" style="color: #fef08a; text-decoration: underline; font-weight: 600;">Ver versión actual en producción</a>
  </div>
"""
        index_with_indicator = re.sub(r'(<body[^>]*>)', r'\1\n' + preview_indicator, index_content)
        updated_avisos = replace_live_alert(index_with_indicator, AVISO_COMPACTO_HTML)
        
        if updated_avisos:
            with open(PREVIEW_AVISOS_PATH, "w", encoding="utf-8") as f:
                f.write(updated_avisos)
            print("  [OK] preview_avisos.html generado con formato compacto 1:1.")
            
            # También soportar la ruta previews/avisos.html por si el usuario navega a esa subcarpeta
            os.makedirs(PREVIEWS_DIR, exist_ok=True)
            # Para previews/avisos.html, corregimos las rutas relativas (css/ -> ../css/, etc.)
            content_subfolder = updated_avisos.replace('href="css/', 'href="../css/').replace('src="images/', 'src="../images/').replace('src="js/', 'src="../js/').replace('href="images/', 'href="../images/').replace('href="index.html', 'href="../index.html').replace('href="cronograma_general.html', 'href="../cronograma_general.html').replace('href="programa.html', 'href="../programa.html').replace('href="cena.html', 'href="../cena.html').replace('href="docs/', 'href="../docs/')
            with open(PREVIEWS_AVISOS_PATH, "w", encoding="utf-8") as f:
                f.write(content_subfolder)
            print("  [OK] previews/avisos.html generado con rutas relativas ajustadas.")
        else:
            print("  [WARN] No se pudo encontrar el bloque liveAlert en index.html.")

    # 3. Actualizar preview_sedes_miercoles.html
    if os.path.exists(PREVIEW_SEDES_PATH):
        with open(PREVIEW_SEDES_PATH, "r", encoding="utf-8") as f:
            sedes_content = f.read()

        AVISO_SEDES_COMPACTO = """    <!-- BANNER DE ALERTA: REESTRUCTURACIÓN DE SEDES Y AVISOS GENERALES -->
    <aside id="liveAlert" class="live-alert-card" role="alert" style="border-left: 5px solid #d97706; background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); padding: 10px 14px; margin-bottom: 14px;">
      <svg class="live-alert-icon" width="20" height="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="margin-top: 1px; min-width: 20px;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line>
        <line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div class="live-alert-content">
        <h4 style="color:#b45309;font-weight:800; font-size:12px; margin: 0 0 4px 0;">⚠️ Sede Miércoles 28/10 en Institutos CONICET</h4>
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <p style="margin: 0; font-size: 11.5px; line-height: 1.35; color: #78350f;">
            <strong>• Acreditaciones:</strong> Habilitadas a partir de las 08:30 hs en el Hall Central (2do Subsuelo).
          </p>
          <p style="margin: 0; font-size: 11.5px; line-height: 1.35; color: #78350f;">
            <strong>• Pósters (Sede CIM):</strong> Deben permanecer colocados toda la jornada del día de su presentación.
          </p>
          <p style="margin: 0; font-size: 11.5px; line-height: 1.35; color: #78350f;">
            <strong>• Mesas Redondas y Orales (Institutos):</strong> Acercar previamente el archivo a los encargados de sala asignada.
          </p>
        </div>
      </div>
    </aside>"""

        updated_sedes = replace_live_alert(sedes_content, AVISO_SEDES_COMPACTO)
        if updated_sedes:
            with open(PREVIEW_SEDES_PATH, "w", encoding="utf-8") as f:
                f.write(updated_sedes)
            print("  [OK] preview_sedes_miercoles.html actualizado con aviso compacto.")
        else:
            print("  [WARN] No se pudo encontrar el bloque liveAlert en preview_sedes_miercoles.html.")

    print("\nProceso finalizado con éxito.")

if __name__ == "__main__":
    main()
