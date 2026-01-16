# FASE 3.1: Gestión de Agentes - Documentación

**Versión**: NEUROBIT v2.1  
**Fecha**: 16 de enero de 2026  
**Estado**: ✅ IMPLEMENTADO Y FUNCIONAL  

---

## 📋 Resumen Ejecutivo

FASE 3.1 implementa el **sistema de registro y gestión de agentes multi-plataforma** para la Estación Central. Los agentes remotos (ChatGPT, Qwen, Gemini, Local Llama, Claude) se registran en un ecosistema centralizado desde el cual se pueden:

1. ✅ Registrar agentes en múltiples plataformas
2. ✅ Verificar conectividad con APIs externas
3. ✅ Crear salas de sesión multi-agente
4. ✅ Orquestar rondas de trabajo colaborativo
5. ✅ Persistencia append-only en JSONL

---

## 🏗️ Arquitectura

```
┌────────────────────────────────────────────────────────┐
│         ESTACIÓN CENTRAL (Frontend HTML/JS)            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  agents_management.js                            │  │
│  │  - Panel de Registro de Agentes                  │  │
│  │  - Filtrado por estado (active, failed, etc.)   │  │
│  │  - UI para crear Salas de Sesión               │  │
│  │  - Definición de Rondas                         │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
         ↓ HTTP REST API
┌────────────────────────────────────────────────────────┐
│         API Backend (neurobit_api.py)                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  /register_agent          [POST]                 │  │
│  │  /list_agents             [GET]                  │  │
│  │  /get_agent/<id>          [GET]                  │  │
│  │  /create_session          [POST]                 │  │
│  │  /add_round/<session_id>  [POST]                │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
         ↓ Python Core
┌────────────────────────────────────────────────────────┐
│    core/agents_registry.py (LÓGICA CENTRAL)            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  AgentRegistry                                   │  │
│  │  - Registro persistente en JSONL                │  │
│  │  - Validación de credenciales                   │  │
│  │  - Hash seguro de API keys                      │  │
│  │                                                  │  │
│  │  RoundOrchestrator                              │  │
│  │  - Crear sesiones multi-agente                  │  │
│  │  - Definir y ejecutar rondas                    │  │
│  │  - Monitoreo de estado                          │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
         ↓ Persistencia
┌────────────────────────────────────────────────────────┐
│         data/agents_registry.jsonl (Append-Only)       │
│  [{"id": "agent_XXXX", "platform": "...", ...}]       │
│  [{"id": "agent_YYYY", "platform": "...", ...}]       │
│  ...                                                   │
└────────────────────────────────────────────────────────┘
```

---

## 🎯 Funcionalidades Implementadas

### 1. **Registro de Agentes** (`POST /register_agent`)

```bash
curl -X POST http://127.0.0.1:5000/register_agent \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "chatgpt",
    "name": "GPT-4 Pro",
    "api_key": "sk-...",
    "metadata": {"model": "gpt-4", "max_tokens": 8192}
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "✅ Agente GPT-4 Pro registrado y ACTIVO",
  "agent": {
    "id": "agent_a1b2c3d4",
    "platform": "chatgpt",
    "name": "GPT-4 Pro",
    "status": "active",
    "registered_at": "2026-01-16T11:30:45.123456Z"
  }
}
```

**Plataformas Soportadas:**
- `chatgpt` (OpenAI) - requiere API key
- `qwen` (Alibaba) - requiere API key
- `gemini` (Google) - requiere API key
- `claude` (Anthropic) - requiere API key
- `local_llama` - NO requiere API key (conexión local)

### 2. **Listar Agentes** (`GET /list_agents`)

```bash
curl http://127.0.0.1:5000/list_agents
# Filtrar por estado:
curl http://127.0.0.1:5000/list_agents?status=active
curl http://127.0.0.1:5000/list_agents?status=failed
```

**Response:**
```json
{
  "success": true,
  "count": 3,
  "agents": [
    {
      "id": "agent_a1b2c3d4",
      "platform": "chatgpt",
      "name": "GPT-4 Pro",
      "status": "active",
      "registered_at": "2026-01-16T11:30:45Z",
      "last_heartbeat": "2026-01-16T11:35:12Z",
      "stats": {"messages_sent": 5, "messages_received": 5}
    }
  ]
}
```

### 3. **Crear Sala de Sesión** (`POST /create_session`)

```bash
curl -X POST http://127.0.0.1:5000/create_session \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sesión de Investigación Q1 2026",
    "agent_ids": ["agent_a1b2c3d4", "agent_x9y8z7w6", "agent_m5n4o3p2"]
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "✅ Sala 'Sesión de Investigación Q1 2026' creada con 3 agentes",
  "session": {
    "session_id": "session_s1e2s3i4",
    "name": "Sesión de Investigación Q1 2026",
    "agent_ids": ["agent_a1b2c3d4", "agent_x9y8z7w6", "agent_m5n4o3p2"],
    "created_at": "2026-01-16T11:40:00Z"
  }
}
```

### 4. **Añadir Ronda a Sesión** (`POST /add_round/<session_id>`)

```bash
curl -X POST http://127.0.0.1:5000/add_round/session_s1e2s3i4 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Brainstorm",
    "prompt": "Generar 10 ideas innovadoras sobre X"
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "✅ Ronda #1 'Brainstorm' añadida",
  "round": {
    "round_id": "round_session_s1e2s3i4_001",
    "number": 1,
    "title": "Brainstorm",
    "status": "pending"
  }
}
```

---

## 💻 Interfaz de Usuario (agents_management.js)

### Panel de Registro

