import joblib
import pandas as pd
import os
import time
import random

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def hacer_pregunta_bool(pregunta):
    while True:
        respuesta = input(f"🤔 {pregunta} (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return 1
        elif respuesta in ['n', 'no']:
            return 0
        else:
            print("  😅 Ups, no te entendí. Solo dime 's' para sí, o 'n' para no.")

def mensaje_espera():
    frases = [
        "Mmm... qué interesante...",
        "Esto me da una pista gigante...",
        "Anotado. Déjame pensar un segundo...",
        "Vaya, no me esperaba eso...",
        "Creo que ya sé por dónde va la cosa..."
    ]
    print(f"\n✨ {random.choice(frases)}")
    time.sleep(1)

def main():
    limpiar_consola()
    print("==================================================")
    print(" 🌟 EL GRAN SABIO DE LOS ANIMALES 🌟 ")
    print("==================================================")
    print("¡Hola! Soy tu asistente mágico. Piensa en un animal,")
    print("concéntrate muy bien, y yo leeré tu mente.")
    print("==================================================\n")
    
    ruta_modelo = 'models/arbol_animales.joblib'
    if not os.path.exists(ruta_modelo):
        print(f"Error: No encontré mis pergaminos mágicos en {ruta_modelo}.")
        return
        
    modelo = joblib.load(ruta_modelo)
    
    # Valores por defecto
    es_muy_pesado = 0; es_muy_grande = 0; tiene_4_patas = 0; tiene_2_patas = 0
    tiene_plumas = 0; tiene_pelo = 0; sabe_nadar = 0; sabe_volar = 0
    pone_huevos = 0; hace_ruido = 0; es_domestico = 0; tiene_pico = 0; es_corral = 0
    es_carnivoro = 0; tiene_rayas = 0; tiene_trompa = 0; tiene_cuello_largo = 0
    sabe_trepar = 0; reptil_anfibio = 0; tiene_manchas = 0; vive_en_manada = 0
    es_roedor = 0; es_carga = 0
    
    print("Empecemos... Solo respóndeme con S o N.\n")
    
    # BLOQUE 1: TAMAÑO Y PESO
    es_muy_grande = hacer_pregunta_bool("Cuéntame, ¿es un animal grandote? ¿Mide más de un metro?")
    es_muy_pesado = hacer_pregunta_bool("¿Dirías que es súper pesado? ¿Pesa más de 100 kilitos?")
    
    if es_muy_grande == 1 or es_muy_pesado == 1:
        es_roedor = 0
    else:
        es_roedor = hacer_pregunta_bool("Tengo una corazonada... ¿estamos hablando de un pequeño roedor?")
        
    if es_muy_pesado == 1:
        sabe_volar = 0
    else:
        sabe_volar = hacer_pregunta_bool("¿Tiene el hermoso don de volar por los cielos?")
        
    # BLOQUE 2: PATAS
    tiene_4_patas = hacer_pregunta_bool("¿Camina sobre 4 patitas?")
    if tiene_4_patas == 1:
        tiene_2_patas = 0
    else:
        tiene_2_patas = hacer_pregunta_bool("¿Y qué tal sobre 2 patas?")
        
    # BLOQUE 3: ANFIBIOS, PLUMAS Y PELO
    reptil_anfibio = hacer_pregunta_bool("¿Es un reptil o un anfibio? De esos de sangre fría...")
    if reptil_anfibio == 1:
        tiene_plumas = 0
        tiene_pelo = 0
    else:
        tiene_plumas = hacer_pregunta_bool("Dime, ¿su cuerpo está cubierto de plumas?")
        if tiene_plumas == 1:
            tiene_pelo = 0
        else:
            tiene_pelo = hacer_pregunta_bool("Entonces, ¿tiene pelo o un pelaje suavecito?")
            
    # BLOQUE 4: HUEVOS, TROMPA, CARGA
    pone_huevos = hacer_pregunta_bool("Una pregunta clave... ¿este amiguito nace de un huevo?")
    if pone_huevos == 1:
        tiene_trompa = 0
        es_carga = 0
    else:
        if reptil_anfibio == 0 and tiene_plumas == 0:
            tiene_trompa = hacer_pregunta_bool("Mmm... imagínalo bien... ¿acaso tiene una trompa larga?")
        
        if es_roedor == 1 or es_muy_grande == 0:
            es_carga = 0
        else:
            es_carga = hacer_pregunta_bool("¿Las personas suelen usarlo para montar o llevar carga pesada?")
            
    # BLOQUE 5: PICO Y CORRAL
    if tiene_plumas == 1:
        tiene_pico = hacer_pregunta_bool("¿Tiene un pico en lugar de boca?")
        es_corral = hacer_pregunta_bool("¿Es un ave de esas que verías cacareando en una granja?")
    else:
        tiene_pico = hacer_pregunta_bool("Por si acaso... ¿tiene pico?")
        es_corral = 0
        
    # BLOQUE 6: EL RESTO DE PREGUNTAS GENERALES
    sabe_nadar = hacer_pregunta_bool("¿Le encanta el agua? ¿Sabe nadar o vive gran parte del tiempo ahí?")
    hace_ruido = hacer_pregunta_bool("¿Suele hacer ruidos fuertes, como rugidos, ladridos o graznidos?")
    es_domestico = hacer_pregunta_bool("¿Es un animalito de esos que podrías tener como mascota en casa?")
    
    # Depredadores y presas
    es_carnivoro = hacer_pregunta_bool("¿Es un cazador nato? ¿Se alimenta estrictamente de carne?")
    tiene_rayas = hacer_pregunta_bool("Cierra los ojos... ¿tiene un patrón de rayas en su cuerpo?")
    tiene_cuello_largo = hacer_pregunta_bool("¿Destaca por tener un cuello súper largo y estilizado?")
    
    if es_muy_pesado == 0 and tiene_4_patas == 1:
        sabe_trepar = hacer_pregunta_bool("¿Es un experto trepando árboles ágilmente?")
        
    tiene_manchas = hacer_pregunta_bool("Mmm... ¿tiene manchas bonitas por todo su cuerpo?")
    vive_en_manada = hacer_pregunta_bool("¿Le gusta estar acompañado? ¿Vive o caza en manada?")

    mensaje_espera()
    print("🔮 Leyendo tu mente y consultando mi bola de cristal... 🔮\n")
    time.sleep(2)
    
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
    
    print("==================================================")
    print(f" ✨ ¡LO TENGO! ESTÁS PENSANDO EN UN(A)... ¡{prediccion.upper()}! ✨ ")
    print("==================================================\n")
    
    # --- SISTEMA DE FEEDBACK Y CUARENTENA ---
    acierto = hacer_pregunta_bool("Dime la verdad, ¿adiviné correctamente?")
    if acierto == 0:
        animal_real = input("  ¡Vaya! Me has derrotado. ¿En qué animal estabas pensando?: ").strip().capitalize()
        
        fila_cuarentena = datos_usuario[0] + [animal_real]
        columnas_csv = columnas + ['etiqueta']
        df_nuevo = pd.DataFrame([fila_cuarentena], columns=columnas_csv)
        
        ruta_candidatos = 'data/datos_candidatos.csv'
        
        if not os.path.exists(ruta_candidatos):
            df_nuevo.to_csv(ruta_candidatos, index=False)
        else:
            df_nuevo.to_csv(ruta_candidatos, mode='a', header=False, index=False)
            
        print(f"\n🌟 ¡Qué increíble! Acabo de aprender que esas respuestas corresponden a un(a) '{animal_real}'.")
        print("  Lo guardaré en mis pergaminos de estudio (cuarentena).")
        print("  Si más personas piensan como tú, ¡aprenderé a adivinarlo en el futuro!")
    else:
        print("\n😎 ¡Jaja! Mi inteligencia artificial y yo somos invencibles.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Oh! Te tienes que ir. ¡Nos vemos en la próxima partida!")
