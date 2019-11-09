# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:32:16 2019

@author: seanl
"""
dataset1_file = "/Users/seanl/Documents/506/final_project/6ddcd912-32a0-43df-9908-63574f8c7e77.csv"
dataset2_file = "/Users/seanl/Documents/506/final_project/fy19fullpropassess.csv"

headname =['permitnumber','comments','issued_date','zip',
           'property_id','parcel_id','lat','long']
keyword_test = 'heat|solar|electric'

import pandas as pd
from pandas import DataFrame
    

def process_intervention_data_from_file(dataset_file):
    raw_data = pd.read_csv(dataset_file)[headname]
    #fill null
    raw_data['comments']=raw_data['comments'].fillna('null')
    
    #select intervention related sample 
    df = pd.DataFrame(raw_data)
    df = df[df['comments'].str.contains(keyword_test) ]
    print(df)    
    
process_intervention_data_from_file(dataset1_file)