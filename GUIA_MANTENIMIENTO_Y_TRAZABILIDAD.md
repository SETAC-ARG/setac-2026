# 📘 Guía Maestra de Mantenimiento, Trazabilidad y Operación
## X Congreso SETAC Argentina 2026 — Ecosistema Digital y Portal Móvil (`d_LittleLink`)

---

## 1. Arquitectura y Diagnóstico del Ecosistema Web (`d_LittleLink`)

El portal web está alojado en la carpeta `d_LittleLink/` y sincronizado con el repositorio GitHub oficial [SETAC-ARG/setac-2026](https://github.com/SETAC-ARG/setac-2026) bajo la rama `main`, servido a través de **GitHub Pages**.

### 📱 Componentes y Páginas Integradas

| Archivo / Ruta | Función y Propósito | Insumos / Dependencias |
| :--- | :--- | :--- |
| **`index.html`** | Portal central (Hub móvil y de escritorio) escaneado desde el código QR principal. | `css/`, `images/`, `docs/`, `js/app.js` |
| **`cronograma_general.html`** | Matriz horaria apaisada y cuadrícula continua de 4 días y 4 salas con buscador reactivo. | `js/cronograma_general_data.js`, `docs/Programa_a_primera_vista.pdf` |
| **`programa.html`** | Buscador interactivo completo con filtros por día, sala, texto reactivo, autores completos, resúmenes y palabras clave. | `js/programa_autores_data.js` |
| **`cena.html`** | Pantalla móvil exclusiva de la Cena de Camaradería con copia rápida de CBU/Alias bancario, mapa y Google Form. | Enlace Google Maps Bukowski Bar, Formulario de Google |
| **`qr.html`** | Herramienta auxiliar para regenerar y descargar códigos QR de alta resolución (300 DPI y vectores SVG). | Scripts de generación QR |
| **`docs/`** | Repositorio de documentos oficiales descargables por los asistentes. | `Programa_Final_Ordenado.pdf`, `Libro_Resumenes_SETAC_2026_Final.pdf`, etc. |

### 🛡️ Medidas de Actualización Inmediata (Anti-Caché)
Para evitar que los teléfonos móviles guarden versiones viejas al recargar o escanear el QR, todas las páginas cuentan con:
1. **Meta tags anti-caché**: `Cache-Control: no-cache, no-store, must-revalidate`.
2. **Versionado de recursos (`cache-busting`)**: Enlaces a CSS, JS y PDFs llevan parámetros de control (ej. `?v=20261025_v7`). Al cambiar cualquier archivo crítico, incrementar este sufijo fuerza a los navegadores a descargar la versión nueva al instante.

---

## 2. Mapa de Trazabilidad de Datos (De las Planillas a la Web)

Todo el flujo de datos del congreso sigue un pipeline automatizado, auditable y cruzado:

```
[Fuentes Maestras / Excel]               [Scripts de Procesamiento]                  [Salidas Web (d_LittleLink)]
------------------------------------------------------------------------------------------------------------------
a_Libro_Resumenes/                       motor_libro_resumenes.py -------------->   docs/Libro_Resumenes_SETAC_2026_Final.pdf
Base_Libro_Resumenes - copia.xlsx                                                   (8.7 MB, 503 resúmenes)
(Hoja: Todo_Curado_Ord)
         │
         ▼ (Cruce cruzado estricto)
c_Programa/                              procesar_programa.py ------------------>   js/programa_data.js
Programa_Detallado.xlsx                  generar_pestana_autores.py ------------>   js/programa_autores_data.js (Buscador)
                                                                                    docs/Programa_Final_Ordenado.pdf (1.0 MB)
                                                                                  
c_Programa/Programa_Detallado_Final/     Generador de Matriz ------------------->   js/cronograma_general_data.js (Cuadrícula)
Programa_a_primera_vista.xlsx                                                       docs/Programa_a_primera_vista.pdf (172 KB)
```

### Detalle de Fuentes e Insumos:

#### A. Libro de Resúmenes
* **Ubicación**: `g:\Mi unidad\Inv\2026\pruebas_Congreso_SETAC\a_Libro_Resumenes\`
* **Archivo base**: `Base_Libro_Resumenes - copia.xlsx` (Hoja: `Todo_Curado_Ord`).
* **Volumen**: 503 trabajos con códigos canónicos unificados (ej. `EDA-01-003`, `CUR-05`, `GEA-02-001`, `TOA-04-012`).
* **Motor de armado**: `motor_libro_resumenes.py` con módulos de curaduría tipográfica, cursivas de especies taxonómicas y armado de índices por autor y tema.
* **Documento resultante**: `d_LittleLink/docs/Libro_Resumenes_SETAC_2026_Final.pdf`.

#### B. Programa Detallado, PDF Oficial y Buscador Interactivo
* **Ubicación de Fuentes**: `g:\Mi unidad\Inv\2026\pruebas_Congreso_SETAC\c_Programa\`
* **Archivos base**:
  * `Programa_Detallado_Final/Programa_Final_Ordenado.pdf`: Versión oficial de 40 páginas con 10 columnas (`FECHA`, `DÍA`, `TURNO`, `HORA`, `AUDITORIO/SALA`, `ID SESION`, `MODALIDAD`, `ORDEN`, `TITULO`, `AUTORES`). Ordena las actividades en salas primero (por día/turno) y agrupa los pósters de cada día en páginas dedicadas al final de la jornada.
  * `Ultimo enviado Pedro/Programa_Detallado.xlsx` y `Program_Definitivo_Borrado261019.pdf`.
* **Procesadores**:
  * `procesar_programa.py`: Cruza las presentaciones del programa con el Libro de Resúmenes, homologa etiquetas a `Sala 1, 2, 3, 4` y emite la auditoría `informe_auditoria_libro_vs_programa.xlsx`.
  * `generar_pestana_autores.py`: Extrae autores completos, afiliaciones limpias, país del disertante y asegura que exactamente **1 único presentador** quede marcado.
* **Insumos resultantes para la Web**:
  * **PDF descargable oficial**: `d_LittleLink/docs/Programa_Final_Ordenado.pdf` (también sincronizado con `docs/Programa_Detallado.pdf` y `docs/Programa_SETAC_2026.pdf` para preservar enlaces directos).
  * **Dataset del buscador**: `d_LittleLink/js/programa_autores_data.js` (utilizado por el buscador interactivo `programa.html`).

#### C. Cronograma General a Primera Vista (Cuadrícula Horaria)
* **Ubicación**: `c_Programa/Programa_Detallado_Final/Programa_a_primera_vista.xlsx`.
* **Insumo resultante para la Web**: `d_LittleLink/js/cronograma_general_data.js` (utilizado por `cronograma_general.html`) y el PDF apaisado `d_LittleLink/docs/Programa_a_primera_vista.pdf`.

#### D. Doble Verificación Cruzada y Auditoría de Producción
Todo el dataset oficial de producción (`js/programa_autores_data.js`) fue auditado y cruzado de forma estricta contra las tres fuentes:
1. **Homologación de Salas (100%)**: Todas las actividades se distribuyen exclusivamente entre `Sala 1` (55), `Sala 2` (62), `Sala 3` (40), `Sala 4` (36) y `Foyer` (289 pósters). La palabra "Auditorio" fue completamente reemplazada por "Sala".
2. **Horarios Minuto a Minuto**: Se incorporaron las horas exactas de inicio de cada exposición (`11:30`, `11:42`, `11:54`, `12:06`...), validadas con 0 errores en formato `HH:MM`.
3. **Número de ORDEN y Código de Libro**: Cada tarjeta cuenta en su pie horizontal con el código canónico del libro a la izquierda (`📖 Cód. Libro: ...`) y el número de turno correlativo a la derecha (`🏷️ Orden #...`).
4. **Coherencia Temática**: 100% de coincidencia en las 32 sesiones científicas entre el Libro de Resúmenes, el Programa Detallado Ordenado y la Matriz de Programa a Primera Vista.

---

## 3. Manual Práctico de Modificación Rápida ("Cheat Sheet")

Ante cualquier imprevisto durante el evento, consultar esta sección para saber exactamente qué archivo editar:

### Caso 1: Avisos Urgentes en Vivo o Cambios de Red WiFi (30 segundos)
* **Archivo a editar**: `d_LittleLink/index.html`
* **Acción**:
  * **Aviso urgente**: Ir a la línea 87 (`<aside id="liveAlert">`) y modificar el texto dentro de `<p>...</p>`.
  * **Ocultar aviso**: Dejar el `<p></p>` vacío o agregar `style="display:none;"` a la etiqueta `aside`.
  * **Cambiar red o clave WiFi**: Ir a la línea 105 para el nombre de red y línea 108 para la clave en `data-wifi-password="NUEVA_CLAVE"`.
* **Publicar**: Guardar y ejecutar Git Push.

### Caso 2: Modificar una Charla, Autor, Título o Resumen en el Buscador Web
* **Edición inmediata en caliente (Web)**:
  * Abrir `d_LittleLink/js/programa_autores_data.js`.
  * Buscar por ID (ej. `PROG-0125`) o apellido del autor.
  * Modificar directamente el campo deseado (`titulo`, `presentador`, `hora_inicio`, `auditorio` con valor `'Sala 1'`, `'Sala 2'`, `'Sala 3'`, `'Sala 4'` o `'Foyer'`).
* **Edición estructural (Planilla maestra)**:
  * Modificar `c_Programa/Ultimo enviado Pedro/Programa_Detallado.xlsx`.
  * Ejecutar en terminal: `python c_Programa/procesar_programa.py`.
  * Reemplazar el archivo PDF correspondiente en `d_LittleLink/docs/Programa_Final_Ordenado.pdf` (y sincronizar `Programa_Detallado.pdf`).
* **Publicar**: Guardar y ejecutar Git Push.

### Caso 3: Cambiar Horarios o Salas en la Cuadrícula Horaria
* **Archivo a editar en la Web**: `d_LittleLink/js/cronograma_general_data.js`.
  * Buscar el bloque horario (ej. `"start_time": "14:00"`, `"day_id": "miercoles"`).
  * Ajustar el texto o la sala.
* **Archivo PDF asociado**: Reemplazar `d_LittleLink/docs/Programa_a_primera_vista.pdf`.
* **Publicar**: Guardar y ejecutar Git Push.

### Caso 4: Modificar Información de la Cena de Camaradería
* **Archivo a editar**: `d_LittleLink/cena.html`.
  * **Datos de cuenta**: Líneas 508 (CBU) y 512 (Alias).
  * **Formulario de inscripción**: Línea 540 (`href="URL_DEL_GOOGLE_FORM"`).
  * **Ubicación Maps**: Línea 460.
* **Publicar**: Guardar y ejecutar Git Push.

---

## 5. Flujo de Publicación Oficial a GitHub Pages

Cada vez que se guarde un cambio en cualquiera de los archivos de `d_LittleLink`, abrir la terminal en esa carpeta y ejecutar los siguientes 3 comandos:

```bash
# 1. Posicionarse en el directorio del portal
cd "g:\Mi unidad\Inv\2026\pruebas_Congreso_SETAC\d_LittleLink"

# 2. Agregar cambios y crear commit descriptivo
git add .
git commit -m "update: actualizacion de horarios y avisos de sala"

# 3. Subir a GitHub
git push origin main
```

> [!TIP]
> Tras ejecutar `git push origin main`, los cambios estarán disponibles en línea en menos de 60 segundos en la URL pública:  
> **`https://setac-arg.github.io/setac-2026/`**
