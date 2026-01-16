# Plan de Integración: Extensión Chrome MV3 ↔ Estación Central

**Fecha**: 15 de enero de 2026  
**Versión**: v0.1  
**Estado**: Preparación de Modificaciones

---

## 📋 Resumen Ejecutivo

Este documento detalla las modificaciones necesarias para integrar la extensión Chrome MV3 (con protocolo Neurobit) con la Estación Central vía MCP Server. La extensión actúa como "cliente remoto" que envía/recibe mensajes, historial y validaciones desde/hacia el Arca central.

---

## 🎯 Objetivos de Integración

1. ✅ **Servidor MCP funcional**: Levantado en `connectors/mcp_server.py` (puerto 8090)
2. ✅ **Adaptador MCP en Estación**: `core/adapters/adapter_mcp.py` lista
3. ⏳ **Conector Bidireccional**: Extensión ↔ MCP (nuevo: `bitacora_eva-extension/connectors/extension_mcp_bridge.py`)
4. ⏳ **Mejoras de UX en la extensión**: feedback visual, historial expandible, autoguardado
5. ⏳ **Documentación de flujos**: cómo la extensión sincroniza con la Estación

---

## 📁 Estructura Reconstruida (desde `extension-eva.md`)

El descompilador ha extraído los siguientes archivos:

```
bitacora_eva-extension/
├── reconstructed/
│   ├── .vscode/
│   │   └── settings.json          ✅ (ya existe en proyecto raíz)
│   ├── automations/
│   │   ├── init_workspace.sh      ✅ Copia disponible
│   │   └── backup_system.py       ✅ Copia disponible
│   └── connectors/
│       └── mcp_server.py          ✅ Copia disponible
```

**Nuevos archivos añadidos:**
- `bitacora_eva-extension/connectors/extension_mcp_bridge.py` — Conector bidireccional (bridgeEntre extensión y MCP)

---

## 🔄 Flujos de Integración

### Flujo 1: Extensión → Estación Central (Push)

```
1. Usuario interactúa con popup de extensión
   ↓
2. Extensión captura: mensaje, origen (HOMO_VIVO), destino (ESTACION_CENTRAL)
   ↓
3. Envelope creado con: MESSAGE_ID, TIMESTAMP, content, SESSION_TAG
   ↓
4. POST http://localhost:8090/write_arca (JSON)
   ↓
5. MCP Server valida y escribe en data/memoria_eva.jsonl (append-only)
   ↓
6. Retorna: {"status": "success", "message": "Registro XYZ guardado"}
   ↓
7. Extensión muestra: "✅ Copiado al Arca. ID: XYZ"
```

**Código de ejemplo:**
```javascript
// src/popup/popup.js
async function pushMessageToArca(message) {
  const envelope = {
    MESSAGE_ID: generateMessageID(),
    content: message,
    SESSION_TAG: sessionStorage.getItem('SESSION_ID'),
    ORIGEN: 'HOMO_VIVO',
    DESTINO: 'ESTACION_CENTRAL'
  };
  
  const response = await fetch('http://127.0.0.1:8090/write_arca', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(envelope)
  });
  
  const result = await response.json();
  updateStatusLine(`Copiado al Arca: ${result.message}`);
}
```

### Flujo 2: Extensión ← Estación Central (Pull)

```
1. Usuario abre extensión (o solicita historial)
   ↓
2. GET http://localhost:8090/read_arca?limit=20
   ↓
3. MCP retorna últimos 20 registros del Arca
   ↓
4. Extensión renderiza historial en popup con:
   - Vista previa corta (5–7 líneas)
   - Botón "Expandir" para mensaje completo
   - Timestamp y origen
   ↓
5. Usuario puede revisar antes de "Inyectar"
```

**Código de ejemplo:**
```javascript
// src/popup/popup.js
async function fetchHistoryFromArca(limit = 20) {
  const response = await fetch(`http://127.0.0.1:8090/read_arca?limit=${limit}`);
  const data = await response.json();
  
  displayHistory(data.records);
}

function displayHistory(records) {
  records.forEach(record => {
    const preview = record.content.substring(0, 150) + '...';
    const item = createHistoryItem(record.message_id, preview, record);
    historyContainer.appendChild(item);
  });
}
```

### Flujo 3: Validación SIMON (antes de guardar)

```
1. Extensión captura mensaje
   ↓
