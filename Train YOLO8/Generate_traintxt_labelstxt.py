import os

# Rutas a tus carpetas de imágenes y etiquetas
image_folder = r'C:\Users\mtto_\OneDrive\Escritorio\Proyect\Augmentation\New_img'
label_folder = r'C:\Users\mtto_\OneDrive\Escritorio\Proyect\Augmentation\New_labels'

train_percentaje = int( ( len(os.listdir(image_folder)) / 100 ) * 80 )



def generate_txt_train(image_folder, label_folder, output_file):
        
    with open(output_file, 'w') as f:
        for img_file in os.listdir(image_folder)[:train_percentaje]:
            if img_file.endswith('.jpg') or img_file.endswith('.png'):
                
                label_file = img_file.replace('.jpg', '.txt').replace('.png', '.txt')
                f.write(f"{os.path.join(image_folder, img_file)} {os.path.join(label_folder, label_file)}\n")



def generate_txt_val(image_folder, label_folder, output_file):
        
    with open(output_file, 'w') as f:
        for img_file in os.listdir(image_folder)[train_percentaje:]:
            if img_file.endswith('.jpg') or img_file.endswith('.png'):
                
                label_file = img_file.replace('.jpg', '.txt').replace('.png', '.txt')
                f.write(f"{os.path.join(image_folder, img_file)} {os.path.join(label_folder, label_file)}\n")


# Generar train.txt y val.txt (puedes dividir tus datos como prefieras)
generate_txt_train(image_folder, label_folder, 'train.txt')
generate_txt_val(image_folder, label_folder, 'val.txt')

