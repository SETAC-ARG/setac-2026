# Hub de Enlaces para el X Congreso SETAC Argentina 2026

Portal web móvil y de carga ultrarrápida diseñado para concentrar toda la información oficial, académica y social del **X Congreso de la Sociedad de Toxicología y Química Ambiental (SETAC Argentina)** bajo **un único código QR estático** impreso en banners roll-up, credenciales y programas.

* 🌐 **URL Oficial en Producción**: [https://setac-arg.github.io/setac-2026/](https://setac-arg.github.io/setac-2026/)
* 🗓️ **Fecha del Evento**: 27 al 30 de Octubre de 2026
* 🏛️ **Sede Oficial**: Centro de Convenciones Sergio Karakachoff (UNLP), La Plata, Argentina
* 📍 **Geolocalización**: [Ver en Google Maps](https://maps.google.com/?q=Centro+de+Convenciones+Karakachoff+UNLP+La+Plata)

---

## 🚀 Módulos y Servicios del Ecosistema

El portal no es solo una página de enlaces, sino una suite integrada de servicios web optimizados para teléfonos móviles y pantallas de escritorio:

| Módulo / Archivo | Descripción y Funcionalidad |
| :--- | :--- |
| **`index.html`** | **Hub Principal**: Cabecera institucional con arte oficial del afiche, banner dinámico para avisos de último momento, tarjeta WiFi con copiado de clave en un toque, enlaces a documentos oficiales, actividades sociales y grilla de avales y patrocinadores. |
| **`cronograma_general.html`** | **Programa a Primera Vista**: Matriz horaria apaisada y continua que despliega los 4 días del evento y las 4 salas simultáneas en una única cuadrícula con buscador reactivo y enlace de descarga al PDF diseñado. |
| **`programa.html`** | **Buscador y Programa Interactivo**: Motor de búsqueda reactivo sobre los 503 trabajos aprobados. Permite filtrar por día, sala o texto libre (título, autores, palabras clave) y desplegar el resumen completo, afiliaciones institucionales y país del expositor. |
| **`cena.html`** | **Cena de Camaradería**: Pantalla móvil dedicada para el evento social en Bukowski Bar con copiado rápido de CBU/Alias bancario al portapapeles, mapa interactivo y enlace directo al formulario de inscripción. |
| **`qr.html`** | **Centro de Descarga de Códigos QR**: Permite visualizar y descargar los códigos QR en alta resolución (PNG 300 DPI y vectores SVG limpios o con recuadro) listos para imprenta. |
| **`docs/`** | **Biblioteca de Documentos Oficiales**: Alberga los archivos PDF finales del congreso: *Programa Detallado*, *Libro de Resúmenes*, *Programa a Primera Vista* y variantes de imprenta. |

---

## 🎨 Identidad Visual y Experiencia Móvil

* **Paleta Oficial**: Derivada directamente del afiche del congreso:
  * Azul Institucional Primario: `#0f4c81`
  * Celeste de Acento y Enlaces: `#0284c7`
  * Paleta temática para los 5 ejes científicos: Toxicología (TOA), Tecnología (TEA), Gestión (GEA), Química (QUA) y Educación Ambiental (EDA).
* **Control Estricto de Caché**:
  * Implementa directivas meta `Cache-Control: no-cache, no-store, must-revalidate` y sufijos de versión en estilos y scripts (`?v=...`).
  * Garantiza que cualquier asistente que escanee el QR desde su celular reciba de inmediato los cambios y avisos urgentes sin retención de caché.
* **Avales y Patrocinios**: Grilla responsiva categorizada en 3 niveles oficiales (Avales Institucionales, Patrocinantes y Auspiciantes) con formato sobrio integrado al fondo.

---

## 🔄 Trazabilidad de los Datos Base

Todos los datos visibles en el portal provienen de un pipeline auditable y validado:
1. **Libro de Resúmenes (`a_Libro_Resumenes/`)**:
   * Base consolidada de 503 trabajos en `Base_Libro_Resumenes - copia.xlsx` con identificadores canónicos oficiales (ej. `EDA-01-003`, `CUR-05`, `GEA-02-001`).
   * Salida PDF: `docs/Libro_Resumenes_SETAC_2026_Final.pdf`.
2. **Programa Detallado y Autores (`c_Programa/`)**:
   * Archivo maestro `Programa_Detallado.xlsx` procesado mediante scripts de cruce (`procesar_programa.py` y `generar_pestana_autores.py`).
   * Alimenta el dataset interactivo `js/programa_autores_data.js`.
3. **Cronograma a Primera Vista**:
   * Matriz horaria en `Programa_a_primera_vista.xlsx` exportada tanto a `js/cronograma_general_data.js` como a `docs/Programa_a_primera_vista.pdf`.

---

## ✏️ Manual de Modificaciones Rápidas Durante el Evento

Ante cualquier cambio imprevisto durante el transcurso del congreso:

* **Modificar un Aviso Urgente**:
  En `index.html`, editar el texto dentro del bloque `<aside id="liveAlert">`. Si no se desea mostrar ningún aviso, dejar el `<p>` vacío.
* **Actualizar la Clave WiFi**:
  En `index.html`, editar la clave en el atributo `data-wifi-password="CLAVE"` y en el texto visible del botón.
* **Corregir una Charla o Autor en el Buscador**:
  Editar directamente el registro correspondiente en `js/programa_autores_data.js` buscando por ID de presentación o autor.
* **Ajustar una Sala o Franja Horaria en la Cuadrícula**:
  Editar el bloque horario en `js/cronograma_general_data.js`.

---

## 📤 Despliegue de Cambios a GitHub Pages

Para publicar cualquier modificación en vivo, abrir la terminal en esta carpeta (`d_LittleLink`) y ejecutar:

```bash
# 1. Registrar todos los cambios modificados
git add .

# 2. Crear el commit descriptivo
git commit -m "update: aviso de cambio de aula y actualización de programa"

# 3. Subir a GitHub
git push origin main
```

En aproximadamente 30 a 60 segundos, GitHub Pages actualizará la versión pública automáticamente.
