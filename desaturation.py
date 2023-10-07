from PIL import Image
import numpy as np

def image_grayscale(path:str,verbose=True,saturation = 1):
        img = np.array(Image.open(path))
        img_desaturated = np.empty_like(img)
        for c in range(img.shape[2]):
            saturation_matrix = [1-saturation,1-saturation,1-saturation]
            saturation_matrix[c] += saturation 
            img_desaturated[:,:,c] = np.sum(img*saturation_matrix,axis=2)/(3-2*saturation)


        img_desaturated = (img_desaturated/np.max(img_desaturated,axis=2)[:,:,None])*np.max(img,axis=2)[:,:,None]
        img_desaturated = Image.fromarray(img_desaturated.astype(np.uint8))
        if verbose:
            img_desaturated.show()
        return img_desaturated



saturation = 0.5
img_grayscale = image_grayscale(path = "Data/Penguins.jpg", verbose=True,saturation = saturation)
