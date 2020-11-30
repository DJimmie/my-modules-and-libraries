"""Allows user to assign names (tags,ID,etc.) to positions (objects) on an image."""

import pygame
import json

import os
import sys
import logging
# try:
#     import tkinter.ttk
#     from tkinter import *
# #     from tkinter.ttk import *
# except:
#     from tkinter import *

from tkinter import messagebox

import gui_build as gb
import program_work_dir as pwd

# Create program working folder and its subfolders
config_parameters={'database server':{'N/A':'N/A'}}
client=pwd.ClientFolder(os.path.basename(__file__),config_parameters)
ini_file=f'c:/my_python_programs/{client}/{client}.ini'

log_file=f'c:/my_python_programs/{client}/{client}_log.log'
logging.basicConfig(filename=log_file, level=logging.INFO, filemode='w', format=' %(asctime)s -%(levelname)s - %(message)s')
logging.info('Start')

class UserInterface():
    """Parent class for the UI. Instantiates the composit Window.
    User Interface with fields for entering a data to the database. 
    Also, when the UI is launched, username is retrieved."""
    logging.info('UserInterface()')

    def __init__(self):
        """Interface build."""
        gb.UI(None,title='IMAGE MAPPING WITH PYGAME',
        banner='IMAGE MAPPER',
        win_color='#003366',
        window_width=750)

        ImageMapGui()
        
        gb.mainloop()

    
class ImageMapGui():
    """Build the GUI and implement it's methods"""
    logging.info('ImageMapGui()')

    def __init__(self):
        self.build_the_gui()

    def build_the_gui(self):

        ## FRAMES
        self.mapping_frame=gb.Frames(row=1,col=0,bg='brown',relief='raised',
        banner_font='Ariel 12 bold',
        banner_text='Mapper',
        fg='yellow',
        sticky=gb.NW)

        self.tag=gb.Entries(self.mapping_frame.F,name='Map Object Tag',row=1,col=0)
        self.start_mapping_btn=gb.Buttons(self.mapping_frame.F,name='Start Mapping',row=3,col=0,width=20,command=None,sticky=gb.W,pady=10)
        self.stop_mapping_btn=gb.Buttons(self.mapping_frame.F,name='Stop Mapping',row=3,col=1,width=20,command=None,sticky=gb.E,pady=10)
        # self.load_image_btn=gb.Buttons(self.gb.UI.w,name='Stop Mapping',row=3,col=1,width=20,command=None,sticky=gb.E,pady=10)

        





        


## FUNCTIONS--------------------------FUNCTIONS--------------------------FUNCTIONS
def get_config_values(section,option):
    """Used to retrieve values from the program's configuration file."""
    config=pwd.configparser.ConfigParser()
    config.read(ini_file)

    return config[section][option]

def exit_operations():
    """Operations to perform prior to the program exit"""
    # remove images from the image folder after each session

    # save the table as a json file in the working directory
    pass



## MAIN-----------------MAIN-----------------MAIN
if __name__ == '__main__':

    UserInterface()

