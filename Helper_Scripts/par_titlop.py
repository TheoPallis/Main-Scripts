import pandas as pd
import os
from pathlib import Path



file_name = 'mapping recovery.xlsx'
folder_path = r'../TFT_20_12-main/Helper Scripts/file_name'
# Construct the full path to the file
mapping_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)

def apply_recovery_mapping(df) :
    mapping_df = pd.read_excel(mapping_path, sheet_name='Mapping')
    date = mapping_df['Ημερομηνία τιτλοποίησης']
    date = pd.to_datetime(date)
    mapping_df['Ημερομηνία τιτλοποίησης'] = date.dt.strftime('%d/%m/%Y')
    merged_df = pd.merge(df,mapping_df,left_on='date_titlop',right_on='Ημερομηνία τιτλοποίησης',how = 'left')
    return merged_df
    