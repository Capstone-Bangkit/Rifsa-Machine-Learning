import os
from PIL import Image

f1 = r'D://Bangkit Capstone/RiceLeafsv3/validation/leaf_scald'

for file in os.listdir(f1):
    f_img = f1+"/"+file
    img = Image.open(f_img)
    
    #resize image
    img = img.resize((1600,1600))
    
    img.save("D://Bangkit Capstone/RiceLeafsv3/validation/leaf_scald/"+file)
    
print('finish')
