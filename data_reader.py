import datatable

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

DATA_FILE_PATH = 'data/iris.data'
DATA_COLUMNS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'flower']

def read_data():
    data = datatable.fread(file=DATA_FILE_PATH, columns=DATA_COLUMNS)
    return data


read_data()