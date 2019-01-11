import tkinter.ttk
from tkinter import filedialog
from tkinter import *
import os
import sys
import pandas as pd



class my_window(Tk):

    def __init__(self,parent,*args,**kargs):
        Tk.__init__(self,parent,*args,**kargs)
        self.parent=parent
        self.initialize()

    def initialize(self):
        self.title('Main Window')
        the_window_width=self.winfo_screenwidth()
        the_window_height=self.winfo_screenheight()
#         self.configure(width=the_window_width,height=the_window_height)
        self.geometry(f'{the_window_width}x{the_window_height}+0+0')
        self.attributes('-fullscreen', True)
        self['borderwidth']=4
        self['bg']='blue'

    def get_info(self):
        for item in self.keys():
            print (item,':',self[item])
    
    def bye_bye(self):
        self.destroy()


class My_Frame(Frame):
    
    def __init__ (self,the_window,*args,**kwargs):
        Frame.__init__(self,the_window,*args,**kwargs)
#         self.the_window=the_window  
#         Frame.master=the_window
        self.the_frame=Frame(self)    
        self['background']='red'
        self['relief']='raised'
        self['borderwidth']=9
#         self['width']=150
#         self['height']=150
        
    def place_frame(self,the_row,the_col):
        self.grid(row=the_row,column=the_col,padx=10,pady=10)
        
        
    def get_info(self):
        """Diagnostics tool to check the attributes of the Frame"""
        for item in self.keys():
            print (item,':',self[item])


    def frame_header(self,header,rows=0,columns=0,the_span=2):
        self.frame_title=Label(self,text=header,font='Ariel 12 bold')
        self.frame_title.grid(row=rows,column=columns,columnspan=the_span)
    
    global ypad
    ypad=10        
    r=1
    c=0
    entries=[]
    each_entry=[]
    entry_labels=[]
    def frame_label_entries(self,text,rows,columns):
        self.the_label=Label(self,text=text,font='Ariel 12 bold')
        self.entry_var=StringVar()
        self.entry=Entry(self,font='Ariel 10 bold',width=60,textvariable=self.entry_var)
        self.entries.append(self.entry_var)
        self.each_entry.append(self.entry)
        self.the_label.grid(row=rows,column=0,sticky=W,pady=ypad)
        self.entry.grid(row=rows,column=columns,sticky=W,padx=180)
        self.entry_labels.append(self.the_label)

        
    def frame_button(self,text,the_command,rows,columns):
        self.the_button=Button(self,text=text,bg='black',fg='white',relief='raised',
                       command=the_command)
        self.the_button.grid(row=rows,column=columns,sticky=W)

    

    combos=[]    
    combo_selections=[]
    combo_labels=[]
    def frame_combo(self,text,c_list,rows,columns):
        self.name_combo=Label(self,text=text,font='Ariel 12 bold')
        self.combo_var=StringVar()
        self.the_combobox=ttk.Combobox(self,font='Ariel 10 bold',width=30,
                                   background='red',textvariable=self.combo_var,values=c_list)
        self.combo_selections.append(self.combo_var)
        self.name_combo.grid(row=rows,column=0,sticky=W,pady=ypad)
        self.the_combobox.grid(row=rows,column=columns,sticky=W,padx=180)
        self.combos.append(self.the_combobox)
        self.combo_labels.append(self.name_combo)

    
    texts=[]
    def frame_text(self,rows,columns,the_height=20,the_width=120):
        self.the_text=Text(self,borderwidth=2,height=the_height,width=the_width,font=8,wrap=NONE)
        self.the_text.grid(row=rows,column=columns,columnspan=2,sticky=W)
        self.texts.append(self.the_text)


    radios=[]
    def radio_button(self,list_options,rows,columns,radio_comm=None):
        self.var=IntVar()
        val=1
        self.radio_comm=None
        for val, list_option in enumerate(list_options, start=1):
            self.the_radio=Radiobutton(self,text=list_option,pady = ypad,bg='red',command=radio_comm,variable=self.var,value=val)
            self.the_radio.grid(row=rows,column=columns,columnspan=1,sticky=W)
            self.radios.append(self.the_radio)
            rows=rows+1

    def the_list_box(self,rows,columns):
        self.list_box=Listbox(self,font=20,borderwidth=2,height=30,width=100)
        self.list_box.grid(row=rows,column=columns,columnspan=1,sticky=W)
        
    def the_tree(self,rows,columns,head_cols):
        self.my_tree=ttk.Treeview(self,height=20,columns=head_cols)
        self.my_tree.bind("<Double-1>", self.OnDoubleClick)
        self.my_tree.grid(row=rows,column=columns)
        
    def OnDoubleClick(self, event):
        item = self.my_tree.selection()[0]
        print("you clicked on", self.my_tree.item(item))
        d=self.my_tree.item(item)
        print('Your header is  '+d['values'][1])
        print('The data type is  '+d['values'][0])
    









            
