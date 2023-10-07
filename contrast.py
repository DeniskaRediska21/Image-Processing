from PIL import Image
import numpy as np

def image_contrast(path:str,verbose=True,factor = [1,1,1], bias = [128,128,128]):
	img = np.array(Image.open(path))
	img_contrasted =np.clip(np.add(np.multiply(factor,np.subtract(img,bias)),bias),0,255).astype(np.uint8)
	img_contrasted = Image.fromarray(img_contrasted)
	if verbose:
		img_contrasted.show()
	return img_contrasted




img_contrasted = image_contrast(path = "Data/Penguins.jpg", verbose=True,factor = [1,1,1], bias = [128,128,128])
