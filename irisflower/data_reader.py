import pandas as pd
'''
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica

'''

DATA_FILE_PATH = '/Users/felipe/Repos/Python/irisflower_classification/data/iris.data'
DATA_COLUMNS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'flower']

def read_data():
    data = pd.read_csv(DATA_FILE_PATH, header=None, names=DATA_COLUMNS)
    return data