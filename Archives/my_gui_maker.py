import tkinter.ttk
from tkinter import filedialog
from tkinter import *
import os
import sys
import pandas as pd
from pandas import set_option

""" (1-11-19) This module contains the class for the Tkinter objects.
It allows the user to build custom GUIs"""


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
        val=0
        self.radio_comm=None
        for val, list_option in enumerate(list_options, start=0):
            self.the_radio=Radiobutton(self,text=list_option,pady = ypad,bg='red',command=radio_comm,variable=self.var,value=val)
            self.the_radio.grid(row=rows,column=columns,columnspan=1,sticky=W)
            self.radios.append(self.the_radio)
            rows=rows+1

    def the_list_box(self,rows,columns):
        self.list_box=Listbox(self,font=20,borderwidth=2,height=30,width=100)
        self.list_box.grid(row=rows,column=columns,columnspan=1,sticky=W)
        
##    def the_tree(self,rows,columns,head_cols):
##        self.my_tree=ttk.Treeview(self,height=20,columns=head_cols)
##        self.my_tree.bind("<Double-1>", self.OnDoubleClick)
##        self.my_tree.grid(row=rows,column=columns)


    tree_list=[]
    def the_tree(self,rows,columns,df):

        head_cols=tuple(df.columns.tolist())
        self.my_tree=ttk.Treeview(self, height=10,columns=head_cols)
        self.my_tree.bind("<Double-1>", self.OnDoubleClick)
        self.tree_list.append(self.my_tree)
        
# Create header and column properties for the index
        self.my_tree.heading('#0',text='Index',anchor=CENTER)
        self.my_tree.column(column='#0',width=50,anchor='center')
        
        #     Creating the headers for the data 
        for col_num,i in enumerate(head_cols,1):
            col_index='#'+str(col_num)
            self.my_tree.heading(col_index,text=i,anchor=CENTER)
            self.my_tree.column(column=i,width=80,anchor='center')
            
        #     Creating (inserting) the index column values
        for j in range(0,len(df)):
            self.my_tree.insert('',str(j),'index'+str(j),text=str(j),tag='blue')
            
        #     Setting the data values to the cooresponding index
            for k,sd in enumerate(head_cols,0):
                self.my_tree.set(item='index'+str(j),column=sd,value=df[sd].iloc[j])
        
        
        yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.my_tree.yview)
        xscrollbar = ttk.Scrollbar(self, orient='horizontal', command=self.my_tree.xview)
##        self.my_tree['yscroll'] = yscrollbar.set
##        self.my_tree['xscroll'] = xscrollbar.set

        self.my_tree.grid(row=rows,column=columns,sticky=W)

##        yscrollbar.grid(row=rows, column=columns+1, sticky='ns',in_=self.the_frame)
##        xscrollbar.grid(row=rows+1, column=columns, sticky='we',in_=self.the_frame)

        yscrollbar.grid(row=rows, column=columns+1, sticky='ns')
        xscrollbar.grid(row=rows+1, column=columns, sticky='we')
        
        yscrollbar.config(command=self.my_tree.yview)
        xscrollbar.config(command=self.my_tree.xview)
        
        self.my_tree.configure(yscrollcommand = yscrollbar.set, xscrollcommand = xscrollbar.set, selectmode="browse")
        
        
    def OnDoubleClick(self, event):
        item = self.my_tree.selection()[0]
        print("you clicked on", self.my_tree.item(item))
        d=self.my_tree.item(item)
        print('Your header is  '+d['values'][1])
        print('The data type is  '+d['values'][0])


##    
    def my_dlist_canvas(self,rows,columns,df):
        self.dlist_canvas=Canvas(self,bd=0, highlightthickness=0,bg="yellow")
        self.dlist_canvas.configure(width=500,height=200)

        self.Lframe=Frame(self.dlist_canvas)
        set_option('precision',3)
        index_count=df.index.shape[0]
        head_cols=tuple(df.columns.tolist())
        col=0
        for col_num,i in enumerate(head_cols,0):
            self.dlist=Listbox(self.Lframe,width=15,height=1)
            self.dlist.insert(END,i)
            self.dlist.configure(bg="black",fg="white")
            self.dlist.grid(row=1,column=col_num,sticky=W)
            col=col+1
        
        for i in head_cols:
            col_index=head_cols.index(i)
            row_index=2
#             print(col_index,row_index,len(df))
            for p in range(len(df)):
                self.dlist=Listbox(self.Lframe,width=15,height=1) 
                data=df.iloc[p][col_index]
                self.dlist.insert(END,data)
                self.dlist.grid(row=row_index,column=col_index,sticky=W)
                row_index=row_index+1

##            print ('frame width: ',self.Lframe.winfo_width())
        self.data_window=self.dlist_canvas.create_window(0,0,window=self.Lframe,anchor='nw',tags=('data_holder'))
            
        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.dlist_canvas.yview)
        self.xscrollbar = ttk.Scrollbar(self, orient='horizontal', command=self.dlist_canvas.xview)
        
        self.yscrollbar.pack(side=RIGHT,fill=Y)

        self.dlist_canvas.config(yscrollcommand = self.yscrollbar.set)
        self.dlist_canvas.config(xscrollcommand = self.xscrollbar.set)  
        self.xscrollbar.pack(side=BOTTOM,fill=X)
        
        self.dlist_canvas.pack(side=LEFT)

##        self.dlist_canvas.grid(row=rows,column=columns,sticky=W)
        
    
        self.Lframe.bind("<Configure>", self.OnFrameConfigure)
##        self.dlist_canvas.bind('<Configure>', self.FrameWidth)
        

    def FrameWidth(self, event):
        canvas_width = event.width
        self.dlist_canvas.itemconfig(self.data_window, width=canvas_width)
##        self.dlist_canvas.config(width=canvas_width)

    def OnFrameConfigure(self, event):
        self.dlist_canvas.configure(scrollregion=self.dlist_canvas.bbox('data_holder'))
#         print('the data_window bbox: ',self.dlist_canvas.bbox('data_holder'))


    def adjust_index_geo(self, event):
        """fixes the index canvas in a confined geometry"""
        canvas_width = event.width
        canvas_height=event.height
        self.dlist_canvas.itemconfig(self.data_window, width=canvas_width, height=canvas_height)
        self.dlist_canvas.config(width=canvas_width,height=canvas_height)




                        








            
