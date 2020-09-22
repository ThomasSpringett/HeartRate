import numpy as np
import pandas as pd

    
def oftype(x):
    if isinstance(x,pd.core.series.Series):
        print ('pandas series')
    elif isinstance(x,pd.DataFrame):
        print ("pandas DataFrame")
        df = x
        print (df.shape)
        percent = 100*(df.isnull().sum().sum()/(df.shape[0]*df.shape[1]))
        print ("\nThe total number of missing values: {} or {:.1f}%. \
        ".format(df.isnull().sum().sum(),percent))
        display (df.head())
    elif isinstance(x,np.ndarray):
        df = x
        print ("numpy",df.shape)
    elif isinstance(x,int):
        print ("Integer 32")
    elif isinstance(x,float):
        print ("float")
    elif isinstance(x,str):
        print ("string")
    elif isinstance(x,dict):
        print ("Dictionary")
        
def describe_df(df):
    try:
        print (df.shape)
        percent = 100*(df.isnull().sum().sum()/(df.shape[0]*df.shape[1]))
        print ("\nThe total number of missing values: {} or {:.1f}%. \
        ".format(df.isnull().sum().sum(),percent))
        display (df.head())
        #print (df.info())
        #print (df.dtypes) 
    except AttributeError:
        pass
    except NameError:
        pass
def restart():
    azdias_clean = pd.read_pickle("azdias_clean.pkl")
    pca2 = pickle.load(open('pca_robust_10', 'rb'))
    Xpca25 = pickle.load(open("Xpca10", 'rb'))
    return azdias_clean, pca10, Xpca10

class Limits1: 
    
    def __init__(self,cdc_moderate_low):
        self.cdc_moderate_low = cdc_moderate_low

class Limits2: 
    
    def __init__(self,cdc_moderate_low):
        self.cdc_moderate_low = cdc_moderate_low
class Limits5: 
    
    def __init__(self,cdc_moderate_low):
        self.cdc_moderate_low = cdc_moderate_low