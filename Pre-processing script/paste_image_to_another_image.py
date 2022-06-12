import os
import PIL
from PIL import Image, ImageOps

f1 = r'D://Bangkit Capstone/sementara/test'

for file in os.listdir(f1):
    f_img = f1+"/"+file
    img = Image.open(f_img)
    bg = Image.open('D://Bangkit Capstone/dataset(2)/test/white.jpg')
    bg_im = bg.copy()
    
    #resize image
    #img = img.rotate(45, PIL.Image.NEAREST, expand = 1)
    
    img = img.resize((1600,500))
    
    #paste to bg
    bg_im.paste(img, (0,550))
    
    
    bg_im.save("D://Bangkit Capstone/sementara/output/"+file)
    
print('finish')
