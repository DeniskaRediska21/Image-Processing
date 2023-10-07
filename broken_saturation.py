from PIL import Image
import numpy as np

def image_grayscale(path:str,verbose=True,saturation = 1):
        img = np.array(Image.open(path))
        max_img = np.max(img,axis=2)[:,:,None]
        min_img = np.min(img,axis=2)[:,:,None]
        img_desaturated = saturation*(img-min_img) + (1/saturation)*min_img
#        img_desaturated = max_img*(tmp/np.max(tmp,axis=2)[:,:,None])


        img_desaturated = Image.fromarray(img_desaturated.astype(np.uint8))
        if verbose:
            img_desaturated.show()
        return img_desaturated



saturation = 0.1
img_grayscale = image_grayscale(path = "Data/Lerik.jpg", verbose=True,saturation = saturation)
