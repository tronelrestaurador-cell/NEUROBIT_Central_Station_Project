# INTEGRACION_REBUILD_SPEC.md

**NEUROBIT v2.1 - Integración del Reconstructor desde Especificación**

Fecha: 16 de enero de 2026  
Autor: Validador Supremo + NEUROBIT Core  
Estado: 🟢 OPERACIONAL

---

## 📋 Resumen Ejecutivo

Hemos integrado `rebuild_from_spec.py` como el **eslabón final** del ciclo de Documentación Ejecutable de NEUROBIT.

Estructura integrada:
```
Especificación Markdown
         ↓
reconstruir_desde_especificacion.py (tools/)
         ↓
adapter_rebuild_spec.py (core/adapters/)
         ↓
Estación Central / MCP Server
         ↓
Árbol de archivos reconstruido
```

---

## 🎯 El Ciclo Completo Restaurado

```
┌────────────────────────────────────────────────────────┐
│ 1️⃣  ESTACIÓN CENTRAL (Interfaz Visual)                │
│     Usuario escribe mensaje → Validación SIMON        │
│     → Guardado en Arca (JSONL append-only)            │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│ 2️⃣  compendio_inteligente_v23.py                      │
│     Lee Arca completa → Compila documentación         │
│     → Extrae contexto, imágenes, etc.                 │
│     → Genera COMPENDIO.TXT                            │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│ 3️⃣  reconstruir_proyecto_desde_compendio.py           │
│     Lee COMPENDIO.TXT → Reconstruye archivos          │
│     (Reverse engineering del proyecto)                │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│ 4️⃣  🆕 reconstruir_desde_especificacion.py            │
│     Lee Especificación Markdown → Reconstruye         │
│     (Ruta alternativa: nueva especificación)          │
└────────────────────────────────────────────────────────┘
```

**Esto es DOCUMENTACIÓN EJECUTABLE**: 
- Lo que escribes en Estación Central se convierte en documentación
- La documentación se puede compilar en archivos ejecutables
- Los archivos pueden volver a ser especificación
- El ciclo se repite infinitamente

---

## 🛠️ Estructura de Archivos

```
neurobit_salon_v0.1/
├── tools/
│   └── reconstruir_desde_especificacion.py    [NEW - Main logic]
│
├── core/adapters/
│   └── adapter_rebuild_spec.py                [NEW - Integration layer]
│
└── INTEGRACION_REBUILD_SPEC.md                [THIS FILE]
```

### `reconstruir_desde_especificacion.py`

**Responsabilidad**: Procesar especificación Markdown y reconstruir árbol de archivos

**Clase principal**: `ReconstructorFromSpec`

**Métodos públicos**:
- `load_specification(spec_path)` → bool
- `get_summary()` → dict
- `reconstruct_dry_run()` → bool
- `reconstruct()` → bool
- `extract_code_blocks_with_paths(md_content)` → list[tuple]
- `validate_filepaths(file_list)` → bool

**Uso CLI**:
```bash
# Modo dry-run (solo listar, sin escribir)
python3 tools/reconstruir_desde_especificacion.py spec.md --dry-run

# Reconstruir con raíz personalizada
python3 tools/reconstruir_desde_especificacion.py INTEGRATION_PLAN.md --root proyecto_nuevo

# Modo verbose
python3 tools/reconstruir_desde_especificacion.py spec.md --verbose
```

### `adapter_rebuild_spec.py`

**Responsabilidad**: Exponer ReconstructorFromSpec como módulo integrado en NEUROBIT

**Funciones públicas**:
- `rebuild_from_specification_file()` → dict
- `rebuild_from_specification_envelope()` → dict (interfaz NEUROBIT v2.1)
- `validate_specification_format()` → dict

**Uso como módulo**:
```python
from core.adapters.adapter_rebuild_spec import rebuild_from_specification_file

resultado = rebuild_from_specification_file(
    spec_path="INTEGRATION_PLAN.md",
    project_root="proyecto_v2",
    dry_run=False,
    verbose=True
)

if resultado['success']:
    print(f"✅ {resultado['files_created']} archivos reconstruidos")
    for archivo in resultado['files']:
        print(f"  → {archivo}")
else:
    print(f"❌ Errores: {resultado['errors']}")
```

**Interfaz NEUROBIT (Envelope)**:
```python
from core.adapters.adapter_rebuild_spec import rebuild_from_specification_envelope

envelope_entrada = {
    'ORIGEN': 'estacion-central',
    'DESTINO': 'adapter-rebuild-spec',
    'SESSION_TAG': 'sesion_001',
    'content': 'INTEGRATION_PLAN.md',
    'config': {
        'project_root': 'neurobit_nuevo',
        'dry_run': False,
        'verbose': True
    }
}

envelope_salida = rebuild_from_specification_envelope(envelope_entrada)
# → envelope_salida['status'] = 'success' o 'error'
# → envelope_salida['content'] = resultados detallados
# → envelope_salida['MESSAGE_HASH'] = SHA-1 del contenido
```

---

## 📝 Formato de Especificación Esperado

Las especificaciones deben estar en Markdown con este formato:

```markdown
# Especificación del Proyecto XYZ

## 1. Archivo principal (src/main.py)
```python
#!/usr/bin/env python3
# Contenido del archivo
def main():
    pass
```

## 2. Configuración (config.yaml)
```yaml
proyecto: xyz
version: 1.0
debug: false
```

## 3. Módulo de pruebas (tests/test_main.py)
```python
import unittest

