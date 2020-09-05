import pandas as pd
import numpy as np
import datetime as dt
from datetime import timedelta
import re
import sqlite3
import os
import sys
import time

from tkinter import messagebox

## FUNCTIONS-----------------FUNCTIONS-----------------FUNCTIONS

def database_server():
    # server='C:/Users/Crystal/Desktop/Programs/Systems-Database/hctc_systems_database.db'
    server='C:/Users/JDowd/OneDrive - Schlumberger/Programming/TRIS-database/HCTC_TRIS_database.db'
    return server

def query_list(the_sql_command):
    """Query the database for combobox drop down values list"""
    
    print (the_sql_command)

    try:
        query=query_the_database(the_sql_command) 
        # query=executeTheCommand(the_sql_command) 
        header=query.columns[0]
        combo_box_list=list(query[header])
    except:
        combo_box_list=['a','b','c']

    return combo_box_list

def query_the_database(the_sql_command):
    
    sqlite_server=database_server()
    try:
        conn=sqlite3.connect(sqlite_server)
        cur=conn.cursor()
        results=pd.read_sql_query(sql=the_sql_command,con=conn, index_col=None)
    except:
        results=pd.DataFrame(data={'N/A': ['Enter Item']})
        messagebox.showerror('UNABLE TO ACCESS DATABASE','UNABLE TO ACCESS DATABASE: Server is not responding or query is invalid. Try Again or See Administrator.')
        # sys.exit()

    return results

def executeTheCommand(the_sql_command,values=None):
    
    sqlite_server=database_server()
    try:
        conn=sqlite3.connect(sqlite_server)
        cur=conn.cursor()
        if (values==None):
            cur.execute(the_sql_command)
        else:
            cur.execute(the_sql_command,values)
        data = cur.fetchall()
        conn.commit()
        print ('Database Upload Complete')
    except:
        print('UNABLE TO ACCESS DATABASE. TRY AGAIN')
        messagebox.showerror('UNABLE TO ACCESS DATABASE','UNABLE TO ACCESS DATABASE: Server is not responding or query is invalid. Try Again or See Administrator.')