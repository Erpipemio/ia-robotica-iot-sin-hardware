# Clase 12 – Detección de Anomalías con IA (Simulada)

Este proyecto aplica el modelo `Isolation Forest` para detectar valores fuera de lo común en datos simulados de sensores.

## 🎯 Objetivo

- Simular datos normales y anómalos
- Aplicar un modelo de IA sin supervisión
- Visualizar resultados con colores

## 🐍 Requisitos

- numpy
- matplotlib
- scikit-learn

Instala con:

```bash
pip install numpy matplotlib scikit-learn
```

## 🚀 Ejecución

```bash
python clase12_anomalias.py
```

Aparecerá un gráfico con los puntos normales y los que el modelo considera anómalos.

## 💡 Detalles

- Modelo usado: `IsolationForest`
- `contamination=0.05` significa que espera un 5% de anomalías