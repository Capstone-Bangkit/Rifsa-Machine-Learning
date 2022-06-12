import os
from PIL import Image

#f1 = r'D://Bangkit Capstone/sementara/brown_spot_test'
f1 = r'C:\xampp\htdocs\TOPSIS\spk_thbo_topsis\images\1'

for file in os.listdir(f1):
    f_img = f1+"/"+file
    img = Image.open(f_img)
    
    #resize image
    img = img.resize((500,250))
    
    img.save(f_img)
    
print('finish')
