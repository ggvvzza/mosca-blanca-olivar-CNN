# =============================================================
# Script de Preprocesamiento - Version 1
# Proyecto: Deteccion temprana de mosca blanca en olivos
# Lugar: Bosque El Olivar, San Isidro, Lima - Peru
# Autora: Gabriela Graciela Villegas Vasquez
# Universidad Nacional de Ingenieria - Maestria en IA
# =============================================================

import os
import logging
from pathlib import Path
import cv2
import numpy as np

# Configuracion de logging
logging.basicConfig(
    filename="logs/preprocesamiento.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Directorios
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
INFESTADAS_RAW = RAW_DIR / "infestadas"
SANAS_RAW = RAW_DIR / "sanas"
INFESTADAS_PROCESSED = PROCESSED_DIR / "infestadas"
SANAS_PROCESSED = PROCESSED_DIR / "sanas"

# Parametros de preprocesamiento
TAMANO_IMAGEN = (640, 640)
EXTENSIONES_VALIDAS = [".jpg", ".jpeg", ".png"]

def crear_directorios():
    """Crea los directorios de salida si no existen."""
    INFESTADAS_PROCESSED.mkdir(parents=True, exist_ok=True)
    SANAS_PROCESSED.mkdir(parents=True, exist_ok=True)
    logging.info("Directorios de salida creados correctamente.")

def preprocesar_imagen(ruta_entrada, ruta_salida):
    """Redimensiona y normaliza una imagen."""
    imagen = cv2.imread(str(ruta_entrada))
    if imagen is None:
        logging.warning(f"No se pudo cargar la imagen: {ruta_entrada}")
        return False
    imagen_redimensionada = cv2.resize(imagen, TAMANO_IMAGEN)
    cv2.imwrite(str(ruta_salida), imagen_redimensionada)
    logging.info(f"Imagen procesada: {ruta_salida}")
    return True

def procesar_directorio(dir_entrada, dir_salida):
    """Procesa todas las imagenes de un directorio."""
    imagenes = [
        f for f in Path(dir_entrada).iterdir()
        if f.suffix.lower() in EXTENSIONES_VALIDAS
    ]
    procesadas = 0
    for imagen in imagenes:
        ruta_salida = dir_salida / imagen.name
        if preprocesar_imagen(imagen, ruta_salida):
            procesadas += 1
    logging.info(f"Imagenes procesadas en {dir_entrada}: {procesadas}/{len(imagenes)}")
    print(f"Procesadas {procesadas} de {len(imagenes)} imagenes en {dir_entrada}")
    return procesadas

if __name__ == "__main__":
    crear_directorios()
    print("\n===== PREPROCESAMIENTO DEL DATASET =====")
    total_infestadas = procesar_directorio(INFESTADAS_RAW, INFESTADAS_PROCESSED)
    total_sanas = procesar_directorio(SANAS_RAW, SANAS_PROCESSED)
    print(f"\nTotal imagenes preprocesadas: {total_infestadas + total_sanas}")
    print("Imagenes guardadas en data/processed/")
    logging.info(f"Preprocesamiento completado. Total: {total_infestadas + total_sanas} imagenes.")
    print("=========================================\n")
