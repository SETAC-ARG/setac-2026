// LittleLink SETAC 2026 Hub Application Logic

document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  initWiFiCopy();
  initLiveAlert();
  initCenaLink();
  initRegistroLink();
});

/**
 * Sistema de Pestañas con Detección Automática de Fecha
 */
function initTabs() {
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');

  function activateTab(tabId, updateHash = true) {
    tabButtons.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
    });

    tabPanes.forEach(pane => {
      pane.classList.toggle('active', pane.id === tabId);
    });

    if (updateHash && history.replaceState) {
      history.replaceState(null, null, `#${tabId}`);
    }
  }

  // Event Listeners para clicks
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const targetTab = button.getAttribute('data-tab');
      activateTab(targetTab);
    });
  });

  // Determinar pestaña inicial:
  // 1. Si hay un hash en la URL (#dia1, #dia2, #formularios, etc.)
  const hash = window.location.hash.replace('#', '');
  const validTabs = ['general', 'dia1', 'dia2', 'dia3', 'dia4', 'formularios'];

  if (hash && validTabs.includes(hash)) {
    activateTab(hash, false);
    return;
  }

  // 2. Detección automática según la fecha real del teléfono
  const today = new Date();
  const year = today.getFullYear();
  const month = today.getMonth() + 1; // 10 = Octubre
  const day = today.getDate();

  // Fechas del X Congreso SETAC: 27 al 30 de Octubre de 2026
  if (year === 2026 && month === 10) {
    if (day === 27) {
      activateTab('dia1', false);
      return;
    } else if (day === 28) {
      activateTab('dia2', false);
      return;
    } else if (day === 29) {
      activateTab('dia3', false);
      return;
    } else if (day === 30) {
      activateTab('dia4', false);
      return;
    }
  }

  // 3. Fallback por defecto: Pestaña General
  activateTab('general', false);
}

/**
 * Función para copiar la clave WiFi al portapapeles
 */
function initWiFiCopy() {
  const copyBtn = document.getElementById('copyWifiBtn');
  if (!copyBtn) return;

  const wifiPassword = copyBtn.getAttribute('data-wifi-password') || 'SETAC2026';

  copyBtn.addEventListener('click', async () => {
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(wifiPassword);
      } else {
        // Fallback para navegadores antiguos
        const tempInput = document.createElement('input');
        tempInput.value = wifiPassword;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
      }

      // Feedback visual
      const originalHtml = copyBtn.innerHTML;
      copyBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        ¡Copiada!
      `;
      copyBtn.style.backgroundColor = '#16a34a';
      copyBtn.style.color = '#ffffff';
      copyBtn.style.borderColor = '#16a34a';

      setTimeout(() => {
        copyBtn.innerHTML = originalHtml;
        copyBtn.style.backgroundColor = '';
        copyBtn.style.color = '';
        copyBtn.style.borderColor = '';
      }, 2500);
    } catch (err) {
      console.error('Error al copiar:', err);
    }
  });
}

/**
 * Manejo de alerta en vivo (opción de descartar en sesión)
 */
function initLiveAlert() {
  const alertCard = document.getElementById('liveAlert');
  if (!alertCard) return;

  // Si está vacío o configurado como oculto, no mostrar
  const text = alertCard.querySelector('p, li, .live-alert-content') || alertCard;
  if (!text || text.textContent.trim() === '') {
    alertCard.style.display = 'none';
  }
}

/**
 * Enrutamiento inteligente del botón Cena de Camaradería:
 * - Computadora / Pantalla ancha (> 768px): abre la página web oficial completa en pestaña nueva.
 * - Celular / Dispositivo móvil (<= 768px): abre la pantalla optimizada para celular (cena.html).
 */
function initCenaLink() {
  const btnCena = document.getElementById('actividadSocialCena');
  if (!btnCena) return;

  btnCena.href = 'cena.html?v=20261028_v5';
  btnCena.removeAttribute('target');
  btnCena.removeAttribute('rel');
}

/**
 * Enrutamiento inteligente del botón Registro e Inscripción:
 * - Computadora / Pantalla ancha (> 768px): abre la página web oficial completa en pestaña nueva.
 * - Celular / Dispositivo móvil (<= 768px): abre la pantalla optimizada para celular (registro.html).
 */
function initRegistroLink() {
  const btnReg = document.getElementById('btnRegistroInscripcion');
  if (!btnReg) return;

  function updateRegistroLink() {
    const isDesktop = window.innerWidth > 768;
    if (isDesktop) {
      btnReg.href = 'https://setacargentina.setac.org/inscripciones';
      btnReg.target = '_blank';
      btnReg.rel = 'noopener';
    } else {
      btnReg.href = 'registro.html?v=20261027_v1';
      btnReg.removeAttribute('target');
      btnReg.removeAttribute('rel');
    }
  }

  updateRegistroLink();
  window.addEventListener('resize', updateRegistroLink);
}
