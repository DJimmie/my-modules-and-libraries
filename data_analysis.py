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
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
pd.options.display.precision=2
##% matplotlib inline
plt.style.use('ggplot')



def check_unique(the_data,the_header):
    the_count=the_data[the_header].value_counts(normalize=False)
    the_percentage=the_data[the_header].value_counts(normalize=True)
   
    unique_items=the_data[the_header].nunique()
    print('Number of unique: ',unique_items, '\n')
    print(the_count,' \n')
    print(the_percentage,' \n')
    plot_title='Breakdown of '+the_header+' Data'
    
    if (unique_items<=7):
        pie_plot(the_count,plot_title)
    elif(unique_items>7):
        Horz_Bar(the_data,the_header)


def the_hist(the_data):
    the_data.hist(bins=50,figsize=(15,15))
    the_data.plot(kind='density',subplots=True,layout=(5,5),sharex=False, figsize=(15,15))
    the_data.plot(kind='box',subplots=True,layout=(5,5),sharex=False, sharey=False,figsize=(15,15))
    #SKEW
    skew=the_data.skew()
    print('Skew:\n',skew)
    
    plt.show()


def pie_plot(a,the_title):
    labels=a.index
    plt.figure(figsize=(8,8))
    plt.title(the_title)
    plt.pie(a,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)

    plt.axis('tight')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def Horz_Bar(the_data,the_header):
    
    data_counts=the_data[the_header].value_counts(normalize=True)
   
    y_pos = np.arange(len(data_counts))
    
    plt.figure(figsize=(10,15))
    plt.barh(y_pos,data_counts)
    plt.xlabel('Percentage Breakdown')
    plt.xlim(0,1)

    plt.yticks(y_pos,data_counts.index, Rotation=0)
    plt.grid()
    plt.show()


def correlations(the_data):
    """CORRELATIONS"""

    correlations=the_data.corr(method='pearson')
    set_option('display.width',120)
    set_option('precision',3)
    print ('CORRELATION MATRIX:\n',correlations)

    #Correlation Matrix Plot
    header_names=the_data.columns.tolist()
    num_features=len(header_names)-1
    fig=plt.figure(figsize=(20,20))
    ax=fig.add_subplot(111)
    cax=ax.matshow(correlations,cmap='jet',vmin=-1,vmax=1)
    fig.colorbar(cax)
    ticks=np.arange(0,num_features,1)
    ax.set_xticks(ticks=ticks)
    ax.set_yticks(ticks=ticks)
    ax.set_xticklabels(header_names)
    ax.set_yticklabels(header_names)
    plt.show()
