#import os
import pandas as pd
import cv2


############ LEEMOS LAS COORDENADAS Y LA IMAGEN CON EL OBJETIVO DE OBTENER SU ANCHO Y ALTO
img = cv2.imread("C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Data/Tablero_C - copia.png")

# [class, x , y, width, height] 
with open("Labels/Tablero_C - copia.txt", "r") as labels:
        lines = labels.readlines()
       
        
       
####### LEEMOS CADA RENGLÓN DEL DOCUMENTO Y AL RENGLÓN LO SEPARAMOS CADA ESPACIIO Y AGREGAMOS LOS ELEMENTOS DE ESTE RENGLÓN A UNA LISTA       
array = []        
for line in lines:
    array.append(line.split(" "))
    
# CONVERTIMOS A DATA FRAME LA LISTA
df = pd.DataFrame(array)


### LE SUMAMOS A LAS LABELS + 9, YA QUE EL OBJETIVO ES CONVERTIR 0 -> 9, 1 -> 10.  9 Y 10 SON LAS ETIQUETAS ORIGINALES. 0, 1 CORRESPONDEN AL 9 Y 10 EN IDIOMA MAKE-SENSE
for i, labels in enumerate(df[:][0]):
    df[0][i] = int(labels) + 9
    
    
##### DESNORMALIZAMOS X, Y, WIDTH Y HEIGHT DE LA IMAGE, MULTIPLICANDO EL NÚMERO NORMALIZADO QUE NOS DA MAKE-SENSE POR EL LARGO O ALTO DE LA IMAGEN
for i, labels in enumerate(df[:][1]):
    df[1][i] = float(labels) * img.shape[1]

for i, labels in enumerate(df[:][2]):
    df[2][i] = float(labels) * img.shape[0]

for i, labels in enumerate(df[:][3]):
    df[3][i] = float(labels) * img.shape[1]

for i, labels in enumerate(df[:][4]):
    df[4][i] = float(labels) * img.shape[0]


##### LE DAMOS FORMATO AL CSV
df.columns = ["labels", "x", "y", "width", "height"]
df = df.reset_index()
df_to_csv = df.to_csv("a.csv", index=False)