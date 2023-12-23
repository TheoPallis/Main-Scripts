custom_text_dict = {
'custom_city_gen' : ', κατοίκου ',
'custom_street_gen' :  ', οδός ',
'custom_TK_gen' :  ', ΤΚ ',
'custom_ΑΦΜ_gen' : ', με ΑΦΜ ',
}

custom_gen_strings = {
    "article" : "",
    'first_name': "",
    'last_name': "" ,
    'father_name': "του ",
    'city': custom_text_dict['custom_city_gen'],
    'street' : custom_text_dict['custom_street_gen'],
    'number': ", αριθμός ",  
    'postal_code' : custom_text_dict['custom_TK_gen'],
    'vat': custom_text_dict['custom_ΑΦΜ_gen'],
    # 'product': "",
    'relationship': ", ",
    }


def create_associated_text_dict(selected_columns) :
    print("Created the associated text dict")
    return{var: custom_gen_strings[var] for var in custom_gen_strings.keys()}
