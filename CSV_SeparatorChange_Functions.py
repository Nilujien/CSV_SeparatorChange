import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog

from pandas import *

'Calque peut rester'
"Ou isoler chaque colonne dans une liste"
"La nouvelle donne : profiter du format xls pour une délimitation en colonnes performante,"
"Isoler les coordonnées de MidPoint et se débarrasser des parenthèses superflues"
"J'ai obtenu les MidPoint correctement, en listes fusionnables "

def identify_csv_separator(file):
    global chemin_du_fichier
    chemin_du_fichier = file
    """Ouverture et attribution d'un alias au fichier CSV sélectionné"""
    with open(chemin_du_fichier, newline='') as csv_file:
        """Définition du dialecte du fichier CSV avec Sniffer"""
        dialect = csv.Sniffer().sniff(csv_file.read(100))
        """Définition du séparateur CSV utilisé par le fichier"""
        global csv_delimiter_detected
        csv_delimiter_detected = dialect.delimiter
        print("Le délimiteur détecté est : ")
        print(dialect.delimiter)
        "Identification du séparateur, face à une liste de possibles"
        if csv_delimiter_detected == ",":
            csv_delimiter_literal_description = "[Virgule]"
        elif csv_delimiter_detected == ";":
            csv_delimiter_literal_description = "[Point-virgule]"
        elif csv_delimiter_detected == " ":
            csv_delimiter_literal_description = "[Espace]"
        elif csv_delimiter_detected == ".":
            csv_delimiter_literal_description = "[Point]"
        elif csv_delimiter_detected == "|":
            csv_delimiter_literal_description = "[Barre verticale]"
        else:
            csv_delimiter_literal_description = "[Non répertorié]"
        label_separator_detected_result.configure(
            text=str(dialect.delimiter) + ' ' + csv_delimiter_literal_description)

        return chemin_du_fichier, csv_delimiter_detected


def read_xls_geometry_file(file_to_read):
    if file_to_read is not None:
        # reading XLS file
        data = read_excel(file_to_read)
        columns_headers = read_excel(file_to_read).columns
        print("---- Description des colonnes : ")
        print(columns_headers)
        columns_headers_list = columns_headers.tolist()
        print(columns_headers_list)
        "Nombre,Nom,BaseHeight,Calque,InstanceWidth,JustificationType,Length,MidPoint,Rotation,Width,XDir,YDir,ZDir"
        # converting column data to list
        cl_justification_type = 0
        cl_mid_point_X = data["MidPoint"].tolist()
        cl_mid_point_Y = data["Rotation"].tolist()
        cl_mid_point_Z = data["Width"].tolist()
        cl_instance_width = data["InstanceWidth"].tolist()
        cl_base_height = data["BaseHeight"].tolist()

        # printing list data
        print('MidPoint:', cl_mid_point_X)
        print('Rotation:', cl_mid_point_Y)
        print('Width:', cl_mid_point_Z)
        print('InstanceWidth:', cl_instance_width)
        print('Shampoo:', cl_base_height)

    else:
        print("File is None.")


def browse_file_to_import():
    """Fenêtre de choix du fichier, limité au format CSV, retourne un objet Io"""
    global file_obtained
    file_obtained = filedialog.askopenfilename(filetypes=[('Fichier XLS', '*.xls')])
    """'Si le retour de askopenfile est non-null, exécuter les actions suivantes"""
    if file_obtained is not None:
        """Configure le label de résultat, qui ne contient que le nom et l'extension du fichier"""
        label_file_name_result.configure(text=str(file_obtained))
        # identify_csv_separator(file_obtained)


    else:
        print("No file_obtained selected")


"_____________ TKINTER"

'Create root window'
root = tk.Tk()
root.title('GDL : Assembleur de CSV')
# root.minsize(300, 100)
# root.geometry('500x200')

'Create Frame 1'
frame_1 = LabelFrame(root, text='Extraction de données du cloisonnement')
frame_1.pack(padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill='both')

'Create Import Button'
button_import_csv = ttk.Button(frame_1, text="Importer un fichier XLS", command=browse_file_to_import)
button_import_csv.grid(column=0, row=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Imported File Label'
label_file_name = ttk.Label(frame_1, text="Nom du fichier importé : ", relief='groove', anchor='center')
label_file_name.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10)

'Create Imported File Result Label'
label_file_name_result = ttk.Label(frame_1, text="---", relief='groove', anchor='center', background='lightgrey')
label_file_name_result.grid(column=1, row=1, padx=10, pady=10, ipadx=10, ipady=10)

'Create Separator Detected Label'
label_separator_detected = ttk.Label(frame_1, text="Séparateur détecté : ", relief='groove', anchor='center')
label_separator_detected.grid(column=0, row=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Separator Detected Result Label'
label_separator_detected_result = ttk.Label(frame_1, text="---", relief='groove', anchor='center',
                                            background='lightgrey')
label_separator_detected_result.grid(column=1, row=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

frame_2 = LabelFrame(root, text='Table de nomenclature du cloisonnement')
frame_2.pack(padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill='both')

'Create Import Button'
button_import_nomenclature_table_csv = ttk.Button(frame_2, text="Importer un fichier XLS",
                                                  command=browse_file_to_import)
button_import_nomenclature_table_csv.grid(column=0, row=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10,
                                          sticky='nsew')

'Create Imported File Label'
label_nomenclature_file_name = ttk.Label(frame_2, text="Nom du fichier importé : ", relief='groove', anchor='center')
label_nomenclature_file_name.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10)

frame_3 = LabelFrame(root, text='Lecture des XLS')
frame_3.pack(padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill='both')

'Create Target Separator Label'
label_target_separator = ttk.Label(frame_3, text="Séparateur visé : ", relief='groove', anchor='center')
label_target_separator.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create List of Separators'
items = ('Virgule', 'Point-virgule', 'Espace', 'Barre verticale')
list_items = tk.Variable(value=items)

'Liste déroulante de choix du séparateur'
combobox_target_separator = ttk.Combobox(frame_3, values=items, state='readonly', background='lightgrey')
combobox_target_separator.grid(column=1, row=0, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')


button_read_csv = ttk.Button(frame_3, text="Lire le CSV", command=lambda: read_xls_geometry_file(file_obtained))
button_read_csv.grid(column=0, row=2, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')
'Launch the mainloop'
root.mainloop()
