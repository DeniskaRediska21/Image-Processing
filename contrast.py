from PIL import Image
import numpy as np

def image_contrast(PATH:str,factor = [1,1,1], bias = [128,128,128], verbose=True):
	img = np.array(Image.open(PATH))
	img_contrasted =np.clip(np.add(np.multiply(factor,np.subtract(img,bias)),bias),0,255).astype(np.uint8)
	img_contrasted = Image.fromarray(img_contrasted)
	if verbose:
		img_contrasted.show()
	return img_contrasted




#img_contrasted = image_contrast(PATH = "Data/Penguins.jpg", verbose=True,factor = [2,2,2], bias = [128,128,128])
#img_contrasted.save("Results/double_contrast.jpg")
#
#img_contrasted = image_contrast(PATH = "Data/Penguins.jpg", verbose=True,factor = [0.5,0.5,0.5], bias = [128,128,128])
#img_contrasted.save("Results/half_contrast.jpg")
