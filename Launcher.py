import csv
import tkinter as tk
import os
from tkinter import ttk
from tkinter import *
from tkinter import filedialog


"_____________ TKINTER"

'Create root window'
root = tk.Tk()
root.title('GDL : Assembleur de CSV')
root.minsize(300, 100)
# root.geometry('500x200')

'Create Frame 1'
frame_1 = LabelFrame(root, text='Extraction de données du cloisonnement')
frame_1.pack(fill="both", expand=1, padx=10, pady=10, ipadx=10, ipady=10)

'Create Import Button'
button_import_csv = ttk.Button(frame_1, text="Importer un fichier CSV", command=browse_file_to_import)
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
frame_2.pack(fill="both", expand=1, padx=10, pady=10, ipadx=10, ipady=10)

'Create Import Button'
button_import_nomenclature_table_csv = ttk.Button(frame_2, text="Importer un fichier CSV",
                                                  command=browse_file_to_import)
button_import_nomenclature_table_csv.grid(column=0, row=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10,
                                          sticky='nsew')

'Create Imported File Label'
label_nomenclature_file_name = ttk.Label(frame_2, text="Nom du fichier importé : ", relief='groove', anchor='center')
label_nomenclature_file_name.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10)

frame_3 = LabelFrame(root, text='Conversion du séparateur')
frame_3.pack(fill="both", expand=1, padx=10, pady=10, ipadx=10, ipady=10)

'Create Target Separator Label'
label_target_separator = ttk.Label(frame_3, text="Séparateur visé : ", relief='groove', anchor='center')
label_target_separator.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Create List of Separators'
items = ('Virgule', 'Point-virgule', 'Espace', 'Barre verticale')
list_items = tk.Variable(value=items)

'Liste déroulante de choix du séparateur'
combobox_target_separator = ttk.Combobox(frame_3, values=items, state='readonly', background='lightgrey')
combobox_target_separator.grid(column=1, row=0, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

"Création du bouton de conversion, noter l'utilisation de lambda pour passer des arguments à la fonction"
button_convert_csv_separator = ttk.Button(frame_3, text="Convertir le séparateur du CSV",
                                          command=lambda: convert_csv_separator(chemin_du_fichier,
                                                                                csv_delimiter_detected, ';'))
button_convert_csv_separator.grid(column=0, row=1, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky='nsew')

'Launch the mainloop'
root.mainloop()