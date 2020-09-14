from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import matplotlib.pyplot as plt
from matplotlib import image
from PIL import Image

import numpy as np

import os
import sys


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeTofile(data,filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename)


def open_directory():
    """Opens the directory folder for user to access"""  

    x=filedialog.askopenfilename(initialdir = 'C:/my_temp_dirs/',title = "Directory",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    print(x)
    pic_file=os.path.basename(x)

    # photo=display_with_mat(x)
    
    print(pic_file)
    
    binary_file_to_upload=convertToBinaryData(x)

    return binary_file_to_upload

    Tk().destroy()


    # sql_upload_command(pic_file,binary_file_to_upload)


def make_temp_directory():
    pass



def display_with_mat(photo):
    pic = image.imread(photo)
    
    print(pic.dtype)
    print(pic.shape)

    rgb_weights = [0.2989, 0.5870, 0.1140]
    grayscale_image = np.dot(pic[...,:3], rgb_weights)

    print(grayscale_image.dtype)
    print(grayscale_image.shape)

    # pic=image_resizing(grayscale_image)

    plt.imshow(pic)
    # plt.imshow(grayscale_image)
    plt.show()

    return pic

def bye_bye():
    """Exit Program"""
    exit()
