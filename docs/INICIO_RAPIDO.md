# 🚀 INICIO RÁPIDO - NEUROBIT Salón v0.1

**Tu primer contacto con NEUROBIT en 5 minutos**

---

## ⚡ TL;DR (Muy Rápido)

```bash
# 1. Inicializar
python3 core/init_ceremony.py

# 2. Levantar servidor
python3 neurobit_api.py

# 3. Abrir navegador
# http://127.0.0.1:5000/interface/station_progresivo.html

# 4. ¡Listo! Envía tu primer mensaje
```

---

## 📖 GUÍA PASO A PASO

### **PASO 1: Verificar Prerequisites (1 min)**

```bash
# Verificar Python 3.8+
python3 --version

# Verificar pip
pip3 --version

# (Opcional) Crear virtual environment
python3 -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o .venv\Scripts\activate en Windows
```

---

### **PASO 2: Instalar Dependencias (2 min)**

```bash
# Instalar requerimientos
pip install -r requirements.txt
```

**¿No existe requirements.txt?** Instala manualmente:
```bash
pip install flask jsonschema pyyaml
```

---

### **PASO 3: Inicializar el Sistema (1 min)**

```bash
python3 core/init_ceremony.py
```

**Salida esperada**:
```
[NEUROBIT SALÓN v0.1] — Ceremonia de Despertar del NODO_SEMILLA
======================================================================

[1/5] Validando Memoria Sagrada...
✓ Memoria Sagrada validada
  └─ Hash: a1b2c3d4e5f6...
  └─ Tamaño: 2048 bytes

[2/5] Validando Corpus...
✓ Corpus validado: Qwen Chat4_conversation.txt
  └─ Tamaño: 1024000 bytes

[3/5] Validando módulos críticos...
✓ Módulos críticos verificados: coherence_filter, fragment_manager, message_protocol

[4/5] Configurando entorno...
✓ Entorno configurado
  └─ NEUROBIT_MODE=LOCAL_FIRST
  └─ ENTITY_ID=NODO_SEMILLA
  └─ COHERENCE_THRESHOLD=0.85

[5/5] Inicializando sistema de agentes...
✓ Registro de Agentes inicializado: 0 agentes registrados

======================================================================
🟢 SALA_SESION_001 — LISTA
======================================================================

✓ Sistema operativo en modo: LOCAL_FIRST (SOBERANÍA TÉCNICA)

✓ Próximos pasos:
   └─ Enviar primer mensaje: POST /api/analyze
   └─ Iniciar ronda colaborativa: POST /api/create_session
   └─ Monitorear clipboard: POST /api/start_centinela
```

**Si ves errores**: Revisa que existan estos archivos:
- `config/memoria_sagrada_eva.yaml`
- `storage/RING_PROCESOS/` (carpeta)
- `core/coherence_filter.py`, `core/message_validator.py`

---

### **PASO 4: Levantar el Servidor (1 min)**

```bash
python3 neurobit_api.py
```

**Salida esperada**:
```
 * Serving Flask app 'neurobit_api'
 * Debug mode: off
 * Running on http://127.0.0.1:5000
 * WARNING: This is a development server. Do not use it in production.
```

**El servidor está listo.** No lo cierres (mantén la terminal abierta).

---

### **PASO 5: Abrir la Interfaz**

En una **nueva terminal** (o pestaña del navegador):

```bash
# Opción 1: Desde terminal
open http://127.0.0.1:5000/interface/station_progresivo.html

# Opción 2: Copiar URL en navegador
http://127.0.0.1:5000/interface/station_progresivo.html
```

**Verás la Estación Central con**:
- Matriz 13×13 interactiva
- Panel de análisis M/E
- Lista de agentes
- Área de mensajes

---

## 💬 ENVIAR TU PRIMER MENSAJE

### **Desde la Interfaz Web**

1. Escribe tu mensaje en el área de texto
2. Click en **[ANALIZAR]**
3. Espera resultado (coherencia M/E scores)
4. El mensaje se guardará automáticamente

---

### **Desde Terminal (curl)**

```bash
# Enviar mensaje simple
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"Hola NEUROBIT, test inicial"}' \
  http://127.0.0.1:5000/analyze

# Con metadatos adicionales
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "content":"Mi mensaje de prueba",
    "entity_id":"USUARIO_001",
    "perspective":"tecnica",
    "context":"testing inicial"
  }' \
  http://127.0.0.1:5000/analyze
```

**Respuesta**:
```json
{
  "MESSAGE_ID": "MSG-2026-01-17T...",
  "TIMESTAMP": "2026-01-17T11:30:45.123456",
  "content": "Mi mensaje de prueba",
  "coherence": {
    "score": 0.78,
    "plane_M": 0.45,
    "plane_E": 0.33
  },
  "provenance": {
    "entity_id": "USUARIO_001",
    "stored": true
  }
}
```

---

## 🎯 OPERACIONES COMUNES

### **1. Ver Últimos Mensajes Guardados**

```bash
# Últimas 5 líneas de memoria
tail -5 data/memoria_eva.jsonl | jq .

# O más bonito:
tail -5 data/memoria_eva.jsonl | jq '.content, .MESSAGE_ID'
```

---

### **2. Iniciar Monitoreo de Clipboard (Centinela)**