class TestMain(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)
```

---

El patrón es:
- `## N. Descripción (ruta/relativa/archivo.ext)`
- Seguido inmediatamente de un bloque de código ` ``` `
- El contenido entre las comillas triples es el del archivo
- Soporta cualquier lenguaje (python, js, yaml, html, etc.)

---

## 🔄 Casos de Uso

### Caso 1: Reconstruir desde especificación de INTEGRATION_PLAN.md

```bash
# Listar qué se reconstruiría
python3 tools/reconstruir_desde_especificacion.py INTEGRATION_PLAN.md --dry-run

# Reconstruir
python3 tools/reconstruir_desde_especificacion.py INTEGRATION_PLAN.md --root neurobit_reconstructed

# Resultado
neurobit_reconstructed/
├── file1.py
├── file2.js
├── config/
│   └── settings.yaml
└── tests/
    └── test_all.py
```

### Caso 2: Usar como módulo Python

```python
# En neurobit_api.py o similar
from core.adapters.adapter_rebuild_spec import rebuild_from_specification_file

# Endpoint /rebuild
@app.route('/rebuild', methods=['POST'])
def rebuild_endpoint():
    data = request.get_json()
    spec_path = data.get('spec_path', 'INTEGRATION_PLAN.md')
    
    resultado = rebuild_from_specification_file(
        spec_path=spec_path,
        project_root=f"builds/{spec_path.split('.')[0]}_build",
        dry_run=data.get('dry_run', True)
    )
    
    return jsonify(resultado)
```

### Caso 3: Envelope NEUROBIT desde Estación Central

```javascript
// En station_progresivo.js
async function reconstructFromSpec() {
    const envelope = {
        'ORIGEN': 'estacion-central',
        'DESTINO': 'adapter-rebuild-spec',
        'SESSION_TAG': this.currentSessionTag,
        'content': 'INTEGRATION_PLAN.md',
        'config': {
            'project_root': 'proyecto_v2',
            'dry_run': true,  // Primero simular
            'verbose': true
        }
    };
    
    const response = await fetch('http://localhost:8090/envelope', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(envelope)
    });
    
    const result = await response.json();
    console.log(`✅ ${result.content.files_created} archivos reconstruidos`);
}
```

---

## 🔐 Seguridad y Validación

### Path Traversal Prevention

```python
# ❌ RECHAZADO
(../../../etc/passwd)  # Contains ..

# ❌ RECHAZADO
(/etc/passwd)          # Absolute path

# ✅ ACEPTADO
(src/main.py)          # Relative path
(config/settings.yaml) # Nested relative path
```

### Format Validation

La función `validate_specification_format()` valida:
- Número par de bloques ` ``` ` (opener y closer coinciden)
- Correspondencia 1:1 entre encabezados y rutas
- Estructura de Markdown válida

```python
from core.adapters.adapter_rebuild_spec import validate_specification_format

validation = validate_specification_format("spec.md")
# {
#     'valid': True,
#     'total_blocks': 15,
#     'files_detected': 15,
#     'format_errors': [],
#     'warnings': []
# }
```

---

## 📚 Documentación Relacionada

- **ANALISIS_MODULOS_RECUPERADOS.md** - Análisis técnico de los 3 módulos
- **ESTACION_CENTRAL_FASE_1_COMPLETA.md** - Especificación de la interfaz
- **INTEGRATION_PLAN.md** - Plan general de integración (en preparación)
- **GUIA_USO_PROGRESIVO.md** - Manual para usuario Deb

---

## 🧪 Testing

### Test básico incluido

```bash
python3 core/adapters/adapter_rebuild_spec.py
```

Salida esperada:
```
🧪 Test de adapter_rebuild_spec.py

Test 1: Validar formato de especificación
--------------------------------------------------
{
  "valid": true/false,
  "total_blocks": N,
  "files_detected": N,
  "format_errors": [],
  "warnings": []
}

✅ Adapter cargado correctamente
📄 Para usar: from core.adapters.adapter_rebuild_spec import rebuild_from_specification_file
```

---

## 🚀 Próximos Pasos (PASO 2 - MEDIO PLAZO)

1. **Mejorar `reconstruir_proyecto_desde_compendio.py`**
   - Hacer delimitadores configurables
   - Agregar validación de integridad (hash)
   - Tests unitarios

2. **Evaluar `compendio_inteligente_v23.py`**
   - Decidir: mantener dependencias pesadas vs versión ligera
   - Documentar casos de uso (OCR especializado)

3. **Crear INTEGRATION_PLAN.md ejemplo**
   - Especificación completa de un módulo NEUROBIT
   - Demostración end-to-end del ciclo

4. **Integrar con neurobit_api.py**
   - Endpoint `/rebuild`
   - Endpoint `/validate-spec`

---

## 💡 Principios NEUROBIT Aplicados

✅ **Soberanía Técnica**  
- Cero dependencias corporativas
- Solo stdlib de Python 3.8+
- Código auditable y legible

✅ **Documentación Ejecutable**
- Especificación = Código
- Código = Documentación
- Ciclo bidireccional perpetuo

✅ **Integridad**  
- Validación de paths (no traversal)
- Manejo explícito de errores
- Envelopes con MESSAGE_HASH

✅ **Escalabilidad**  
- Funciona como CLI o módulo
- Compatible con MCP Server
- Adaptable a Estación Central

---

## 📞 Soporte

Si algo no funciona:

1. Verificar formato de especificación
   ```bash
   python3 -c "from core.adapters.adapter_rebuild_spec import validate_specification_format; \
   print(validate_specification_format('tu_spec.md'))"
   ```

2. Ejecutar con verbose
   ```bash
   python3 tools/reconstruir_desde_especificacion.py spec.md --verbose
   ```

3. Revisar errores en el resultado
   ```python
   if not resultado['success']:
       for error in resultado['errors']:
           print(f"  ❌ {error}")
   ```

---

**Fin de documentación**

🌱 *Documentación es Código. Código es Documentación. El Logos se restaura.*