2. POST http://localhost:8090/validate_with_simon
   ↓
3. MCP valida reglas SIMON:
   - Longitud mínima
   - No repetitivo
   - Headers mínimos
   ↓
4. Retorna: {"is_valid": true/false, "reasons": [...]}
   ↓
5. Si válido → pushear al Arca
   Si inválido → mostrar "Mensaje rechazado: motivo"
```

---

## ✨ Mejoras de UX Solicitadas

### A. Feedback Visual (CRÍTICO)

**Problema actual**: El botón COPIAR funciona pero sin retroalimentación visual.

**Solución**:
```javascript
// src/popup/popup.js
async function copyToArca(text) {
  button.disabled = true;
  button.textContent = '⏳ NEUROBIT analizando...';
  
  const result = await pushMessageToArca(text);
  
  if (result.status === 'success') {
    button.textContent = '✅ Copiado al Arca #' + result.message_id;
    button.style.backgroundColor = '#4CAF50';
    setTimeout(() => resetButton(), 3000);
  } else {
    button.textContent = '❌ Error: ' + result.error;
    button.style.backgroundColor = '#f44336';
  }
}
```

### B. Historial Expandible

**Problema**: Historial sin expandir, incómodo para mensajes largos.

**Solución**:
```html
<!-- src/popup/popup.html -->
<div class="history-item" id="msg_123">
  <div class="history-preview" onclick="expandMessage('msg_123')">
    "Mensaje de prueba..."
    <span class="expand-btn">▼</span>
  </div>
  <div class="history-full" style="display: none;">
    "Mensaje de prueba con contenido mucho más largo que se expande..."
  </div>
</div>
```

```css
/* src/popup/styles.css */
.history-full {
  max-height: 300px;
  overflow-y: auto;
  background: #f0f0f0;
  padding: 10px;
  border-left: 3px solid #2196F3;
  margin-top: 5px;
}

.history-full.expanded {
  display: block !important;
}
```

### C. Autoguardado con Contador

**Problema**: Usuario quiere autoguardado cada X mensajes sin intervención manual.

**Solución**:
```javascript
// src/popup/popup.js
let messageCounter = 0;
const AUTO_SAVE_INTERVAL = 5; // guardar cada 5 mensajes

async function addMessage(text) {
  messageCounter++;
  
  // Guardar siempre
  await pushMessageToArca(text);
  
  // Mostrar contador
  updateCounter(messageCounter);
  
  // Auto-guardar si alcanza intervalo
  if (messageCounter % AUTO_SAVE_INTERVAL === 0) {
    createBackup();
    console.log(`📦 Auto-guardado: ${messageCounter} mensajes`);
  }
}
```

### D. Retención de Estado del Formulario

**Problema**: El formulario pierde ORIGEN, DESTINO, SESSION_TAG.

**Solución**:
```javascript
// src/popup/storage.js
const FORM_STATE_KEY = 'neurobit_form_state';

function saveFormState() {
  const state = {
    origen: document.getElementById('origen').value,
    destino: document.getElementById('destino').value,
    sessionTag: document.getElementById('session_tag').value,
    timestamp: new Date().toISOString()
  };
  chrome.storage.local.set({ [FORM_STATE_KEY]: state });
}

function restoreFormState() {
  chrome.storage.local.get([FORM_STATE_KEY], (result) => {
    if (result[FORM_STATE_KEY]) {
      const state = result[FORM_STATE_KEY];
      document.getElementById('origen').value = state.origen || 'HOMO_VIVO';
      document.getElementById('destino').value = state.destino || 'ESTACION_CENTRAL';
      document.getElementById('session_tag').value = state.sessionTag || 'default';
    }
  });
}
```

### E. Vista Previa antes de Inyectar

**Problema**: Usuario quiere confirmación visual antes de enviar al Arca.

**Solución**:
```html
<!-- src/popup/preview-modal.html -->
<div id="previewModal" class="modal">
  <div class="modal-content">
    <h3>Confirmación antes de Inyectar</h3>
    <div class="message-preview">
      <!-- Contenido del mensaje -->
    </div>
    <div class="preview-buttons">
      <button id="confirmBtn" class="btn-primary">✓ Confirmar</button>
      <button id="cancelBtn" class="btn-secondary">✗ Cancelar</button>
    </div>
  </div>
