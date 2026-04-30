import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
import matplotlib.pyplot as plt

def main():
    print("Comprobando modelo...")
    # Asegurarnos de que el directorio de modelos existe
    os.makedirs('models', exist_ok=True)
    
    ruta_modelo = 'models/arbol_animales.joblib'
    if os.path.exists(ruta_modelo):
        print(f"✔️  El modelo ya está entrenado y guardado en '{ruta_modelo}'. Saltando entrenamiento.")
        print("   (Si deseas re-entrenarlo, elimina el archivo y vuelve a ejecutar este script).")
        return
        
    # 1. Cargar los datos
    ruta_csv = 'data/dataset_animales.csv'
    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró el archivo {ruta_csv}. Ejecuta generate_data.py primero.")
        return
        
    df = pd.DataFrame(pd.read_csv(ruta_csv))
    
    # 2. Separar características (X) de la etiqueta (y)
    # Las columnas son: ['peso_kg', 'altura_cm', 'numero_patas', 'tiene_plumas', 'tiene_pelo', 'sabe_nadar', 'sabe_volar', 'pone_huevos', 'hace_ruido_fuerte', 'es_domestico', 'tiene_pico', 'es_ave_de_corral', 'etiqueta']
    X = df.drop(columns=['etiqueta'])
    y = df['etiqueta']
    
    # 3. Dividir en set de entrenamiento y prueba (80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Crear y entrenar el modelo
    print("Entrenando el Árbol de Decisión...")
    # max_depth=None o un número limita qué tan profundo puede pensar el árbol.
    # min_samples_split=2 asegura que no sobreajuste tanto.
    modelo = DecisionTreeClassifier(random_state=42, criterion='entropy')
    modelo.fit(X_train, y_train)
    
    # 5. Evaluar precisión
    y_pred = modelo.predict(X_test)
    precision = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo en el set de prueba: {precision * 100:.2f}%")
    
    # 6. Guardar el modelo entrenado
    joblib.dump(modelo, ruta_modelo)
    print(f"Modelo guardado exitosamente en: {ruta_modelo}")
    
    # Opcional: Mostrar las reglas que aprendió en texto
    print("\nResumen de las primeras reglas aprendidas:")
    reglas = export_text(modelo, feature_names=list(X.columns), max_depth=3)
    print(reglas)

if __name__ == "__main__":
    main()
