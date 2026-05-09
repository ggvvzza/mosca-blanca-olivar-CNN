# Detección Temprana de Mosca Blanca en Olivos del Bosque El Olivar
## Universidad Nacional de Ingeniería – Maestría en IA
**Autora:** Gabriela Graciela Villegas Vasquez  
**Lugar:** Bosque El Olivar, San Isidro, Lima – Perú  
**Duración:** Mayo 2026 – Julio 2027

---

## ¿De qué trata este proyecto?

Estoy desarrollando mi tesis de maestría en la UNI. El objetivo es crear un sistema que pueda detectar automáticamente la mosca blanca (*Aleurothrixus floccosus*) en los olivos del Bosque El Olivar de San Isidro, usando inteligencia artificial y visión por computadora.

Trabajo en el Bosque El Olivar como especialista en cultivo de olivo, y vi que detectar esta plaga a tiempo es muy difícil porque hay que revisar árbol por árbol manualmente. Quiero que un modelo de IA pueda ayudar con eso.

---

## ¿Por qué es importante?

El Bosque El Olivar es un patrimonio histórico de Lima. No se pueden usar pesticidas fuertes ahí, así que hay que detectar la plaga temprano para aplicar control biológico a tiempo. Actualmente la detección se hace a ojo, lo cual depende mucho de la experiencia de la persona que revisa.

---

## ¿Qué estoy usando?

| Herramienta | Para qué la uso |
|-------------|-----------------|
| YOLOv8s | Modelo principal de detección |
| SAHI | Para detectar mejor objetos pequeños como la mosca blanca |
| PyTorch | Framework de deep learning |
| OpenCV | Procesamiento de imágenes |
| Raspberry Pi | Para probar el sistema en campo |
| Python | Lenguaje principal |

---

## ¿Cómo voy a evaluar si el modelo funciona bien?

| Métrica | Qué mide |
|---------|----------|
| mAP@0.5 | Precisión promedio del modelo |
| mAP@0.5:0.95 | Precisión en diferentes umbrales |
| Precision | Qué tan exactas son las detecciones |
| Recall | Cuántas plagas logra detectar |
| F1-score | Balance entre precisión y recall |
| Tiempo de inferencia (ms) | Si funciona en tiempo real en campo |

---

## Mis datos

Tomé las fotos yo misma en el Bosque El Olivar, con registro de georeferenciación. Las fotos fueron tomadas en diferentes horas del día y en diferentes posiciones de la hoja (alta, media y baja en el árbol).

**Estado actual del dataset:**
- Imágenes infestadas: 210
- Imágenes sanas: 27 (en proceso de captura)
- Total: 237 imágenes reales de campo

Como complemento, voy a usar imágenes públicas del dataset Pest Dataset V2 (Kaggle, autor: Ibrahima Gabar Diop, licencia CC0), solo la clase mosca blanca.

---

## Estructura del repositorio
mosca-blanca-olivar-CNN/
├── cuadernos/
│   ├── EDA_basico.ipynb
│   └── ingesta_dataset_v0.py
├── datos/
├── documentos/
├── registros/
├── resultados/
├── src/
└── LÉAME.md
## Cómo correr el notebook

1. Abrir Google Colab
2. Conectar Google Drive
3. Abrir `cuadernos/EDA_basico.ipynb`
4. Ejecutar todas las celdas

---

## Lo que ya hice

- ✅ Captura de 210 imágenes infestadas en campo
- ✅ Análisis exploratorio del dataset (EDA completo)
- ✅ Análisis de dimensiones y canales RGB
- ✅ Baseline con Regresión Logística
- ✅ Variante 1: HOG + SVM
- ✅ Variante 2: ResNet50 Transfer Learning
- ✅ Validación cruzada 5-Fold estratificado

## Lo que falta

- ⏳ Completar captura de imágenes sanas (meta: 100)
- ⏳ Etiquetado con bounding boxes
- ⏳ Entrenamiento YOLOv8s
- ⏳ Validación final y comparación con inspección visual

---

## Cronograma

| N° | Etapa | Periodo |
|----|-------|---------|
| 1 | Habilitación de equipos | Mayo 2026 |
| 2 | Diseño y planificación | Junio – Julio 2026 |
| 3 | Captura y preparación de datos | Julio – Agosto 2026 |
| 4 | Entrenamiento del modelo | Agosto 2026 |
| 5 | Validación experimental | Setiembre – Octubre 2026 |
| 6 | Análisis y documentación | Noviembre 2026 |
| 7 | Presentación y sustentación | Diciembre 2026 – Julio 2027 |

---

## Referencias

- Feng et al. (2024). Enhancing cotton whitefly detection with deep learning on Raspberry Pi. *Plant Methods*, 20(161).
- Tusubira et al. (2020). Improving cassava whitefly surveillance with machine learning. *CVPRW*.
- Chand et al. (2022). Detection of whitefly pests using image enhancement and machine learning. *IJAEE*, 10(102).
- Bellout et al. (2024). Advanced YOLO models for tomato leaf disease detection. *Mathematical Modeling and Computing*, 11(4).
- Zhang et al. (2023). Automatic pest identification in greenhouse using deep learning. *Frontiers in Plant Science*, 14.

---

**Autora:** Ing. Agrónoma Gabriela Graciela Villegas Vasquez  
**Especialista en Cultivo de Olivo – Bosque El Olivar, Municipalidad de San Isidro**  
**Maestría en Ciencias con Mención en Inteligencia Artificial – UNI**
