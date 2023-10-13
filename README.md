# Image-Processing

Various basic image pocessing techniques implemented in python

## image_brightness Function Defenition

```
image_brightness(PATH:str, bias = [0,0,0], verbose=True)
```

### Inputs 

+ PATH (Str) - path to original image
+ bias (RGB triplet) - brightness offset
+ verbose (True/False)- if True show image on screen

### Outputs

+ PIL Image - containig resulting image
________

### Brightness Results
________

#### Brightness +50

```
img_contrasted = image_brightness(path = "Data/Penguins.jpg", verbose=True, bias = [50,50,50])
img_contrasted.save("Results/plus_50_brightness.jpg")
```
________

#### Brightness -50

```
img_contrasted = image_brightness(path = "Data/Penguins.jpg", verbose=True, bias = [-50,-50,-50])
img_contrasted.save("Results/minus_50_brightness.jpg")
```

| Original Image                       | Minus 50 brightness                                     | Plus 50 brightness                                    |
|--------------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| ![Original Image](Data/Penguins.jpg) | ![Minus 50 brightness](Results/minus_50_brightness.jpg) | ![Plus 50 brightness](Results/plus_50_brightness.jpg) |

________

## image_saturation Function Defenition

```
image_saturation(PATH:str, saturation = 1, verbose=True)
```

### Inputs 

+ PATH - path to original image
+ saturation - saturation multiplier *can't be 0*
+ verbose - if True show resulting image on screen

### Outputs

+ PIL Image - containig resulting image

________

## Saturation Results


### Double Saturation

```
img = image_saturation(PATH = "Data/Penguins.jpg", verbose=True,saturation = [2,2,2])
img.save("Results/double_saturation.jpg")
```

________

### Half Saturation

```
img = image_saturation(PATH = "Data/Penguins.jpg", verbose=True,saturation = [0.5,0.5,0.5])
img.save("Results/half_saturation.jpg")
```

________

| Original Image                       | Half Saturation                                 | Double Saturation                                   |
|--------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| ![Original Image](Data/Penguins.jpg) | ![Half Saturation](Results/half_saturation.jpg) | ![Double Saturation](Results/double_saturation.jpg) |
________

## image_contrast Function Defenition

```
image_contrast(PATH:str,factor = [1,1,1], bias = [128,128,128], verbose=True)
```

### Inputs 

+ PATH - path to original image
+ factor - contrasting factor
+ bias - bias of contrasting formula, [128,128,128] for no bias
+ verbose - if True show resulting image on screen

### Outputs

+ PIL Image - containig resulting image

________

## Contrast Results

________

### Double Contrast

```
img_contrasted = image_contrast(PATH = "Data/Penguins.jpg", verbose=True,factor = [2,2,2], bias = [128,128,128])
img_contrasted.save("Results/double_contrast.jpg")
```

________

### Half Contrast

```
img_contrasted = image_contrast(PATH = "Data/Penguins.jpg", verbose=True,factor = [0.5,0.5,0.5], bias = [128,128,128])
img_contrasted.save("Results/half_contrast.jpg")
```

________

| Original Image                       | Half Contrast                               | Double Contrast                                 |
|--------------------------------------|---------------------------------------------|-------------------------------------------------|
| ![Original Image](Data/Penguins.jpg) | ![Half Contrast](Results/half_contrast.jpg) | ![Double Contrast](Results/double_contrast.jpg) |

________


## image_grayscale

```
image_grayscale(PATH:str,factor = [1,1,1],verbose=True)
```

### Inputs 

+ PATH - path to original image
+ factor - each colors contribution to final color
+ verbose - if True show resulting image on screen

### Outputs

+ PIL Image - containig resulting image

________

## Grayscale Results

| Original Image                       | Grayscale with mean colors                    | Grayscale with different color contributions      |
|--------------------------------------|-----------------------------------------------|---------------------------------------------------|
| ![Original Image](Data/Penguins.jpg) | ![Mean Grayscale](Results/grayscale_mean.jpg) | ![Custom Grayscale](Results/grayscale_custom.jpg) |

________


