import pandas as pd
import os
import subprocess

UMBRAL_APROBACION = 100

def main():
    print("=======================================")
    print("  VALIDADOR DE CUARENTENA (AKINATOR)  ")
    print("=======================================\n")
    
    ruta_candidatos = 'data/datos_candidatos.csv'
    ruta_dataset = 'data/dataset_animales.csv'
    ruta_modelo = 'models/arbol_animales.joblib'
    
    if not os.path.exists(ruta_candidatos):
        print("No hay datos en cuarentena. ¡Todo limpio!")
        return
        
    df_candidatos = pd.read_csv(ruta_candidatos)
    
    if df_candidatos.empty:
        print("El archivo de cuarentena está vacío.")
        return
        
    # Agrupar por nombre de animal (etiqueta) y contar
    conteos = df_candidatos['etiqueta'].value_counts()
    
    animales_aprobados = conteos[conteos >= UMBRAL_APROBACION].index.tolist()
    
    if not animales_aprobados:
        print(f"Ningún animal ha alcanzado el umbral de {UMBRAL_APROBACION} reportes.")
        print("Estado actual de la cuarentena:")
        print(conteos)
        return
        
    print(f"¡Atención! Se han aprobado los siguientes animales: {animales_aprobados}")
    
    # Separar los aprobados de los que siguen en cuarentena
    df_aprobados = df_candidatos[df_candidatos['etiqueta'].isin(animales_aprobados)]
    df_restantes = df_candidatos[~df_candidatos['etiqueta'].isin(animales_aprobados)]
    
    # Añadir los aprobados al dataset principal
    if os.path.exists(ruta_dataset):
        df_principal = pd.read_csv(ruta_dataset)
        df_nuevo_principal = pd.concat([df_principal, df_aprobados], ignore_index=True)
        # Mezclar por si acaso
        df_nuevo_principal = df_nuevo_principal.sample(frac=1).reset_index(drop=True)
        df_nuevo_principal.to_csv(ruta_dataset, index=False)
        print(f"Se han inyectado {len(df_aprobados)} nuevos registros al dataset oficial.")
    else:
        print("Error: No se encontró el dataset principal para inyectar los datos.")
        return
        
    # Sobrescribir la cuarentena solo con los restantes
    if df_restantes.empty:
        os.remove(ruta_candidatos)
        print("La cuarentena ha quedado vacía.")
    else:
        df_restantes.to_csv(ruta_candidatos, index=False)
        print("Los animales no aprobados siguen en cuarentena.")
        
    # Borrar el modelo antiguo para forzar re-entrenamiento
    if os.path.exists(ruta_modelo):
        os.remove(ruta_modelo)
        print("Modelo antiguo eliminado.")
        
    # Llamar al script de entrenamiento
    print("\nIniciando re-entrenamiento automático...")
    subprocess.run(['python', 'src/train.py'])
    
    print("\n¡Proceso de validación completado con éxito!")

if __name__ == "__main__":
    main()
