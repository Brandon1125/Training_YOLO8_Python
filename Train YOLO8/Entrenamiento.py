from ultralytics import YOLO
import os

# Cambia al directorio donde están tus archivos .yaml
os.chdir('C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Train YOLO8')

# Inicializa el modelo
#model = YOLO('yolov8.yaml')  # Asegúrate de que 'yolov8.yaml' esté en la misma carpeta o proporciona la ruta completa
model = YOLO('yolov8x.yaml')  # Asegúrate de que 'yolov8.yaml' esté en la misma carpeta o proporciona la ruta completa

# Entrena el modelo 5568, 2532 -> 2784, 1266 -> 1856, 844
#results = model.train(data='data.yaml', epochs=5, batch=2, resume=True, imgsz=[1856, 844])  # Ajusta el número de épocas según sea necesario
#results = model.train(data='data.yaml', epochs=100, batch=6, resume=True, imgsz=640)  # Ajusta el número de épocas según sea necesario
#results = model.train(data='data.yaml', epochs=25, batch=6, resume=True, imgsz=640, lr0=0.01, momentum=0.9, optimizer="SGD")  # Ajusta el número de épocas según sea necesario<<<<<<<
#results = model.train(data='data.yaml', epochs=150, batch=4, resume=True, imgsz=640, lr0=0.05, lrf=0.0001,momentum=0.9)  # Ajusta el número de épocas según sea necesario<<<<<<<
results = model.train(data='data.yaml', epochs=150, batch=4, resume=True, imgsz=1920, lr0=0.05, lrf=0.0001,momentum=0.9)  # Ajusta el número de épocas según sea necesario<<<<<<<

"""
496041984 en la pc corei5t, el valor de los bytes alojados para el entrenamiento, tienen que ser menor a esta cifra
7936671744
1488125952

"""