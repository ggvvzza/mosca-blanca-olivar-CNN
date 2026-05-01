# =============================================================
# Script de Ingesta - Version 1
# Proyecto: Deteccion temprana de mosca blanca en olivos
# Lugar: Bosque El Olivar, San Isidro, Lima - Peru
# Autora: Gabriela Graciela Villegas Vasquez
# Universidad Nacional de Ingenieria - Maestria en IA
# =============================================================

import os
import logging
from pathlib import Path

# Configuracion de logging
logging.basicConfig(
    filename="logs/ingesta.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Directorios del dataset
RAW_DIR = Path("data/raw")
INFESTADAS_DIR = RAW_DIR / "infestadas"
SANAS_DIR = RAW_DIR / "sanas"

# Extensiones validas
EXTENSIONES_VALIDAS = [".jpg", ".jpeg", ".png"]

def crear_estructura():
    """Crea la estructura de carpetas del dataset."""
    INFESTADAS_DIR.mkdir(parents=True, exist_ok=True)
    SANAS_DIR.mkdir(parents=True, exist_ok=True)
    logging.info("Estructura de carpetas creada correctamente.")
    print("Estructura de carpetas creada correctamente.")

def verificar_imagenes(directorio):
    """Verifica y lista las imagenes disponibles en un directorio."""
    imagenes = [
        f for f in Path(directorio).iterdir()
        if f.suffix.lower() in EXTENSIONES_VALIDAS
    ]
    logging.info(f"Directorio {directorio}: {len(imagenes)} imagenes encontradas.")
    print(f"Directorio: {directorio} — {len(imagenes)} imagenes encontradas.")
    return imagenes

def resumen_dataset():
    """Muestra un resumen del estado actual del dataset."""
    print("\n===== RESUMEN DEL DATASET =====")
    logging.info("Iniciando resumen del dataset.")
    infestadas = verificar_imagenes(INFESTADAS_DIR)
    sanas = verificar_imagenes(SANAS_DIR)
    total = len(infestadas) + len(sanas)
    print(f"Imagenes infestadas : {len(infestadas)}")
    print(f"Imagenes sanas      : {len(sanas)}")
    print(f"Total               : {total}")
    logging.info(f"Total de imagenes en dataset: {total}")
    print("================================\n")

if __name__ == "__main__":
    crear_estructura()
    resumen_dataset()
