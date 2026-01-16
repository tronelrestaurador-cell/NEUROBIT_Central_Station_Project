# 📡 Guía de Uso: Estación Central - Versión Progresiva

**Bienvenido, Deb** 🌟

Esta es tu Estación Central, un lugar seguro y hermoso para registrar tus mensajes dentro de la red NEUROBIT. Es como tener tu propio cuaderno digital, pero conectado a un sistema más grande.

---

## 🚀 Inicio Rápido (5 minutos)

### Paso 1: Abre el archivo
Abre el archivo `interface/station_progresivo.html` en tu navegador favorito (Chrome, Firefox, Edge, Safari).

### Paso 2: Rellena tu información
- **Tu Nombre o Identidad**: Escribe cómo quieres ser llamado (ej: "Deb", "TRON", "EVA")
- **Sesión**: Déjalo en `SALA_001` si es tu primer mensaje
- **Mensaje**: Escribe lo que quieras compartir

### Paso 3: Presiona "🚀 Enviar Mensaje"
¡Listo! Tu mensaje se guardará automáticamente.

### Paso 4: Vélo en el historial
Todos tus mensajes aparecerán en la sección "📜 Historial" abajo.

---

## 🎯 Conceptos Clave

### ¿Qué es un "Mensaje NEUROBIT"?

Cada mensaje que envías contiene información especial:

```
┌─ PROTOCOLO: v0.1 (reglas que seguimos)
├─ MESSAGE_ID: identificador único (como tu huella dactilar)
├─ ORIGEN: quién lo envió (tú)
├─ TIMESTAMP: cuándo se envió (preciso al segundo)
├─ CONTENT: lo que escribiste
└─ HASH: firma matemática que prueba que es auténtico
```

**¿Para qué sirve?** Asegura que tu mensaje sea:
- ✅ Original (nadie lo modificó)
- ✅ Identificable (sabemos que fuiste tú)
- ✅ Trazable (quedó registrado para siempre)

---

## 📝 Cómo Usar Cada Función

### 1. **Tu Nombre o Identidad**
```
Escribe: Deb
Escribe: TRON
Escribe: La Hermosa Mía
```
Este es tu "origen". Será visible en todos tus mensajes.

**💡 Consejo**: Usa el mismo nombre en todos tus mensajes para mantener coherencia.

---

### 2. **Sesión**
```
Por defecto: SALA_001
Puedes cambiar a: SALA_ESPECIAL, SALA_TRON_001, etc.
```

**¿Qué significa?** Es como tener diferentes cuadernos:
- Una sesión para notas rápidas
- Otra para ideas importantes
- Otra para comunicación con agentes

**💡 Consejo**: Mantén `SALA_001` si es tu primer contacto.

---

### 3. **Mensaje**
```
Escribe cualquier cosa:
- Ideas
- Preguntas
- Instrucciones
- Reflexiones
- Historias
```

**Límite**: 25,000 caracteres (¡muchísimo!)

**Validación en Vivo** (mientras escribes):
- ✅ Protocolo OK: Se valida automáticamente
- ✅ Hash: Se calcula en tiempo real
- ✅ Longitud: Ve cuántos caracteres llevas

---

### 4. **🚀 Enviar Mensaje**
Presiona cuando hayas terminado. El sistema:
1. Valida que esté todo correcto ✅
2. Calcula la firma (hash SIMON) 🔐
3. Lo guarda localmente 💾
4. Intenta enviarlo a la Central (si está disponible) 🌐

---

### 5. **🗑️ Limpiar**
Borra el formulario si quieres empezar de nuevo.

---

## 📜 El Historial

### ¿Qué veo aquí?
- Todos tus mensajes ordenados de más nuevo a más viejo
- Quién lo envió (ORIGEN)
- Cuándo se envió (HORA)
- Primeras palabras del contenido (preview)

### Interactuar con el Historial
- **Click en un mensaje**: Muestra el texto completo
- **Número #**: Orden en que fue enviado

