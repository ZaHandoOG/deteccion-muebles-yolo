# 🪑 Detección de Muebles con YOLOv11

Este proyecto implementa un modelo de detección de objetos basado en YOLOv11 para identificar 22 categorías de muebles en imágenes y entornos reales. El entrenamiento está optimizado para ejecutarse en entornos Windows utilizando aceleración gráfica (CUDA).

## 🚀 Requisitos

* Python 3.8 o superior
* Tarjeta gráfica NVIDIA (Recomendado para aceleración CUDA)

Instala las dependencias necesarias ejecutando:

```bash
pip install ultralytics opencv-python
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)
