from ultralytics import YOLO
import os

# Cambia al directorio donde están tus archivos .yaml
#os.chdir('C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Train YOLO8')
#os.chdir('/home/orin/Downloads/Training_YOLO8_Python-main/Train YOLO8')

# Inicializa el modelo
model = YOLO('/home/orin/Downloads/Training_YOLO8_Python-main/Train YOLO8/yolov8.yaml')
#model = YOLO('/home/orin/Downloads/Training_YOLO8_Python-main/Train YOLO8/yolov8l-big.yaml') 
  # Asegúrate de que 'yolov8.yaml' esté en la misma carpeta o proporciona la ruta completa
#model = YOLO('yolov8x.yaml')  # Asegúrate de que 'yolov8.yaml' esté en la misma carpeta o proporciona la ruta completa

# Entrena el modelo 5568, 2532 -> 2784, 1266 -> 1856, 844
#results = model.train(data='data.yaml', epochs=5, batch=2, resume=True, imgsz=[1856, 844])  # Ajusta el número de épocas según sea necesario
#results = model.train(data='data.yaml', epochs=100, batch=6, resume=True, imgsz=640)  # Ajusta el número de épocas según sea necesario
#results = model.train(data='data.yaml', epochs=25, batch=6, resume=True, imgsz=640, lr0=0.01, momentum=0.9, optimizer="SGD")  # Ajusta el número de épocas según sea necesario<<<<<<<
#results = model.train(data='data.yaml', epochs=150, batch=4, resume=True, imgsz=640, lr0=0.05, lrf=0.0001,momentum=0.9)  # Ajusta el número de épocas según sea necesario<<<<<<<
# EL DE ABAJO ES EL CHIDO
#results = model.train(data='/home/orin/Downloads/Training_YOLO8_Python-main/Train YOLO8/data.yaml', epochs=250, patience=30,workers=6,batch=8, resume=True,lr0=0.01, lrf=0.01, imgsz=1600, weight_decay=0.0001, warmup_epochs=10, warmup_momentum=0.5, warmup_bias_lr=0.1, hsv_h=0.015, hsv_s=0.8, hsv_v=0.1, degrees=0, translate=0.1, scale=0.7, mosaic=0, mixup=1, flipud=0, shear=25, perspective=0.001)
results = model.train(data='/home/orin/Downloads/Training_YOLO8_Python-main/Train YOLO8/data.yaml', epochs=250, patience=30,workers=6,batch=8, optimizer="AdamW",resume=True,lr0=0.01, lrf=0.01, imgsz=1600, weight_decay=0.0001, warmup_epochs=10, warmup_momentum=0.5, warmup_bias_lr=0.1)
#results = model.train(data='/home/orin/Downloads/Training_YOLO8_Python-main/Train YOLO8/data.yaml', epochs=250, patience=50,workers=6,batch=33, resume=True, imgsz=1920, lr0=0.01, lrf=0.01,momentum=0.95,hsv_h=0.015, hsv_s=0.8, hsv_v=0.1, degrees=0, translate=0.1, scale=0.7, mosaic=0, mixup=1, flipud=0, shear=25, perspective=0.001)

"""
496041984 en la pc corei5t, el valor de los bytes alojados para el entrenamiento, tienen que ser menor a esta cifra
7936671744
1488125952

"""
