from rembg import remove
from PIL import Image

input_path = 'eu2.jpg'
output_path = input_path.replace( 'eu2.jpg', 'eu2_sf.jpeg')

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

'''
    É preciso instalar o rembg, para isso, execute o comando:
        pip install rembg
    É preciso instalar o Pillow, para isso, execute o comando:
        pip install Pillow
    É preciso instalar o onnxruntime, para isso, execute o comando:
        pip install onnxruntime
'''