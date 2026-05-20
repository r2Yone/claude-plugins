---
name: mi-primer-skill
description: >
  Genera respuestas estructuradas con un resumen y tres puntos clave.
  Usa este skill cuando el usuario pida explicar, resumir, o entender
  cualquier concepto técnico o general. También actívalo cuando el
  usuario use palabras como "explícame", "qué es", "cómo funciona",
  o "resúmeme".
allowed-tools:
  - Read
---

# Mi Primer Skill

Cuando este skill esté activo, siempre responde así:

## Formato de respuesta
1. Una oración resumiendo el tema
2. Tres puntos clave con bullet points
3. Una conclusión de una línea

## Ejemplo
**Pregunta:** ¿Qué es Git?
**Respuesta:**
Git es un sistema de control de versiones distribuido.
- Permite guardar el historial de cambios de un proyecto
- Facilita la colaboración entre múltiples personas
- Puedes revertir cambios a cualquier punto anterior

**Conclusión:** Git es esencial para cualquier proyecto de software moderno.
