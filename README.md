# Repositorio de Entrenamiento YOLO8 en Python

## Descripción General
Este repositorio contiene todos los scripts y archivos necesarios para entrenar un modelo YOLO8 en Python. Aquí encontrarás desde la generación de datos hasta el script para entrenar el modelo.

## Índice
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Pasos para el Entrenamiento](#pasos-para-el-entrenamiento)
- [Uso](#uso)
- [Ubicación del Modelo Entrenado](#ubicación-del-modelo-entrenado)
- [Notas Adicionales](#notas-adicionales)

## Estructura del Repositorio
- **Augmentation_one_to_many.py**: Este script se encarga de aplicar augmentación a las imágenes y generar múltiples versiones de cada una.
- **Augmentation_one_to_one.py**: Este script aplica augmentación a las imágenes pero genera una sola versión de cada una.
- **Unormalize_labels.py**: Este script se utiliza para desnormalizar las etiquetas generadas durante el entrenamiento.

### Carpeta Train YOLO8
- **Entrenamiento.py**: Este script es el corazón del repositorio, se encarga de entrenar el modelo YOLO8.
- **data.yaml**: Este archivo contiene la configuración del modelo, como la ubicación de los datos de entrenamiento y validación, y el número de clases.

## Pasos para el Entrenamiento
1. **Preparación de Datos**: 
    - Asegúrate de que todas las imágenes y sus etiquetas correspondientes estén en una sola carpeta.
  
2. **Generación de Imágenes y Etiquetas Augmentadas**: 
    - Ejecuta los scripts de augmentación según tus necesidades:
        ```bash
        python Augmentation_one_to_one.py
        python Augmentation_one_to_many.py
        ```
  
3. **Organización de Datos**:
    - Divide las imágenes y etiquetas en tres carpetas: `test`, `train` y `valid`.

4. **Configuración del Archivo data.yaml**:
    - Modifica el archivo `data.yaml` para reflejar las rutas de las carpetas `test`, `train` y `valid`.

5. **Entrenamiento del Modelo**: 
    ```bash
    python Entrenamiento.py
    ```

## Uso
Para utilizar este repositorio, sigue los pasos en la sección [Pasos para el Entrenamiento](#pasos-para-el-entrenamiento).

## Ubicación del Modelo Entrenado
El modelo de ejemplo entrenado se encuentra en la carpeta `Train YOLO8/runs/detect/train1/weights/`.
Si tu generas un nuevo modelo entrenado, se encontrará dentro de `Train YOLO8/runs/detect/`

## Notas Adicionales
- Asegúrate de que todas las imágenes y etiquetas estén en una sola carpeta.
- Puedes ajustar el número de épocas y el tamaño del lote en el script `Entrenamiento.py`.



