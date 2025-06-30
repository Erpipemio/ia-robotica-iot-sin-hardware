import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Cargar datos de entrenamiento
df = pd.read_csv(
    "c:/Users/Dy2g_/Documents/GitHub/ia-robotica-iot-sin-hardware/Fase_2/Semana_2/Clase_13_IA_CSV_KNN/data.csv")

# Separar variables y etiqueta
X = df[["temperatura", "humedad"]]
y = df["estado"]

# Crear y entrenar modelo
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# Simular nuevos datos
nuevos = pd.DataFrame({
    "temperatura": [30, 40, 34, 28],
    "humedad": [60, 85, 68, 55]
})

# Predecir
predicciones = modelo.predict(nuevos)
nuevos["prediccion"] = predicciones

# Mostrar resultados
print(nuevos)

# Visualización
plt.scatter(X["temperatura"], X["humedad"], c=y,
            cmap='coolwarm', label="Entrenamiento")
plt.scatter(nuevos["temperatura"], nuevos["humedad"],
            c=predicciones, cmap='coolwarm', marker='x', label="Nuevos")
plt.xlabel("Temperatura")
plt.ylabel("Humedad")
plt.legend()
plt.title("Clasificación de datos con IA (KNN)")
plt.show()
