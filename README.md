# Detección Temprana de Mosca Blanca en Olivos del Bosque El Olivar
## Tesis de Maestría en IA - UNI | Gabriela Graciela Villegas Vasquez

---

## Estado del Proyecto - Semana 5

### Dataset
| Clase | Imágenes | Estado |
|-------|----------|--------|
| Infestadas | 210 | ✅ Completo |
| Sanas | 27 | ✅ Cargadas (parcial) |
| **Total** | **237** | En progreso |

### EDA Completado
- ✅ Conteo y distribución de clases
- ✅ Análisis de dimensiones (402x537px promedio)
- ✅ Visualización de muestras (9 imágenes)
- ✅ Análisis de canales RGB
- ✅ Riesgos identificados (desbalance, heterogeneidad, variabilidad lumínica)

### Experimentos - Semana 5
| Modelo | Precision | Recall | F1 | Accuracy |
|--------|-----------|--------|----|----------|
| Baseline (DummyClassifier) | 1.00* | 1.00* | 1.00* | 1.00* |
| Baseline (Reg. Logística) | 0.87 | 0.93 | 0.90 | 0.93 |
| Variante 1 (HOG + SVM) | Pendiente | Pendiente | Pendiente | Pendiente |
| Variante 2 (ResNet50) | Pendiente | Pendiente | Pendiente | Pendiente |

*Resultado esperado con dataset de una sola clase.

### Riesgos Identificados
1. **Desbalance de clases**: 210 infestadas vs 0 sanas → captura en progreso
2. **Tamaño heterogéneo**: 128px a 408px → estandarizar a 640x640px
3. **Variabilidad de iluminación**: fotos en diferentes horas del día → normalización

### Próximos Pasos
1. Capturar mínimo 100 imágenes de hojas sanas
2. Reentrenar baseline con clasificación binaria real
3. Ejecutar Variante 1: HOG + SVM
4. Ejecutar Variante 2: ResNet50 transfer learning
5. Completar tabla comparativa con métricas reales
