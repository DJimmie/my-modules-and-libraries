import gui_build as gb

try:
    import tkinter.ttk
    from tkinter import *
    # from tkinter.ttk import *
except:
    from tkinter import *


class UserInterface():
    """Parent class for the UI. Instantiates the composit Window.
    User Interface with fields for entering a data to the database. 
    Also, when the UI is launched, username is retrieved."""

    def __init__(self):
        """Interface build."""
        gb.UI(None,title='Autofill',
        banner='COMBOBOX AUTUFILL',
        win_color='#003366',
        window_width=800,
        window_height=800)

        SystemGui()
        
        mainloop()  


class SystemGui():

    def __init__(self):
        self.build_the_gui()

    def build_the_gui(self):

        self.j_frame=gb.Frames(row=1,col=1,bg='brown',relief='raised',
        banner_font='Ariel 30 bold',
        banner_text='Autofill',
        fg='yellow')

        self.a=['Lexi','Lexus','Lice','Love','fog','fire','fly','fluffy','creamy']

        self.systemID=gb.Entries(self.j_frame.F,name='SYSTEM',row=1,col=0)
        self.my_drop_box=gb.Combos(self.j_frame.F,name='Type in Here',row=3,col=0,drop_down_list=self.a)

        # self.my_drop_box.combo.focus_set()
        # self.systemID.entry.focus_set()

        # self.my_drop_box.combo.bind("<FocusIn>", lambda x:self.see_what_happens())
        # self.my_drop_box.combo.bind("<Return>", lambda x:self.see_what_happens())
        # self.my_drop_box.combo.bind("<FocusOut>", lambda x:self.see_what_happens())
        self.my_drop_box.combo.bind("<KeyRelease>", lambda x:self.see_what_happens())
        # self.my_drop_box.combo.bind("<<ComboboxSelected>>", lambda x:self.see_what_happens())

        # self.my_drop_box.combo.validate='key'
        # self.my_drop_box.combo.config(validatecommand=(lambda x:self.see_what_happens,'%W'))

        # self.my_drop_box.validate='all'
        # self.my_drop_box.combo.config(validatecommand=lambda x:self.see_what_happens)

    def see_what_happens(self):
        
        w=self.my_drop_box.combo.get()
        print(w)
        
        new_list=[]
        for i in self.a:
            print (i)
            if (w in i):
                new_list.append(i)
            
        if (len(new_list)!=0):
            self.my_drop_box.combo['values']=new_list

        print(self.a)
        print(self.my_drop_box.combo['values'])
        

        self.my_drop_box.combo.event_generate('<Down>')

        
        

UserInterface()