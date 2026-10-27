#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Gestión y Activación Inmediata: Reestructuración de Sedes Miércoles 28/10
X Congreso SETAC Argentina 2026

Permite:
  1. python activar_sedes_miercoles.py --preview (Verificar estado de los archivos de preview)
  2. python activar_sedes_miercoles.py --activar (Crear backup automático de producción y promover la versión de sedes del miércoles)
  3. python activar_sedes_miercoles.py --revertir (Restaurar producción al esquema original desde el último backup)
"""

import os
import shutil
import sys
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKUP_DIR = os.path.join(BASE_DIR, "backups_produccion")

PROD_FILES = [
    "index.html",
    "cronograma_general.html",
    "programa.html",
    os.path.join("js", "programa_autores_data.js"),
    os.path.join("js", "cronograma_general_data.js")
]

PREVIEW_MAP = {
    "index.html": "preview_sedes_miercoles.html",
    "cronograma_general.html": "cronograma_general_preview_sedes.html",
    "programa.html": "programa_preview_sedes.html",
    os.path.join("js", "programa_autores_data.js"): os.path.join("js", "programa_autores_data_preview_sedes.js"),
    os.path.join("js", "cronograma_general_data.js"): os.path.join("js", "cronograma_general_data_preview_sedes.js")
}

def check_status():
    print("=" * 65)
    print(" ESTADO DE ARCHIVOS - ECOSISTEMA PREVIEW SEDES MIÉRCOLES")
    print("=" * 65)
    all_ok = True
    for prod_name, prev_name in PREVIEW_MAP.items():
        prev_path = os.path.join(BASE_DIR, prev_name)
        exists = os.path.exists(prev_path)
        size = os.path.getsize(prev_path) if exists else 0
        status = f"LISTO ({size:,} bytes)" if exists else "FALTA"
        if not exists: all_ok = False
        print(f"  * {prev_name:<45} : {status}")
    print("-" * 65)
    if all_ok:
        print("  [OK] Todos los archivos de preview estan listos para utilizarse.")
    else:
        print("  [X] Faltan archivos de preview. Ejecutar primero la generacion.")
    print("=" * 65)

def activar_produccion():
    print("=" * 65)
    print(" ACTIVANDO VERSIÓN DE SEDES MIÉRCOLES EN PRODUCCIÓN")
    print("=" * 65)
    
    # 1. Crear backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target_backup = os.path.join(BACKUP_DIR, f"backup_pre_sedes_{timestamp}")
    os.makedirs(target_backup, exist_ok=True)
    os.makedirs(os.path.join(target_backup, "js"), exist_ok=True)

    print(f"1. Creando backup de seguridad en:\n   {target_backup}\n")
    for f in PROD_FILES:
        src = os.path.join(BASE_DIR, f)
        dst = os.path.join(target_backup, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"   [OK] Resguardado: {f}")

    # 2. Promover archivos de preview a producción
    print("\n2. Promoviendo archivos de preview a producción:")
    for prod_name, prev_name in PREVIEW_MAP.items():
        src_prev = os.path.join(BASE_DIR, prev_name)
        dst_prod = os.path.join(BASE_DIR, prod_name)
        
        with open(src_prev, "r", encoding="utf-8") as f:
            content = f.read()

        # Ajustar enlaces internos para que apunten a los nombres canónicos de producción
        content = content.replace("preview_sedes_miercoles.html", "index.html")
        content = content.replace("cronograma_general_preview_sedes.html", "cronograma_general.html")
        content = content.replace("programa_preview_sedes.html", "programa.html")
        content = content.replace("programa_autores_data_preview_sedes.js", "programa_autores_data.js")
        content = content.replace("cronograma_general_data_preview_sedes.js", "cronograma_general_data.js")
        content = content.replace("?v=20261028_preview_sedes", f"?v=20261028_sedes_{timestamp}")

        with open(dst_prod, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   [OK] Activado en producción: {prod_name} (desde {prev_name})")

    print("\n" + "=" * 65)
    print(" ¡ACTIVACIÓN LOCAL COMPLETADA EXITOSAMENTE!")
    print(" Si se decide publicar a GitHub Pages, ejecutar:")
    print("   git add .")
    print('   git commit -m "update: activacion de sedes alternativas miercoles 28"')
    print("   git push origin main")
    print("=" * 65)

def revertir_produccion():
    print("=" * 65)
    print(" REVERTIENDO PRODUCCIÓN AL ESQUEMA ORIGINAL")
    print("=" * 65)

    if not os.path.exists(BACKUP_DIR):
        print("ERROR: No existe la carpeta de backups.")
        return

    backups = sorted([d for d in os.listdir(BACKUP_DIR) if d.startswith("backup_pre_sedes_")])
    if not backups:
        print("ERROR: No se encontraron copias de seguridad para restaurar.")
        return

    latest_backup = os.path.join(BACKUP_DIR, backups[-1])
    print(f"Restaurando desde el último backup:\n  {latest_backup}\n")

    for f in PROD_FILES:
        src = os.path.join(latest_backup, f)
        dst = os.path.join(BASE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  [OK] Restaurado: {f}")

    print("\n" + "=" * 65)
    print(" ¡REVERSIÓN COMPLETADA! Producción restaurada al estado original.")
    print("=" * 65)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--activar":
        activar_produccion()
    elif len(sys.argv) > 1 and sys.argv[1] == "--revertir":
        revertir_produccion()
    else:
        check_status()
        print("\nUso del script:")
        print("  python scripts/activar_sedes_miercoles.py --preview  (Verificar estado)")
        print("  python scripts/activar_sedes_miercoles.py --activar  (Pasar a producción con backup)")
        print("  python scripts/activar_sedes_miercoles.py --revertir (Volver a la versión previa)")
