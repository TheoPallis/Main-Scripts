#
# Original

import pandas as pd
import numpy as np
 
from Helper_Scripts.format_cols import (tou,onoma_gen,eponimo_gen,cities,check_for_εταιρεία_gen,add_3869)
from Helper_Scripts.combine_columns_custom_gen  import create_the_concatenated_string
from Helper_Scripts.set_values import sxesi_dict,sxesi_order_dict
# from olografos_clean import *


def fill_cols(df,selected_columns) :
    if 'last_name' in selected_columns.keys(): 
        df["Επώνυμο_γεν"] = selected_columns['last_name'].apply(eponimo_gen)
        selected_columns["last_name"] = df["Επώνυμο_γεν"] 
    
    if 'first_name' in selected_columns.keys() :
        df["Άρθρο_γεν"] = selected_columns['first_name'].apply(tou)        
        df["Όνομα_γεν"] = selected_columns['first_name'].apply(onoma_gen)     
        # df["Όνομα_γεν"] = df["Όνομα_γεν"].fillna(df['Επώνυμο_γεν'])
        df['Εταιρείας'] = df.apply(lambda row: check_for_εταιρεία_gen(row,"Της εταιρείας",selected_columns), axis=1)
        df['Έδρα'] = df.apply(lambda row: check_for_εταιρεία_gen(row,"η οποία εδρεύει",selected_columns), axis=1)
        df["Άρθρο_γεν"] = df.apply(lambda row: check_for_εταιρεία_gen(row,"Της εταιρείας",selected_columns) if check_for_εταιρεία_gen(row,"Της εταιρείας",selected_columns) else row["Άρθρο_γεν"], axis=1)
        selected_columns["first_name"] = df["Όνομα_γεν"] 
        selected_columns["article"] = df["Άρθρο_γεν"] 

    if 'city' in selected_columns.keys() : 
        df['City'] = selected_columns['city'].apply(cities)
        selected_columns["city"] = df["City"] 
    
    if 'father_name' in selected_columns.keys() :
       df['Father_name'] = selected_columns['father_name'].apply(onoma_gen).replace("","-")
       selected_columns['father_name'] = df['Father_name']

    if 'relationship' in selected_columns.keys() :
       df['relationship'] = selected_columns['relationship'].map(sxesi_dict)
       selected_columns['relationship']  =df['relationship']
       df['Order_Σχέση_Ενεχομένων'] = df['relationship'].map(sxesi_order_dict)  
    if '3869' in selected_columns.keys():
        column_name = selected_columns['3869'].name
        df['3869'] = selected_columns['3869'].apply(lambda value: add_3869(value, column_name))


    print('Formatted all of the columns')
    return df 

def trim_concatenated_string(df,selected_columns) :
    if 'father_name' in selected_columns.keys() :
        df["Στοιχεία_Γεν_Custom"] =  df["Στοιχεία_Γεν_Custom"].apply(lambda x : str(x).replace(" , ",  ", ")) 
        return df


# df["Στοιχεία_Γεν_Custom"].str.replace("του -, κατοίκου", ", η οποία εδρεύει στην περιοχή"),
            
def apply_edreuei(df) :
    df["Στοιχεία_Γεν_Custom"] = np.where(
            df['Εταιρείας'] == "Της εταιρείας",df["Στοιχεία_Γεν_Custom"].str.replace(" του - , κατοίκου", ", η οποία εδρεύει στην περιοχή").str.replace("  , η οποία εδρεύει",", η οποία εδρεύει"),
            df["Στοιχεία_Γεν_Custom"]
            )

    return df


def trim_vat(df,selected_columns) :
    # selected_columns['vat'] = selected_columns['vat'].str.replace("ΑΦΜ 0","ΑΦΜ ")
    return df

# Optimised wip
# import pandas as pd
# import numpy as np
# from set_cols_and_vars import (check_for_εταιρεία_gen,check_for_εταιρεία_edra,combine_columns_custom_gen)
# from format_cols import (tou,onoma_gen,eponimo_gen,cities)
# from set_cols_and_vars import (check_for_εταιρεία_gen,check_for_εταιρεία_edra,combine_columns_custom_gen)
# from set_values import sxesi_dict,sxesi_order_dict
# # from olografos_clean import *

