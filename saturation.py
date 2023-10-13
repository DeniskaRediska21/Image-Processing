from PIL import Image
import numpy as np

def image_saturation(PATH:str, saturation = 1, verbose=True):
        saturation = np.array(saturation)
        img = np.array(Image.open(PATH))
        max_img = np.max(img,axis=2)[:,:,None]
        min_img = np.min(img,axis=2)[:,:,None]
        tmp = saturation*(img-min_img) + (1/saturation)*min_img

        delim = np.max(tmp,axis=2)[:,:,None]
        delim[delim == 0] = 1
        img_saturated = max_img*(tmp/delim)


        img_saturated = Image.fromarray(img_saturated.astype(np.uint8))
        if verbose:
            img_saturated.show()
        return img_saturated



#img = image_saturation(PATH = "Data/Penguins.jpg", verbose=True,saturation = [2,2,2])
#img.save("Results/double_saturation.jpg")
#
#img = image_saturation(PATH = "Data/Penguins.jpg", verbose=True,saturation = [0.5,0.5,0.5])
#img.save("Results/half_saturation.jpg")
