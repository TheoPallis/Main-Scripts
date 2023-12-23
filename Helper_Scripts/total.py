   # Πώς : np.where(main+extra_cols_dict[v] (= If extra_cols are null),
            # main+extra_cols_dict[k]( = then insert main_cols)
            # main+extra_cols_dict[v]( = else insert extra_cols)
excel = r"C:\Users\Θοδωρής\Downloads\TFT_16_12-working_15_00\Project Files\Non Frontier\ΣΤΟΙΧΕΙΑ ΕΝΕΧΟΜΕΝΩΝ ΝΟΝ FRONTIER 16.12.2023 ΣΙΟΥΦΑΣ.xlsx"

def create_total_cols(file)
    df = pd.read_excel(excel)
    m_auto_columns  = ['main CUST FIRST NAME',
                  'main CUST LAST NAME',
                  'main CUST FATH NAME',
                  'main CUST AFM',
                  'STREET',
                  'POSTCODE',
                  'CITY']
    e_auto_columns  = ['EXTRA FIRST NAME',
                       'EXTRA LAST NAME',
                       'EXTRA FATH NAME',
                       'EXTRA AFM',
                       'EXTRA STREET',
                       'EXTRA POSTCODE',
                       'EXTRA CITY'                                        
                  ]
    total_dict = dict(zip(m_auto_columns, e_auto_columns))
    if "Unnamed: 0" in total_dict:
        del total_dict["Unnamed: 0"]
    for k, v in total_dict.items():
        df[f"total_{k}"] = np.where(df[v].isna(), df[k], df[v])
    df.iloc[:,-8:]
    df.to_excel('total.xlsx')
    os.startfile('total.xlsx')


