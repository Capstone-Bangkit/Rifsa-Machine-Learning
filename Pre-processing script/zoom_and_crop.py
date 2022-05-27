import os
import PIL
from PIL import Image, ImageOps


f1 = r'D://Bangkit Capstone/dataset(2)/narrow brown spot'

for file in os.listdir(f1):
    f_img = f1+"/"+file
    img = Image.open(f_img)
    
    #resize image
    img = img.resize((1600,1600))
        
    img.save("D://Bangkit Capstone/dataset(2)/output/"+file, 'JPEG')
    
print('finish')
