import h5py
import numpy as np
import pandas as pd

'''
def open_h5(filepath):
    dataset = h5py.File(filepath, 'r')
    grid = dataset['default']
    keys = list(grid.keys())
    df = pd.DataFrame()
    #df['security'] = grid['block0_values'][0]
    df['date'] = grid['block1_values']
    df['monthly_returns'] = [grid['block2_values'][i][0] for i in range(len(grid['block2_values']))]
    df['monthly_returns_f1'] = [grid['block2_values'][i][1] for i in range(len(grid['block2_values']))]
    print(len(set(grid['block0_values'][0])))
'''

def open_pandas(filepath):
    df = pd.read_hdf(filepath, key='default')
    df.to_csv(filepath.split('.')[0]+'.csv', index=False)

if __name__ == '__main__':
    filepath = 'data/x_df_comp_factors/x_df_comp_factors.h5'
    open_pandas(filepath)