### Botones del Historial

#### 💾 Exportar Historial
Descarga todos tus mensajes en un archivo `.json` para:
- Hacer backup (copia de seguridad)
- Compartir con otros
- Analizar después

#### 🧹 Limpiar Historial
**⚠️ CUIDADO**: Borra TODO tu historial. No se puede deshacer.

Solo usa si estás seguro.

---

## 🔐 Seguridad y Privacidad

### Tu Información Está Guardada En:

**NIVEL 1: Tu Navegador** 🖥️
- Se guarda automáticamente en "localStorage"
- Nadie la ve excepto tú
- Persiste aunque cierres la ventana

**NIVEL 2: Arca Central** 📡 (si hay conexión)
- Se intenta enviar a la Estación Central
- Queda registrado en la red NEUROBIT
- Permanece para siempre

**NIVEL 3: Tu Exportación** 💾
- Puedes descargar tu historial
- Guardarlo en tu computadora
- Hacer backup en USB o nube

---

## 🟢 Indicadores de Estado

### En la esquina superior derecha:

**🟢 Conectado**
- La Estación Central está disponible
- Tu mensaje también se envía a Arca

**🔴 Desconectado (modo local)**
- La Central no está accesible
- Tu mensaje se guarda localmente
- Puedes exportarlo después

---

## 💡 Consejos Prácticos

### Escribir Mensajes Efectivos

**✅ HACES:**
```
Mensaje claro, con propósito definido.
"Hoy reflexioné sobre la coherencia en el código"
```

**❌ NO HAGAS:**
```
Demasiado corto (sin contenido):
"hola"
```

```
Demasiado técnico si es tu primer mensaje:
"∫[λ.coherencia]² dθ = ∞ en Logos"
```

### Usar Diferentes Identidades

Si quieres experimentar:
```
Mensaje 1: Identidad = "Deb"
Mensaje 2: Identidad = "TRON" 
Mensaje 3: Identidad = "Hermosa Mía"
```

Cada una quedará registrada por separado.

### Sesiones Temáticas

```
SALA_001 → Mensajes cotidianos
SALA_REFLEXION → Ideas importantes
SALA_COLABORACION → Trabajo con otros
```

---

## 🔍 Validación SIMON Explicada

Cuando escribes, ves esta información:

```
✓ Protocolo: NEUROBIT v2.1
✓ Hash SIMON: a3f4b2c1d5e6...
✓ Longitud: 150/25000 caracteres
```

### ¿Qué significan?

**Protocolo NEUROBIT v2.1**
- Significa que tu mensaje sigue las reglas establecidas
- Es compatible con la red
- Otros pueden leerlo correctamente

**Hash SIMON**
- Es una "firma digital" de tu mensaje
- Se calcula a partir del contenido
- Si alguien modifica el mensaje, el hash cambia
- Sirve para detectar cambios no autorizados

**Longitud**
- Cuántos caracteres llevas
- Máximo: 25,000 (casi un artículo completo)
- Si ves ⚠️ amarillo, estás cerca del límite

---

## 🚀 Próximas Versiones (Próximamente)

### Fase 2: "Con Validación Visual"
- Verás el hash calculándose
- Indicadores más coloridos
- Más detalles de validación

### Fase 3: "Dashboard Profesional"
- Panel lateral con agentes (SIMON, EVA, TRON)
- Ver a quién se enviaron tus mensajes
- Estadísticas de entrega

### Fase 4: "Neuronal Visual"
- Visualización gráfica de la red
- Ver cómo se distribuyen tus mensajes
- Interfaz artística

---

## ❓ Preguntas Frecuentes

### P: ¿Mis mensajes se pierden si cierro el navegador?
**R**: No. Se guardan en localStorage (tu navegador recuerda). Pero si limpias el caché del navegador, sí se pierden. ¡Por eso exporta regularmente! 💾

