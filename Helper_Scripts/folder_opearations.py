import os

def get_directory_paths(base_path, subdirs) :
    paths = {}
    for subdir in subdirs :
        paths[subdir] = os.path.join(base_path, subdir)
    return paths

parent_directory = os.path.dirname(os.getcwd())
directories = get_directory_paths(parent_directory, ["Template Files", "Results", "Multiple Template Files"])

templates = directories["Template Files"]


multiple_template_directory = directories["Multiple Template Files"]
results = directories["Results"]

placeholders = [
'Placeholderdaneiou',
'Stoixeia1',
'Stoixeia2',
'Stoixeia3',
'Stoixeia4',
'CASE_CONTR_NUM']