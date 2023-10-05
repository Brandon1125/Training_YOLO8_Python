from ultralytics import YOLO
import os

# Cambia al directorio donde están tus archivos .yaml
os.chdir('C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Train YOLO8')

# Inicializa el modelo
model = YOLO('yolov8.yaml')  # Asegúrate de que 'yolov8.yaml' esté en la misma carpeta o proporciona la ruta completa

# Entrena el modelo 5568, 2532 -> 2784, 1266 -> 1856, 844
results = model.train(data='data.yaml', epochs=5, batch=2, resume=True, imgsz=[2784, 1266])  # Ajusta el número de épocas según sea necesario

"""
496041984 en la pc corei5t, el valor de los bytes alojados para el entrenamiento, tienen que ser menor a esta cifra
7936671744
1488125952

"""