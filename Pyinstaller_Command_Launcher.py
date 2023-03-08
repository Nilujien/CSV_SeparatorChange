
import os

creation_command = 'cd c:\\users\\jcuartero\\pycharmprojects\\csv_separatorchange\\'

pyinstaller_command = 'pyinstaller --clean -w' \
                      ' --onefile' \
                      ' --hidden-import plyer.platforms.win.notification' \
                      ' --add-data "Pipette.png;."'\
                      ' --add-data "Pipette_vide.png;."' \
                      ' --add-data "Pipette_MisClose.png;."' \
                      ' --add-data "Dots.png;."' \
                      ' --add-data "Dots_vides.png;."' \
                      ' --add-data "GDL_Couteau_Suisse.ico;."' \
                      ' --icon "GDL_Couteau_Suisse.ico"' \
                      ' GDL_Multitool_V-2.0.py'

os.system(creation_command)

os.system(pyinstaller_command)