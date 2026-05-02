import pandas as pd
import numpy as np
import os
import random

# Asegurarse de que el directorio data existe
os.makedirs('data', exist_ok=True)

# Configurar semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

# Si existe, lo sobreescribiremos porque estamos cambiando la estructura (más columnas)
ruta_csv = 'data/dataset_animales.csv'

# Clases de animales (26 animales en total)
animales = [
    'Perro', 'Gato', 'Paloma', 'Hamster', 'Cuy', 'Pato', 'Pollo', 'Pavo', 'Ganso',
    'Leon', 'Elefante', 'Jirafa', 'Tigre', 'Cebra', 'Mono', 'Cocodrilo', 'Rana',
    'Delfin', 'Ballena', 'Aguila', 'Pinguino', 'Avestruz', 'Vaca', 'Caballo', 'Cerdo', 'Oveja'
]

# Definimos las reglas base para cada animal
# Columnas: peso, altura, patas, plumas, pelo, nadar, volar, huevos, ruido, domestico, pico, corral
# NUEVAS: carnivoro, rayas, trompa, cuello_largo, trepar, reptil_anfibio, manchas, manada, roedor, carga
reglas = {
    'Perro':    {'peso': (15.0, 10.0), 'altura': (45.0, 20.0),  'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Gato':     {'peso': (4.5, 1.5),   'altura': (25.0, 5.0),   'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Paloma':   {'peso': (0.3, 0.1),   'altura': (20.0, 3.0),   'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Hamster':  {'peso': (0.15, 0.05), 'altura': (5.0, 2.0),    'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 1, 'carga': 0},
    'Cuy':      {'peso': (0.9, 0.2),   'altura': (10.0, 2.0),   'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 1, 'carga': 0},
    'Pato':     {'peso': (1.5, 0.5),   'altura': (30.0, 5.0),   'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Pollo':    {'peso': (2.5, 0.5),   'altura': (40.0, 5.0),   'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Pavo':     {'peso': (8.0, 2.0),   'altura': (80.0, 10.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Ganso':    {'peso': (4.0, 1.0),   'altura': (60.0, 8.0),   'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    
    'Leon':     {'peso': (190.0, 30.0), 'altura': (120.0, 15.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Elefante': {'peso': (4000.0, 1000.0), 'altura': (300.0, 50.0), 'patas': 4, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 1, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Jirafa':   {'peso': (1200.0, 200.0), 'altura': (500.0, 50.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 1, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Tigre':    {'peso': (220.0, 40.0), 'altura': (100.0, 15.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 1, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Cebra':    {'peso': (350.0, 50.0), 'altura': (130.0, 10.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 1, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Mono':     {'peso': (20.0, 10.0),  'altura': (60.0, 20.0),  'patas': 2, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Cocodrilo':{'peso': (400.0, 100.0), 'altura': (40.0, 10.0), 'patas': 4, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Rana':     {'peso': (0.05, 0.02),  'altura': (5.0, 2.0),   'patas': 4, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Delfin':   {'peso': (150.0, 30.0), 'altura': (200.0, 40.0), 'patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Ballena':  {'peso': (30000.0, 5000.0), 'altura': (1500.0, 300.0), 'patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Aguila':   {'peso': (5.0, 1.5),   'altura': (80.0, 15.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Pinguino': {'peso': (20.0, 5.0),  'altura': (90.0, 15.0),  'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Avestruz': {'peso': (100.0, 20.0), 'altura': (210.0, 30.0), 'patas': 2, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Vaca':     {'peso': (700.0, 150.0), 'altura': (150.0, 20.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 1, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Caballo':  {'peso': (500.0, 100.0), 'altura': (160.0, 20.0), 'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 1},
    'Cerdo':    {'peso': (150.0, 50.0), 'altura': (80.0, 15.0),  'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Oveja':    {'peso': (60.0, 15.0),  'altura': (90.0, 10.0),  'patas': 4, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
}

muestras_por_animal = 300 # Total = 26 * 300 = 7800 registros
datos = []

for animal, prop in reglas.items():
    for _ in range(muestras_por_animal):
        peso = max(0.01, np.random.normal(prop['peso'][0], prop['peso'][1]))
        altura = max(1.0, np.random.normal(prop['altura'][0], prop['altura'][1]))
        
        # Ocasionalmente mutar alguna propiedad booleana para introducir ruido (5% de las veces)
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
            prop['carnivoro'],
            prop['rayas'],
            prop['trompa'],
            prop['cuello_largo'],
            prop['trepar'],
            prop['reptil_anfibio'],
            prop['manchas'],
            prop['manada'],
            prop['roedor'],
            prop['carga'],
            animal
        ])

columnas = [
    'peso_kg', 'altura_cm', 'numero_patas', 'tiene_plumas', 'tiene_pelo', 
    'sabe_nadar', 'sabe_volar', 'pone_huevos', 'hace_ruido_fuerte', 
    'es_domestico', 'tiene_pico', 'es_ave_de_corral', 
    'es_carnivoro', 'tiene_rayas', 'tiene_trompa', 'tiene_cuello_largo', 
    'sabe_trepar_arboles', 'es_reptil_o_anfibio', 'tiene_manchas', 
    'vive_en_manada', 'es_roedor', 'es_animal_de_carga', 'etiqueta'
]

df = pd.DataFrame(datos, columns=columnas)
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(ruta_csv, index=False)

print(f"Dataset masivo generado exitosamente en: {ruta_csv}")
print(f"Total de registros: {len(df)}")
print(f"Número de características: {len(columnas)-1}")
