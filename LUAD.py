import pandas as pd
import numpy as np

def correctLabels(df):
    labels = df.iloc[range(5)].drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2'],axis=1).copy()
    labels.index = labels['days_to_last_follow_up']
    labels = labels.transpose()
    labels = labels.reset_index()
    labels.replace("'--",np.nan,inplace=True)
    labels.drop(index=0,inplace=True)
    return labels

def getData(df):
    data = df[~df.index.isin(range(7))].drop(['Unnamed: 0','Unnamed: 2','days_to_last_follow_up'],axis=1).copy()
    data.index = data['Unnamed: 1']
    return np.array(data.drop('Unnamed: 1',axis=1).transpose()), data.index

class LUADDataViewer:
    def __init__(self,filelocation):
        df = pd.read_csv(filelocation,index_col=False)
        
        self.labels = correctLabels(df)
        self.data,self.index = getData(df)
    
    def getLabels(self,numberofyears=5):
        values = np.array(self.labels['days_to_death'])
        y = []
        for value in values:
            try:
                value=int(value)
                if np.isnan(value):
                    y.append(0)
                else:
                    if value<(365*numberofyears):
                        y.append(1)
                    else:
                        y.append(0)
            except:
                y.append(0)
        return np.array(y)
    
    def getData(self):
        return self.data
    
    def sampleNumber(self):
        return self.data.shape[0]
    
    def idnames(self):
        return self.index
    
