import os

def load_images_path(root, exts=(".png")):
    images_path = []
    
    for r, d, f in os.walk(root):
        for file in f:
            if file.lower().endswith(exts):
                images_path.append(os.path.join(r, file).replace(os.sep, '/'))
            
    return images_path

png_images_path = load_images_path(root="./")

for png_image_path in png_images_path:
    jpg_image_path = png_image_path.replace(".png", ".jpg")
    os.system("ffmpeg -y -i " + png_image_path + " -qscale:v 3 -pix_fmt yuvj420p " + jpg_image_path)
