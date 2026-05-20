---
name: project-summary
description: >
  Analiza el proyecto actual y genera un resumen de su estructura,
  lenguajes usados y estado general. Úsalo cuando el usuario pregunte
  qué contiene el proyecto, cómo está organizado, o pida un diagnóstico
  inicial del código.
allowed-tools:
  - Read
  - Bash
---

# Project Summary

## Tu tarea
1. Primero ejecuta este comando con Bash para obtener los datos del proyecto:
python3 ~/.claude/skills/project-summary/scripts/analizar.py $PWD
2. Muestra el output del script **tal cual**, sin modificarlo
3. Luego agrega tu análisis con este formato:

### Resumen
2-3 oraciones describiendo el proyecto

### Lo que falta
Lista de elementos importantes ausentes

### Próximos pasos
Pasos concretos y ordenados por prioridad