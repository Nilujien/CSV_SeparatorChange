
import os

creation_command = 'cd c:\\users\\jcuartero\\pycharmprojects\\csv_separatorchange\\'

pyinstaller_command = 'pyinstaller --clean -w' \
                      ' --onefile' \
                      ' --hidden-import pywintypes' \
                      ' --add-data "Aguiles_Logo.png;."' \
                      ' --add-data "GDL_Couteau_Suisse.ico;."' \
                      ' --icon "GDL_Couteau_Suisse.ico"' \
                      ' Repartiteur_Dynamique.py'

os.system(creation_command)

os.system(pyinstaller_command)