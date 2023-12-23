 
import pandas as pd
from Helper_Scripts.format_df import format_df
import os
import datetime
from Helper_Scripts.format_cols import categorize1,categorize2

pvt_col_list = [ 'source','ΗΜΕΡΟΜΗΝΙΑ ΤΙΤΛΟΠΟΙΗΣΗΣ','Pool Ενεχομένων','Stoixeia0','Stoixeia1', 'Stoixeia2', 'Stoixeia3', 'Stoixeia4', 'Stoixeia5','Stoixeia6']
non_pvt_col_list = ['CASE_CONTR_NUM','Στοιχεία_Γεν_Custom']
excel_save_location = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\3) Αναθέσεις\TFT_20_12-main\Created Excel Files"


def load_df(file_path, sheet_name='DATA'):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=str).fillna("")
        print("Loaded the df.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    return df
  
def trim_df(df):
    try :
      # Stripping whitespace from string columns
        for col in df.select_dtypes(['object']).columns:
            df[col] = df[col].str.strip()
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = pd.to_datetime(df[col]).dt.strftime('%d/%m/%Y')  # Format as "dd/mm/yyyy"


        print("Trimmed the df.")
    except Exception as e: 
        print(f"Error trimming df: {e}")
    return df




def sort_df(df,contract,post_code) :
    df['Pool Ενεχομένων'] = df.groupby(contract)[contract].transform('count')
    df = df.sort_values(by=['Pool Ενεχομένων', post_code,'Order_Σχέση_Ενεχομένων'], ascending=[False, True, True])
    print("Sorted the df.")
    return df

def filter_df(df,col_list) :
 df = df[col_list]
 print("Filtered the df.")
 return df


def pivot_df(df,contract,stoixeia) :
    # contract = st.selectbox("Group column",options  = df.columns, index = case_index)
    df['Pool Ενεχομένων'] = df.groupby(contract)[contract].transform('count')
    # Create a unique sequence within each 'ContractID' group
    df['UniqueSeq'] = df.groupby(contract).cumcount()+1
    # Pivot the DataFrame
    df_pivot = df.pivot(index=contract, columns='UniqueSeq', values=stoixeia)
    # Reset index
    df_pivot.reset_index(inplace=True)
    # Rename the columns
    df_pivot.columns = [f'Stoixeia{i-1}' for i in range(1, len(df_pivot.columns)+1)]
    df_final = pd.merge(df.drop_duplicates(subset=contract), df_pivot, left_on=contract,right_on = df_pivot.iloc[:,0])
    # df_final = filter_df(df_final,pvt_col_list)
    file_name = generate_timestamp_filename('Pivoted','.xlsx')
    file_name = os.path.join(excel_save_location,file_name)
    df_final.to_excel(file_name,index = False)
    format_df(file_name)    
    print("Pivoted the df.")
    return(file_name,df_final)

def generate_timestamp_filename(filename_prefix,type):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%d-%m-%y_%H-%M")
    return f"{filename_prefix}_{timestamp}{type}"


def non_pivot_df(df) :
    df_final =  df
    # df_final = filter_df(df,non_pvt_col_list)
    file_name = generate_timestamp_filename('Unpivoted','.xlsx')
    file_name = os.path.join(excel_save_location,file_name)
    df_final.to_excel(file_name,index = False)
    format_df(file_name)    
    return(file_name,df_final)
    
def create_placeholder_cols(df,selected_columns) :
    SPV = selected_columns['spv'].name
    contract = selected_columns['case'].name 
    daneio = selected_columns['product'].name
    card = selected_columns['card'].name
    df['placeholderdaneiou'] = df.apply(lambda row : categorize1(row,daneio,card), axis=1)
    df['placeholderdaneio'] = df.apply(lambda row : categorize2(row,daneio,card), axis=1)
    SPV_filter = df[SPV].isin(['CAIRO1', 'CAIRO2', 'MEXICO'])
    SPV_filter = df[SPV].isin(['CAIRO1', 'CAIRO2', 'MEXICO'])
    RECOVERY_filter = df[SPV] == 'RECOVERY'
    ERB_filter = df[SPV] == 'ERB'
    df.loc[SPV_filter, 'placeholder4b'] = df[contract]
    df.loc[SPV_filter, 'placeholder4c'] = 'Σύμβαση'
    df.loc[SPV_filter | ERB_filter, 'placeholder4d'] = df['placeholderdaneiou']
    df.loc[RECOVERY_filter, 'placeholder2f'] = df[contract]
    df.loc[RECOVERY_filter, 'placeholder2g'] = 'σύμβασης'
    df.loc[df[SPV].isin(['MEXICO', 'RECOVERY']), 'placeholder2h'] = df[contract]
    print("Created Placeholder Columns.")
    return(df)


# # 1a. Αν επιλεγεί στήλη αποθηκεύεται στο selected_columns_dict με τη μορφή : 
# #     selected_columns['user_defined_name'] = selected_column
# # 1b. Επιλογή 4 τιμών στήλης και εισαγωγή σε λίστα 1
# # 1c. Επιλογή 4 λεκτικών και εισαγωγή σε λίστα 2
# # 1d. Χρήση replace τιμών λίστας 1 με τιμές λίστας 2
# # 1e. Αφαίρεση κενών τιμών στο selected_columns_dict
# # 2a. Δημιουργία dict για χειρισμό εξαιρέσεων πόλεων  
# # 2b. Δημιουργία 2ου dict για χειρισμό εξαιρέσεων πόλεων (άγιος/νέος)  
# # 2c. Δημιουργία λίστας με όλες τις καταλήξεις εταιριών για αναγνώριση περίπτωησς εταρείας 
# # 3a. Του       : Αν το όνομα τελειώνει σε Α/Η -> Της, ΟΣ/ΑΣ/ΉΣ/υπόλοιπα -> Του 
# # 3b. Τον       : Αν το όνομα τελειώνει σε Α/Η -> Την, ΟΣ/ΑΣ/ΗΣ/υπόλοιπα -> Τον
# # 3d. Αιτιατική : Αν το όνομα τελειώνει σε Α/Η/υπόλοιπα -> όνομα, ΟΣ/ΑΣ/ΗΣ -> όνομα χωρίς το ς
# # 3e. Γενική    : Αν το όνομα τελειώνει σε Α/Η/υπόλοιπα -> όνομα + ς, ΑΣ/ΗΣ -> όνομα χωρίς το ς, ΟΣ -> ΟΥ
# # 3f. Πατρώνυμο : Αν το όνομα τελειώνει σε ΑΣ/ΗΣ -> όνομα χωρίς το ς, ΟΣ -> ΟΥ
# # 4a. Πόλη  (αν επιλεγεί) : Αν η πόλη βρίσκεται στο 2a ή στο 2b,αντικατάσταση πόλης-key με πόλη=value, ΑΣ->Α, ΕΣ/ΟΙ -> ΩΝ, Α/Η-> ΑΣ/ΗΣ, Ο,Ι->ΟΥ                                                
# #  Να μετατρέψω σε κεφαλαία❗

# [item for item in list(df["Στοιχεία_Γεν_Custom"])]
