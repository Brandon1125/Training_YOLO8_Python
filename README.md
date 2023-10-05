# Repositorio de Entrenamiento YOLO8 en Python

## Descripción General
Este repositorio contiene todos los scripts y archivos necesarios para entrenar un modelo YOLO8 en Python. Aquí encontrarás desde la generación de datos hasta el script para entrenar el modelo.

---

## Índice
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Pasos para el Entrenamiento](#pasos-para-el-entrenamiento)
- [Notas Adicionales](#notas-adicionales)

---

## Estructura del Repositorio

- **Augmentation_one_to_many.py**: Este script se encarga de aplicar augmentación a las imágenes y generar múltiples versiones de cada una.
  
- **Augmentation_one_to_one.py**: Este script aplica augmentación a las imágenes pero genera una sola versión de cada una.

### Carpeta Train YOLO8

- **Entrenamiento.py**: Este script es el corazón del repositorio, se encarga de entrenar el modelo YOLO8.
  
- **Generate_traintxt_labelstxt.py**: Este script genera los archivos `train.txt` y `val.txt` que son necesarios para el entrenamiento.

- **data.yaml**: Este archivo contiene la configuración del modelo, como la ubicación de los datos de entrenamiento y validación, y el número de clases.

---

## Pasos para el Entrenamiento

1. **Preparación de Datos**: 
    - Asegúrate de que todas las imágenes y sus etiquetas correspondientes estén en una sola carpeta.

2. **Generación de Archivos de Entrenamiento y Validación**: 
    ```bash
    python Generate_traintxt_labelstxt.py
    ```
  
3. **Entrenamiento del Modelo**: 
    ```bash
    python Entrenamiento.py
    ```

---

## Notas Adicionales

- Asegúrate de que todas las imágenes y etiquetas estén en una sola carpeta. Esto es crucial para el correcto funcionamiento de los scripts.

- Puedes ajustar el número de épocas y el tamaño del lote en el script `Entrenamiento.py` según tus necesidades.

- Los archivos `train.txt` y `val.txt` generados contienen las rutas a las imágenes y etiquetas, asegúrate de que estas rutas sean accesibles desde donde ejecutes el script de entrenamiento.


