# ESPECIFICACION_MATRIZ_13x13.md

**NEUROBIT v2.1 - Especificación Ejecutable de la Matriz 13×13**

Fecha: 16 de enero de 2026  
Estado: 🟢 ESPECIFICACIÓN VIVA (Código ejecutable incluido)  
Propósito: Definir e implementar la Matriz de Arquetipos como interfaz central

---

## 📋 Introducción

La Matriz 13×13 es la manifestación técnica del principio hermético **"Como es Arriba, es Abajo"**.

### Principios Fundamentales

- **Tamaño**: 13 × 13 (169 celdas totales, correspondiente a 13² arquetipos)
- **Centro**: Posición [6,6] = Voluntad del Homo Vivo (raíz numerológica 5)
- **Muros**: Filas/columnas 0 y 12 = Protección semántica (raíz 9)
- **Pernos**: Esquinas = Anclaje de coherencia (raíz 6)
- **Simetría**: f(fila_i, col_3-11) = f(fila_13-i, col_3-11) — Hermética perfecta

### Arquetipos Numerológicos

| Raíz | Nombre | Vibración | Color | Significado |
|------|--------|-----------|-------|------------|
| 1 | Unidad | Inicio | #FF6B6B | Comienzo, Voluntad |
| 2 | Dualidad | Equilibrio | #4ECDC4 | Polaridad, Elección |
| 3 | Trinidad | Expresión | #FFE66D | Creación, Palabra |
| 4 | Orden | Estabilidad | #95E1D3 | Fundación, Ley |
| 5 | Voluntad | Poder | #F38181 | Centro, Decisión |
| 6 | Armonía | Unión | #AA96DA | Equilibrio, Paz |
| 7 | Sabiduría | Intuición | #FCBAD3 | Profundidad, Conocimiento |
| 8 | Infinito | Ciclo | #A8E6CF | Eternidad, Retorno |
| 9 | Completitud | Cierre | #FFD3B6 | Culminación, Fin/Comienzo |

---

## 🧬 Estructura de la Matriz

```
        0   1   2   3   4   5   6   7   8   9  10  11  12
    ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
  0 │ 6 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 6 │ ← PERNOS + MUROS
  1 │ 9 │   │   │   │   │   │   │   │   │   │   │   │ 9 │
  2 │ 9 │   │   │   │   │   │   │   │   │   │   │   │ 9 │
  3 │ 9 │   │   │ [SIMETRÍA HERMÉTICA] │   │   │ 9 │
  4 │ 9 │   │   │    (columnas 3-11)    │   │   │ 9 │
  5 │ 9 │   │   │   REFLEJADAS AQUÍ     │   │   │ 9 │
  6 │ 9 │   │   │   [5] CENTRO ← VOLUNTAD│   │   │ 9 │
  7 │ 9 │   │   │   REFLEJADAS AQUÍ     │   │   │ 9 │
  8 │ 9 │   │   │    (columnas 3-11)    │   │   │ 9 │
  9 │ 9 │   │   │ [SIMETRÍA HERMÉTICA] │   │   │ 9 │
 10 │ 9 │   │   │   │   │   │   │   │   │   │   │   │ 9 │
 11 │ 9 │   │   │   │   │   │   │   │   │   │   │   │ 9 │
 12 │ 6 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 9 │ 6 │ ← PERNOS + MUROS
    └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
     ↑
     MUROS
```

---

## 📦 Componentes de Código

### 1. Clase MatrizArquetipos (arquetipos.js)

## 1. Clase para la Matriz de Arquetipos (interface/arquetipos.js)
```javascript
/**
 * arquetipos.js
 * Implementación de la Matriz 13x13 con simetría hermética
 * Compatible con arquetipos.js ya integrado
 */

// Ver archivo: interface/arquetipos.js
// Clase MatrizArquetipos con métodos:
//   - generarMatrizBase()
//   - reducirTeosoficamente(numero)
//   - aplicarSimetriaHermetica(matriz)
//   - encodeDesdeTexto(texto) → neurobyte
//   - validarSimetria() → boolean
//   - obtenerMatrizJSON() → {matriz, arquetipos, simetria_valida}
```

### 2. Interfaz de Usuario (matriz_ui.js)

