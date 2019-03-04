
# coding: utf-8

# In[223]:


import pandas as pd
from pandas import set_option
from io import StringIO
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('ggplot')
from pandas.plotting import scatter_matrix
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
pd.options.display.precision=2
plt.style.use('ggplot')
import sys
import sqlite3
import logging
import webbrowser

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')



class DataWorld():
    """THIS IS THE PARENT CLASS FOR THE DATA TO BE STUDIED. IT'S PRIMARY PURPOSE IS TO RETREIVE THE SOURCE DATA AND ASSIGN IT
    AS A PANDAS DATAFRAME (the_data)"""
    
#     file_path=r'C:\Users\Crystal\Desktop\Programs\stock_analysis\daily_scan_data'
    
    def __init__(self):
        self.file_path='Enter the source file path'
        self.what='WTF'
        
    def get_data(self,source_file,source_file_type,**csvargs):
        """RETRIEVING THE DATA per the user slection of file type"""
        logging.info('def get_()data has been called')
        
        self.source_file=source_file
        self.source_file_type=source_file_type
        self.source_file_name=self.source_file+'.'+self.source_file_type
#         self.location=DataWorld.file_path+'\\'+self.file_name
        self.location=self.file_path+'\\'+self.source_file_name
        
        if (self.source_file_type=='csv'):
            self.the_data=pd.read_csv(self.location,**csvargs)
            
        elif(self.source_file_type=='sqlite3' or self.source_file_type=='db'):
            conn=sqlite3.connect(self.location)
            cur=conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            self.table_list=cur.fetchall()
            print(self.table_list)
            
            self.list_of_tables=[]
            for i in range(len(self.table_list)):
                print(self.table_list[i][0])
                self.list_of_tables.append(self.table_list[i][0])
            print(self.list_of_tables)

            self.the_data=pd.read_sql_query("SELECT * FROM "+self.list_of_tables[0],conn)
            cur.close()
            conn.close()
            
        pd.options.display.precision=2



    def look_at_SQL(self,sql_table,the_limit=5):
        
        logging.info('def look_at_SQL() has been called')
        
        conn=sqlite3.connect(self.location)
        cur=conn.cursor()
        self.the_data=pd.read_sql_query("SELECT * FROM "+sql_table,conn)

        cur.close()
        conn.close()
        
      
#     @classmethod
#     def specify_path(cls,new_path):
#         cls.file_path=new_path
        
    
    def view_data(self):
        """***(2-9-2019) Display data headers, data types and the null value counts
This information is displayed as a dataframe."""
        logging.info('def view_data() has been called')
         
        
##        print(self.the_data.info(),'\n')
##        print('Checking for null values: \n',self.the_data.isnull().sum())
##        print('\n')
##        print(self.the_data.head())
        

        headers=[]
        the_types=[]
        no_null_count=[]
        is_null_count=[]
        headers=self.the_data.columns.tolist()
        for i in headers:
            the_types.append(self.the_data[i].dtypes)
            no_null_count.append(self.the_data[i].notnull().sum())
            is_null_count.append(self.the_data[i].isnull().sum())

        info_data = {'headers': headers, 'data_types': the_types, 'non_null_count': no_null_count,'is_null_count': is_null_count}
        self.the_info=pd.DataFrame.from_dict(info_data)
       
   


# In[ ]:



class clean_the_data(DataWorld):
    
    def data_clean(self):
        """CLEANING THE HEADERS BY REMOVING SPACES & MAKING ALL LOWER CASE"""
        logging.info('def data_clean() has been called')
        #Removed the NaN columns

        #All of the columns named UNUSED
        p=self.the_data.loc[:, self.the_data.columns.str.contains('Unnamed')].head()
        #Removing the UNUSED columns
        self.the_data.drop(p,axis=1,inplace=True)
        #replacing header spaces with underscores 
        self.the_data.columns=self.the_data.columns.str.replace(' ','_')
        #replacing header dashes with underscores
        self.the_data.columns=self.the_data.columns.str.replace('-','_')
        #replacing header dashes with underscores
        self.the_data.columns=self.the_data.columns.str.replace('#','_')    
        #make all headers lower case
        self.the_data.columns=self.the_data.columns.str.lower()
    
