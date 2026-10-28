# Registro y Control de Botones, Enlaces y Estados (Congreso SETAC 2026)

Este documento es la **fuente única de verdad** para consultar rápidamente qué botones y secciones están actualmente visibles en producción (`index.html`), cuáles están en modo borrador (`preview.html`) y cuáles están ocultos o esperando datos (links de Forms, montos, etc.).

---

## 📊 1. Resumen Rápido de Estados

| Estado | Significado | Cantidad |
| :--- | :--- | :---: |
| 🟢 **VISIBLE (PROD)** | Activo y visible para todos los asistentes en `index.html`. | 11 |
| 🟡 **MODO PREVIEW** | En prueba en `preview.html`, no visible aún en producción. | 1 |
| 🔴 **OCULTO / PENDIENTE** | Maquetado en el código (`style="display: none;"`), esperando confirmación o enlace para publicarse. | 1 |

---

## 📋 2. Tabla Maestra de Enlaces y Botones

### A. Cabecera y Accesos Directos
| Bloque / Elemento | ID en Código | Estado | Destino / Enlace | Notas / Acción pendiente |
| :--- | :--- | :---: | :--- | :--- |
| **Sede Karakachoff** | `meta-venue-link` | 🟢 Visible | Google Maps (Karakachoff UNLP) | Operativo. |
| **Alerta en Vivo** | liveAlert | 🟢 Visible | Banner de texto superior | Publicado: Acreditaciones, Pósters (toda la jornada) y Mesas Redondas/Orales. |
| **Tarjeta WiFi** | `copyWifiBtn` | 🟢 Visible | Red `Centro-Convenciones` / Clave `ConvencionesUNLP` | Botón interactivo de 1 clic para copiar clave. |

---

### B. Navegación Principal
| Bloque / Elemento | ID / Archivo | Estado | Destino / Enlace | Notas / Acción pendiente |
| :--- | :--- | :---: | :--- | :--- |
| **Cronograma y Primera Vista** | `cronograma_general.html` | 🟢 Visible | `cronograma_general.html` | Vista rápida de tablas y cronograma general. |
| **Buscador y Programa Interactivo** | `programa.html` | 🟢 Visible | `programa.html` | Filtros por día, autor, sala, horarios específicos. |

---

### C. Información del Congreso
| Bloque / Elemento | ID / Archivo | Estado | Destino / Enlace | Notas / Acción pendiente |
| :--- | :--- | :---: | :--- | :--- |
| **Sitio Web Oficial** | — | 🟢 Visible | `https://setacargentina.setac.org/congreso2026` | Web institucional SETAC. |
| **Programa Completo (PDF)** | — | 🟢 Visible | `docs/Programa_Final_Ordenado.pdf` | Descarga de PDF oficial ordenado. |
| **Libro de Resúmenes (PDF)** | — | 🟢 Visible | `docs/Libro_Resumenes_SETAC_2026_Final.pdf` | Descarga de compendio de resúmenes. |
| **📝 Registro e Inscripción** | `btnRegistroInscripcion` | 🟢 Visible | Móvil: `registro.html`<br>Desktop: Web oficial (`/inscripciones`) | Operativo: Aranceles, CBU/Alias Fundación Exactas y Formulario Google. |
| **Mail Oficial de Secretaría** | `secretariaEmailCard` | 🟢 Visible | `mailto:setaclaplata2026@gmail.com` | Correo de contacto y coordinación. |

---

