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

def main():
    limpiar_consola()
    print("=======================================")
    print("  EL ÁRBOL ADIVINADOR DE ANIMALES  ")
    print("=======================================")
    print("¡Responderé tus preguntas e intentaré adivinarlo!")
    print("=======================================\n")
    
    ruta_modelo = 'models/arbol_animales.joblib'
    if not os.path.exists(ruta_modelo):
        print(f"Error: No se encontró el modelo en {ruta_modelo}.")
        print("Asegúrate de ejecutar train.py primero.")
        return
        
    modelo = joblib.load(ruta_modelo)
    
    print("Responde las siguientes preguntas sobre tu animal (Solo S/N):\n")
    es_muy_pesado = hacer_pregunta_bool("1. ¿Es un animal muy pesado (más de 100 KG en su edad adulta)?")
    es_muy_grande = hacer_pregunta_bool("2. ¿Es un animal muy grande o largo (mide más de 1 metro)?")
    tiene_4_patas = hacer_pregunta_bool("3. ¿Tiene 4 patas?")
    if tiene_4_patas == 1:
        tiene_2_patas = 0
    else:
        tiene_2_patas = hacer_pregunta_bool("4. ¿Tiene 2 patas?")
    tiene_plumas = hacer_pregunta_bool("5. ¿Tiene plumas?")
    if tiene_plumas == 1:
        tiene_pelo = 0
    else:
        tiene_pelo = hacer_pregunta_bool("6. ¿Tiene pelo/pelaje?")
    sabe_nadar = hacer_pregunta_bool("7. ¿Sabe nadar o vive gran parte del tiempo en el agua?")
    sabe_volar = hacer_pregunta_bool("8. ¿Sabe volar?")
    pone_huevos = hacer_pregunta_bool("9. ¿Pone huevos?")
    hace_ruido = hacer_pregunta_bool("10. ¿Hace ruidos fuertes (como ladridos, graznidos, rugidos, etc)?")
    es_domestico = hacer_pregunta_bool("11. ¿Es un animal comúnmente doméstico/mascota?")
    tiene_pico = hacer_pregunta_bool("12. ¿Tiene pico?")
    es_corral = hacer_pregunta_bool("13. ¿Es un ave comúnmente criada en corrales/granjas?")
    
    # Preguntas para mayor inteligencia
    es_carnivoro = hacer_pregunta_bool("14. ¿Es un animal estrictamente carnívoro o depredador?")
    tiene_rayas = hacer_pregunta_bool("15. ¿Su cuerpo tiene un patrón de rayas visible (ej: tigre, cebra)?")
    tiene_trompa = hacer_pregunta_bool("16. ¿Tiene una trompa larga?")
    tiene_cuello_largo = hacer_pregunta_bool("17. ¿Se caracteriza por tener un cuello inusualmente largo?")
    sabe_trepar = hacer_pregunta_bool("18. ¿Es conocido por trepar árboles ágilmente?")
    reptil_anfibio = hacer_pregunta_bool("19. ¿Es un reptil o anfibio?")
    tiene_manchas = hacer_pregunta_bool("20. ¿Tiene un patrón de manchas distintivas (ej: vaca, jirafa)?")
    vive_en_manada = hacer_pregunta_bool("21. ¿Suele vivir o cazar en manada/rebaño?")
    es_roedor = hacer_pregunta_bool("22. ¿Es un roedor?")
    es_carga = hacer_pregunta_bool("23. ¿Es comúnmente usado como animal de carga o transporte (ej: caballo)?")

    print("\nAnalizando tus respuestas...")
    time.sleep(1.5)
    
    columnas = [
        'es_muy_pesado', 'es_muy_grande', 'tiene_4_patas', 'tiene_2_patas',
        'tiene_plumas', 'tiene_pelo', 'sabe_nadar', 'sabe_volar', 'pone_huevos', 
        'hace_ruido_fuerte', 'es_domestico', 'tiene_pico', 'es_ave_de_corral', 
        'es_carnivoro', 'tiene_rayas', 'tiene_trompa', 'tiene_cuello_largo', 
        'sabe_trepar_arboles', 'es_reptil_o_anfibio', 'tiene_manchas', 
        'vive_en_manada', 'es_roedor', 'es_animal_de_carga'
    ]
    
    datos_usuario = [[
        es_muy_pesado, es_muy_grande, tiene_4_patas, tiene_2_patas,
        tiene_plumas, tiene_pelo, sabe_nadar, sabe_volar, pone_huevos, hace_ruido, 
        es_domestico, tiene_pico, es_corral,
        es_carnivoro, tiene_rayas, tiene_trompa, tiene_cuello_largo,
        sabe_trepar, reptil_anfibio, tiene_manchas,
        vive_en_manada, es_roedor, es_carga
    ]]
    
    df_prediccion = pd.DataFrame(datos_usuario, columns=columnas)
    prediccion = modelo.predict(df_prediccion)[0]
    
    print("=======================================")
    print(f" ¡EL ÁRBOL DICE QUE ESTÁS PENSANDO EN UN... {prediccion.upper()}! ")
    print("=======================================\n")
    
    # --- SISTEMA DE FEEDBACK Y CUARENTENA ---
    acierto = hacer_pregunta_bool("¿Adiviné correctamente?")
    if acierto == 0:
        animal_real = input("¡Vaya! ¿En qué animal estabas pensando? (Escribe el nombre): ").strip().capitalize()
        
        fila_cuarentena = datos_usuario[0] + [animal_real]
        columnas_csv = columnas + ['etiqueta']
        df_nuevo = pd.DataFrame([fila_cuarentena], columns=columnas_csv)
        
        ruta_candidatos = 'data/datos_candidatos.csv'
        
        if not os.path.exists(ruta_candidatos):
            df_nuevo.to_csv(ruta_candidatos, index=False)
        else:
            df_nuevo.to_csv(ruta_candidatos, mode='a', header=False, index=False)
            
        print(f"\n¡Gracias! He anotado que esas características corresponden a un '{animal_real}'.")
        print("He enviado este registro a la CUARENTENA de datos.")
        print("Si muchos usuarios reportan lo mismo, aprenderé a predecirlo en el futuro.")
    else:
        print("\n¡Genial! Soy invencible gracias a mis datos puramente booleanos.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n¡Juego cancelado! Hasta la próxima.")
