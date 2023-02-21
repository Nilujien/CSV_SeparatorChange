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
"Tu as trouvé !!! Par le style de EndCap associé au style de cloison"

global file_obtained


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
        print("No file selected")
        label_file_name_result.configure(text="---")


"_____________ TKINTER"

'Create root window'
root = tk.Tk()
root.title('GDL : Assembleur de XLS')
root.attributes('-topmost', True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# root.minsize(300, 100)
# root.geometry('500x200')

"______________________________________ --- Geometrie"

logo_GDL_mergeXLS = tk.PhotoImage(file='Logo_GDL_lg-300px.png')

label_logo_GDL = ttk.Label(root, image=logo_GDL_mergeXLS, relief='groove', anchor='center')
label_logo_GDL.grid(padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

"______________________________________ --- Extraction de données"

frame_1 = LabelFrame(root, text='Extraction de données du cloisonnement')
frame_1.columnconfigure(0, weight=1)
frame_1.rowconfigure(0, weight=1)
frame_1.grid(padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Import Button'
button_import_csv = ttk.Button(frame_1, text="Importer un fichier XLS", command=browse_file_to_import)
button_import_csv.grid(column=0, row=0, columnspan=3, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Imported File Label'
label_file_name = ttk.Label(frame_1, text="Nom du fichier importé : ", relief='groove', anchor='center')
label_file_name.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Imported File Result Label'
label_file_name_result = ttk.Label(frame_1, text="---", relief='groove', anchor='center', background='lightgrey')
label_file_name_result.grid(column=1, row=1, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Separator Detected Label'
label_separator_detected = ttk.Label(frame_1, text="Séparateur détecté : ", relief='groove', anchor='center')
label_separator_detected.grid(column=0, row=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Separator Detected Result Label'
label_separator_detected_result = ttk.Label(frame_1, text="---", relief='groove', anchor='center',
                                            background='lightgrey')
label_separator_detected_result.grid(column=1, row=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

"______________________________________ --- Nomenclature"

frame_2 = LabelFrame(root, text='Table de nomenclature du cloisonnement')
frame_2.columnconfigure(0, weight=1)
frame_2.rowconfigure(0, weight=1)
frame_2.grid(padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create Import Button'
button_import_nomenclature_table_csv = ttk.Button(frame_2, text="Importer un fichier XLS",
                                                  command=browse_file_to_import)
button_import_nomenclature_table_csv.grid(column=0, row=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10,
                                          sticky='nsew')

'Create Imported File Label'
label_nomenclature_file_name = ttk.Label(frame_2, text="Nom du fichier importé : ", relief='groove', anchor='center')
label_nomenclature_file_name.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

"______________________________________ --- Lecture des XLS"

frame_3 = LabelFrame(root, text='Lecture des XLS')
frame_3.columnconfigure(0, weight=1)
frame_3.rowconfigure(0, weight=1)
frame_3.grid(padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

button_read_csv = ttk.Button(frame_3, text="Lire le XLS - Geometrie",
                             command=lambda: read_xls_geometry_file(file_obtained))
button_read_csv.grid(column=0, row=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

button_read_csv = ttk.Button(frame_3, text="Lire le XLS - Nomenclature",
                             command=lambda: read_xls_geometry_file(file_obtained))
button_read_csv.grid(column=0, row=1, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Root Configuration : Rows and Columns'

'Launch the mainloop'
root.mainloop()