##        return self.the_data.info()
        self.view_data()
        return self.the_info
    
    def rename_this_column(self,old,new):

        logging.info('def rename_this_column() has been called')
        self.the_data.rename(columns={old:new},inplace=True)
    
    def convert_data_types(self,the_header,convert_to):

        logging.info('def convert_data_types() has been called')
        
        if (convert_to=='datetime'):
            self.the_data[the_header]=pd.to_datetime(self.the_data[the_header])
            #the_data[the_header] =  pd.to_datetime(the_data[the_header], format='%d%b%Y:%H:%M:%S.%f')
            self.view_data()
            return self.the_info

        if (convert_to=='float'):
            self.the_data[the_header]=self.the_data[the_header].iloc[0:None].str.replace(',','').astype('float')
            self.view_data()
            return self.the_info

        if (convert_to=='object'):
            logging.info('convert_data_type to an object')
            self.the_data[the_header]=self.the_data[the_header].iloc[0:None].astype('object')
            self.view_data()
            return self.the_info
            
        
            
    def drop_these_columns(self,header_list):

        logging.info('def drop_these_columns() has been called')
        print(header_list)
        self.the_data.drop(header_list, axis=1,inplace=True)

    def drop_these_rows(self,index_list):
        print(index_list)
        self.the_data.drop(index_list, axis=0,inplace=True)

    def drop_these_rows_num_index(self,a,b):
        print(a,b)
        self.the_data.drop(self.the_data.index[a:b],inplace=True)

    def list_the_header_dtypes(self):

        logging.info('def list_the_header_dtypes() has been called')
        
        headers=self.the_data.columns.tolist()
        object_headers=[]
        int_headers=[]
        float_headers=[]
        for i in headers:
            if self.the_data[i].dtype.kind=='O':
                object_headers.append(i)
            elif self.the_data[i].dtype.kind=='i':
                int_headers.append(i)
            else:
                float_headers.append(i)
        return object_headers,int_headers,float_headers


# In[ ]:


class my_datasets(clean_the_data):
    
    def list_the_headers(self):
        print(self.the_data.columns.tolist())
    
    def data_subset(self,the_header_list):
        self.subset=self.the_data[the_header_list]

    def data_aggregates(self,the_header):
        agg=self.the_data[the_header].aggregate(['min', 'max','sum','mean','median','std','count'])
        return agg

    def check_unique(self,the_data,the_header):
        the_count=the_data[the_header].value_counts(normalize=False)
        the_percentage=the_data[the_header].value_counts(normalize=True)
       
        unique_test_areas=the_data[the_header].nunique()
        print('Number of unique: ',unique_test_areas, '\n')
        print(the_count,' \n')
        print(the_percentage,' \n')
        plot_title='Breakdown of '+the_header+' Data'

        plt.figure(figsize=(12,3))
        plt.subplot(1, 3, 1)
        play_count_kde=self.the_data[the_header].value_counts(normalize=False)
        play_count_kde.plot(kind='kde')

        plt.subplot(1, 3, 2)
        play_count_box=self.the_data[the_header].value_counts(normalize=False)
        play_count_box.plot(kind='box')

        plt.subplot(1, 3, 3)
        play_count_hist=self.the_data[the_header].value_counts(normalize=False)
        play_count_hist.hist(bins=20)

        plt.show()

        
##        if (unique_test_areas<=7):
##            pie_plot(the_count,plot_title)
##        elif(unique_test_areas>7):
##            Horz_Bar(the_data,the_header)


def pie_plot(a,the_title):
    labels=a.index
    plt.figure(figsize=(8,8))
    plt.title(the_title)
    plt.pie(a,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)

    plt.axis('tight')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def data_info(the_data):
    
    headers=[]
    the_types=[]
    no_null_count=[]
    is_null_count=[]
    headers=the_data.columns.tolist()
    for i in headers:
        the_types.append(the_data[i].dtypes)
        no_null_count.append(the_data[i].notnull().sum())
        is_null_count.append(the_data[i].isnull().sum())

    info_data = {'headers': headers, 'data_types': the_types, 'non_null_count': no_null_count,'is_null_count': is_null_count}
    the_info=pd.DataFrame.from_dict(info_data)
    return the_info



        
