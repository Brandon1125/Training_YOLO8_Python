Descripción General
Este repositorio contiene scripts y archivos necesarios para entrenar un modelo YOLO8 en Python. Aquí encontrarás todo lo que necesitas para llevar a cabo el proceso de entrenamiento, desde la generación de datos hasta el entrenamiento del modelo.

Estructura del Repositorio
Augmentation_one_to_many.py: Este script se encarga de aplicar augmentación a las imágenes y generar múltiples versiones de cada una.

Augmentation_one_to_one.py: Este script aplica augmentación a las imágenes pero genera una sola versión de cada una.

Train YOLO8/Entrenamiento.py: Este script es el corazón del repositorio. Se encarga de entrenar el modelo YOLO8.

Train YOLO8/Generate_traintxt_labelstxt.py: Este script genera los archivos train.txt y val.txt que son necesarios para el entrenamiento.

Train YOLO8/data.yaml: Este archivo contiene la configuración del modelo, como la ubicación de los datos de entrenamiento y validación, y el número de clases.

Pasos para el Entrenamiento
Preparación de Datos: Asegúrate de que todas las imágenes y sus etiquetas correspondientes estén en una sola carpeta.

Generación de Archivos de Entrenamiento y Validación: Ejecuta el script Generate_traintxt_labelstxt.py para generar los archivos train.txt y val.txt.

bash
Copy code
python Generate_traintxt_labelstxt.py
Entrenamiento del Modelo: Ejecuta el script Entrenamiento.py para iniciar el proceso de entrenamiento.

bash
Copy code
python Entrenamiento.py
Notas Adicionales
Asegúrate de que todas las imágenes y etiquetas estén en una sola carpeta. Esto es crucial para el correcto funcionamiento de los scripts.

Puedes ajustar el número de épocas y el tamaño del lote en el script Entrenamiento.py según tus necesidades.

Los archivos train.txt y val.txt generados contienen las rutas a las imágenes y etiquetas, asegúrate de que estas rutas sean accesibles desde donde ejecutes el script de entrenamiento.
