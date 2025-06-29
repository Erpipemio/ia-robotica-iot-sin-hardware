# Clase 10 – Alertas Inteligentes con Python

Este proyecto simula un sistema de monitoreo ambiental que genera alertas cuando se superan ciertos umbrales de temperatura o humedad.

## 🎯 Objetivo
Aprender a:
- Leer datos simulados de sensores
- Detectar valores críticos (umbrales)
- Ejecutar respuestas automáticas (mensajes, sonido)

## 🐍 Requisitos
- Python 3.x
- (Opcional Windows): `winsound` para alertas sonoras

## 🚀 Ejecución

```bash
python alertas_inteligentes.py
```

## ⚠ Umbrales usados

- Temperatura > 32 °C → 🔥 Alerta con sonido (solo Windows)
- Humedad > 65 % → 💧 Alerta visual

## 📁 Archivos

- `alertas_inteligentes.py`: Script principal
- `README.md`: Este archivo