# Árbol de Decisión: Adivinador de Animales 🌳🔮

Este es un proyecto educativo de Machine Learning que utiliza un **Árbol de Decisión** para predecir un animal (Perro, Gato, Paloma, Hamster, Cuy, Pato, Pollo, Pavo, Ganso) en base a sus características físicas.

Está compuesto por un dataset sintético rico en variaciones para que el modelo no solo memorice, sino que aprenda a generalizar, y cuenta con un script interactivo en la terminal estilo "Akinator" para poner a prueba el árbol entrenado.

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

### 1. Generar los datos
Genera un archivo CSV en la carpeta `data/` con miles de ejemplos de animales aplicando ligeras variaciones (mutaciones) en su peso, altura y características para dar realismo al dataset.
```bash
python src/generate_data.py
```

### 2. Entrenar el Modelo
Lee el CSV generado, entrena un clasificador `DecisionTreeClassifier` usando el 80% de los datos y guarda el modelo inteligente en la carpeta `models/`. Imprime la precisión y algunas de las reglas aprendidas por el árbol.
```bash
python src/train.py
```

### 3. ¡Jugar!
Inicia el script interactivo que te hará preguntas sobre el animal en el que estás pensando. Responderás con `s/n` o números, y al final, el modelo de Machine Learning intentará adivinar de qué animal se trata.
```bash
python src/juego.py
```

## Estructura de Carpetas
- `/data`: Contiene los datasets generados.
- `/models`: Contiene el modelo de Machine Learning exportado (`.joblib`).
- `/src`: Contiene los scripts fuente.

---
*Desarrollado para fines de aprendizaje de estructuras lógicas de Árboles de Decisión.*
