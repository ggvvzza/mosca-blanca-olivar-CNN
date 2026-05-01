Pega este código:
python# =============================================================
# Script de Baseline - Version 1
# Proyecto: Deteccion temprana de mosca blanca en olivos
# Lugar: Bosque El Olivar, San Isidro, Lima - Peru
# Autora: Gabriela Graciela Villegas Vasquez
# Universidad Nacional de Ingenieria - Maestria en IA
# =============================================================

import os
import logging
import numpy as np
from pathlib import Path
from PIL import Image
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split

# Configuracion de logging
logging.basicConfig(
    filename="logs/baseline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Directorios
PROCESSED_DIR = Path("data/processed")
INFESTADAS_DIR = PROCESSED_DIR / "infestadas"
SANAS_DIR = PROCESSED_DIR / "sanas"

# Parametros
TAMANO_IMAGEN = (64, 64)
EXTENSIONES_VALIDAS = [".jpg", ".jpeg", ".png"]

def cargar_imagenes(directorio, etiqueta):
    """Carga imagenes y asigna etiqueta."""
    imagenes = []
    etiquetas = []
    for ruta in Path(directorio).iterdir():
        if ruta.suffix.lower() in EXTENSIONES_VALIDAS:
            try:
                img = Image.open(ruta).convert("RGB").resize(TAMANO_IMAGEN)
                imagenes.append(np.array(img).flatten())
                etiquetas.append(etiqueta)
            except Exception as e:
                logging.warning(f"Error al cargar {ruta}: {e}")
    return imagenes, etiquetas

def entrenar_baseline():
    """Entrena y evalua un modelo baseline DummyClassifier."""
    print("\n===== ENTRENAMIENTO BASELINE =====")
    logging.info("Iniciando entrenamiento baseline.")

    X_infestadas, y_infestadas = cargar_imagenes(INFESTADAS_DIR, 1)
    X_sanas, y_sanas = cargar_imagenes(SANAS_DIR, 0)

    X = np.array(X_infestadas + X_sanas)
    y = np.array(y_infestadas + y_sanas)

    print(f"Total imagenes cargadas: {len(X)}")
    print(f"Infestadas: {sum(y == 1)} | Sanas: {sum(y == 0)}")
    logging.info(f"Dataset cargado: {len(X)} imagenes.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    modelo = DummyClassifier(strategy="most_frequent")
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    print("\n--- Reporte de clasificacion ---")
    print(classification_report(y_test, y_pred, target_names=["Sana", "Infestada"]))

    f1 = f1_score(y_test, y_pred, average="weighted")
    print(f"F1-score baseline: {f1:.4f}")
    logging.info(f"F1-score baseline: {f1:.4f}")

    print("\nBaseline completado. Resultados guardados en logs/baseline.log")
    print("===================================\n")

if __name__ == "__main__":
    entrenar_baseline()
