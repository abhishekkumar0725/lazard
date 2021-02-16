import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def data_normalization(df, index):
    #mu, sigma = np.mean(df[index]), np.std(df[index])
    #return (df[index] - mu) /sigma
    sc = StandardScaler()
    return sc.fit_transform(np.array(df[index]).reshape(-1,1))


def text_to_one_hot(text, index):
    encoding = {}
    options = list(set(text[index]))
    lower_bound = (len(options)-1)//2
    for i, val in enumerate(options):
        encoding[val] = i - lower_bound
    return [encoding[val] for val in list(text[index])]

def open_h5(filepath):
    df = pd.read_hdf(filepath, key='default')
    df.to_csv(filepath.split('.')[0]+'.csv', index=False)
    return df