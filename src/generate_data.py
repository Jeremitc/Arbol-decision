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

# Clases de animales (34 animales en total)
animales = [
    'Perro', 'Gato', 'Paloma', 'Hamster', 'Cuy', 'Pato', 'Pollo', 'Pavo', 'Ganso',
    'Leon', 'Elefante', 'Jirafa', 'Tigre', 'Cebra', 'Mono', 'Cocodrilo', 'Rana',
    'Delfin', 'Ballena', 'Aguila', 'Pinguino', 'Avestruz', 'Vaca', 'Caballo', 'Cerdo', 'Oveja',
    'Tiburon', 'Cangrejo', 'Camaron', 'Lobo', 'Capibara', 'Tortuga', 'Araña', 'Caracol'
]

# Definimos las reglas base para cada animal (100% Booleano - 27 características)
reglas = {
    'Perro':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Gato':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Paloma':   {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Hamster':  {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 1, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Cuy':      {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 1, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Pato':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Pollo':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Pavo':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Ganso':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 1, 'pico': 1, 'corral': 1, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    
    'Leon':     {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Elefante': {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 1, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Jirafa':   {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 1, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Tigre':    {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 1, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Cebra':    {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 1, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Mono':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Cocodrilo':{'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Rana':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Delfin':   {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 1, 'insecto_crustaceo': 0, 'comestible': 0},
    'Ballena':  {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 1, 'insecto_crustaceo': 0, 'comestible': 0},
    'Aguila':   {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 1, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Pinguino': {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 1, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 1, 'insecto_crustaceo': 0, 'comestible': 0},
    'Avestruz': {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 1, 'plumas': 1, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 1, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Vaca':     {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 1, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Caballo':  {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 1, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Cerdo':    {'es_muy_pesado': 1, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Oveja':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 0, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 1, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    
    # NUEVOS ANIMALES
    'Tiburon':  {'es_muy_pesado': 1, 'es_muy_grande': 1, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 1, 'insecto_crustaceo': 0, 'comestible': 1},
    'Cangrejo': {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 1, 'aletas': 0, 'insecto_crustaceo': 1, 'comestible': 1},
    'Camaron':  {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 1, 'aletas': 0, 'insecto_crustaceo': 1, 'comestible': 1},
    'Lobo':     {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 1, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 0},
    'Capibara': {'es_muy_pesado': 0, 'es_muy_grande': 1, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 1, 'nadar': 1, 'volar': 0, 'huevos': 0, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 1, 'roedor': 1, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Tortuga':  {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 1, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 1, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 1, 'pico': 1, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 1, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 1, 'aletas': 0, 'insecto_crustaceo': 0, 'comestible': 1},
    'Araña':    {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 1, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 1, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 0, 'aletas': 0, 'insecto_crustaceo': 1, 'comestible': 0},
    'Caracol':  {'es_muy_pesado': 0, 'es_muy_grande': 0, 'tiene_4_patas': 0, 'tiene_2_patas': 0, 'plumas': 0, 'pelo': 0, 'nadar': 0, 'volar': 0, 'huevos': 1, 'ruido': 0, 'domestico': 0, 'pico': 0, 'corral': 0, 'carnivoro': 0, 'rayas': 0, 'trompa': 0, 'cuello_largo': 0, 'trepar': 0, 'reptil_anfibio': 0, 'manchas': 0, 'manada': 0, 'roedor': 0, 'carga': 0, 'caparazon': 1, 'aletas': 0, 'insecto_crustaceo': 1, 'comestible': 1},
}

muestras_por_animal = 300 # Total = 34 * 300 = 10,200 registros
datos = []

for animal, prop in reglas.items():
    for _ in range(muestras_por_animal):
        # Mutaciones leves para forzar generalización
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
            prop['caparazon'],
            prop['aletas'],
            prop['insecto_crustaceo'],
            prop['comestible'],
            animal
        ])

columnas = [
    'es_muy_pesado', 'es_muy_grande', 'tiene_4_patas', 'tiene_2_patas',
    'tiene_plumas', 'tiene_pelo', 'sabe_nadar', 'sabe_volar', 'pone_huevos', 
    'hace_ruido_fuerte', 'es_domestico', 'tiene_pico', 'es_ave_de_corral', 
    'es_carnivoro', 'tiene_rayas', 'tiene_trompa', 'tiene_cuello_largo', 
    'sabe_trepar_arboles', 'es_reptil_o_anfibio', 'tiene_manchas', 
    'vive_en_manada', 'es_roedor', 'es_animal_de_carga',
    'tiene_caparazon_o_exosqueleto', 'tiene_aletas', 'es_insecto_o_crustaceo', 'es_comestible',
    'etiqueta'
]

df = pd.DataFrame(datos, columns=columnas)
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(ruta_csv, index=False)

print(f"Dataset Booleano V2 (34 animales) generado exitosamente en: {ruta_csv}")
print(f"Total de registros: {len(df)}")
print(f"Número de características: {len(columnas)-1}")
