# Protocolo de Activación y Mantenimiento: Sedes Alternativas Miércoles 28/10
## X Congreso SETAC Argentina 2026 • Ecosistema Digital (`d_LittleLink`)

---

## 1. Resumen Ejecutivo del Escenario Alternativo

Este ecosistema contiene la reestructuración completa de las actividades del día **Miércoles 28 de Octubre de 2026**, trasladando las sesiones desde el Centro de Convenciones Sergio Karakachoff hacia **5 institutos de CONICET La Plata**, manteniendo los días Martes 27, Jueves 29 y Viernes 30 centralizados en Karakachoff sin ninguna alteración.

### Matriz de Mapeo y Geolocalización en Google Maps

| Espacio Original | Sede Alternativa Miércoles | Dirección en La Plata | Enlace Google Maps Directo |
| :--- | :--- | :--- | :---: |
| **Sala 1** | **INIFTA (Sala 1)** | Diag. 113 y 64 | [📍 Mapa INIFTA](https://www.google.com/maps/search/?api=1&query=INIFTA+CONICET+La+Plata) |
| **Sala 2** | **CEQUINOR (Sala 2)** | Blvd. 120 e/ 60 y 64 | [📍 Mapa CEQUINOR](https://www.google.com/maps/search/?api=1&query=CEQUINOR+CONICET+La+Plata) |
| **Sala 3** | **CEPAVE (Sala 3)** | Blvd. 120 e/ 60 y 64 | [📍 Mapa CEPAVE](https://www.google.com/maps/search/?api=1&query=CEPAVE+CONICET+La+Plata) |
| **Sala 4** | **ILPLA (Sala 4)** | Blvd. 120 y 62 | [📍 Mapa ILPLA](https://www.google.com/maps/search/?api=1&query=ILPLA+CONICET+La+Plata) |
| **Posters (Foyer)** | **CIM (Posters)** | Fac. Cs. Exactas UNLP (Blvd. 120 e/ 60 y 64) | [📍 Mapa CIM](https://www.google.com/maps/search/?api=1&query=Centro+de+Investigaciones+del+Medioambiente+CIM+Exactas+UNLP) |

---

## 2. Inventario de Archivos Preparados y Listos para Usar

Todos los archivos se encuentran generados, verificados y autocontenidos en la carpeta `d_LittleLink/`:

| Archivo | Tipo | Función / Contenido |
| :--- | :--- | :--- |
| **`preview_sedes_miercoles.html`** | Web (Hub) | Portal central alternativo con aviso de reestructuración, directorio interactivo de los 5 institutos con links a Maps, y botones con descripciones explícitas de las nuevas sedes. |
| **`cronograma_general_preview_sedes.html`** | Web (Matriz) | Cuadrícula horaria continua de 4 días. Las columnas del miércoles rotulan `INIFTA (Sala 1)`, `CEQUINOR (Sala 2)`, `CEPAVE (Sala 3)`, `ILPLA (Sala 4)`, mapa en cabecera y `Sede CIM • Pósters`. |
| **`programa_preview_sedes.html`** | Web (Buscador) | Buscador de presentaciones con pestañas por día. En la pestaña Miércoles los chips de sala cambian dinámicamente a los institutos y cada tarjeta incluye link a Google Maps. |
| **`js/programa_autores_data_preview_sedes.js`** | Datos (1.8 MB) | Base de 482 trabajos con los 157 registros del miércoles convertidos a las sedes de los institutos y URLs de Maps. |
| **`js/cronograma_general_data_preview_sedes.js`** | Datos (211 KB) | Matriz horaria con los bloques y columnas del miércoles adaptados a las sedes alternativas. |
| **`scripts/activar_sedes_miercoles.py`** | Script Python | Herramienta de automatización para verificar estado, hacer backup y activar o revertir producción en 1 clic. |
| **`scripts/reestructuracion_miercoles/generar_datasets_sedes.py`** | Script Python | Generador reproducible de los datasets alternativos por si se modifica el programa base. |

---

## 3. Procedimientos Operativos para Mañana

Ante la decisión de utilizar este esquema, existen **dos alternativas operativas**:

### Opción A: Difundir como Enlace Directo (Sin tocar los archivos de producción)
Si se desea mantener la versión de producción actual intacta y compartir el enlace de sedes solo a coordinadores o asistentes:
* Enviar o abrir directamente el archivo:
  `preview_sedes_miercoles.html`
* O subirlo a GitHub Pages sin alterar `index.html` ejecutando:
  ```bash
  git add preview_sedes_miercoles.html cronograma_general_preview_sedes.html programa_preview_sedes.html js/*sedes*
  git commit -m "feat: agregar version preview sedes miercoles"
  git push origin main
  ```
  La URL pública será: `https://setac-arg.github.io/setac-2026/preview_sedes_miercoles.html`

---

### Opción B: Activación Oficial Total en Producción (Reemplazo Automático con Backup)
Si el comité organizador decide que toda la web principal del congreso (`index.html`) pase a mostrar la reestructuración del miércoles:

1. Abrir una terminal en `d_LittleLink/`.
2. Ejecutar el script automatizado:
   ```bash
   python scripts/activar_sedes_miercoles.py --activar
   ```
   **El script automáticamente:**
   * Crea una copia de seguridad íntegra de `index.html`, `cronograma_general.html`, `programa.html` y los datasets en `backups_produccion/backup_pre_sedes_TIMESTAMP/`.
   * Promueve la versión de preview a producción.
   * Ajusta los enlaces internos canónicos y añade control de versión anti-caché.
3. Para publicar en vivo en GitHub Pages:
   ```bash
   git add .
   git commit -m "update: activacion oficial de sedes alternativas del miercoles"
   git push origin main
   ```

---

### Opción C: Cómo Revertir Inmediatamente al Esquema Original (Rollback)
Si por cualquier motivo se necesita volver atrás y restaurar la sede central Karakachoff:

1. Ejecutar en terminal:
   ```bash
   python scripts/activar_sedes_miercoles.py --revertir
   ```
2. Publicar la restauración:
   ```bash
   git add .
   git commit -m "rollback: restauracion a sede central Karakachoff"
   git push origin main
   ```

---

## 4. Auditoría y Verificación de Integridad

* **Estado de Git actual**: Limpio, `origin/main` al día. Ningún archivo modificado en producción.
* **Prueba de funcionamiento**:
  Para chequear el estado de los archivos en cualquier momento:
  ```bash
  python scripts/activar_sedes_miercoles.py --preview
  ```
