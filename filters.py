import cv2
import numpy as np
def gray_image(image_array):
        gray=cv2.cvtColor(image_array,cv2.COLOR_RGB2GRAY)
        return gray

def blur_image(image_array,blur_value):
    blur=cv2.GaussianBlur(image_array,(blur_value,blur_value),0)
    return blur

def invert_image(image_array):
    invert=255-image_array
    return invert

def brightness_filter(image_array,brightness_value):
    
    bright = np.clip(image_array.astype(np.int16) + brightness_value, 0, 255)

    return bright.astype(np.uint8)

def contrast_filter(image_array,alpha):
    contrast = np.clip(image_array.astype(np.float32) * alpha, 0, 255)

    return contrast.astype(np.uint8)

def edge_detection(image_array,low_threshold,high_threshold):
    gray=cv2.cvtColor(image_array,cv2.COLOR_RGB2GRAY)
    edges=cv2.Canny(gray,low_threshold,high_threshold)
    return edges

def sharpen_filter(image_array,strength):

    kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
    ])

    sharpened = cv2.filter2D(image_array, -1, kernel)
    output=cv2.addWeighted(image_array,1,sharpened,strength,0)

    return output
def sepia_filter(image_array,strength):

    kernel = np.array([
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]
    ])

    sepia = cv2.transform(image_array, kernel)

    sepia = np.clip(sepia, 0, 255).astype(np.uint8)
    output=cv2.addWeighted(image_array,1-strength,sepia,strength,0)


    return output


# 9. Black & White Threshold Filter
def threshold_filter(image_array,threshold_value):

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    _, threshold = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
    )

    return threshold


# 10. Red Channel Filter
def red_filter(image_array,intensity):

    red = image_array.copy().astype(np.float32)

# Boost RED
    red[:, :, 0] *= (1 + intensity / 3)

# Reduce GREEN
    red[:, :, 1] *= (1 - intensity / 5)

# Reduce BLUE
    red[:, :, 2] *= (1 - intensity / 5)

    red = np.clip(red, 0, 255)

    return red.astype(np.uint8)


# 11. Green Channel Filter
def green_filter(image_array,intensity):

    green = image_array.copy().astype(np.float32)

# reduce RED
    green[:, :, 0] *= (1 - intensity / 5)

# boost GREEN
    green[:, :, 1] *= (1 + intensity / 3)

# Reduce BLUE
    green[:, :, 2] *= (1 - intensity / 5)

    green = np.clip(green, 0, 255)

    return green.astype(np.uint8)


# 12. Blue Channel Filter
def blue_filter(image_array,intensity):

    blue = image_array.copy().astype(np.float32)

# reduce RED
    blue[:, :, 0] *= (1 - intensity / 5)

# reduce GREEN
    blue[:, :, 1] *= (1 - intensity / 5)

# boost BLUE
    blue[:, :, 2] *= (1 + intensity / 3)

    blue = np.clip(blue, 0, 255)

    return blue.astype(np.uint8)