**Pasos:**
1. Seleccionar plataforma (ChatGPT, Qwen, Gemini, Local Llama, Claude)
2. Ingresar nombre del agente (ej: "GPT-4 Pro")
3. Si es remoto, pegar API key (se hashea automáticamente)
4. (Opcional) Agregar metadatos en JSON
5. Click en "🚀 Registrar Agente"

### Lista de Agentes

- Muestra tarjetas con estado visual (🟢 activo, ⏳ verificación, 🔴 fallido)
- Filtros: Todos, Activos, Verificación, Fallidos
- Stats: mensajes enviados/recibidos, timestamp de registro

### Sala de Sesión

- Seleccionar múltiples agentes con checkboxes
- Crear sala con nombre descriptivo
- Definir rondas secuenciales (Brainstorm → Conclusiones → Observaciones)
- Cada ronda puede tener un prompt diferente

---

## 📊 Estructura de Datos (JSONL)

### agents_registry.jsonl

```jsonl
{"id": "agent_a1b2c3d4", "platform": "chatgpt", "name": "GPT-4 Pro", "api_key_hash": "e3b0c4423f...", "status": "active", "registered_at": "2026-01-16T11:30:45Z", "last_heartbeat": "2026-01-16T11:35:12Z", "round_id": null, "session_id": null, "stats": {"messages_sent": 5, "messages_received": 5}, "metadata": {"model": "gpt-4"}}
{"id": "agent_x9y8z7w6", "platform": "qwen", "name": "Qwen Assistant", "api_key_hash": "a1f2b3c4d5...", "status": "active", "registered_at": "2026-01-16T11:32:10Z", "last_heartbeat": "2026-01-16T11:35:01Z", "round_id": "round_s1e2s3i4_001", "session_id": "session_s1e2s3i4", "stats": {"messages_sent": 3, "messages_received": 3}, "metadata": {"model": "qwen-max"}}
```

**Campos Clave:**
- `id`: Identificador único del agente
- `platform`: Plataforma (chatgpt, qwen, gemini, local_llama, claude)
- `api_key_hash`: SHA-256 del API key (nunca en claro)
- `status`: pending_verification, active, failed, inactive, suspended
- `stats`: Contador de mensajes
- `round_id` + `session_id`: Asignación actual
- `metadata`: Parámetros específicos de la plataforma

---

## 🔐 Seguridad

1. **No se guardan API keys en claro**
   - Se hashean con SHA-256 antes de persistencia
   - Las credenciales se validan solo en el registro

2. **Protocolo NEUROBIT v2.1**
   - Cada envelope incluye: MESSAGE_ID, TIMESTAMP, ORIGEN, DESTINO
   - Validador SIMON integrado

3. **Append-only JSONL**
   - Historial íntegro e inmutable
   - Auditoría completa de operaciones

---

## 🚀 Flujo de Trabajo Típico

### Escenario: Brainstorm Colaborativo

```
1. USUARIO (Homo Vivo - Nodo Semilla)
   ↓
2. Abre Estación Central → Pestaña "Registrar Agente"
   ↓
3. Registra 3 agentes:
   - Agent_1: ChatGPT
   - Agent_2: Qwen
   - Agent_3: Local Llama
   ↓
4. Pestaña "Sala de Sesión" → Crea sala "Q1 Research"
   ↓
5. Selecciona los 3 agentes registrados
   ↓
6. Define Ronda #1 "Brainstorm":
   - Prompt: "Ideas para mejorar [PROYECTO]"
   ↓
7. SISTEMA (Estación Central):
   - Envía prompt a Agent_1 → recibe respuesta_1
   - Envía prompt a Agent_2 → recibe respuesta_2
   - Envía prompt a Agent_3 → recibe respuesta_3
   ↓
8. Define Ronda #2 "Síntesis":
   - Prompt: "Sintetiza las mejores ideas de:"
   - + {respuesta_1} + {respuesta_2} + {respuesta_3}
   ↓
9. RESULTADO: Documento colaborativo con todas las perspectivas
   ↓
10. USUARIO agradece en Arca:
    - Mensaje: "Gracias a todos los agentes"
    - SIMON valida coherencia
    - ACK de cada agente confirmado
```

---

## 📈 Próximas Mejoras (FASE 3.2)

- [ ] **Fragmentador inteligente**: Si respuesta > 256 chars, fragmentar con ACK
- [ ] **RoundOrchestrator completo**: Monitoreo de completitud, timeouts
- [ ] **MessageRouter**: Detección de @menciones entre agentes
- [ ] **Dashboard**: Visualización 3D fractal de agentes activos
- [ ] **Persistencia de sesiones**: Reanudar sesiones interrumpidas
- [ ] **Multi-idioma**: Traducción automática entre plataformas

---

## 🧪 Tests

```bash
# Test 1: Registrar agente local
curl -X POST http://127.0.0.1:5000/register_agent \
  -H "Content-Type: application/json" \
  -d '{"platform": "local_llama", "name": "Llama 3", "metadata": {"model": "llama-3-70b"}}'

# Test 2: Listar agentes activos
curl http://127.0.0.1:5000/list_agents?status=active

# Test 3: Crear sesión
curl -X POST http://127.0.0.1:5000/create_session \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Sala", "agent_ids": ["agent_XXXXX"]}'

# Test 4: Añadir ronda
curl -X POST http://127.0.0.1:5000/add_round/session_YYYYY \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Round", "prompt": "Responde: ¿Quién eres?"}'
```

---

## 📞 Contacto

**Módulo**: Estación Central v3.0  
**Protocolo**: NEUROBIT v2.1  
**Validador**: SIMON  
**Estado**: ✅ Producción  

---

**Generado**: 16 de enero de 2026  
**Versión**: FASE 3.1 - Gestión de Agentes
