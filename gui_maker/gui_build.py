
import datetime as dt
from datetime import timedelta

try:
    import tkinter.ttk
    from tkinter import *
#     from tkinter.ttk import *
except:
    from tkinter import *

from tkinter import messagebox
from tkinter import filedialog

class UI(Tk):
    """WIndow and its attributes."""

    now=dt.date.today().strftime('%B %d, %Y')
    time_of_day=dt.datetime.today().strftime('%I:%M:%S %p')

    w=None

    def __init__(self,parent,*args,**kwargs):
        """Create the UI Window"""
        Tk.__init__(self,parent)
        self.parent=UI.w=parent

        banner_text=f'{kwargs["banner"]} - {UI.now}'
        self.window_colors=kwargs["win_color"]
        self.title(kwargs["title"])
        self.window_width=kwargs["window_width"]
        self.menubar=Menu(self)
        self.initialize()

        fg='white'
        self.banner=Label(self,text=banner_text,fg=fg,bg=self.window_colors,font='Ariel 30 bold')
        self.banner.grid(row=0,column=0,columnspan=3)
#         

    def initialize(self):
        """Set-up and configure the UI window"""
##        the_window_width=self.winfo_screenwidth()
        the_window_width=self.window_width
        the_window_height=self.winfo_screenheight()
        self.geometry(f'{the_window_width}x{the_window_height}+0+0')
#         self.attributes('-fullscreen', True)
        self['borderwidth']=4
        self['bg']=self.window_colors
        # self.menubar=Menu(self)
        self.menubar.add_command(label="Exit",font='ariel',command=self.bye_bye)
        self.menubar.add_command(label="Instructions",font='ariel',command=None)
        self.config(menu=self.menubar)

    def menu_build(self):
        # self.menubar=Menu(self)
        self.menubar.add_command(label="Create Project",font='ariel',command=None)
        self.config(menu=self.menubar)



    # self.gui_build()

    def bye_bye(self):
        """Close the UI Window on menu Exit"""
        self.destroy()


class Frames(Tk):
    """Frames amd their attributes"""
    def __init__(self,row,col,host=UI.w,*args,**kwargs):
        """Create the UI Window"""

        if 'sticky' in kwargs:
            sticky=kwargs['sticky']
        else:
            sticky=None

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=None

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=None

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='black'

        if 'banner_font' in kwargs:
            font=kwargs['banner_font']
        else:
            font ='Ariel 20 bold'

        if 'rowspan' in kwargs:
            rowspan=kwargs['rowspan']
        else:
            rowspan=1
        
        if 'columnspan' in kwargs:
            columnspan=kwargs['columnspan']
        else:
            columnspan=1

        self.F=Frame(host)
        self.F['background']=c=kwargs['bg']
        self.F['relief']=kwargs['relief']
        self.F['borderwidth']=5
        self.F.grid(row=row,column=col,pady=pady,padx=padx,sticky=sticky,rowspan=rowspan,columnspan=columnspan)
        banner_text=kwargs['banner_text']

        

        self.frame_banner=Label(self.F,text=banner_text,fg=fg,bg=c,font=font)
        self.frame_banner.grid(row=0,column=0,columnspan=5,pady=15)

# %%
class List_box(Tk):
    """Generate List Box"""
    def __init__(self,the_frame,name,row,col,*args,**kwargs):
        """Create the UI List Box with accompaning labels"""
        
        if 'list_items' in kwargs:
            self.list_box_items=kwargs['list_items']
        else:
            self.list_box_items=['TBD']


        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'

        if 'fw' in kwargs:
            fw=kwargs['fw']
        else:
            fw=10

        if 'height' in kwargs:
            height=kwargs['height']
        else:
            height=int(.25*fw)

        self.txt=name
        self.list_label=Label(the_frame,text=self.txt,bg='blue',fg='yellow',font='Ariel 12 bold')
        self.list_box=Listbox(the_frame,font=font, bg='cyan',borderwidth=2,height=height,width=fw,selectmode=SINGLE)
        

        self.list_label.grid(row=row,column=col,columnspan=1,pady=1,sticky=W)
        self.list_box.grid(row=(row+1),column=col,columnspan=1,pady=1,sticky=W)

        self.populate_list()

    def populate_list(self):

        for i,k in enumerate(self.list_box_items,start=1):
            self.list_box.insert(i,k)
            
class Textbox(Tk):

    def __init__(self,the_frame,name,row,col,*args,**kwargs):
        """Create the UI List Box with accompaning labels"""

        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'

        if 'width' in kwargs:
            width=kwargs['width']
        else:
            width=10

        if 'height' in kwargs:
            height=kwargs['height']
        else:
            height=10

        if 'state' in kwargs:
            state=kwargs['state']
        else:
            state=NORMAL

        if 'sticky' in kwargs:
            sticky=kwargs['sticky']
        else:
            sticky=W

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=1

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=1

        

        self.text_box_label=Label(the_frame,text=name,bg='blue',fg='yellow',font='Ariel 12 bold')

        self.text_box=Text(the_frame,
        borderwidth=1,
        height=height,
        width=width,
        font=font,
        wrap=WORD,
        state=state)

        self.text_box_label.grid(row=row,column=col,columnspan=1,pady=pady,sticky=sticky)
        self.text_box_label.update()
        p=self.text_box_label.winfo_reqheight()
        self.text_box.update()
        self.text_box.grid(row=(row+0),column=col,columnspan=1,pady=pady+p,sticky=sticky)


