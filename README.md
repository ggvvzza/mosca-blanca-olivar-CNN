# Detección Temprana de Mosca Blanca en Olivos del Bosque El Olivar mediante Visión Artificial

**Universidad Nacional de Ingeniería – Unidad de Postgrado FIIS**  
**Maestría en Ciencias con Mención en Inteligencia Artificial**  
**Autora:** Gabriela Graciela Villegas Vasquez  
**Lugar de estudio:** Bosque El Olivar, Distrito de San Isidro, Lima – Perú  
**Duración estimada:** mayo 2026 – diciembre 2027

## Descripción del Proyecto

Este proyecto de investigación propone el diseño de un sistema de visión artificial basado en Redes Neuronales Convolucionales (CNN) para la detección temprana de la mosca blanca (*Aleurothrixus floccosus*) en olivos (*Olea europaea*) del Bosque El Olivar de San Isidro, Lima – Perú.

El Bosque El Olivar es un ecosistema urbano patrimonial sujeto a restricciones estrictas en el uso de productos químicos de síntesis. La detección temprana automatizada de plagas permite optimizar las estrategias de control biológico y preservar el equilibrio ecológico del bosque urbano.

---

## Objetivos

### Objetivo General

Diseñar un sistema de visión artificial basado en redes neuronales convolucionales (CNN) para la detección temprana de la mosca blanca (*Aleurothrixus floccosus*) en olivos (*Olea europaea*) del Bosque El Olivar, Lima – Perú.

### Objetivos Específicos

- Construir un conjunto de datos de imágenes de hojas de olivo con y sin presencia de mosca blanca, capturadas en condiciones reales de campo.
- Identificar y analizar características visuales relevantes asociadas a infestaciones tempranas.
- Entrenar y evaluar un modelo YOLOv8s mediante transferencia de aprendizaje.
- Comparar el desempeño del sistema propuesto con el diagnóstico visual tradicional.
- Evaluar la viabilidad de replicar el sistema en otros espacios verdes urbanos.

- ## Planteamiento del Problema

La identificación actual de mosca blanca en el Bosque El Olivar se basa en inspecciones visuales manuales realizadas por personal técnico en campo. Este enfoque presenta limitaciones vinculadas a la subjetividad del observador, la variabilidad en la experiencia del evaluador y la dificultad para detectar infestaciones en estadios tempranos, cuando los síntomas visibles aún no son evidentes.

La detección tardía incrementa el riesgo de expansión poblacional de la plaga y retrasa la liberación oportuna de controladores biológicos, que constituye una de las principales estrategias permitidas dentro del Bosque El Olivar. Existe, por tanto, una brecha tecnológica entre las necesidades reales del manejo fitosanitario urbano y las herramientas actualmente disponibles.

## Tecnologías Utilizadas


| Herramienta | Uso |
|---|---|
| YOLOv8s | Modelo principal de detección de objetos en tiempo real |
| SAHI (Slicing Aided Hyper Inference) | Mejora de detección de objetos pequeños en imágenes grandes |
| PyTorch | Framework de aprendizaje profundo |
| OpenCV | Procesamiento y análisis de imágenes |
| Raspberry Pi | Implementación en campo de bajo costo |
| Python | Lenguaje de programación principal |

## Métricas de Evaluación


El modelo será evaluado con las siguientes métricas estándar en detección de objetos:

| Métrica | Descripción |
|---|---|
| mAP@0.5 | Precisión promedio al umbral de IoU = 0.5 |
| mAP@0.5:0.95 | Precisión promedio en múltiples umbrales de IoU |
| Precisión | Exactitud de las detecciones realizadas por el sistema |
| Recall | Capacidad del modelo para detectar la totalidad de plagas presentes |
| F1-score | Balance entre precisión y recall |
| Tiempo de inferencia (ms) | Viabilidad del sistema para aplicaciones en tiempo real en campo |

## Cronograma


| N° | Etapa | Actividades Principales | Periodo |
|---|---|---|---|
| 1 | Habilitación de equipo y herramientas | Listado de materiales y herramientas de trabajo | Octubre 2026 |
| 2 | Diseño y planificación | Revisión bibliográfica, diseño del pipeline de datos y arquitectura del modelo | Octubre – Noviembre 2026 |
| 3 | Colecta y preparación de datos | Toma de imágenes en campo, etiquetado, preprocesamiento y aumento de datos | Diciembre 2026 – Enero 2027 |
| 4 | Implementación del modelo | Entrenamiento de YOLOv8s con SAHI, ajuste de hiperparámetros, pruebas iniciales | Febrero – Marzo 2027 |
| 5 | Validación experimental | Evaluación con K-Fold, bootstrapping y comparación con inspección visual | Abril – Mayo 2027 |
| 6 | Análisis y documentación | Interpretación de resultados, redacción de capítulos, elaboración de conclusiones | Junio 2027 |
| 7 | Presentación y sustentación | Revisión y preparación del informe final | Julio 2027 |

## Metodología


La investigación se enmarca en un enfoque de investigación tecnológica aplicada, con una metodología híbrida que combina principios de Agile+AI para la gestión iterativa del desarrollo y prácticas de MLOps (Machine Learning Operations) para integrar, validar y desplegar el modelo de manera eficiente y reproducible.

El pipeline de datos comprende las siguientes etapas:

