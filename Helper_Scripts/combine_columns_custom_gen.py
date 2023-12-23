from Helper_Scripts.set_values import all_possible_etairies_combinations_list


def create_the_concatenated_string(row,df,associated_text_custom_gen,selected_columns):
    
    result = ""
    for k2 in associated_text_custom_gen.keys() :
        if k2 in selected_columns.keys() :  

            result += associated_text_custom_gen[k2]
            
            try :
                col_name = selected_columns[k2].name
         
                result += row[col_name] + " " 
            
            
            except Exception as e:
                print(f"Failed to concatenate column {k2} of case {row[selected_columns['case'].name]}. Error : {e}" )

    return(result)





def apply_concatenating_cols(df,associated_text_custom_gen,selected_columns):
    df["Στοιχεία_Γεν_Custom"] = df.apply(
        lambda row: create_the_concatenated_string(row, df, associated_text_custom_gen, selected_columns), axis=1
    ).replace(" 0 ", "")
    return df["Στοιχεία_Γεν_Custom"] 




# if 'Ποσό' in selected_columns.keys() :        
#     df['Ολογράφως_Αιτ'] : df[Ποσό].apply(olog)
#     df['Ολογράφως_Γεν'] : df[Ποσό].apply(olog_gen)





# Refactored  set_selected_columns
# def set_selected_columns(df, anathesi_type, mode):
#     # Define column mappings for each anathesi type
#     column_mappings = {
#         'Frontier': [
#             "ΕΠΩΝΥΜΙΑ", "Middle Name", "Πόλη", "Οδός", "Τ.Κ.", "Σχέση", "VAT Number", "ΠΡΟΙΟΝ", "Υπόθεση", "Denounced Amount"
#         ],
#         'Non_Frontier': [
#             'total_main CUST FIRST NAME', 'total_main CUST LAST NAME', 'total_main CUST FATH NAME', 
#             'total_CITY', '"total_STREET"', 'total_POSTCODE', 'RT DESC', 'total_main CUST AFM', 
#             'CASE_BU', 'CASE CONTR NUM', "Denounced Amount"
#         ],
#         'Undefined': [
#             'ΟΝΟΜΑ', 'ΕΠΩΝΥΜΟ', 'ΠΑΤΡΩΝΥΜΟ', 'ΠΟΛΗ', 'RT_DESC', 'CASE_BU', 'CASE_CONTR_NUM', 
#             'STREET', 'POSTCODE', "ΧΑΡΤΟΦΥΛΑΚΙΟ"
#         ]
#     }

#     # Keys for selected_columns dictionary
#     keys = ['first_name', 'last_name', 'father_name', 'city', 'relationship', 'product', 'case', 'street', 'postal_code', 'spv']

#     # Select the appropriate columns based on anathesi_type
#     selected_columns = dict(zip(keys, column_mappings.get(anathesi_type, [])))

#     # Append 'Number' to 'street' if mode is 'Number'
#     if mode == 'Number' and 'street' in selected_columns:
#         selected_columns['street'] = df['STREET'] + " " + df['Number']

#     # Special handling for 'first_name' and 'last_name' from 'ΕΠΩΝΥΜΙΑ' column
#     if 'ΕΠΩΝΥΜΙΑ' in df.columns:
#         eponymia_split = df["ΕΠΩΝΥΜΙΑ"].str.split(" ", expand=True)
#         selected_columns['first_name'] = eponymia_split[0]
#         selected_columns['last_name'] = eponymia_split[1:].apply(lambda x: ' '.join(x.dropna()), axis=1)

#     return selected_columns