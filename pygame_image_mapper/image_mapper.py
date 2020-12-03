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

    image_gui=None
    def __init__(self):
        self.build_the_gui()

    def build_the_gui(self):

        ## FRAMES
        self.mapping_frame=gb.Frames(row=1,col=0,bg='brown',relief='raised',
        banner_font='Ariel 12 bold',
        banner_text='Mapper',
        fg='yellow',
        sticky=gb.NW)

        self.temporary_frame=gb.Frames(row=2,col=0,bg='brown',relief='raised',
        banner_font='Ariel 12 bold',
        banner_text='Display Selection',
        fg='yellow',
        sticky=gb.NW)

        self.tag=gb.Entries(self.mapping_frame.F,name='Map Object Tag',row=1,col=0)
        self.start_mapping_btn=gb.Buttons(self.mapping_frame.F,name='Start Mapping',row=3,col=0,width=20,command=None,sticky=gb.W,pady=10)
        self.stop_mapping_btn=gb.Buttons(self.mapping_frame.F,name='Stop Mapping',row=3,col=1,width=20,command=None,sticky=gb.E,pady=10)
        self.load_image_btn=gb.Buttons(self.mapping_frame.F,name='Open Map',row=5,col=1,width=20,command=the_map,sticky=gb.W,pady=10)

        self.display_selected=gb.Entries(self.temporary_frame.F,name='Item Selected',row=1,col=0)
        self.selected_item_info=gb.Textbox(self.temporary_frame.F,name='DESCRIPTION',row=3,col=0,width=30)

        
        
    def display_the_selection(self,k):
        self.display_selected.entry.insert(0,k)
        self.selected_item_info.text_box.insert(gb.INSERT,map_dict[k]['type'])
        self.selected_item_info.text_box.insert(gb.INSERT,map_dict[k]['uid'])



# def map_selection(mouse_pos):
#     # print(f'mouse x pos: {mouse_pos}')
#     x=mouse_pos[0]
#     y=mouse_pos[1]
    
#     for k,v in map_dict.items():
#         check=[v['pos'][0]<=x<=v['pos'][1],v['pos'][2]<=y<=v['pos'][3]]
#         if all(check):
#             print(f"Map Item is: {k}\nThe items is a {v['type']}")
#             ImageMapGui().display_the_selection(k)
#             break

def get_map_file():
    with open("map_file.json", "r") as read_file:
        x = json.load(read_file)
    return x

def the_map():

    global map_dict
    map_dict=get_map_file()

    pygame.init()

    image=pygame.image.load('manifold.png')
    image_size=image.get_size()

    w=image_size[0]
    h=image_size[1]

    global screen
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Manifold')

    screen.blit(image, (0, 0))

    rect=image.get_rect()
    # print(f'image size:{image.get_size()}')
    # print(f'rect: {rect}')
    #Add this before loop.
    clock = pygame.time.Clock()

    done = False

    while not done:

        #Add this in loop.
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pygame.mouse.get_pressed()[0]:
            # map_selection(pygame.mouse.get_pos())

            mouse_pos=pygame.mouse.get_pos()
            x=mouse_pos[0]
            y=mouse_pos[1]
            
            for k,v in map_dict.items():
                check=[v['pos'][0]<=x<=v['pos'][1],v['pos'][2]<=y<=v['pos'][3]]
                if all(check):
                    print(f"Map Item is: {k}\nThe items is a {v['type']}")
                    ImageMapGui().display_the_selection(k)
                    done=True
                    pygame.display.quit()
                    break
        
        if done:
            break
        else:       
            pygame.display.flip()
        


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

    


