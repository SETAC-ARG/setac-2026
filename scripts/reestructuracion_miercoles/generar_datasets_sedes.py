import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
JS_DIR = os.path.join(BASE_DIR, "js")

src_prog = os.path.join(JS_DIR, "programa_autores_data.js")
dst_prog = os.path.join(JS_DIR, "programa_autores_data_preview_sedes.js")
src_crono = os.path.join(JS_DIR, "cronograma_general_data.js")
dst_crono = os.path.join(JS_DIR, "cronograma_general_data_preview_sedes.js")

MAPS_URLS = {
    "INIFTA": "https://www.google.com/maps/search/?api=1&query=INIFTA+CONICET+La+Plata",
    "CEQUINOR": "https://www.google.com/maps/search/?api=1&query=CEQUINOR+CONICET+La+Plata",
    "CEPAVE": "https://www.google.com/maps/search/?api=1&query=CEPAVE+CONICET+La+Plata",
    "ILPLA": "https://www.google.com/maps/search/?api=1&query=ILPLA+CONICET+La+Plata",
    "CIM": "https://www.google.com/maps/search/?api=1&query=Centro+de+Investigaciones+del+Medioambiente+CIM+Exactas+UNLP",
    "KARAKACHOFF": "https://maps.google.com/?q=Centro+de+Convenciones+Karakachoff+UNLP+La+Plata"
}