### D. Actividades Sociales
| Bloque / Elemento | ID en Código | Estado | Destino Actual | Notas y Estado de Preparación |
| :--- | :--- | :---: | :--- | :--- |
| **🍸 Cóctel (Martes 27)** | `actividadSocial1` | 🟢 Visible | [Google Maps (Espacio Dickinson)](https://maps.app.goo.gl/wrUP3BJ9NAPMGW5MA) | **Horario**: 20:00 hs.<br>**Lugar**: Espacio Dickinson (Mismo edificio Sergio Karakachoff, UNLP). |
| **🍻 Pincha Debate (Miércoles 28)** | `actividadSocial2` | 🟡 **PREVIEW** | **Prod**: Web oficial<br>**Preview**: `actividad_social_2_preview.html` | **Horario**: 20:30 hs.<br>**Lugar**: León Bar Bistró (Estadio UNO).<br>**Propuesta**: 1 cerveza con papas ($ 10.000 ARS / 10 USD).<br>✅ Formulario de Google, CBU/Alias y pago internacional vía PayPal (10 USD) con QR operativos en preview. |
| **🍽️ Cena de Camaradería (Jueves 29)** | `actividadSocialCena` | 🟢 Visible | Móvil: `cena.html`<br>Desktop: Web oficial SETAC | **Horario**: 20:30 hs.<br>**Lugar**: Bukowski Bar.<br>Totalmente operativo con transferencia bancaria (AR), pago internacional vía PayPal (10 USD), código QR y formulario. |

---

### E. Actividades SETAC Argentina
| Bloque / Elemento | ID en Código | Estado | Destino Actual | Notas |
| :--- | :--- | :---: | :--- | :--- |
| **🎓 Asamblea de Estudiantes** | `asambleaEstudiantes` | 🟢 Visible | Grupo WhatsApp / Convocatoria | Miércoles 28 Oct • 19:00 hs. |
| **🏛️ Asamblea General SETAC ARG** | `asambleaSetac` | 🟢 Visible | Web oficial institucional | Jueves 29 Oct • 19:00 hs. |

---

### F. Tu Opinión Nos Interesa *(Nuevo Bloque)*
| Bloque / Elemento | ID en Código | Estado | Destino Actual | Notas y Próxima Acción |
| :--- | :--- | :---: | :--- | :--- |
| **📋 Encuesta DE&I (Diversidad, Equidad e Inclusión)** | `encuestaDEI` | 🟢 **VISIBLE** | [Google Forms](https://forms.gle/uWp6z9FiVvN1q83h9) | Formulario activo para el conversatorio del Jueves 29. |
| **💬 ¿Nos ayudás con SETAC Argentina?** | `encuestaAyudaSetac` | 🔴 **OCULTO** | `#` *(Placeholder)* | ⏳ **Pendiente**: Recibir enlace del Google Form.<br>Una vez recibido, cambiar `style="display: none;"` por visible. |

---

### G. Comunidad y Redes Sociales
| Bloque / Elemento | ID en Código | Estado | Destino Actual | Notas |
| :--- | :--- | :---: | :--- | :--- |
| **💬 WhatsApp Estudiantes** | — | 🟢 Visible | Grupo de WhatsApp oficial | Comunidad estudiantil. |
| **📸 Instagram Oficial** | — | 🟢 Visible | `https://instagram.com/setacarg` | Novedades y fotos del evento. |
| **📂 Fotos del Congreso** | — | 🟢 Visible | Google Drive colaborativo | Carpeta abierta para compartir fotos. |

---

## 🛠️ 3. Procedimiento para Activar Botones Ocultos o en Preview

### Caso 1: Publicar el botón "¿Nos ayudás con SETAC Argentina?"
1. Abrir `index.html` (y `preview.html`).
2. Buscar `id="encuestaAyudaSetac"`.
3. Reemplazar `href="#"` por la URL de Google Forms.
4. Quitar `style="display: none;"`.

### Caso 2: Promover "Pincha Debate (León Bar Bistró)" de Preview a Producción
1. Los datos ya están listos en `actividad_social_2_preview.html` ($ 10.000, 1 cerveza con papas, Formulario y CBU/Alias).
2. Si se decide pasar a producción: copiar a `actividad_social_2.html` o activar en `index.html` (y en `js/app.js`).




### Caso 3: Aviso Oficial para Expositores (Pósters y Sesiones Orales)
1. **Archivos de Preview Generados**:
   - `preview_avisos.html`: Versión 1:1 idéntica a producción con barra indicadora superior.
   - `preview.html`: Laboratorio de variantes estéticas con el aviso incorporado.
   - `preview_sedes_miercoles.html`: Versión alternativa de sedes del miércoles con el aviso integrado.
2. **Promoción a Producción**:
   - Ejecutar: `python scripts/activar_aviso_produccion.py` (crea backup automático y actualiza `index.html`).