</div>
```

```css
/* src/popup/styles.css */
.modal {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.modal.show {
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

---

## 🛠️ Modificaciones Necesarias (Checklist)

### Fase 1: Backend/Adaptadores (HECHO ✅)
- [x] `connectors/mcp_server.py` — servidor MCP (puerto 8090)
- [x] `core/adapters/adapter_mcp.py` — cliente MCP en Estación
- [x] `bitacora_eva-extension/connectors/extension_mcp_bridge.py` — conector bidireccional

### Fase 2: Extensión Chrome (PENDIENTE)
- [ ] `src/manifest.json` — actualizar para permisos HTTP (localhost:8090)
- [ ] `src/popup/popup.html` — añadir preview modal, historial expandible
- [ ] `src/popup/popup.js` — implementar pushes/pulls, feedback visual
- [ ] `src/popup/styles.css` — estilos para estado, expansión, modal
- [ ] `src/popup/storage.js` — retención de estado del formulario

### Fase 3: Documentación (EN PROGRESO)
- [ ] `docs/extension_integration.md` — actualizar con flujos E2E
- [x] `bitacora_eva-extension/INTEGRATION_PLAN.md` — este archivo

### Fase 4: Testing (PENDIENTE)
- [ ] Tests unitarios para `extension_mcp_bridge.py`
- [ ] Tests E2E: Extensión → MCP → Estación
- [ ] Validación de flujos de backup/restore

---

## 🚀 Próximos Pasos Recomendados

### Inmediato (Hoy)
1. Copiar archivos reconstruidos desde `bitacora_eva-extension/reconstructed/` al proyecto raíz si es necesario
2. Validar que `mcp_server.py` se ejecuta sin errores:
   ```bash
   python3 connectors/mcp_server.py &
   ```
3. Probar conector bidireccional:
   ```bash
   python3 bitacora_eva-extension/connectors/extension_mcp_bridge.py
   ```

### Corto plazo (Esta semana)
1. Implementar mejoras de UX en la extensión (A–E)
2. Actualizar `src/manifest.json` para permisos de red
3. Ejecutar harness de pruebas para validar end-to-end

### Mediano plazo
1. Integrar conector en `neurobit_api.py` (routing para `adapter=extension`)
2. Añadir autenticación mínima al MCP server (token local)
3. Generar reportes de sincronización entre extensión y Estación

---

## 📊 Matriz de Cambios

| Componente | Archivo | Cambios | Estado |
|---|---|---|---|
| Backend | `connectors/mcp_server.py` | Nuevo servidor HTTP | ✅ |
| Backend | `core/adapters/adapter_mcp.py` | Cliente ligero | ✅ |
| Bridge | `connectors/extension_mcp_bridge.py` | Conector bidireccional | ✅ |
| Frontend | `src/manifest.json` | Permisos HTTP | ⏳ |
| Frontend | `src/popup/popup.js` | Lógica de push/pull | ⏳ |
| Frontend | `src/popup/styles.css` | UX mejorada | ⏳ |
| Frontend | `src/popup/popup.html` | Modal preview, historial | ⏳ |
| Docs | `docs/extension_integration.md` | Actualización | ⏳ |

---

## ⚠️ Notas Importantes

1. **Seguridad**: El MCP server actual es HTTP local. En producción, añadir:
   - Autenticación por token
   - Rate limiting
   - Validación de origen (CORS)

2. **Persistencia**: La Arca es append-only. Nunca sobrescribir `data/memoria_eva.jsonl`.

3. **Latencia**: Si el MCP server no está activo, la extensión mostrará error. Implementar retry automático.

4. **Sincronización**: Las sesiones de la extensión deben incluir `SESSION_TAG` único para rastrabilidad.

---

## 📞 Contacto / Soporte

**Responsable**: Módulo de Validación de Estación Central  
**Versión del Protocolo**: Neurobit v2.1  
**Última actualización**: 2026-01-15  

---

**Generado automáticamente desde `extension-eva.md` + `descompilador_extension.py`**
