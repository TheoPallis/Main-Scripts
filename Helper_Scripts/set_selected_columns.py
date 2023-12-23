
import pandas as pd
def set_selected_columns(df,anathesi_type,numbered) :
    selected_columns = {}
    if anathesi_type == 'Frontier' :
                            
        # selected_columns = {(key for key in self.keys) :  
              
        selected_columns['first_name'] = df['ΟΝΟΜΑ']            
        selected_columns['last_name'] = df['ΕΠΩΝΥΜΟ']
        selected_columns['father_name'] = df['ΠΑΤΡΩΝΥΜΟ']
        # selected_columns['first_name'] = df["ΕΠΩΝΥΜΙΑ"].str.split(" ")[0]            
        # selected_columns['last_name'] = df["ΕΠΩΝΥΜΙΑ"].str.split(" ")[1:]
        # selected_columns['father_name'] = df['Middle Name']
        selected_columns['city'] =df['Πόλη']
        selected_columns['street'] =df['Οδός']
        selected_columns['postal_code'] = df['Τ.Κ.']    
        selected_columns['relationship'] = df["Σχέση"]
        selected_columns['vat'] = df["VAT Number"]
        selected_columns['product'] = df["Business Unit"]         
        # selected_columns['product'] = df["ΠΡΟΙΟΝ"] 
        selected_columns['case'] = df[ "Υπόθεση"] 
        selected_columns['amount'] = df['Denounced Amount']
        selected_columns['spv'] = df['Προμηθευτής']
  
        
    elif anathesi_type == 'Non_Frontier' :
     
        selected_columns = {}
        selected_columns['first_name'] = df['total_main CUST FIRST NAME']            
        selected_columns['last_name'] = df['total_main CUST LAST NAME']
        selected_columns['father_name'] = df['total_main CUST FATH NAME']
        selected_columns['city'] =df['total_CITY']
        selected_columns['street'] =df['total_STREET']
        selected_columns['postal_code'] = df['total_POSTCODE']    
        selected_columns['relationship'] = df['RT DESC']
        selected_columns['vat'] = df['total_main CUST AFM']
        selected_columns['product'] = df['CASE_BU'] 
        selected_columns['card'] = df['CASE_BU'] 
        selected_columns['case'] = df['CASE CONTR NUM'] 
        selected_columns['amount'] = df["Denounced Amount"]
        selected_columns['spv'] = df['Προμηθευτής']
        selected_columns['date_titlop'] = df['Ημερομηνία τιτλοποίησης']
        selected_columns['date_titlop'] = pd.to_datetime(selected_columns['date_titlop'])
        df['date_titlop'] = selected_columns['date_titlop'].dt.strftime('%d/%m/%Y')

        # if numbered == 'numbered':
        #     selected_columns['street'] = df['total_STREET'] + " " + df['Address Number']

    else :

        # Replace with grid columns selectors
        
    #     selected_columns['first_name'] = df['ΟΝΟΜΑ']            
    #     selected_columns['last_name'] = df['ΕΠΩΝΥΜΟ']
    #     selected_columns['father_name'] = df['ΠΑΤΡΩΝΥΜΟ']
    #     selected_columns['city'] =df['ΠΟΛΗ']
    #     selected_columns['relationship'] = df['RT_DESC']
    #     # selected_columns['vat'] = df['main_CUST_AFM']
    #     selected_columns['product'] = df['CASE_BU'] 
    #     selected_columns['case'] = df['CASE_CONTR_NUM'] 
    #     selected_columns['street'] =df['STREET']
    #     selected_columns['postal_code'] = df['POSTCODE']  
    #     selected_columns['spv'] = df["ΧΑΡΤΟΦΥΛΑΚΙΟ"]
    # if mode =='Number' :
    #         selected_columns['street'] =df['STREET'] + " " + df['Number']

        selected_columns['first_name'] = df['First Name']            
        selected_columns['last_name'] = df['Surname']
        selected_columns['father_name'] = df['Middle Name']
        selected_columns['city'] = df['City2']
        selected_columns['street'] = df['Address Line 1']
        selected_columns['number'] = df['Address Number']
        selected_columns['postal_code'] = df['Postal Code']
        selected_columns['vat'] = df['Tax Number']
        selected_columns['relationship'] = df['QC Relation Type']
        selected_columns['symbasi'] = df['Αρ. Σύμβασης μετάπτωσης']
        selected_columns['old_account'] = df['Αρ. Λογαριασμού_Παλιός']
        selected_columns['denouncement_date'] = df['Denouncement Date']
        selected_columns['case'] = df['Αρ. Σύμβασης μετάπτωσης']
        selected_columns['new_account'] = df['Account Reference']
        selected_columns['amount'] = df['Balance at denouncement']
        # 'olog' key is not matched with any new dict key, handle separately if needed
        selected_columns['spv'] = df['Portfolio Name']
        selected_columns['product'] = df['Sub-Product']
        selected_columns['customer_segment'] = df['Customer Segment']
        selected_columns['card'] = df['Περιγραφή Προϊόντος ΕΤΕ']
        selected_columns['3869'] = df['Allocation Type']

        # if numbered == 'numbered':
        #     selected_columns['street'] = df['Address Line 1'] + " " + df['Address Number']

    return(selected_columns)



def update_selected_cols(df,selected_columns) :
    selected_columns['Pool_Ενεχομένων'] = df['Pool Ενεχομένων']
    selected_columns['Στοιχεία_Γεν_Custom'] = df['Στοιχεία_Γεν_Custom']
    return df