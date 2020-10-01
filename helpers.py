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




def findK(df,limit): 
    
    # The elbow method would suggest that most of the improvement in the cluster scores happens prior to k=5.
    # The algorithm below allows for selection of k based on the diminishing benefits of increasing clusters. 
    # 5 clusters is being chosen, not just by the elbow method above as it also matches up with the 5 zones 
    # defined by the Polar (tm) methodology. 

    for k in range(len(df)):
        if k == len(df):
           print ("\nEnd of array reached.") 
        elif k == len(df): 
          improvement = 'None'
          print ("end of array reached prior to limit")
          print ("K=0")
        elif k > 0:
          improvement = (round(100*((df[k-1]-df[k])/df[k-1])))
          #print (k,round(df[k]/100000000,2),improvement)
          if improvement < limit:
                #print ("Improvement of {}% is less than lower limit of {}% for k = {}. k max is {} ".format(improvement,limit,k,len(df)))
                break
    print ("Maximum value of number of clusters (k) is: ",len(df))
    print ("Less than {}% improvement in score after k = {}".format(limit,k))