from PIL import Image
import numpy as np

def to_palet(PATH, colors = [0,255], verbose = True): 
    # PATH = 'Data/Penguins.jpg'
    # colors = [[0,255],[0,255],[0,255]]
    # verbose = True
    
    colors = np.array(colors)
    img = np.array(Image.open(PATH))/255
    
    if len(colors.shape) == 1:
        colors = colors[None,:]
        img = np.mean(img,axis = 2)[:,:,None]
        
    coords = (img*(colors.shape[1]-1)+0.5).astype(np.uint8)
    
    for  i in range(colors.shape[0]):
        coords[:,:,i] = colors[i,coords[:,:,i]]
    
    
    if img.shape[2]==1:
        coords = np.squeeze(coords)
    
    coords = Image.fromarray(coords)
    if verbose:
        coords.show()
    return coords

to_palet('Data/Penguins.jpg', colors = [[0,255],[0,255],[0,255]], verbose = True)

