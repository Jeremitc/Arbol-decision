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

# Clases de animales (26 animales en total)
animales = [
    'Perro', 'Gato', 'Paloma', 'Hamster', 'Cuy', 'Pato', 'Pollo', 'Pavo', 'Ganso',
    'Leon', 'Elefante', 'Jirafa', 'Tigre', 'Cebra', 'Mono', 'Cocodrilo', 'Rana',
    'Delfin', 'Ballena', 'Aguila', 'Pinguino', 'Avestruz', 'Vaca', 'Caballo', 'Cerdo', 'Oveja'
]

# Definimos las reglas base para cada animal (100% Booleano)
# Columnas antiguas numericas eliminadas (peso, altura, patas)
# Nuevas columnas booleanas: es_muy_pesado, es_muy_grande, tiene_4_patas, tiene_2_patas
reglas = {
    'Perro':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Gato':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Paloma':   {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Hamster':  {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 1, 'carga': 0},
    'Cuy':      {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 1, 'carga': 0},
    'Pato':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Pollo':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Pavo':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Ganso':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    
    'Leon':     {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Elefante': {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 1, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Jirafa':   {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 1, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Tigre':    {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 1, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Cebra':    {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 1, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Mono':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Cocodrilo':{'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Rana':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Delfin':   {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Ballena':  {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Aguila':   {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Pinguino': {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Avestruz': {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Vaca':     {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 1, 'manada': 1, 'roedor': 0, 'carga': 0},
    'Caballo':  {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 1},
    'Cerdo':    {'es_muy_pesado': 1, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0},
    'Oveja':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0},
}

muestras_por_animal = 300 # Total = 26 * 300 = 7800 registros
datos = []

for animal, prop in reglas.items():
    for _ in range(muestras_por_animal):
        # Mutaciones leves en algunas variables booleanas para crear ruido y forzar al modelo a generalizar
        # El 2% de las veces, un animal podria tener una mutacion (ej: una vaca sin manchas, un caballo solitario)
        
        datos.append([
            prop['es_muy_pesado'] if random.random() > 0.02 else (1 - prop['es_muy_pesado']),
            prop['es_muy_grande'] if random.random() > 0.02 else (1 - prop['es_muy_grande']),
            prop['tiene_4_patas'],
            prop['tiene_2_patas'],
            prop['plumas'],
            prop['pelo'],
            prop['nadar'] if random.random() > 0.02 else (1 - prop['nadar']),
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
            prop['manchas'] if random.random() > 0.02 else (1 - prop['manchas']),
            prop['manada'] if random.random() > 0.02 else (1 - prop['manada']),
            prop['roedor'],
            prop['carga'],
            animal
        ])

columnas = [
    'es_muy_pesado', 'es_muy_grande', 'tiene_4_patas', 'tiene_2_patas',
    'tiene_plumas', 'tiene_pelo', 'sabe_nadar', 'sabe_volar', 'pone_huevos', 
    'hace_ruido_fuerte', 'es_domestico', 'tiene_pico', 'es_ave_de_corral', 
    'es_carnivoro', 'tiene_rayas', 'tiene_trompa', 'tiene_cuello_largo', 
    'sabe_trepar_arboles', 'es_reptil_o_anfibio', 'tiene_manchas', 
    'vive_en_manada', 'es_roedor', 'es_animal_de_carga', 'etiqueta'
]

df = pd.DataFrame(datos, columns=columnas)
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(ruta_csv, index=False)

print(f"Dataset 100% Booleano generado exitosamente en: {ruta_csv}")
print(f"Total de registros: {len(df)}")
print(f"Número de características booleanas: {len(columnas)-1}")
