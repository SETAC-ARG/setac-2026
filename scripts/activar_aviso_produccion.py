#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para promover el aviso compacto de 3 puntos (Acreditaciones, Pósters y Mesas Redondas/Orales)
a producción (index.html), generando un backup preventivo previo.
"""

import os
import shutil
import re
from datetime import datetime

BASE_DIR = r"g:\Mi unidad\Inv\2026\pruebas_Congreso_SETAC\d_LittleLink"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
BACKUP_DIR = os.path.join(BASE_DIR, "backups_produccion")

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

def promover_a_produccion():
    if not os.path.exists(INDEX_PATH):
        print(f"Error: {INDEX_PATH} no existe.")
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"index_backup_{timestamp}.html")
    shutil.copy2(INDEX_PATH, backup_path)
    print(f"  [BACKUP] Creado: {backup_path}")

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'<!-- BANNER DE ALERTA.*?-->\s*<aside id="liveAlert".*?</aside>', re.DOTALL)
    if not pattern.search(content):
        pattern = re.compile(r'<aside id="liveAlert".*?</aside>', re.DOTALL)

    updated = pattern.sub(AVISO_COMPACTO_HTML, content, count=1)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print("  [EXITO] index.html actualizado en producción con el aviso compacto de 3 puntos.")

if __name__ == "__main__":
    promover_a_produccion()
