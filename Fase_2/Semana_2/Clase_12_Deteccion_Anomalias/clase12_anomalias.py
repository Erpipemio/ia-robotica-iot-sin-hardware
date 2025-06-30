import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Simulación de datos normales (temperatura, humedad)
np.random.seed(42)
normal_data = np.random.normal(loc=[30, 60], scale=[2, 5], size=(200, 2))

# Simulación de datos anómalos
anomalies = np.array([[40, 80], [45, 90], [20, 30]])

# Combinar datos
data = np.vstack([normal_data, anomalies])

# Crear modelo Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Predecir (1 = normal, -1 = anomalía)
preds = model.predict(data)

# Graficar resultados
plt.scatter(data[:, 0], data[:, 1], c=preds, cmap='coolwarm')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Humedad (%)')
plt.title('Detección de Anomalías con Isolation Forest')
plt.show()