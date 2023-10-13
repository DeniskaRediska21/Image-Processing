from PIL import Image
import numpy as np

def image_grayscale(PATH:str,factor = [1,1,1],verbose=True):
	img = np.array(Image.open(PATH))
	img_contrasted = np.mean(np.clip(np.multiply(factor,img),0,255),2).astype(np.uint8)
	img_contrasted = Image.fromarray(img_contrasted)
	if verbose:
		img_contrasted.show()
	return img_contrasted



#factor = [3*0.2126,3*0.7152,3*0.0722]
factor = [1,1,1]
img = image_grayscale(PATH = "Data/Penguins.jpg", verbose=True,factor = factor)
img.save("Results/grayscale_mean.jpg")


factor = [3*0.299,3*0.587,3*0.114]
img = image_grayscale(PATH = "Data/Penguins.jpg", verbose=True,factor = factor)
img.save("Results/grayscale_custom.jpg")
