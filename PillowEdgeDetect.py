# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:07:40 2021

@author: jackb
"""
from PIL import Image, ImageFilter, ImageOps
import numpy as np

def saveImage(fileName):
    #open new image
    img = Image.open(fileName + ".jpg")
    #image save
    img.save('{}.png'.format(fileName))
    print("Image saved to working directory")

    


def getPillowEdgeImage(image):  
    #Convert to pillow image for pillow
    image=Image.fromarray(image)
    
    # Converting the image to greyscale, as edge detection  
    # requires input image to be of mode = Greyscale (L) 
    image = image.convert("L") 
  
    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES 
    image = image.filter(ImageFilter.FIND_EDGES)
    
    #Convert the image back into RGB to perform pixel swapping
    image = image.convert("RGB") 
    
    #Flip black and white for cleaner image
    image = ImageOps.invert(image)

    #Convert back to numpy array for cv2
    image = np.array(image)
    return image

#########
'''
Create a function that takes an image frame (numpy array) and a list of four integers [x,y,w,h] 
where (x,y) and (x+w,y+h) are the coordinates of the rectangle that serves as the boundary for the 
image filter boundary


filename = 'CopyofPicture020.png'

image = Image.open(filename)


image = np.array(image)

coordinates = [700,500,200,300]
'''

def filterRectangle(image,coordinates):
    
    #Create rectangle from coordinates
    rectangle = image[coordinates[1]:coordinates[1]+coordinates[3],
                      coordinates[0]:coordinates[0]+coordinates[2]]
    
    #Filter the rectangle
    rectangle = getPillowEdgeImage(rectangle)
    
    #Replace the rectangle in the original image
    image[coordinates[1]:coordinates[1]+coordinates[3],
                      coordinates[0]:coordinates[0]+coordinates[2]] = rectangle
    return image

