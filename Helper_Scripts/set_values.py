import itertools
        
all_possible_etairies_combinations_list = []
suffixes = ["AE", "IKE", "EE", "EPE", "OE","ΑΕ","ΙΚΕ","ΕΕ","ΕΠΕ","ΟΕ"]  
letters = ['A-Z', 'Α-Ω']  # English and Greek capital letters.
patterns = ['', '.']  # With and without dots.        εταιρείες = []

female_exceptions = ['ΕΛΙΣΑΒΕΤ']


for suffix in suffixes:
    for letter_pattern in itertools.product(patterns, repeat=len(suffix)):
        new_suffix = ''.join(f"{letter}{pattern}" for letter, pattern in zip(suffix, letter_pattern))
        all_possible_etairies_combinations_list.append(new_suffix)

special_city_keys = ["ΒΡΙΛΗΣΙΑ","ΒΡΙΛΗΣΣΙΑ","ΙΛΙΟΝ","ΠΑΝΟΡΑΜΑ","ΣΕΡΡΕΣ","ΚΙΛΚΙΣ","ΑΜΠΕΛΑΚΙΑ","ΑΡΓΟΣ","ΧΑΝΙΑ","ΦΑΡΣΑΛΑ","ΙΩΑΝΝΙΝΑ","ΣΕΠΟΛΙΑ","ΤΡΙΚΑΛΑ","ΑΝΩ ΛΙΟΣΙΑ","ΚΑΛΥΒΙΑ","ΜΕΓΑΡΑ","ΝΈΟ ΗΡΑΚΛΕΙΟ","ΠΑΛΑΙΟ ΦΑΛΗΡΟ","ΝΕΑ ΙΩΝΙΑ","ΑΓΙΟΙ ΑΝΑΡΓΥΡΟΙ","ΑΓΙΑ ΠΑΡΑΣΚΕΥΗ"]

special_city_values = ["ΒΡΙΛΗΣΙΩΝ","ΒΡΙΛΗΣΣΙΩΝ","ΙΛΙΟΥ","ΧΑΝΙΩΝ","ΠΑΝΟΡΑΜΑΤΟΣ","ΦΑΡΣΑΛΩΝ","ΑΜΠΕΛΑΚΙΩΝ","ΑΡΓΟΥΣ","ΙΩΑΝΝΙΝΩΝ","ΣΕΠΟΛΙΩΝ","ΤΡΙΚΑΛΩΝ","ΑΝΩ ΛΙΟΣΙΩΝ","ΚΑΛΥΒΙΩΝ","ΜΕΓΑΡΩΝ","ΝΕΟΥ ΗΡΑΚΛΕΙΟΥ","ΠΑΛΑΙΟΥ ΦΑΛΗΡΟΥ","ΝΕΑΣ ΙΩΝΙΑΣ","ΑΓΙΩΝ ΑΝΑΡΓΥΡΩΝ","ΑΓΙΑΣ ΠΑΡΑΣΚΕΥΗΣ",]

special_city_dict = dict(zip(special_city_keys, special_city_values))


replacements = {
    "ΝΕΟΣ": "ΝΕΟΥ ",
    "ΑΓΙΟΣ ": "ΑΓΙΟΥ ",
    "ΝΕΑ": "ΝΕΑΣ ",
    "ΑΓΙΑ": "ΑΓΙΑΣ ",
    "ΑΓΙΟ": "ΑΓΙΟΥ ",
    "ΝΕΟ": "ΝΕΟΥ ",
    "ΑΓΙΟΙ": "ΑΓΙΩN ",
    "ΝEOI": "ΝΕΩΝ ",
    "ΝΕΕΣ": "ΝΕΩΝ ",
    "ΑΓΙΕΣ": "ΑΓΙΩΝ ",
    "ΑΡΧΑΙΑ" :"ΑΡΧΑΙΑΣ"}



            
sxesi_dict = {
        "οφειλέτης"    : "ως πρωτοφειλέτη",
        "ΠΡΩΤΟΦΕΙΛΕΤΗΣ" : "ως πρωτοφειλέτη",
        "Πρωτοφειλέτης": "ως πρωτοφειλέτη",
        "Primary Owner": "ως πρωτοφειλέτη",
        "Primary Owner": "ως πρωτοφειλέτη",
        "Εγγυητής"     : "ως εγγυητή",
        "Εγγυητής"     : "ως εγγυητή",
        "ΕΓΓΥΗΤΗΣ"     : "ως εγγυητή",
        "Guarantor"    : "ως εγγυητή",
        "Συμπιστούχος" : "ως συμπιστούχο",
        "Συνοφειλέτης" : "ως συμπιστούχο",
        "Πιστούχος"     : "ως συμπιστούχο",
        "ΠΙΣΤΟΥΧΟΣ"     : "ως συμπιστούχο",
        "Co-Owner"     : "ως συμπιστούχο",
        "Co-Owner" :   "ως συμπιστούχο"}





sxesi_order_dict = {
    "ως πρωτοφειλέτη" : 1,
    "ως εγγυητή" : 2 ,
    "ως συμπιστούχο" : 3,

}

placeholder_col_dict = {
    'Σύμβαση': 'placeholdersym',
    'Ολογράφως_Αιτ': 'placeholderolog',
    'Stoixeia1': 'placeholderstoixeia1',    
    'Stoixeia2' :    'placeholderstoixeia2',
    'Stoixeia3' :    'placeholderstoixeia3',
    'Stoixeia4' :'placeholderstoixeia4',
    'Denounced Date': 'placeholderdate',
    'Denounced Amount' : 'placeholderamount',
    'Case Currency' : 'placeholdercur'  
}

