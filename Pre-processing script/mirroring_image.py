import os
import PIL
from PIL import Image

f1 = r'D://Bangkit Capstone/sementara/test'

for file in os.listdir(f1):
    f_img = f1+"/"+file
    img = Image.open(f_img)
    
    #rotate image
    #img = img.rotate(90, PIL.Image.NEAREST, expand = 1)
    
    #mirror image
    #img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
    img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    
    
    img.save("D://Bangkit Capstone/sementara/output/"+file)
    
print('finish')
