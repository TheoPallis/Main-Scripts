import itertools
import os
from Helper_Scripts.set_values import all_possible_etairies_combinations_list,special_city_dict,replacements,female_exceptions


file_name = '3869 par.txt'
folder_path = r'../TFT_20_12-main/Mapping Files/file_name'
# Construct the full path to the file
text_path_3869= os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)

with open(text_path_3869, 'r', encoding='utf-8') as file:
    paragraph_3869 = file.read()




def tou(string):
    if isinstance(string, str) :
        if string.endswith(("Α","A","Η","H","Ω")):
            return "Της"
        elif string.endswith(("ΟΣ", "ΑΣ", "ΗΣ")):
            return "Του"
        elif string in female_exceptions :
            return "Της"
        elif string.split(' ')[-1] in all_possible_etairies_combinations_list :
            return "Της εταιρείας"
        
        else :
            return "Του"
                    

def eponimo_gen(string):
    if isinstance(string, str) :
        if string.endswith("ΟΣ"):
            return string[:-1] + 'Υ'
        elif string.endswith("Σ"):
            return string[:-1] 
        else :
            return string

def onoma_gen(string):
    if isinstance(string, str) :
        if string.endswith("ΟΣ"):
            return string[:-1] + "Υ"
        elif string.endswith(("ΑΣ","ΗΣ")):
            return string[:-1]
        elif string.endswith(("Α","Η","Ω")):
            return string + "Σ"
        else:
            return string


def cities(string):
    city_list = []
    if string in special_city_dict:
            string = special_city_dict[string]
    else :
        if isinstance(string, str) and string != "" :
            last_two = string[-2:]
            if last_two in ('ΑΣ', 'ΗΣ') :
                    return string[:-1]
            elif last_two in ('ΕΣ', 'ΟΙ','ΑΙ'):
                    return string[:-2] + 'ΩΝ'
            elif string[-1] in  ('Α','Η','A','H'):
                    return string + 'Σ'
            elif string[-1] == 'Ι':
                    return string + 'ΟΥ'
            elif string[-1] == 'Ο':
                    return string + 'Υ'
            elif last_two == 'ΟΣ':
                    return string[:-1] + 'Y'
            else :
                return string
                
    for key,value in replacements.items():
        if key in string:
            string.replace(key, value)
    return string


# def process_vat_number(vat_number):
    
#     if len(vat_number)  > 9 :
#         print(vat_number[-9:])
#         return vat_number[-9:]

#     return vat_number[-9:]

def check_for_εταιρεία_gen(row, return_value_if_found,selected_columns):
    for col in [selected_columns['first_name'].name, selected_columns['last_name'].name,selected_columns['father_name'].name]:
        if any(εταιρεία in row[col] for εταιρεία in all_possible_etairies_combinations_list):
            return return_value_if_found
    return None  # or some default value

def categorize1(row,product,card):
    if 'SBB' in row[product] :
        return 'επιχειρηματικού δανείου'
    elif 'MLU' in row[product]or 'HE' in row[product]:
        return 'στεγαστικού δανείου'
    elif 'CLB' in row[product]:
        return 'τοκοχρεωλυτικού δανείου'
    elif 'card' in row[card]:
        return 'πιστωτικής κάρτας'
    else:
        return None
    
def categorize2(row,product,card):
    if 'SBB' in row[product] :
        return 'επιχειρηματικό δάνειο'
    elif 'MLU' in row[product] or 'HE' in row[product]:
        return 'στεγαστικό δάνειο'
    elif 'CLB' in row[product]:
        return 'τοκοχρεωλυτικό δάνειο'
    elif 'card' in row[card]:
        return 'πιστωτική κάρτα'
    else:
        return None

def SPV(val):
    if 'CAIRO1' in val:
        return df[contract]
    elif 'CAIRO2' in val:
        return df[contract]
    elif 'RECOVERY' in val:
        return df[contract]
    elif 'ERB' in val:
        return df[contract]
    elif 'RECOVERY' in val:
        return df[contract]
    else:
        return None

def add_3869(val, source):
    if '3869' in val:
        return paragraph_3869
    # Handle the case when '3869' is not in val
    return None  # You may want to return a default value or the original value if needed

