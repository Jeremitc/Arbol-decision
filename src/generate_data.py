import pandas as pd
import numpy as np
import os
import random

# Asegurarse de que el directorio data existe
os.makedirs('data', exist_ok=True)

# Configurar semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

ruta_csv = 'data/dataset_animales.csv'
if os.path.exists(ruta_csv):
    print(f"✔️  El dataset ya existe en '{ruta_csv}'. Saltando generación de datos para ahorrar tiempo.")
    print("   (Si deseas regenerarlo, elimina el archivo y vuelve a ejecutar este script).")
    exit(0)


# Clases de animales
animales = ['Perro', 'Gato', 'Paloma', 'Hamster', 'Cuy', 'Pato', 'Pollo', 'Pavo', 'Ganso']

# Definimos las reglas base para cada animal
# Formato: { 'Animal': { 'caracteristica': (media_peso, std_peso, media_altura, std_altura, patas, plumas, pelo, nadar, volar, huevos, ruido, domestico, pico, corral) } }
reglas = {
    'Perro':   {'peso': (15.0, 10.0), 'altura': (45.0, 20.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0},
    'Gato':    {'peso': (4.5, 1.5),   'altura': (25.0, 5.0),  'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0},
    'Paloma':  {'peso': (0.3, 0.1),   'altura': (20.0, 3.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0},
    'Hamster': {'peso': (0.15, 0.05), 'altura': (5.0, 2.0),   'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0},
    'Cuy':     {'peso': (0.9, 0.2),   'altura': (10.0, 2.0),  'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0},
    'Pato':    {'peso': (1.5, 0.5),   'altura': (30.0, 5.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1},
    'Pollo':   {'peso': (2.5, 0.5),   'altura': (40.0, 5.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1},
    'Pavo':    {'peso': (8.0, 2.0),   'altura': (80.0, 10.0), 'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1},
    'Ganso':   {'peso': (4.0, 1.0),   'altura': (60.0, 8.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1},
}

muestras_por_animal = 300 # Total = 2700 registros
datos = []

for animal, prop in reglas.items():
    for _ in range(muestras_por_animal):
        # Generar peso y altura con distribución normal para darle realismo
        peso = max(0.05, np.random.normal(prop['peso'][0], prop['peso'][1]))
        altura = max(2.0, np.random.normal(prop['altura'][0], prop['altura'][1]))
        
        # Ocasionalmente mutar alguna propiedad booleana para introducir ruido (1% de las veces)
        # Esto ayuda a que el árbol no memorice reglas perfectas
        nadar = prop['nadar'] if random.random() > 0.05 else (1 - prop['nadar'])
        
        datos.append([
            round(peso, 2),
            round(altura, 1),
            prop['patas'],
            prop['plumas'],
            prop['pelo'],
            nadar,
            prop['volar'],
            prop['huevos'],
            prop['ruido'],
            prop['domestico'],
            prop['pico'],
            prop['corral'],
            animal
        ])

columnas = [
    'peso_kg', 'altura_cm', 'numero_patas', 'tiene_plumas', 'tiene_pelo', 
    'sabe_nadar', 'sabe_volar', 'pone_huevos', 'hace_ruido_fuerte', 
    'es_domestico', 'tiene_pico', 'es_ave_de_corral', 'etiqueta'
]

df = pd.DataFrame(datos, columns=columnas)

# Mezclar las filas para que no estén ordenadas por animal
df = df.sample(frac=1).reset_index(drop=True)

# Guardar en CSV
df.to_csv(ruta_csv, index=False)

print(f"Dataset generado exitosamente en: {ruta_csv}")
print(f"Total de registros: {len(df)}")
print("Muestra de los datos:")
print(df.head())