# import pandas as pd
# import numpy as np
# from set_cols_and_vars import check_for_εταιρεία_gen, combine_columns_custom_gen
# from format_cols import tou, onoma_gen, eponimo_gen, cities
# from set_values import sxesi_dict, sxesi_order_dict

# def fill_cols(df, selected_columns, selected_columns):
#     """
#     Processes and fills columns in a DataFrame based on selected columns and variable columns dictionary.

#     Args:
#     df (pd.DataFrame): The DataFrame to be processed.
#     selected_columns (dict): A dictionary indicating which columns are to be processed.
#     selected_columns (dict): A dictionary containing data for generating or modifying specific columns.

#     Returns:
#     pd.DataFrame: The processed DataFrame.
#     """

#     # Process 'Επώνυμο' column
#     if 'Επώνυμο' in selected_columns:
#         df["Επώνυμο_γεν"] = selected_columns['last_name'].apply(eponimo_gen)

#     # Process 'Όνομα' column
#     if 'Όνομα' in selected_columns:
#         df = process_onoma_column(df, selected_columns)

#     # Process 'Πόλη' column
#     if 'Πόλη' in selected_columns:
#         selected_columns['city'] = selected_columns['city'].apply(cities)
   

#     # Process 'Πατρώνυμο' column
#     if 'Πατρώνυμο' in selected_columns:
#         df = process_patronymic_column(df, selected_columns)
    
#     df = stoixeia_gen()

#     # Process 'Σχέση' column
#     if 'Σχέση' in selected_columns:
#         df = process_relationship_column(df, selected_columns)

#     # Process 'ΑΦΜ' column
#     if 'ΑΦΜ' in selected_columns:
#         df = process_vat_column(df, selected_columns)




#     return df

# def process_onoma_column(df, selected_columns):
#     df["Άρθρο_γεν"] = selected_columns['first_name'].apply(tou)        
#     df["Όνομα_γεν"] = selected_columns['first_name'].apply(onoma_gen)     
#     df['Εταιρείας'] = df.apply(lambda row: check_for_εταιρεία_gen(row, "Της εταιρείας"), axis=1)
#     df['Έδρα'] = df.apply(lambda row: check_for_εταιρεία_gen(row, "η οποία εδρεύει"), axis=1)
#     df["Άρθρο_γεν"] = df.apply(lambda row: check_for_εταιρεία_gen(row, "Της εταιρείας") if check_for_εταιρεία_gen(row, "Της εταιρείας") else row["Άρθρο_γεν"], axis=1)
#     return df

# def process_patronymic_column(df, selected_columns):
#     selected_columns['father_name'] = selected_columns['father_name'].apply(onoma_gen)
#     selected_columns['father_name'] = selected_columns['father_name'].fillna("-")      
#     return df

# def process_relationship_column(df, selected_columns):
#     selected_columns['relationship'] = selected_columns['relationship'].replace(sxesi_dict)  
#     df['Order_Σχέση_Ενεχομένων'] = selected_columns['relationship'].replace(sxesi_order_dict)  
#     return df

# def process_vat_column(df, selected_columns):
#     selected_columns['vat'] = np.where(selected_columns['vat'].str.len() == 10, selected_columns['vat'].str[1:], selected_columns['vat'])
#     selected_columns['vat'] = pd.Series(selected_columns['vat']).apply(lambda x: x.zfill(9))
#     return df
    
# def stoixeia_gen() :
#     df["Στοιχεία_Γεν_Custom"] = df.apply(lambda row : combine_columns_custom_gen(row,df), axis=1).replace(" 0 ","")
#     df["Στοιχεία_Γεν_Custom"] =  df["Στοιχεία_Γεν_Custom"].apply(lambda x : str(x).replace(" , ",  ", ")) 
#     df["Στοιχεία_Γεν_Custom"] = np.where(selected_columns['father_name'] == "-", df["Στοιχεία_Γεν_Custom"].apply(lambda x: x.replace("   του  , κατοίκου ", ", η οποία εδρεύει στην περιοχή ")), df["Στοιχεία_Γεν_Custom"])
#     df["Στοιχεία_Γεν_Custom"] = np.where(
#                                         df['Εταιρείας'] == "Της εταιρείας",
#                                         df["Στοιχεία_Γεν_Custom"].str.replace("κατοίκου", "η οποία εδρεύει στην περιοχή").replace("   του  ",""),
#                                         df["Στοιχεία_Γεν_Custom"])

#     return df
