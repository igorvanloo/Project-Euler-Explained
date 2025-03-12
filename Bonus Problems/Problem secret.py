# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:49:49 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 

Answer:

'''
import time, math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

start_time = time.time()

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    img = img.astype(np.int32)
    return img

def display_image(image):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"

    plt.imshow(image)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))
    
def compute():
    img = load_image("C:/Users/IP176077/Desktop/Python-Projects/Project-Euler-Related/0. Project Euler Files/bonus_secret_statement.png")
    display_image(img)
    
    rsize, csize = len(img), len(img[0])
    
    for i in range(10):
        mask = np.zeros((rsize, csize, 3)).astype(np.int32)
        for r in range(rsize):
            for c in range(csize): 
                for k in range(0,3):
                    mask[r, c, k] = (img[r % rsize, (c + 1) % csize, k] + \
                                     img[r % rsize, (c - 1) % csize, k] + \
                                         img[(r - 1) % rsize, c % csize, k] + \
                                             img[(r + 1) % rsize, c % csize, k])
        img = mask
        display_image(img)
        return img

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
