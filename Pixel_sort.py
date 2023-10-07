from PIL import Image
import numpy as np
from scipy.ndimage.filters import gaussian_filter


img = Image.open('Data/Penguins.jpg')


Dithering = True
Binary_dithering = True
Grayscale = False
Reverse = False 

sigma = 1
axis = 1
tresh = 0.05


if axis == 1:
    img = img.transpose(Image.ROTATE_90)

img = np.array(img)/255

if Grayscale:
    img = np.mean(img,axis = 2)    

    
if not Grayscale:
    img_for_DOG = np.mean(img,axis = 2)
else:
    img_for_DOG = img

img_DOG = gaussian_filter(img_for_DOG, 2*sigma) -  gaussian_filter(img_for_DOG, sigma)       
img_DOG[img_DOG<tresh] = 0
img_DOG[img_DOG>=tresh] = 1

for ax in range(img_DOG.shape[0]):
    list_ = np.squeeze(np.where(np.in1d(img_DOG[ax,:],1)))
    for entry in range(np.size(list_)-1):
        tmp = img[ax,list_[entry]:list_[entry+1]]
        I = np.argsort(img_for_DOG[ax,list_[entry]:list_[entry+1]])
        if Reverse:
            I = np.flip(I)
        img[ax,list_[entry]:list_[entry+1]] = tmp[I]
    

# if axis == 1:
#     img = np.transpose(img)
    
img = Image.fromarray((img*255).astype(np.uint8))
if axis == 1:
    img = img = img.transpose(Image.ROTATE_270)


img.show()

