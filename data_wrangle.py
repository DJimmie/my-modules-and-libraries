
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
import seaborn as sns
import pickle
sns.set(style="whitegrid", color_codes=True)
plt.style.use ('seaborn-whitegrid')

open("myProgramLog.txt", "w").close()
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
        logging.info('data_wrangle: def get_()data has been called')
        
        self.source_file=source_file
        self.source_file_type=source_file_type
        self.source_file_name=self.source_file+'.'+self.source_file_type
#         self.location=DataWorld.file_path+'\\'+self.file_name
        self.location=self.file_path+'\\'+self.source_file_name
        logging.debug(f'data_wrangle: self.source_file_name= {self.source_file_name}')
        logging.debug(f'data_wrangle: self.file_path= {self.file_path}')
        logging.debug(f'data_wrangle: self.location= {self.location}')
        
        if (self.source_file_type=='csv'):
            logging.info('data_wrangle: accessing a csv file')
            self.the_data=pd.read_csv(self.location,**csvargs)
            
        elif(self.source_file_type=='sqlite3' or self.source_file_type=='db'):
            logging.info('data_wrangle: accessing a sqlite database file')
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

        elif (self.source_file_type=='pickle'):
            logging.info('data_wrangle: accessing a pickle file')
            infile = open(self.location,'rb')
            new_df = pickle.load(infile)
            infile.close()
            self.the_data=new_df
            
            
    
            
        pd.options.display.precision=2



    def look_at_SQL(self,sql_table,the_limit=5):
        
        logging.info('data_wrangle:def look_at_SQL() has been called')
        
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
        logging.info('data_wrangle:def view_data() has been called')
         
        
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
        logging.info('data_wrangle:def data_clean() has been called')
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

        logging.info('data_wrangle:def rename_this_column() has been called')
        self.the_data.rename(columns={old:new},inplace=True)
    
    def convert_data_types(self,the_header,convert_to):

        logging.info('data_wrangle:def convert_data_types() has been called')
        
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

        logging.info('data_wrangle:def drop_these_columns() has been called')
        print(header_list)
        self.the_data.drop(header_list, axis=1,inplace=True)

    def drop_these_rows(self,index_list):
        print(index_list)
        self.the_data.drop(index_list, axis=0,inplace=True)

    def drop_these_rows_num_index(self,a,b):
        print(a,b)
        self.the_data.drop(self.the_data.index[a:b],inplace=True)

    def list_the_header_dtypes(self):

        logging.info('data_wrangle:def list_the_header_dtypes() has been called')
        
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

    def type_and_null_check(self,the_header):
        not_null=self.the_data[the_header].notnull().sum()
        nulls=self.the_data[the_header].isnull().sum()
        data_type=self.the_data[the_header].dtype
        info_dict={'non_nulls':not_null,'nulls':nulls,'data_type':data_type}
        return info_dict
        

    def check_unique(self,the_data,the_header):

        logging.info('data_wrangle:def check_unique() has been called')
        
        self.the_count=the_data[the_header].value_counts(normalize=False)
        self.the_percentage=the_data[the_header].value_counts(normalize=True).round(2)
        

##        tnc=type_and_null_check(self,the_data,the_header)
##        print(tnc,'\n')
        
        my_dict={'freq'+the_header:self.the_count, '% of Total': (self.the_percentage*100)}
        unique_items=the_data[the_header].nunique()

        unique_results=pd.DataFrame.from_dict(my_dict)
        print(f'Number of unique {the_header}:',unique_items, '\n')
        print(unique_results.head(10))

        number_of_items=f'Number of unique {the_header}: {unique_items}'
               
##        print(self.the_count,' \n')
##        print(self.the_percentage,' \n')

        plot_title='Breakdown of '+the_header+' Data'

##        if (unique_items<=7):
##            pie_plot(self.the_count,plot_title)
##        elif(unique_items>7):
##            Horz_Bar(self.the_percentage[0:10]*100,the_header)




##        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))
        
        fig = plt.figure(figsize=(12, 5))
        axes=plt.axes()

        #Pie
        if (unique_items<=7):
            labels=self.the_count.index
            axes.set_title(plot_title)
            axes.pie(self.the_count,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
            axes.axis('equal')
        else:
            #Bar
            a=self.the_percentage[0:10]*100
            logging.debug(f'data type is: {a.dtype}')
            y_pos = np.arange(len(a))
            

            x_min=a.min()
            x_max=a.max()

            axes.set_title('Breakdown of '+the_header)
            axes.grid()
            axes.barh(y_pos,a,color='blue')
            axes.set_xlabel('Percentage Breakdown')
            axes.set_xlim(0,x_max)
            axes.set_xscale('linear')
            
            logging.debug(f'ypos : {y_pos}')                   
            axes.set_yticks(y_pos)   #y_pos
            axes.set_ylabel(f'{the_header}')
            axes.grid()

    
        plt.tight_layout()
        plt.show()

        

        return fig,unique_results,number_of_items

    def hist_box_kde(self,the_data,the_header):
        logging.info('data_wrangle:def hist_box_kde() has been called')

##        tnc=type_and_null_check(self,the_data,the_header)
##        print(tnc,'\n')
##        print(the_data[the_header].head(10),'\n')

        the_tabulation=the_data[the_header].aggregate(['min', 'max','sum','mean','median','std','count'])
        print(the_tabulation)
##        print(the_data[the_header].describe())

        my_dict={'stats':the_tabulation}
        self.stat_results=pd.DataFrame.from_dict(my_dict)
        self.stat_results.style.format("{:.2f}")
        
##        print(self.stat_results.style.format("{:.2f}"))
        
        # Initialize the plot
##        fig = plt.figure(figsize=(20,10))
##        ax1 = fig.add_subplot(131)
##        ax2 = fig.add_subplot(132)
##        ax3 = fig.add_subplot(133)

####        ax1.hist(x=the_data[the_header],bins=50)
####        ax1=sns.distplot(the_data[the_header], hist=True, kde=True, bins=int(180/5), color = 'darkblue', hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4})
##        ax3=the_data[the_header].plot(kind='hist')
##        ax2.violinplot(the_data[the_header])
        
##        ax2=the_data[the_header].plot(kind='kde')

##        ax3.boxplot(the_data[the_header])
##        ax1=the_data[the_header].plot.box()

        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))
        axes[0].violinplot(the_data[the_header])
        axes[1].boxplot(the_data[the_header])
        axes[2]=sns.distplot(the_data[the_header],
                             hist=True, kde=True,
                             bins=int(180/5),
                             color = 'darkblue',
                             hist_kws={'edgecolor':'black'},
                             kde_kws={'linewidth': 4})
        
        plt.show()
        the_metrics=self.stat_results
##        the_metrics=the_tabulation
        metrics_frame_header='Parameters'
        return fig,the_metrics,metrics_frame_header

        

        


def pie_plot(a,the_title):
    labels=a.index
    plt.figure(figsize=(8,8))
    plt.title(the_title)
    plt.pie(a,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)

    plt.axis('tight')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def Horz_Bar(a,the_header):
    
    logging.info('def Horz_Bar() has been called')

    y_pos = np.arange(len(a))

    x_min=a.min()
    x_max=a.max()

    plt.figure(figsize=(10,15))
    plt.title('Breakdown of '+the_header)
    plt.grid()
    plt.barh(y_pos,a)
    plt.xlabel('Percentage Breakdown')
    plt.xlim(0,x_max)
    plt.xscale('linear')
                       
    plt.yticks(y_pos,a.index, Rotation=0)
    plt.ylabel(f'{the_header}')
    plt.grid()
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



        
