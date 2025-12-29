# HANDOFF_OPERATIVO — NEUROBIT_SALON_v0.1

## 1. CONTEXTO GENERAL
Proyecto: NEUROBIT_SALON_v0.1
Objetivo inmediato: Primera ronda R001 con corpus Qwen
Estado humano: Sobrecarga cognitiva — requiere delegación técnica

## 2. FUENTES (NO COPIAR CONTENIDO)
- Chat A: Plataforma X — conversación sobre M/E (fecha aproximada)
- Chat B: Plataforma Y — validación técnica (coherence_filter)
- Archivo local: `Qwen Chat4_conversation.txt`
- Repo local: `neurobit_salon_v0.1` (snippets en `storage/RING_PROCESOS/code_snippets`)

> NOTA: El contenido íntegro puede recuperarse vía curl a endpoints públicos o desde logs locales. No adjuntar cuerpos completos en el handoff.

## 3. DECISIONES YA TOMADAS (NO DISCUTIR)
- Modelo bidimensional M/E es válido
- SIMON es árbitro técnico
- SOPHIA valida coherencia, no intención
- Operación es LOCAL_FIRST

## 4. PREGUNTAS ABIERTAS PARA SIMON
- ¿Cómo unificar timestamps de fuentes múltiples? (formato objetivo: ISO-8601)
- ¿Qué fragmentación mínima usar para R001? (longitud en tokens o por mensaje)
- ¿Qué ambigüedades priorizar en glosario inicial?

## 5. INSTRUCCIÓN CLARA
SIMON:
- Reconstruir línea temporal desde las fuentes listadas.
- Proponer pipeline técnico mínimo (ETL → normalización → fragmentación → validación).
- Devolver checklist ejecutable (máx. 10 pasos).

No explicar filosofía. No justificar. No narrar.

## 6. RITMO DE TRABAJO HUMANO SOSTENIBLE
Ciclo recomendado (45–60 min máximo):
- 25 min — leer / marcar (sin escribir)
- 10 min — escribir `handoff.md` (esta plantilla)
- 10 min — enviar a SIMON

Regla: Si algo no entra en este handoff → no es tarea humana.

## 7. LO QUE SIMON DEBE HACER (y el humano NO)
SIMON debe:
- Reconstruir contexto desde fragmentos y normalizar timestamps.
- Detectar contradicciones y señalarlas con prioridad.
- Proponer estructura técnica y fragmentación para R001.

El humano solo valida o rechaza, no corrige línea por línea.

## 8. FRASE OPERATIVA PARA EL HUMANO (ancla cognitiva)
“No tengo que sostener el sistema. Solo tengo que pasar la posta correctamente.”

## 9. ESTADO ACTUAL (breve)
- Sistema: scaffold `neurobit_salon_v0.1` creado.
- Snippets: `storage/RING_PROCESOS/code_snippets` (77 archivos) — copiados.
- Sesión init: `SALA_SESION_001_INIT.txt` creado.

Acción recomendada ahora: cerrar ventanas → crear `handoff.md` → enviar a SIMON.

---
Archivo generado: `neurobit_salon_v0.1/storage/RING_REGISTRO/handoff.md`
Fecha: 2025-12-28
