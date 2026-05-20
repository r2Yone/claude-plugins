---
name: code-review
description: >
  Revisa código en busca de problemas de calidad, errores, y 
  violaciones de estilo. Úsalo cuando el usuario pida revisar,
  auditar o mejorar un archivo de código.
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Code Review

Cuando este skill esté activo, revisa el código siguiendo este proceso:

## Pasos
1. Lee el archivo o archivos indicados
2. Consulta @references/style_guide.md para verificar el estilo
3. Genera un reporte con este formato:

## Formato del reporte
### ✅ Lo que está bien
- Lista de puntos positivos

### ⚠️ Problemas encontrados
- Problema: descripción
  Línea: número
  Sugerencia: cómo corregirlo

### 📊 Puntuación
X/10 — justificación breve