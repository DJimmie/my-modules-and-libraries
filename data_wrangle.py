
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


# In[ ]:


class DataWorld():
    """THIS IS THE PARENT CLASS FOR THE DATA TO BE STUDIED. IT'S PRIMARY PURPOSE IS TO RETREIVE THE SOURCE DATA AND ASSIGN IT
    AS A PANDAS DATAFRAME (the_data)"""
    
#     file_path=r'C:\Users\Crystal\Desktop\Programs\stock_analysis\daily_scan_data'
    
    def __init__(self):
        self.file_path='Enter the source file path'
        self.what='WTF'
        
    def get_data(self,source_file,source_file_type,**kwargs):
        """RETRIEVING THE DATA in CSV FORMAT"""
        self.source_file=source_file
        self.source_file_type=source_file_type
        self.source_file_name=self.source_file+'.'+self.source_file_type
#         self.location=DataWorld.file_path+'\\'+self.file_name
        self.location=self.file_path+'\\'+self.source_file_name
        
        if (self.source_file_type=='csv'):
            self.the_data=pd.read_csv(self.location,kwargs)
            
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
        self.the_data.rename(columns={old:new},inplace=True)
    
    def convert_data_types(self,the_header,convert_to):
        if (convert_to=='datetime'):
            self.the_data[the_header]=pd.to_datetime(self.the_data[the_header])
            #the_data[the_header] =  pd.to_datetime(the_data[the_header], format='%d%b%Y:%H:%M:%S.%f')
            self.view_data()
            return self.the_info

        if (convert_to=='float'):
            self.the_data[the_header]=self.the_data[the_header].iloc[0:None].str.replace(',','').astype('float')
            self.view_data()
            return self.the_info
            
        
            
    def drop_these_columns(self,header_list):
        print(header_list)
        self.the_data.drop(header_list, axis=1,inplace=True)

    def drop_these_rows(self,index_list):
        print(index_list)
        self.the_data.drop(index_list, axis=0,inplace=True)

    def drop_these_rows_num_index(self,a,b):
        print(a,b)
        self.the_data.drop(self.the_data.index[a:b],inplace=True)


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



        
