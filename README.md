# Hub de Enlaces para el X Congreso SETAC Argentina 2026 (LittleLink)

Portal móvil liviano y de carga ultrarrápida construido sobre la arquitectura abierta de **LittleLink**. Diseñado para concentrar toda la información del evento bajo **un único código QR estático** impreso en banners, credenciales y programas.

---

## 🎨 Características Implementadas

- **Identidad Visual Oficial**: Paleta cromática extraída directamente del afiche del congreso (`poster setac.pdf`):
  - Azul Institucional Profundo: `#0f4c81`
  - Celeste de Acento: `#0284c7`
  - Fondos suaves y degradados limpios con soporte automático de modo oscuro.
- **Pestañas por Día con Detección Automática**:
  - Pestañas interactivas: `General`, `Día 1 (27 Oct)`, `Día 2 (28 Oct)`, `Día 3 (29 Oct)`, `Día 4 (30 Oct)` y `Formularios`.
  - Si el asistente abre el enlace entre el 27 y el 30 de octubre de 2026, el portal abre automáticamente el cronograma y botones del día correspondiente.
- **Tarjeta WiFi con Copia Rápida**: Muestra el nombre de red y permite copiar la clave al portapapeles con un solo toque.
- **Avisos en Vivo / Último Momento**: Banner destacado en la parte superior para comunicar cambios de aula o anuncios urgentes.
- **Generador de QR para Banners (`qr.html`)**: Herramienta integrada para generar y descargar el código QR en alta resolución listo para enviar a imprenta.

---

## 🚀 Cómo Probar Localmente

1. Puedes abrir directamente el archivo `index.html` en tu navegador favorito haciendo doble clic o desde **Positron**:
   - En Positron: Click derecho sobre `index.html` > *Preview* o *Open with Live Preview*.
2. Para probar el generador de QR, abre `qr.html` en tu navegador.

---

## 🌐 Publicación en GitHub Pages (Paso a Paso)

Dado que este portal será escaneado por el público general desde los banners, **debe ser un repositorio público** para que GitHub Pages sea 100% gratuito.

### Paso 1: Crear el repositorio en GitHub
1. Entra a [github.com/new](https://github.com/new).
2. Nombre del repositorio: por ejemplo `setac-2026` o `littlelink-setac`.
3. Selecciona la opción **Public** (Público).
4. No inicialices con README (ya tenemos todo listo aquí). Haz clic en **Create repository**.

### Paso 2: Subir los archivos desde Positron
Abre la terminal integrada de Positron dentro de la carpeta `d_LittleLink`:

```bash
# 1. Inicializar git
git init -b main

# 2. Agregar todos los archivos
git add .

# 3. Crear el primer commit
git commit -m "feat: Hub inicial LittleLink X Congreso SETAC 2026"

# 4. Vincular a tu repositorio de GitHub (reemplaza con tu usuario y repo)
git remote add origin https://github.com/TU-USUARIO/setac-2026.git

# 5. Subir los cambios
git push -u origin main
```

### Paso 3: Activar GitHub Pages
1. En la página de tu repositorio en GitHub, ve a **Settings** (pestaña superior).
2. En el menú lateral izquierdo, haz clic en **Pages**.
3. En **Build and deployment > Branch**:
   - Selecciona la rama `main`.
   - Selecciona la carpeta `/ (root)`.
   - Haz clic en **Save**.
4. En 1 o 2 minutos, GitHub te dará la URL pública oficial, con la forma:  
   `https://TU-USUARIO.github.io/setac-2026/`

---

## 🖨️ Generar el QR para el Banner Impreso

1. Abre `qr.html` en tu navegador.
2. Pega la URL de GitHub Pages que obtuviste en el paso anterior.
3. Haz clic en **Descargar PNG (Alta Resolución)**.
4. Envía esa imagen al diseñador o imprenta para incluirla en el banner roll-up del congreso.
   - *Tip*: Se recomienda imprimirlo de al menos 12x12 cm con margen blanco alrededor.

---

## ✏️ Cómo Personalizar Enlaces y Avisos

Todos los enlaces se editan en el archivo `index.html`:

- **Reemplazar enlaces de Google Forms**:
  Busca `#preguntas-disertantes-form`, `#votacion-premios-form` o `#encuesta-certificados-form` y reemplázalos por la URL real de tu Google Form.
- **Reemplazar enlace al Libro de Resúmenes o Programa**:
  Busca `#programa-pdf` y `#libro-resumenes-drive` y pon los enlaces compartidos de Google Drive o el PDF subido al repo.
- **Cambiar la clave de WiFi**:
  En `index.html`, busca `data-wifi-password="SETAC2026"` y edita tanto el atributo como el texto de la red.
- **Actualizar o quitar el aviso en vivo**:
  Edita el texto dentro de `<aside id="liveAlert">`. Si dejas el `<p>` vacío o borras el bloque, el banner no se mostrará.
