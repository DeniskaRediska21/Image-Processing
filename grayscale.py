from PIL import Image
import numpy as np

def image_grayscale(path:str,verbose=True,factor = [1/3,1/3,1/3]):
	img = np.array(Image.open(path))
	img_contrasted = np.mean(np.clip(np.multiply(factor,img),0,255),2).astype(np.uint8)
	img_contrasted = Image.fromarray(img_contrasted)
	if verbose:
		img_contrasted.show()
	return img_contrasted



#factor = [3*0.2126,3*0.7152,3*0.0722]
#factor = [1,1,1]
factor = [3*0.299,3*0.587,3*0.114]
img_grayscale = image_grayscale(path = "Data/Lerik.jpg", verbose=True,factor = factor)
