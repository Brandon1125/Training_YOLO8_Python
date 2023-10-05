#import os
import pandas as pd
import cv2

img = cv2.imread("C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Data/Tablero_C - copia.png")

# [class, x , y, width, height] 
with open("Labels/Tablero_C - copia.txt", "r") as labels:
        lines = labels.readlines()
       
        
       
array = []        
for line in lines:
    array.append(line.split(" "))
    

df = pd.DataFrame(array)



# A las Labels le sumamos + 9
for i, labels in enumerate(df[:][0]):
    df[0][i] = int(labels) + 9
    
    
# Al centro en X lo multiplicamos por el ancho de la imagen para desnormalizar
for i, labels in enumerate(df[:][1]):
    df[1][i] = float(labels) * img.shape[1]

for i, labels in enumerate(df[:][2]):
    df[2][i] = float(labels) * img.shape[0]

for i, labels in enumerate(df[:][3]):
    df[3][i] = float(labels) * img.shape[1]

for i, labels in enumerate(df[:][4]):
    df[4][i] = float(labels) * img.shape[0]
    
df.columns = ["labels", "x", "y", "width", "height"]
df = df.reset_index()
df_to_csv = df.to_csv("a.csv", index=False)