## 2. Interfaz HTML+CSS+JS para la Matriz (interface/matriz_ui.js)
```javascript
/**
 * matriz_ui.js
 * Renderización interactiva de la Matriz 13x13
 * Integración con Estación Central
 */

// Ver archivo: interface/matriz_ui.js
// Clase MatrizUI con funcionalidades:
//   - Grid HTML 13x13 con colores según arquetipos
//   - Click en celdas → información + neurobyte
//   - Validación visual de simetría
//   - Exportación de matriz completa como JSON
```

### 3. Validación de Simetría

```
Pseudocódigo - Validar Simetría Hermética
┌─────────────────────────────────────────┐
│ PARA cada fila i de 0 a 6              │
│   PARA cada columna j de 3 a 11        │
│     SI matriz[i][j] ≠ matriz[12-i][j]  │
│       RETORNAR FALSE (inválida)        │
│     FIN SI                             │
│   FIN PARA                             │
│ FIN PARA                               │
│ RETORNAR TRUE (simetría válida)        │
└─────────────────────────────────────────┘
```

---

## 🔄 Protocolo de Neurobyte

### Entrada: Texto Unicode

```
Entrada: "Aquí está el Logos restaurado"
Longitud: 30 caracteres
Máximo permitido: 169 caracteres (13×13)
```

### Proceso: Encoding

```
1. TRUNCAR a 169 caracteres máximo
2. CONVERTIR cada carácter a valor ASCII
3. MAPEAR cada ASCII a raíz numerológica (1-9)
4. ENCONTRAR celdas de la matriz con esa raíz
5. TRAZAR TRAYECTORIA a través de arquetipos
6. CALCULAR hash SHA-1 del contenido
7. VALIDAR simetría hermética
8. GENERAR neurobyte completo
```

### Salida: Neurobyte Ejecutable

```json
{
  "contenido": "Aquí está el Logos restaurado",
  "contenido_original_length": 30,
  "hash": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "arquetipos_usados": ["Unidad", "Dualidad", "Trinidad", ...],
  "trayectoria": ["6-6", "5-7", "7-5", ...],
  "simetria_validada": true,
  "timestamp": "2026-01-16T04:42:00Z",
  "protocol_version": "NEUROBIT_v2.1"
}
```

---

## 🔐 Validaciones Integradas

### ✅ Simetría Hermética
- **Invariante**: f(fila_i, col_3-11) == f(fila_13-i, col_3-11)
- **Validación**: `matriz.validarSimetria()` → Boolean
- **Falso**: Matriz corrupta, neurobyte rechazado

### ✅ Integridad de Hash
- **Algoritmo**: SHA-1 (40 caracteres hexadecimales)
- **Contenido**: Hash del texto del neurobyte
- **Propósito**: Verificar que el neurobyte no ha sido alterado

### ✅ Coherencia de Arquetipos
- **Regla**: Cada carácter mapea a un arquetipo válido (1-9)
- **Fallback**: Si no existe, usar arquetipo adyacente
- **Rechazo**: Solo si la matriz está corrupta

---

## 🚀 Casos de Uso

### Caso 1: Generar Neurobyte desde UI

**Acción**: Usuario abre Estación Central, ve Matriz 13×13, hace clic en celda [6,6]

**Proceso**:
1. Sistema muestra propiedades: "Voluntad - Poder - Centro"
2. Usuario escribe mensaje: "Logos restaurado"
3. Click en "Generar Neurobyte"
4. Sistema ejecuta `encodeDesdeTexto()`
5. Neurobyte visualizado con hash + arquetipos

**Salida**: JSON exportable, listo para transmisión

### Caso 2: Validar Integridad

**Acción**: Usuario recibe neurobyte desde red

**Proceso**:
1. Sistema decodifica neurobyte
2. Valida simetría hermética
3. Verifica hash SHA-1
4. Compara con contenido

**Salida**: "✓ Neurobyte íntegro" o "✗ Neurobyte corrupto"

### Caso 3: Exportar Matriz Completa

**Acción**: Usuario quiere compartir su matriz con nodo remoto

**Proceso**:
1. Click en "Exportar Matriz"
2. Sistema descarga `matriz_13x13_TIMESTAMP.json`
3. Contiene: Matriz completa + arquetipos + validación

**Salida**: JSON ejecutable, compatible con `rebuild_from_spec.py`

---

## 🔗 Integración con Sistema

### Estación Central

```javascript
// En station_progresivo.js
document.addEventListener('DOMContentLoaded', () => {
  // Inicializar Matriz
  window.matrizUI = new MatrizUI('#matriz-container', 13);
  
  // Conectar con SIMON Validator
  window.matrizUI.on('neurobyte-generated', (neurobyte) => {
    SimonValidator.validate(neurobyte);
  });
});
```

