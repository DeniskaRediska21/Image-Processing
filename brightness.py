from PIL import Image
import numpy as np

def image_brightness(path:str,verbose=True, bias = [0,0,0]):
	img = np.array(Image.open(path))
	img_contrasted =np.clip(np.add(img,bias),0,255).astype(np.uint8)
	img_contrasted = Image.fromarray(img_contrasted)
	if verbose:
		img_contrasted.show()
	return img_contrasted




img_contrasted = image_brightness(path = "Data/Lerik.jpg", verbose=True, bias = [100,100,100])