1. **Captura de imágenes en campo:** hojas de olivo con y sin presencia de mosca blanca, en condiciones reales del Bosque El Olivar, incluyendo variaciones de iluminación, sombra y orientación.
2. **Preprocesamiento:** redimensionamiento, normalización y control de calidad de imágenes.
3. **Anotación:** etiquetado manual mediante cajas delimitadoras (bounding boxes).
4. **Aumento de datos:** rotación, variación de brillo, contraste y técnica de mosaico.
5. **Entrenamiento:** YOLOv8s con transferencia de aprendizaje y complemento SAHI.
6. **Validación:** partición Hold-out (entrenamiento / validación / prueba).

## Referencias Bibliográficas

- Feng, Z., Wang, N., Jin, Y., Cao, H., Huang, X., Wen, S., & Ding, M. (2024). Enhancing cotton whitefly (*Bemisia tabaci*) detection and counting with a cost-effective deep learning approach on the Raspberry Pi. *Plant Methods*, 20(161).
- Tusubira, J. F., Nsumba, S., Ninsiima, F., Akera, B., Acellam, G., Nakatumba, J., Mwebaze, E., Quinn, J., & Oyana, T. (2020). Improving in-field cassava whitefly pest surveillance with machine learning. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*, 1–10.
- Chand, L., Dhiman, A. S., & Singh, S. (2022). Detection of whitefly pests in crops employing image enhancement and machine learning. *International Journal of Advanced Technology and Engineering Exploration*, 10(102), 569–579.
- Bellout, A., Zarboubi, M., Dliou, A., Latif, R., & Saddik, A. (2024). Advanced YOLO models for real-time detection of tomato leaf diseases. *Mathematical Modeling and Computing*, 11(4), 1198–1210.
- Zhang, X., Bu, J., Zhou, X., & Wang, X. (2023). Automatic pest identification system in the greenhouse based on deep learning and machine vision. *Frontiers in Plant Science*, 14, 1255719.

---

## Autora

Ing. Agrónoma Gabriela Graciela Villegas Vasquez  
Especialista en Cultivo de Olivo – Bosque El Olivar, Municipalidad de San Isidro  
Maestría en Ciencias con Mención en Inteligencia Artificial – Universidad Nacional de Ingeniería  

---

*Estado actual del proyecto: Fase de planificación y diseño — Inicio de ejecución: Octubre 2026*
7. ## Dataset

Las imágenes han sido capturadas directamente en el Bosque El Olivar, con registro de georreferenciación, en condiciones reales de campo, considerando variación de iluminación y diferentes posiciones de hoja en el árbol: alta, media y baja.

*Dataset en construcción — inicio de colecta programado: Diciembre 2026*
## Autores

| Nombre | Usuario GitHub | Correo |
|---|---|---|
| Gabriela Graciela Villegas Vasquez | @ggvvzza | ggvvzza@gmail.com |

---

## Requisitos

Para ejecutar el pipeline se requiere Python 3.8 o superior. Las dependencias del proyecto se instalan con:
Las principales dependencias son:

- ultralytics (YOLOv8)
- opencv-python
- torch
- torchvision
- sahi
- Pillow
- matplotlib
- numpy

---

## Como ejecutar el pipeline

1. **Ingesta de datos**
Organiza y verifica las imagenes disponibles en data/raw/

2. **Preprocesamiento**
Redimensiona, normaliza y filtra imagenes. Guarda resultados en data/processed/

3. **Exploracion inicial**

Abrir y ejecutar el notebook notebooks/EDA_basico.ipynb

4. **Entrenamiento del modelo**
5. Entrena YOLOv8s con transferencia de aprendizaje sobre el dataset etiquetado.

---

## Resultados esperados

El pipeline genera los siguientes resultados minimos:

- Resumen estadistico del dataset: numero de imagenes por clase, distribucion de tamaños
- Graficas de distribucion de imagenes infestadas vs sanas
- Metricas iniciales del modelo: precision, recall, F1-score y mAP@0.5
- Logs de entrenamiento guardados en logs/

*Resultados disponibles a partir de: Abril 2027*
## Requisitos

Para ejecutar el pipeline se requiere Python 3.8 o superior. Las principales dependencias son:

- ultralytics (YOLOv8)
- opencv-python
- torch
- torchvision
- sahi
- Pillow
- matplotlib
- numpy

Para instalar todas las dependencias ejecutar:

    pip install -r requirements.txt
    ## Como ejecutar el pipeline

1. Ingesta de datos

        python src/ingesta.py

Organiza y verifica las imagenes disponibles en data/raw/

2. Preprocesamiento

        python src/preprocesamiento.py

Redimensiona, normaliza y filtra imagenes. Guarda resultados en data/processed/

3. Exploracion inicial

Abrir y ejecutar el notebook notebooks/EDA_basico.ipynb

4. Entrenamiento del modelo

        python src/entrenamiento_yolov8.py

Entrena YOLOv8s con transferencia de aprendizaje sobre el dataset etiquetado.
## Resultados esperados

El pipeline genera los siguientes resultados minimos:

- Resumen estadistico del dataset: numero de imagenes por clase y distribucion de tamaños
- Graficas de distribucion de imagenes infestadas vs sanas
- Metricas iniciales del modelo: precision, recall, F1-score y mAP@0.5
- Logs de entrenamiento guardados en logs/

*Resultados disponibles a partir de: Abril 2027*
