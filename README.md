# El Gran Sabio de los Animales 🌳🔮

Este es un proyecto educativo de Machine Learning que utiliza un **Árbol de Decisión (DecisionTreeClassifier)** para adivinar en qué animal estás pensando en base a un interrogatorio dinámico e inteligente estilo "Akinator".

El modelo es capaz de predecir entre **34 animales diferentes** (mamíferos, reptiles, aves, crustáceos e insectos) cruzando 27 características booleanas (Sí/No).

## Características Destacadas
- **Inteligencia Deductiva**: El juego no te hace las 27 preguntas de corrido. Posee un motor de lógica interno (`if/else` inteligentes) que autocompleta respuestas obvias. (Ej: Si le dices que es un *bicho*, deduce automáticamente que no tiene *pelo*, no mide *1 metro*, ni pesa *100 kg*).
- **Dataset Masivo**: Genera un dataset de más de **10,200 registros** aplicando un 2% de "ruido" (mutaciones aleatorias) en el entrenamiento para que el modelo no solo memorice, sino que generalice.
- **Lógica 100% Booleana**: Adiós a los números ambiguos. El jugador solo debe responder con `s` (Sí) o `n` (No).
- **Sistema de Cuarentena (Aprendizaje)**: Si el modelo se equivoca o le ganas, guarda tus respuestas y el animal en un archivo `datos_candidatos.csv` para que los desarrolladores puedan revisar los "fallos" e inyectar ese conocimiento en un futuro reentrenamiento.

## Requisitos
- Python 3.11.x (Recomendado gestionarlo con `pyenv`).
- Las librerías están listadas en `requirements.txt`.

## Instalación

1. **Clonar o entrar al repositorio:**
   ```bash
   cd "arbol decision"
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   # En Windows:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # En Linux/Mac:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Flujo de Trabajo (Cómo usarlo)

El proyecto se divide en 3 scripts principales ubicados en la carpeta `src/`. Deben ejecutarse en orden:

### 1. Generar la Base de Conocimiento
Genera el dataset booleano en la carpeta `data/` cruzando a los 34 animales con sus 27 características y aplicando el margen de error probabilístico.
```bash
python src/generate_data.py
```

### 2. Entrenar a la Bestia Matemática
Lee el CSV de 10,200 registros, entrena el Árbol de Decisión usando el 80% de los datos y exporta el "cerebro" (`.joblib`) a la carpeta `models/`.
```bash
python src/train.py
```

### 3. ¡Desafiar al Sabio! (Jugar)
Inicia la consola interactiva donde el sistema leerá tu mente haciéndote preguntas amigables.
```bash
python src/juego.py
```

### 4. (Opcional) Sistema de Cuarentena
Si los usuarios reportaron fallos o animales no adivinados (los cuales se guardan en `data/datos_candidatos.csv`), puedes usar el validador para auditar esa nueva data antes de integrarla oficialmente al generador principal.
```bash
python src/validador.py
```

## Estructura de Carpetas
- `/data`: Datasets generados y archivos de cuarentena.
- `/models`: El cerebro entrenado (`.joblib`).
- `/src`: Scripts fuente (Generador, Entrenador, Juego, Validador).

---
*Desarrollado para explorar el poder de la Lógica Booleana y los Árboles de Decisión de Scikit-Learn de manera lúdica.*