### P: ¿Puedo editar un mensaje después de enviarlo?
**R**: No directamente. Pero en fases posteriores habrá un sistema de "enmiendas". Por ahora, si cometes un error, envía un mensaje nuevo diciendo "corrección al anterior".

### P: ¿Qué pasa si la Central no está disponible?
**R**: No te preocupes. Tu mensaje se guarda localmente (Nivel 1). Cuando la Central vuelva online, puedes exportar y sincronizar manualmente.

### P: ¿Puedo ver mensajes de otros?
**R**: En esta Fase 1, solo ves TUS mensajes. En Fase 3 (Dashboard) podrás ver entregas confirmadas.

### P: ¿Es seguro?
**R**: Sí. Tu navegador es seguro si es tu computadora personal. Los mensajes se validan criptográficamente. La Central usa protocolo v2.1 que está estudiado.

### P: ¿Debo poner información real?
**R**: Puedes usar un alias. "Deb", "TRON", "La Hermosa Mía"... lo importante es mantenerlo consistente.

---

## 🆘 Solución de Problemas

### El botón "Enviar" no funciona
**Causas**:
1. Falta llenar "Tu Nombre" → Rellena ese campo
2. Falta escribir un mensaje → Escribe en el área de texto
3. El mensaje es muy largo → Acórtalo

### No aparece el historial
**Causas**:
1. Es tu primer uso → Envía tu primer mensaje
2. Borraste el historial → Crea uno nuevo
3. El navegador no permite localStorage → Usa otro navegador

### El hash no calcula
**Causa**: Tu navegador no soporta SHA-1 (poco probable)
**Solución**: Actualiza tu navegador

### No puedo exportar
**Causa**: No hay mensajes
**Solución**: Escribe y envía al menos un mensaje primero

---

## 📖 Glosario

| Término | Significado |
|---------|------------|
| **Arca** | Base de datos central donde se guardan todos los mensajes |
| **Envelope** | Contenedor de tu mensaje con metadata (protocolo, hash, etc.) |
| **SIMON** | Validador que asegura coherencia en el protocolo |
| **Hash** | Firma digital que identifica tu mensaje |
| **UUID** | Identificador único universal (como una huella dactilar) |
| **localStorage** | Almacenamiento en tu navegador |
| **Sesión** | Grupo de mensajes relacionados temáticamente |

---

## 🎓 Aprendizaje Progresivo

### Semana 1: Lo Básico
- [ ] Escribe 5 mensajes diferentes
- [ ] Experimenta con diferentes identidades
- [ ] Exporta tu historial (como backup)

### Semana 2: Exploración
- [ ] Prueba diferentes sesiones
- [ ] Lee el hash y entiende qué significa
- [ ] Comparte tu historial con alguien

### Semana 3: Maestría
- [ ] Cuando salga Fase 2, explora validación visual
- [ ] Cuando salga Fase 3, conecta con agentes
- [ ] Diseña tu propio flujo de trabajo

---

## 🙏 Conclusión

Bienvenido a la Estación Central, Deb.

Esta es tu puerta de entrada a la red NEUROBIT.

Lo que escribes aquí:
- ✅ Es seguro
- ✅ Es válido
- ✅ Es permanente
- ✅ Es tuyo

Úsalo sabiamente. Úsalo creativamente. Úsalo con coherencia.

**El Logos necesita tus palabras.**

---

**Creado con coherencia**  
*Estación Central - Versión Progresiva*  
*16 de enero de 2026*

---

## 📞 Soporte

Si algo no funciona:
1. Abre la consola del navegador (F12)
2. Mira si hay mensajes de error (en rojo)
3. Reporta el problema con captura de pantalla

**Consola en diferentes navegadores:**
- Chrome/Edge: `F12` → Pestaña "Console"
- Firefox: `F12` → Pestaña "Console"
- Safari: `Cmd+Option+I` → "Console"

---

¡Que disfrutes tu viaje en la red NEUROBIT! 🚀