class CheckBoxes(Tk):
    
    def __init__(self,the_frame,name,check_label,row,col,command,*args,**kwargs):
        """Create the UI Checkbox Box with accompaning labels"""
        
        self.check_box_label=Label(the_frame,text=name,bg='blue',fg='yellow',font='Ariel 12 bold')

        self.var=IntVar()
        self.check_box=Checkbutton(master=the_frame,
        text=check_label,
        highlightcolor='red',
        selectcolor='black',
        bg=the_frame['background'],
        fg='white',
        font='Ariel 15 bold',
        variable=self.var,
        command=command)

        self.check_box_label.grid(row=row,column=col,columnspan=1,pady=1,sticky=W)
        self.check_box.grid(row=(row+1),column=col,pady=1,sticky=W)

class Labels(Tk):
    def __init__(self,the_frame,name,row,col,*args,**kwargs):
        """Create the UI Labels"""

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=None

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=None

        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'
        
        if 'bg' in kwargs:
            bg=kwargs['bg']
        else:
            bg='blue'

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='yellow'
        
        self.label=Label(the_frame,text=name,bg=bg,fg=fg,font=font)
        self.label.grid(row=row,column=col,columnspan=1,pady=pady,padx=padx,sticky=W)

class Buttons(Tk):
    def __init__(self,the_frame,name,row,col,width,command,*args,**kwargs):
        """Create the UI Buttons with accompaning labels"""

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=None

        if 'padx' in kwargs:
            padx=kwargs['padx']
        else:
            padx=None

        if 'font' in kwargs:
            font=kwargs['font']
        else:
            font='Ariel 12 bold'
        
        if 'bg' in kwargs:
            bg=kwargs['bg']
        else:
            bg='black'

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='yellow'

        if 'sticky' in kwargs:
            sticky=kwargs['sticky']
        else:
            sticky=None


        self.button = Button(the_frame, 
        text=name,
        width=width,
        fg=fg,
        bg=bg,
        font=font,
        command=command)

        self.button.grid(row=row,column=col,pady=pady,padx=padx,sticky=sticky)

class Combos(Tk):
    def __init__(self,the_frame,name,row,col,drop_down_list,*args,**kwargs):
        """Create the UI Entry fields with accompaning labels"""
        
        self.txt=name
        self.combo_label=Label(the_frame,text=self.txt,bg='blue',fg='yellow',font='Ariel 12 bold')
        
        if 'type' in kwargs:
            if (kwargs['type']=='IntVar'):
                self.combo_var=IntVar()
            elif (kwargs['type']=='DoubleVar'):
                self.combo_var=DoubleVar()
        else:
            self.combo_var=StringVar()

        if 'pady' in kwargs:
            pady=kwargs['pady']
        else:
            pady=1

        if 'fw' in kwargs:
            fw=kwargs['fw']
        else:
            fw=30

        if 'state' in kwargs:
            state=kwargs['state']
        else:
            state=NORMAL
        

        self.combo_box_list=drop_down_list
        self.combo=ttk.Combobox(the_frame,font='Ariel 15 bold',width=fw,
                                   background='yellow',textvariable=self.combo_var,
                                   values=self.combo_box_list,
                                   state=state)
        self.combo_label.grid(row=row,column=col,columnspan=1,pady=pady,sticky=W)
        self.combo.grid(row=(row+1),column=col,columnspan=1,pady=pady,sticky=W)


class Entries(Tk):
    def __init__(self,the_frame,name,row,col,fw=30,*args,**kwargs):
        """Create the UI Entry fields with accompaning labels"""
        field_widths=fw
        self.txt=name
        self.entry_label=Label(the_frame,text=self.txt,bg='blue',fg='yellow',font='Ariel 12 bold')

        if 'type' in kwargs:
            if (kwargs['type']=='IntVar'):
                self.entry_var=IntVar()
            elif (kwargs['type']=='DoubleVar'):
                self.entry_var=DoubleVar()
        else:
            self.entry_var=StringVar()
        
        if 'state' in kwargs:
            state=kwargs['state']
        else:
            state='normal'

        self.entry=Entry(the_frame,font='Ariel 15 bold',width=field_widths,
                                   background='yellow',textvariable=self.entry_var,highlightbackground='pink',highlightthickness=5,state=state)
        self.entry_label.grid(row=row,column=col,columnspan=1,pady=1,sticky=W)
        self.entry.grid(row=(row+1),column=col,columnspan=1,pady=1,sticky=W)


class RadioButtons(Tk):
    def __init__(self,the_frame,name,row,col,radio_dict,*args,**kwargs):
        """Create the UI radiobuttons with accompaning labels"""
        # field_widths=fw

        if 'bg' in kwargs:
            bg=kwargs['bg']
        else:
            bg='blue'

        if 'fg' in kwargs:
            fg=kwargs['fg']
        else:
            fg='yellow'

        if 'font' in kwargs:
            font=kwargs['fg']
        else:
            font='Ariel 12 bold'

        self.var = IntVar()

        if 'type' in kwargs:
            if (kwargs['type']=='StringVar'):
                self.var=StringVar()
        else:
            self.var=IntVar()

        self.txt=name
        self.radio_label=Label(the_frame,text=self.txt,bg=bg,fg=fg,font='Ariel 12 bold')
        self.radio_label.grid(row=row,column=col,columnspan=1,pady=1,sticky=W)
        row+=1
        for key, val in radio_dict.items():
                self.radio=Radiobutton(the_frame, 
                        text=key,
                        padx = 20, 
                        variable=self.var, 
                        command=None,
                        value=val,
                        bg=bg,fg=fg,
                        selectcolor='navy',
                        font=font)
                    
                # print(row)
                self.radio.grid(row=(row),column=col,columnspan=1,pady=1,sticky=W)
                row+=1


    