def generar_datasets():
    # 1. Programa
    with open(src_prog, "r", encoding="utf-8") as f:
        prog_content = f.read()

    idx_p = prog_content.find("window.CONGRESO_PROGRAMA = ") + len("window.CONGRESO_PROGRAMA = ")
    prog_data = json.loads(prog_content[idx_p:].strip().rstrip(";"))

    count = 0
    for item in prog_data:
        dia_lower = item.get("dia", "").lower()
        fecha = item.get("fecha", "")
        is_wed = ("mi" in dia_lower) or ("28" in fecha)
        
        if is_wed:
            aud = item.get("auditorio", "")
            mod = item.get("modalidad", "")
            if aud == "Sala 1":
                item["auditorio"] = "INIFTA (Sala 1)"
                item["sede_instituto"] = "INIFTA"
                item["maps_url"] = MAPS_URLS["INIFTA"]
            elif aud == "Sala 2":
                item["auditorio"] = "CEQUINOR (Sala 2)"
                item["sede_instituto"] = "CEQUINOR"
                item["maps_url"] = MAPS_URLS["CEQUINOR"]
            elif aud == "Sala 3":
                item["auditorio"] = "CEPAVE (Sala 3)"
                item["sede_instituto"] = "CEPAVE"
                item["maps_url"] = MAPS_URLS["CEPAVE"]
            elif aud == "Sala 4":
                item["auditorio"] = "ILPLA (Sala 4)"
                item["sede_instituto"] = "ILPLA"
                item["maps_url"] = MAPS_URLS["ILPLA"]
            elif aud == "Foyer" or mod == "POSTER":
                item["auditorio"] = "CIM (Posters)"
                item["sede_instituto"] = "CIM"
                item["maps_url"] = MAPS_URLS["CIM"]
            count += 1
        else:
            item["sede_instituto"] = "Centro de Convenciones Karakachoff"
            item["maps_url"] = MAPS_URLS["KARAKACHOFF"]

    with open(dst_prog, "w", encoding="utf-8") as f:
        f.write("// Base de Datos PREVIEW (Reestructuración Sedes Miércoles 28/10: INIFTA, CEQUINOR, CEPAVE, ILPLA, CIM)\n")
        f.write("window.CONGRESO_PROGRAMA = ")
        json.dump(prog_data, f, ensure_ascii=False, indent=None)
        f.write(";\n")
    print(f"Programa: {count} trabajos del miércoles adaptados a sedes alternativas.")

    # 2. Cronograma
    with open(src_crono, "r", encoding="utf-8") as f:
        crono_content = f.read()

    idx1 = crono_content.find("window.CRONOGRAMA_GENERAL = ") + len("window.CRONOGRAMA_GENERAL = ")
    idx2 = crono_content.find("window.EXACT_MATRIX_ROWS = ")
    cg_data = json.loads(crono_content[idx1:idx2].strip().rstrip(";"))
    matrix_rows = json.loads(crono_content[idx2 + len("window.EXACT_MATRIX_ROWS = "):].strip().rstrip(";"))

    for day in cg_data:
        if day.get("day_id") == "miercoles":
            day["reestructurado"] = True
            for ev in day.get("events", []):
                code = ev.get("session_code", "")
                title = ev.get("clean_title", "")
                raw = ev.get("raw_text", "")
                track = ev.get("track_col")
                if track == 1 and not ev.get("is_plenary"):
                    ev["venue_name"] = "INIFTA (Sala 1)"
                    ev["maps_url"] = MAPS_URLS["INIFTA"]
                elif track == 2 and not ev.get("is_plenary"):
                    ev["venue_name"] = "CEQUINOR (Sala 2)"
                    ev["maps_url"] = MAPS_URLS["CEQUINOR"]
                elif track == 3 and not ev.get("is_plenary"):
                    ev["venue_name"] = "CEPAVE (Sala 3)"
                    ev["maps_url"] = MAPS_URLS["CEPAVE"]
                elif track == 4 and not ev.get("is_plenary"):
                    ev["venue_name"] = "ILPLA (Sala 4)"
                    ev["maps_url"] = MAPS_URLS["ILPLA"]

                if "Póster" in code or "Posters" in code or "Paneles" in title:
                    ev["venue_name"] = "CIM (Posters)"
                    ev["maps_url"] = MAPS_URLS["CIM"]
                    ev["clean_title"] = title + " • Sede CIM"
                    ev["raw_text"] = raw + "\n(Sede CIM - Blvd. 120 e/ 60 y 64)"
                elif "Asamblea" in code or "Asamblea" in title:
                    ev["clean_title"] = "Asamblea Estudiantes (Lugar a confirmar)"
                    ev["raw_text"] = "Asamblea Estudiantes\n(Lugar a confirmar)"
                    ev["duration_label"] = "19:00 a 20:00 hs • Lugar a confirmar"

    for row in matrix_rows:
        for cell in row.get("cells", []):
            if cell.get("day_id") == "miercoles":
                col = cell.get("col")
                val = cell.get("val", "")
                badge = cell.get("badge", "")
                title = cell.get("clean_title", "")
                if col == 6: cell["venue_col"] = "INIFTA (Sala 1)"
                elif col == 7: cell["venue_col"] = "CEQUINOR (Sala 2)"
                elif col == 8: cell["venue_col"] = "CEPAVE (Sala 3)"
                elif col == 9: cell["venue_col"] = "ILPLA (Sala 4)"

                if "Póster" in badge or "Paneles" in title or "Póster" in val:
                    cell["badge"] = "Sede CIM • Pósters"
                    if cell.get("clean_title"): cell["clean_title"] += " (Sede CIM)"
                elif "Asamblea" in badge or "Asamblea" in title or "Asamblea" in val:
                    cell["clean_title"] = "Asamblea Estudiantes (Lugar a confirmar)"
                    cell["badge"] = "Asamblea Estudiantes (Lugar a confirmar)"
                    cell["coords"] = "Lugar a confirmar"

    with open(dst_crono, "w", encoding="utf-8") as f:
        f.write("// Datos consolidados del Cronograma General a Primera Vista (PREVIEW REESTRUCTURACION MIERCOLES 28/10)\n")
        f.write("window.CRONOGRAMA_GENERAL = ")
        json.dump(cg_data, f, ensure_ascii=False, indent=2)
        f.write(";\n\n")
        f.write("window.EXACT_MATRIX_ROWS = ")
        json.dump(matrix_rows, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Cronograma General: Dataset de preview generado.")

if __name__ == "__main__":
    generar_datasets()
