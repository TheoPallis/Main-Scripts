import itertools

from Helper_Scripts.set_values import all_possible_etairies_combinations_list,special_city_dict,replacements,female_exceptions




def tou(string):
    if isinstance(string, str) and string.endswith(("Α","A","Η","H","Ω")):
        return "Της"
    elif isinstance(string, str) and string.endswith(("ΟΣ", "ΑΣ", "ΗΣ")):
        return "Του"
    elif isinstance(string, str) and string in female_exceptions :
        return "Της"
    elif isinstance(string, str) and string.split(' ')[-1] in all_possible_etairies_combinations_list :
        return "Της εταιρείας"
    
    else :
        return "Του"
                    

def eponimo_gen(string):                    
                if isinstance(string, str) and string.endswith("ΟΣ"):
                    return string[:-1] + 'Υ'
                elif isinstance(string, str) and string.endswith("Σ"):
                    return string[:-1] 
                else :
                    return string

def onoma_gen(string):
    if isinstance(string, str) and string.endswith("ΟΣ"):
        return string[:-1] + "Υ"
    elif isinstance(string, str) and string.endswith(("ΑΣ","ΗΣ")):
        return string[:-1]
    elif isinstance(string, str) and string.endswith(("Α","Η","Ω")):
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


