import os
import PIL
from PIL import Image, ImageOps

f1 = r'D://Bangkit Capstone/dataset(2)/test(2)'

for file in os.listdir(f1):
    f_img = f1+"/"+file
    img = Image.open(f_img)
    bg = Image.open('D://Bangkit Capstone/dataset(2)/test/bg.jpg')
    bg_im = bg.copy()
    
    #resize image
    img = img.rotate(45, PIL.Image.NEAREST, expand = 1)
    
    img = img.resize((2300,2300))
    
    #paste to bg
    bg_im.paste(img, (0,0))
    
    
    bg_im.save("D://Bangkit Capstone/dataset(2)/output/"+file)
    
print('finish')
