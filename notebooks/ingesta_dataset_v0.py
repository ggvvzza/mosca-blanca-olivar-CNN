# =============================================================
# Script de Ingesta de Dataset - Versión 0
# Proyecto: Detección temprana de mosca blanca en olivos
# Autora: Gabriela Graciela Villegas Vasquez
# Lugar: Bosque El Olivar, San Isidro, Lima - Perú
# =============================================================

import os
import shutil
from pathlib import Path

# Directorios del dataset
DATASET_DIR = Path("data")
INFESTADAS_DIR = DATASET_DIR / "infestadas"
SANAS_DIR = DATASET_DIR / "sanas"

# Extensiones de imagen aceptadas
EXTENSIONES_VALIDAS = [".jpg", ".jpeg", ".png"]

def crear_estructura():
    """Crea la estructura de carpetas del dataset."""
    INFESTADAS_DIR.mkdir(parents=True, exist_ok=True)
    SANAS_DIR.mkdir(parents=True, exist_ok=True)
    print("Estructura de carpetas creada correctamente.")

def verificar_imagenes(directorio):
    """Verifica y lista las imagenes disponibles en un directorio."""
    imagenes = [
        f for f in Path(directorio).iterdir()
        if f.suffix.lower() in EXTENSIONES_VALIDAS
    ]
    print(f"Directorio: {directorio}")
    print(f"Total de imagenes encontradas: {len(imagenes)}")
    for img in imagenes:
        print(f"  - {img.name}")
    return imagenes

def resumen_dataset():
    """Muestra un resumen del estado actual del dataset."""
    print("\n===== RESUMEN DEL DATASET =====")
    infestadas = verificar_imagenes(INFESTADAS_DIR)
    sanas = verificar_imagenes(SANAS_DIR)
    print(f"\nTotal imagenes infestadas: {len(infestadas)}")
    print(f"Total imagenes sanas: {len(sanas)}")
    print(f"Total general: {len(infestadas) + len(sanas)}")
    print("================================\n")

if __name__ == "__main__":
    crear_estructura()
    resumen_dataset()
