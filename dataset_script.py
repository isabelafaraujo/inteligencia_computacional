#adaptation of a dataset in NER format: conll2003 
#read_file1:
#word NER-tag 
#read_file2
#word _ tag NER-tag 
#to the format
#word tag tag NER-tag

import pandas as pd
import csv

pd.set_option('display.max_rows', None)

def read_file1(file):
  data = pd.read_csv(file, sep='\t')
  return data

def read_file2(file):
  df = pd.read_csv(file, sep=' ', header=None)
  data = df.iloc[:,[0,3]] 
  return data

def insert_columns(data, qnt):
  for q in range(qnt): 
    data.insert(1, 'Tag' + str(q+1), 'O')
  return data

def export_dataset(data, path, name):
  data.to_csv(path+name, header=None, index=None, sep=' ', mode='a')
