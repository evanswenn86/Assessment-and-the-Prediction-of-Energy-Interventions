# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:32:16 2019

@author: seanl
"""

import os

abslote_path = os.path.abspath('.')

dataset1_file = abslote_path + "/6ddcd912-32a0-43df-9908-63574f8c7e77.csv"
dataset2_file = abslote_path + "/ast2018full.csv"

headname =['permitnumber','comments','issued_date','zip',
           'property_id','parcel_id','lat','long']
keyword_test = 'heat|solar|electric'

import pandas as pd
from pandas import DataFrame
    

def process_intervention_data_from_file(dataset_file):
    raw_data = pd.read_csv(dataset_file)[headname]
    # fill null
    raw_data['comments']=raw_data['comments'].fillna('null')

    # display all of the column value
    pd.set_option('display.max_columns', None)
    
    #select intervention related sample 
    df = pd.DataFrame(raw_data)
    df = df[df['comments'].str.contains(keyword_test)]

    # drop all the NAN longitude or latitude
    df.dropna(inplace=True)
    print(df)
    
process_intervention_data_from_file(dataset1_file)