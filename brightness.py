from PIL import Image
import numpy as np

def image_brightness(PATH:str, bias = [0,0,0], verbose=True):
	img = np.array(Image.open(PATH))
	img_contrasted =np.clip(np.add(img,bias),0,255).astype(np.uint8)
	img_contrasted = Image.fromarray(img_contrasted)
	if verbose:
		img_contrasted.show()
	return img_contrasted




# img_contrasted = image_brightness(path = "Data/Penguins.jpg", verbose=True, bias = [50,50,50])
# img_contrasted.save("Results/plus_50_brightness.jpg")
# 
# img_contrasted = image_brightness(path = "Data/Penguins.jpg", verbose=True, bias = [-50,-50,-50])
# img_contrasted.save("Results/minus_50_brightness.jpg")
