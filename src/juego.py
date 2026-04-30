import joblib
import pandas as pd
import os
import time

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def hacer_pregunta_bool(pregunta):
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return 1
        elif respuesta in ['n', 'no']:
            return 0
        else:
            print("Por favor responde con 's' o 'n'.")

def hacer_pregunta_num(pregunta, tipo=float):
    while True:
        respuesta = input(f"{pregunta}: ").strip()
        try:
            valor = tipo(respuesta)
            return valor
        except ValueError:
            print(f"Por favor ingresa un número válido.")

def main():
    limpiar_consola()
    print("=======================================")
    print("  EL ÁRBOL ADIVINADOR DE ANIMALES  ")
    print("=======================================")
    print("Piensa en uno de estos animales:")
    print("[Perro, Gato, Paloma, Hamster, Cuy, Pato, Pollo, Pavo, Ganso]")
    print("¡Responderé tus preguntas e intentaré adivinarlo!")
    print("=======================================\n")
    
    ruta_modelo = 'models/arbol_animales.joblib'
    if not os.path.exists(ruta_modelo):
        print(f"Error: No se encontró el modelo en {ruta_modelo}.")
        print("Asegúrate de ejecutar train.py primero.")
        return
        
    # Cargar el modelo
    modelo = joblib.load(ruta_modelo)
    
    # Hacer las preguntas
    print("Responde las siguientes preguntas sobre tu animal:\n")
    peso_kg = hacer_pregunta_num("1. ¿Cuál es su peso aproximado en KG? (ej: 4.5, 0.2, 15)")
    altura_cm = hacer_pregunta_num("2. ¿Cuál es su altura/longitud aproximada en CM? (ej: 25, 45, 10)")
    numero_patas = hacer_pregunta_num("3. ¿Cuántas patas tiene?", tipo=int)
    tiene_plumas = hacer_pregunta_bool("4. ¿Tiene plumas?")
    tiene_pelo = hacer_pregunta_bool("5. ¿Tiene pelo/pelaje?")
    sabe_nadar = hacer_pregunta_bool("6. ¿Sabe nadar en el agua?")
    sabe_volar = hacer_pregunta_bool("7. ¿Sabe volar (vuelos largos o medios)?")
    pone_huevos = hacer_pregunta_bool("8. ¿Pone huevos?")
    hace_ruido = hacer_pregunta_bool("9. ¿Hace ruidos fuertes (como ladridos, graznidos, cantos)?")
    es_domestico = hacer_pregunta_bool("10. ¿Es un animal comúnmente doméstico/mascota?")
    tiene_pico = hacer_pregunta_bool("11. ¿Tiene pico?")
    es_corral = hacer_pregunta_bool("12. ¿Es un ave comúnmente criada en corrales/granjas?")
    
    print("\nAnalizando tus respuestas...")
    time.sleep(1.5)
    
    # Crear el DataFrame con los nombres exactos de las columnas usadas en entrenamiento
    columnas = [
        'peso_kg', 'altura_cm', 'numero_patas', 'tiene_plumas', 'tiene_pelo', 
        'sabe_nadar', 'sabe_volar', 'pone_huevos', 'hace_ruido_fuerte', 
        'es_domestico', 'tiene_pico', 'es_ave_de_corral'
    ]
    
    datos_usuario = [[
        peso_kg, altura_cm, numero_patas, tiene_plumas, tiene_pelo, 
        sabe_nadar, sabe_volar, pone_huevos, hace_ruido, 
        es_domestico, tiene_pico, es_corral
    ]]
    
    df_prediccion = pd.DataFrame(datos_usuario, columns=columnas)
    
    # Predecir
    prediccion = modelo.predict(df_prediccion)
    
    print("=======================================")
    print(f" ¡EL ÁRBOL DICE QUE ESTÁS PENSANDO EN UN... {prediccion[0].upper()}! ")
    print("=======================================\n")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n¡Juego cancelado! Hasta la próxima.")
