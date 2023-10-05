import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import cv2
import os


def parse_txt(txt_file, img_width, img_height):
    with open(txt_file, "r") as file:
        lines = file.readlines()
    bbs = []
    for line in lines:
        parts = line.strip().split()
        label, x_center, y_center, width, height = parts[0], float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])
        # Convertir coordenadas normalizadas a coordenadas de píxeles
        x_center, y_center, width, height = x_center * img_width, y_center * img_height, width * img_width, height * img_height
        # Convertir coordenadas de centro a coordenadas de esquina
        x1, y1, x2, y2 = x_center - width/2, y_center - height/2, x_center + width/2, y_center + height/2
        bbs.append(BoundingBox(x1=x1, y1=y1, x2=x2, y2=y2, label=label))
    return bbs




input_folder='C:/Users/mtto_/OneDrive/Escritorio/vale/bran/data_num_v'
output_img_dir='New_img'
output_bb_dir='New_labels'
    
# Aplicamos la distorsión augmentación a las imagenes
seq = iaa.Sequential([
    iaa.Crop(px=(0, 16)),
    iaa.Fliplr(0.5),
    iaa.Affine(rotate=(90)),
    iaa.AverageBlur(k=((0, 7), (0, 3)))
])


# Si no existen los folders de salida, crealos
if not os.path.exists(output_img_dir):
    os.makedirs(output_img_dir)
if not os.path.exists(output_bb_dir):
    os.makedirs(output_bb_dir)



for filename in os.listdir(input_folder): # Itera sobre cada archivo del folder    
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"): # Si el archivo es una imagen, entonces

        image_path = os.path.join(input_folder, filename) # Obtenemos la ruta de cada imagen
        txt_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}.txt") # # Obtenemos la ruta de cada etiqueta
        
        image = cv2.imread(image_path) # Leemos cada imagen
        image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # Convertimos la imagen de RGB BGR
        bbs = parse_txt(txt_path, image_rgb.shape[1], image_rgb.shape[0]) # Mandamos las etiquetas a la función parse_txt
        
        bb_objects = BoundingBoxesOnImage(bbs, shape=image_rgb.shape) # Le colocamos las Bounding Boxes a la imágen
        augmented_image, augmented_bbs = seq(image=image_rgb, bounding_boxes=bb_objects) # 
        
        # cv2.imwrite(os.path.join(output_img_dir, f"aug_{filename}"), cv2.cvtColor(augmented_image, cv2.COLOR_BGR2RGB))
        #cv2.imshow("test",cv2.cvtColor(augmented_image, cv2.COLOR_BGR2RGB))
        
        with open(os.path.join(output_bb_dir, f"aug_{os.path.splitext(filename)[0]}.txt"), "w") as file:
            for bb in augmented_bbs.bounding_boxes:
                
                # Convertir coordenadas de esquina a coordenadas de centro
                x_center, y_center = (bb.x1 + bb.x2) / 2, (bb.y1 + bb.y2) / 2
                width, height = bb.x2 - bb.x1, bb.y2 - bb.y1
                
                # Normalizar las coordenadas
                x_center, y_center = x_center / image_rgb.shape[1], y_center / image_rgb.shape[0]
                width, height = width / image_rgb.shape[1], height / image_rgb.shape[0]
                
                if x_center >= 0 and y_center >= 0 and width >= 0 and height >= 0 and x_center < 1 and y_center < 1 and width < 1 and height < 1:
                
                    # Escribir en el archivo
                    cv2.imwrite(os.path.join(output_img_dir, f"aug_{filename}"), cv2.cvtColor(augmented_image, cv2.COLOR_BGR2RGB))
                    file.write(f"{bb.label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