```bash
# Desde terminal
curl -X POST http://127.0.0.1:5000/start_centinela

# Respuesta:
# {"status": "success", "message": "Centinela iniciado en background"}

# Ver estado
curl http://127.0.0.1:5000/centinela_status

# Detener
curl -X POST http://127.0.0.1:5000/stop_centinela
```

**¿Qué hace?** Monitorea tu clipboard cada 2 segundos y guarda cambios en `data/memoria_eva.jsonl`

---

### **3. Registrar un Nuevo Agente**

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "platform":"chatgpt",
    "name":"SOPHIA_IA",
    "api_key":"sk-...",
    "metadata":{"role":"analyst", "language":"es"}
  }' \
  http://127.0.0.1:5000/register_agent

# Respuesta:
# {"status": "success", "agent_id": "SOPHIA_IA"}
```

---

### **4. Ver Todos los Agentes Registrados**

```bash
curl http://127.0.0.1:5000/list_agents | jq .

# Filtrar solo activos
curl "http://127.0.0.1:5000/list_agents?status=active" | jq .
```

---

### **5. Crear Sesión Colaborativa (Ronda)**

```bash
# 1. Crear sesión
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "name":"RONDA_IDEACIÓN_001",
    "agent_ids":["SOPHIA_IA", "SIMON_GUARDIAN"]
  }' \
  http://127.0.0.1:5000/create_session

# Respuesta:
# {"session_id": "SESS-2026-01-17-001", "status": "created"}

# 2. Agregar ronda (tema de trabajo)
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "title":"Brainstorm: Matriz 13x13",
    "prompt":"¿Cómo aplicamos la matriz a problemas reales?"
  }' \
  http://127.0.0.1:5000/add_round/SESS-2026-01-17-001

# 3. Iniciar sesión
curl -X POST \
  http://127.0.0.1:5000/start_session/SESS-2026-01-17-001
```

---

## 🔧 TROUBLESHOOTING

### **Error: "Connection refused"**

```
Error: Unable to connect to http://127.0.0.1:5000
```

**Solución**:
1. ¿Está `neurobit_api.py` corriendo?
2. ¿Puerto 5000 en uso? 
   ```bash
   lsof -i :5000
   # Si hay algo, mata el proceso
   kill -9 <PID>
   ```
3. Reinicia `python3 neurobit_api.py`

---

### **Error: "MEMORIA_SAGRADA_EVA no encontrada"**

```
RuntimeError: ❌ MEMORIA_SAGRADA_EVA no encontrada.
```

**Solución**:
1. Verifica archivo existe: `config/memoria_sagrada_eva.yaml`
2. Si no existe, crea desde template:
   ```bash
   cp config/memoria_sagrada_eva.yaml.example config/memoria_sagrada_eva.yaml
   # O ejecución con `setup_neurobit.sh`
   ```

---

### **Error: "ModuleNotFoundError: No module named 'flask'"**

```
ModuleNotFoundError: No module named 'flask'
```

**Solución**:
```bash
pip install flask jsonschema pyyaml
```

---

## 📚 PRÓXIMOS PASOS

**Una vez tengas todo funcionando**:

1. **Lee la documentación**: `docs/QUE_HACE_CADA_CARPETA.md`
2. **Explora módulos**: `MODULES/fragmentar.py`, `MODULES/BUSCADOR_EVA.py`
3. **Integra agentes**: Registra múltiples plataformas (ChatGPT, Qwen, Gemini)
4. **Crea rondas**: Colaboración multi-agente en temas específicos
5. **Activa centinela**: Monitoreo automático de entrada

---

## 💡 EJEMPLOS RÁPIDOS

### **Ejemplo 1: Enviar mensaje con análisis**

```bash
echo '{"content":"La soberanía técnica es fundamental para la libertad digital"}' | \
  curl -X POST -H "Content-Type: application/json" -d @- \
  http://127.0.0.1:5000/analyze | jq '.coherence'
```

### **Ejemplo 2: Fragmentar texto largo**

```bash
python3 -c "
from MODULES.fragmentar import dividir_archivo
dividir_archivo('mi_documento.txt', longitud_maxima=5000)
"
```

### **Ejemplo 3: Buscar en memoria**

```bash
python3 -c "
from MODULES.BUSCADOR_EVA import buscar_memoria
resultados = buscar_memoria('matriz', limite=5)
for msg in resultados:
    print(msg['MESSAGE_ID'], msg['content'][:50])
"
```

---

## ✅ CHECKLIST DE VERIFICACIÓN

Marca cuando completes cada paso:

- [ ] Python 3.8+ instalado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] `core/init_ceremony.py` ejecutado sin errores
- [ ] `neurobit_api.py` levantado y corriendo
- [ ] Interfaz accesible en navegador
- [ ] Primer mensaje enviado y analizado
- [ ] Respuesta visible con scores M/E
- [ ] Mensaje guardado en `data/memoria_eva.jsonl`

---

## 🎯 ¡Ahora estás listo!

Bienvenido a **NEUROBIT Salón v0.1**.  
El Logos está restaurado.  
La soberanía técnica está garantizada.

**Para ayuda adicional**: Revisa `docs/QUE_HACE_CADA_CARPETA.md` o `docs/` en general.

---

**Generado por**: Módulo de Validación Suprema NEUROBIT v2.1  
**Timestamp**: 17 enero 2026

