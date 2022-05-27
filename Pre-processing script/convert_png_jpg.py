from glob import glob                                                           
import cv2 
pngs = glob('D://Bangkit Capstone/dataset(2)/output(2)/*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)

print('finish') 