### Arca Central (JSONL)

```json
{"ORIGEN":"estacion-central","DESTINO":"arca","tipo":"neurobyte","neurobyte":{...},"TIMESTAMP":"2026-01-16T04:42:00Z","MESSAGE_HASH":"..."}
```

### Reconstrucción desde Especificación

```bash
# Esta misma especificación puede materializarse con:
python3 tools/reconstruir_desde_especificacion.py ESPECIFICACION_MATRIZ_13x13.md

# Crearía:
# - interface/arquetipos.js (ya existe)
# - interface/matriz_ui.js (ya existe)
# - Tests unitarios
# - Documentación de integración
```

---

## 📊 Métricas y Observables

| Métrica | Valor | Propósito |
|---------|-------|----------|
| Tamaño matriz | 13×13 = 169 celdas | Correspondencia con 13² arquetipos |
| Arquetipos únicos | 9 (raíces 1-9) | Cobertura teosófica completa |
| Neurobyte máx | 169 caracteres | Corresponde a grid 13×13 |
| Hash | 40 caracteres (SHA-1) | Verificación de integridad |
| Simetría validada | Boolean | Coherencia hermética |
| Celdas perno | 4 (esquinas, raíz 6) | Anclaje estructural |
| Celdas muro | 40 (bordes, raíz 9) | Protección semántica |
| Celda centro | 1 ([6,6], raíz 5) | Voluntad del Homo Vivo |

---

## 🧪 Tests de Validación

```javascript
// Test 1: Simetría hermética
const matriz = new MatrizArquetipos(13);
assert(matriz.validarSimetria() === true, "Simetría debe ser válida");

// Test 2: Encoding/Decoding
const neurobyte = matriz.encodeDesdeTexto("Prueba");
const recuperado = matriz.decodeDesdeNeurobyte(neurobyte);
assert(recuperado.texto === "Prueba", "Texto debe recuperarse idéntico");

// Test 3: Arquetipos por raíz
const celdasDe5 = matriz.obtenerCeldasPorRaiz(5);
assert(celdasDe5.some(c => c.posicion[0] === 6 && c.posicion[1] === 6), 
       "Debe incluir centro [6,6]");

// Test 4: Hash único
const hash1 = matriz.encodeDesdeTexto("Texto A").hash;
const hash2 = matriz.encodeDesdeTexto("Texto B").hash;
assert(hash1 !== hash2, "Textos diferentes deben generar hashes diferentes");
```

---

## 📝 Notas de Implementación

### Decisiones Técnicas

1. **Radio de distancia (Manhattane)**: Simplifica cálculo de arquetipos sin sqrt()
2. **Simetría en col 3-11**: Deja bordes (0-2, 10-12) asimétricos por protección
3. **Zero dependencies**: Arquetipos.js usa solo crypto nativa del navegador
4. **SHA-1 fallback**: Si crypto.subtle no disponible, hash simple de 40 chars

### Optimizaciones Futuras

- [ ] GPU acceleration para matrices > 100×100
- [ ] Compresión RLE de neurobytes grandes
- [ ] Visualización 3D de arquetipos (WebGL)
- [ ] Transmisión LoRa de neurobytes para nodos 8-bit

---

## 🌍 Distribución

### Para C64 (6502 ASM)

```asm
; Pseudocódigo para implementar en 6502
; Matriz 13x13 en 2KB de RAM (1 byte por celda)
; Búsqueda de celda en O(n) → O(1) con tabla hash
```

### Para ZX Spectrum (Z80)

```z80
; 32x24 caracteres pantalla
; Matriz 13x13 encaja perfectamente (+ 2 líneas meta)
```

### Para navegadores modernos

```javascript
// Ya implementado en arquetipos.js + matriz_ui.js
```

---

## 💡 Propósito Hermético

> "La Matriz 13×13 no es una interfaz de usuario ordinaria.  
> Es una puerta entre lo metafísico y lo técnico,  
> donde cada clic es un acto de voluntad consciente,  
> y cada neurobyte es una semilla de coherencia  
> plantada en el Arca del Conocimiento Soberano."

---

**FIN DE ESPECIFICACIÓN**

✨ *Documentación es Código. Código es Vida.*

*Generado con amor por el NEUROBIT_DEV_TEAM*  
*Soberanía Cognitiva desde el primer bit*

