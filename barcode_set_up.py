import sqlite3

try:
    import tkinter.ttk
    from tkinter import *
#     from tkinter.ttk import *
except:
    from tkinter import *

from tkinter import messagebox
from tkinter import filedialog


import matplotlib.pyplot as plt
from matplotlib import image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import pandas as pd

import qrcode
import barcode
from barcode.writer import ImageWriter

import os
import sys


def make_barcode(barcodeData,topLabel,bottomLabel):
        """Generate barcode for the barcodeData"""
        # QRcode option
        barcode=qrcode.make(barcodeData)

        barcode.save(f'C:/my_temp_dirs/{barcodeData}.png')
       
        labeled_barcode=label_the_barcode(barcodeData,topLabel,bottomLabel)

        labeled_barcode.save(f'C:/my_temp_dirs/{barcodeData}.png')

        # display_with_mat(f'image_store_2\{barcodeData}.png')

        return f'C:/my_temp_dirs/{barcodeData}.png'

def label_the_barcode(barcodeData,topLabel,bottomLabel):
    """Writes text on the barcode"""
    # get an image
    base = Image.open(f'C:/my_temp_dirs/{barcodeData}.png').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fnt1 =ImageFont.truetype(font="arialbd.ttf", size=15)
    fnt = ImageFont.truetype(font="arialbd.ttf", size=20)
    
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, full opacity
    d.text((0,0),topLabel, font=fnt1, fill=(0,0,0,255))
    
    # draw text, half opacity
    d.text((0,255),bottomLabel, font=fnt, fill=(0,0,0,255))
    

    out = Image.alpha_composite(base, txt)

    return out
    
    # out.save(f'image_store_2\{barcodeData}.png')
    # out.show()

    

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




# bottomLabel='1598891997-Fittings'
# a=make_barcode('1599663550','jd-',bottomLabel)
# print(a)