from 

def ton(string,female_exceptions):
    if isinstance(string, str) and string.endswith(("Α","A","Η","H","Ω")):
        return "Την"
    elif isinstance(string, str) and string.endswith(("ΟΣ", "ΑΣ", "ΗΣ")):
        return "Τον"
    elif isinstance(string, str) and string in female_exceptions :
        return "Την"
    elif isinstance(string, str) and string.split(' ')[-1] in εταιρείες :
        return "Την εταιρεία"
    else :
        return "Τον"
def check_for_εταιρεία_ait(row):
    for col in [Όνομα, Πατρώνυμο, Επώνυμο]:
        if any(εταιρεία in row[col] for εταιρεία in εταιρείες):
            return "Την εταιρεία"
    return None  # or some default value



def onoma_ait(string):
    if isinstance(string, str) and string.endswith(("ΟΣ", "ΑΣ", "ΗΣ", "A", "Η")):
        if string.endswith(("ΟΣ", "ΑΣ", "ΗΣ")) :
            return string[:-1]  
        else :
            return string
    else :
        return string


associated_text_custom_ait = {
'Άρθρο_αιτ' : "",
'Επώνυμο_αιτ' : "",
'Όνομα_αιτ' : "",
Πατρώνυμο : " του ",
Πόλη: f", {custom_city_ait}",
"Οδός": f", {custom_street_ait} ",
"Τ.Κ." : f", {custom_TK_ait}",
ΑΦΜ :  f"{custom_ΑΦΜ_gen}",
Σχέση: ",",
# "Αριθμός" : ", με αριθμό "
    }


def combine_columns_custom_ait(row):
    result = ""
    for k in associated_text_custom_ait.keys() :
        if k in df.columns and row[k] is not None:
            result += associated_text_custom_ait[k] 
            result += row[k] + " "
    return(result)


df["Στοιχεία_Αιτ_Custom"] = df.apply(combine_columns_custom_ait, axis=1).replace(" 0 ","")
df["Στοιχεία_Αιτ_Custom"] =  df["Στοιχεία_Αιτ_Custom"].apply(lambda x : str(x).replace(" , ",  ", ")) 



if 'Όνομα' in selected_columns.keys() :

        df["Άρθρο_αιτ"] = df[Όνομα].apply(ton)
        df['Εταιρεία'] = df.apply(check_for_εταιρεία_ait, axis=1)
        df["Άρθρο_ αιτ"] = df.apply(lambda row: check_for_εταιρεία_ait(row) if check_for_εταιρεία_ait(row) else tou(row[Όνομα]), axis=1)        
        df["Άρθρο_αιτ"] = np.where(df['Εταιρεία']  == 'Την εταιρεία', 'Την εταιρεία',df["Άρθρο_αιτ"] )
        df["ο/η"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "ο", "η")
        df["αυτόν/αυτή"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "αυτόν", "αυτή")    

        df["Όνομα_αιτ"] = df[Όνομα].apply(onoma_ait)
        df["Όνομα_αιτ"] = df["Όνομα_αιτ"].fillna('-')
        df["Όνομα_αιτ"] = np.where(df['Όνομα_αιτ'] == '-',df['Επώνυμο_αιτ'],df['Όνομα_αιτ'] )
                
# df["Στοιχεία_Αιτ_Custom"] = np.where(
# df['Εταιρείας'] == "Την εταιρεία",
# df["Στοιχεία_Αιτ_Custom"].str.replace("κατοίκου", "η οποία εδρεύει στην περιοχή").replace("   του  ",""),
# df["Στοιχεία_Αιτ_Custom"])

if 'Πατρώνυμο' in selected_columns.keys() :
    df["Στοιχεία_Αιτ_Custom"] = np.where(df[Πατρώνυμο] == "-",df["Στοιχεία_Αιτ_Custom"].apply(lambda x: x.replace("   του  , κατοίκου ", ", η οποία εδρεύει στην περιοχή ")),df["Στοιχεία_Αιτ_Custom"])



if st.button('Extra Pronouns') :
    df["του/της"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "του", "της")
    df["τον/την"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "τον", "την")
    df["στον/στην"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "στον", "στην")
    df["καθ'ου/καθ'ης"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "καθ'ου", "καθ'ης")
    df["εναγόμενος/εναγόμενη"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "εναγόμενος", "εναγόμενη")
    df["εναγομένου/εναγομένης"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "εναγομένου", "εναγομένης")
    df["εναγόμενο/εναγόμενη"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "εναγόμενο", "εναγόμενη")
    df["μηνυόμενος/μηνυόμενη"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "μηνυόμενος", "μηνυόμενη")
    df["οφειλέτης/οφειλέτιδα"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "οφειλέτης", "οφειλέτιδα")
    df["οφειλέτη/οφειλέτιδας"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "οφειλέτη", "οφειλέτιδας")
    df["οφειλέτη/οφειλέτιδα"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "οφειλέτη", "οφειλέτιδα")
    df["αυτός/αυτή"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "αυτός", "αυτή")
    df["αυτού/αυτής"] = np.where(df["Άρθρο_αιτ"] == 'Τον' , "αυτού", "αυτής")
    format_df(file_name)    
    os.startfile(file_name)


def eponimo_ait(string):                    
    if isinstance(string, str) and string.endswith("Σ"):
        return string[:-1]
    else :
        return string
