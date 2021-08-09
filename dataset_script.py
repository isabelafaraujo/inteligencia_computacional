#adaptation of a dataset in format 
#word NER-tag 
#to the format
#word tag tag NER-tag

import pandas as pd
import csv

def read_file(file):
  data = pd.read_csv(file, sep='\t')
  return data

def insert_columns(data, qnt):
  for q in range(qnt): 
    data.insert(1, 'Tag' + str(q+1), 'O')
  return data
  
def export_dataset(data, path, name):
  data.to_csv(path+name, header=None, index=None, sep=' ', mode='a')
