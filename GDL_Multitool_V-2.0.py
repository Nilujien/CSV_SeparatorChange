import os
import sys
import tkinter.font

import time
import pyperclip
import pyautogui
from tkinter import *
from tkinter.colorchooser import askcolor
from plyer import notification
from PIL import ImageTk, Image


# notification.notify(title='Titre', message='Message', timeout=100)

# définition de la fenêtre Tkinter principale
# noinspection PyTypeChecker, PyArgumentList
class App(Tk):
    dark_theme_bg_color: str
    from pynput import mouse

    def __init__(self):
        # Initialisation de la fenêtre principale Tkinter et de ses variables de base
        Tk.__init__(self)

        # Variable de texte à modifier suivant le survol des boutons et des labels
        texte_informatif = StringVar()
        texte_informatif.set("Survolez un élément pour en décrire les fonctions")

        self.frame_informative = LabelFrame(self, text="Informations")
        self.frame_informative.pack(fill=X, expand=True, padx=5, pady=5)
        self.frame_informative.columnconfigure(0, weight=1)
        self.frame_informative.rowconfigure(0, weight=1)
        self.frame_informative.pack()

        # Label informatif à usage général lors du survol d'un bouton ou d'un label
        self.label_informatif = Label(self.frame_informative, textvariable=texte_informatif, width=40, bg='lightblue')
        self.label_informatif.grid(pady=5, padx=5)

        # couleur de fond générale standard
        self.general_bg_color = '#f0f0f0'

        # couleur de fond générale dark
        self.dark_theme_bg_color = '#2b2b2b'

        # titre de la fenêtre principale
        self.title('Multi-Outil')

        # force l'affichage au-dessus des autres interfaces
        self.attributes('-topmost', True)

        # réglage de l'alpha de la fenêtre principale à 100% d'opacité
        self.attributes('-alpha', 1)

        # self.minsize(200, 100)

        # je n'ai plus aucune idée de ce que fait cette ligne de commande
        self.overrideredirect(False)

        # Esquive de la fermeture de fenêtre lors d'un clic sur le bouton de suppression par une réduction de la fenêtre
        # self.protocol("WM_DELETE_WINDOW", self.iconify)

        # définition de la variable Tkinter du nombre de clics
        self.variable_nombre_de_clics = DoubleVar()

        # définition d'une variable non utilisée censée comptabiliser le temps passé depuis le lancement d'une action
        self.variable_elapsed_time = DoubleVar()

        # définition d'une variable booléenne négative indiquant que le compteur n'est pas activé
        self.is_counter_on = False

        # définition d'une variable booléenne négative indiquant que le compteur n'a jamais été activé
        self.has_counter_ever_been_activated = False

        # définition d'une variable booléenne en défaut pour l'incrément du nombre de clics
        self.increment_variables_bool = True

        # fonction qui défini le réglage du carré de couleur indiquant la couleur pipettée

        def resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        '''Image de la pipette, chemin'''

        self.pipette_logo = resource_path('Pipette.png')

        '''Image de la pipette'''

        self.pipette_logo_image = ImageTk.PhotoImage(Image.open(self.pipette_logo))

        def change_label_color(pipette, color, text_to_display):
            pipette.config(bg=color)
            texte_informatif.set(text_to_display)

        # fonction d'incrément du nombre de clics
        def on_click_to_count(x, y, button, pressed):
            # si le switch d'incrément est activé :
            if self.increment_variables_bool:
                print('Press recorded at / X : ' + str(x) + ' / Y : ' + str(y))
                print('Button Pressed : ' + str(button))
                print(str(pressed))
                self.variable_nombre_de_clics.set(self.variable_nombre_de_clics.get() + 0.5)
            # si le switch d'incrément est désactivé :
            else:
                print('Counter has been de-activated.')

        # définition du Listener de clics, il est nécessaire d'encapsuler cela dans une fonction, afin de pouvoir
        # activer et désactiver un nouveau Listener à loisir, plutôt que de le garder actif pendant toute la boucle
        # principale
        self.mouse_listener = self.mouse.Listener(on_click=on_click_to_count)

        # la fonction suivante est un contournement maladroit face à l'impossibilité de stopper puis réactiver le
        # Listener
        def start_click_listener():
            # si le compteur n'a encore jamais été activé :
            if not self.has_counter_ever_been_activated:
                self.mouse_listener.start()
                self.has_counter_ever_been_activated = True
            # si le compteur a déjà été activé une fois :
            else:
                self.increment_variables_bool = True
                print('Counter has already been activated -- just stopping concerned variables increments.')

        # definition de la fonction de stop d'incrément de clics
        def stop_click_increment():
            self.variable_nombre_de_clics.set(self.variable_nombre_de_clics.get() - 1)
            self.increment_variables_bool = False
            time.sleep(0)

        # définition de la fonction appelée lors de l'activation du comptage de clics
        def click_button_listener():
            # si le compteur est désactivé
            if not self.is_counter_on:
                # active le compteur de clics
                start_click_listener()
                # modifie le texte du bouton
                self.button_launch_listener.config(text='Désactiver le Compteur')
                # active la variable booléenne du compteur
                self.is_counter_on = True
                # modifie le label du compteur en version activé
                self.label_statut_compteur.config(bg="#8be8a2", text="Activé")

                print('::::' + str(self.is_counter_on))
            # si le compteur est activé :
            else:
                # stoppe l'incrément du comptage de clics
                stop_click_increment()
                # modifie le texte du bouton
                self.button_launch_listener.config(text='Activer le Compteur')
                # désactive la variable booléenne du compteur
                self.is_counter_on = False
                print('::::' + str(self.is_counter_on))
                # modifie le label du compteur en version désactivé
                self.label_statut_compteur.config(bg="#f5c0ab", text="Désactivé")

        # définition de la fonction de modification de l'alpha général de l'interface
        # noinspection PyUnusedLocal
        def update_alpha_from_slider_value(slider):
            self.alpha_slider_value = self.slider_alpha.get()
            print(self.slider_alpha.get())
            self.attributes('-alpha', self.alpha_slider_value / 100)

        # définition de la fonction de réinitialisation du nombre de clics comptabilisés
        def reinitialize_clic_count(count):
            count.set(0.0)
            print('Counter has been re-initialized')

        # Logo avorté de l'application, à voir
        # self.logo_GDL = PhotoImage()
        # file = 'Logo_GDL_clic.png'
        # self.label_logo_GDL = Label(self, image=self.logo_GDL, anchor='center')
        # self.label_logo_GDL.pack(padx=10, pady=10, ipadx=10, ipady=10, fill=X, expand=True)

        # frame de titre, inutilisée
        self.frame_title = LabelFrame(self)
        self.frame_title.pack(fill=X, expand=True, padx=5, pady=5)

        # frame du compteur de clics
        self.frame_nombre_de_clics = LabelFrame(self, text='Compteur de Clics')
        self.frame_nombre_de_clics.pack(fill=X, expand=True, padx=5, pady=5)

        # label du nombre de clics
        self.label_nombre_de_clics = Label(self.frame_nombre_de_clics, textvariable=self.variable_nombre_de_clics)
        self.label_nombre_de_clics.pack(fill=X, expand=True, padx=5, pady=5)

        # frame des commandes
        self.frame_commands = LabelFrame(self, text='Commandes')
        self.frame_commands.pack(fill=X, expand=True, padx=5, pady=5)
        self.frame_commands.columnconfigure(0, weight=1)
        self.frame_commands.rowconfigure(0, weight=1)

        # bouton d'activation du compteur de clics
        self.button_launch_listener = Button(self.frame_commands, text='Activer le Compteur', padx=10, pady=10,
                                             command=lambda: click_button_listener())
        self.button_launch_listener.grid(row=0, padx=10, pady=10, sticky='nsew', columnspan=2)

        # label de présentation du compteur
        self.label_compteur = Label(self.frame_commands, text="Compteur", relief='groove')
        self.label_compteur.grid(row=1, column=0, padx=(10, 5), pady=0, sticky='nsew', ipady=5, ipadx=5)

        # Image nulle pour tweak de la taille du statut du compteur
        self.img_null = PhotoImage()

        # label du statut du compteur (activé ou désactivé)
        self.label_statut_compteur = Label(self.frame_commands, text="Désactivé", relief='ridge', background="#f5c0ab",
                                           image=self.img_null, width=100, compound=CENTER)
        self.label_statut_compteur.grid(row=1, column=1, padx=(5, 10), pady=0, sticky='nsew', ipady=5, ipadx=5)

        # bouton de réinitialisation du compteur
        self.button_reinitialize_count = Button(self.frame_commands, text='Réinitialiser le Compteur', padx=10, pady=10,
                                                command=lambda: reinitialize_clic_count(self.variable_nombre_de_clics))
        self.button_reinitialize_count.grid(padx=10, pady=10, sticky='nsew', columnspan=2)

        # frame des Pipettes
        self.frame_colors = LabelFrame(self, text="Pipettes")
        self.frame_colors.pack(padx=5, pady=5, fill=X, expand=True)
        self.frame_colors.columnconfigure((0, 1, 2), weight=1)
        self.frame_colors.rowconfigure((0, 1, 2), weight=1)

        # définition des couleurs affichées de base sur les pipettes

        self.couleur_A = '#bce3e0'  # Couleur 1
        self.couleur_B = '#cfe3bc'  # Couleur 2
        self.couleur_C = '#e3bcbc'  # Couleur 3

        # frame [] couleur A

        self.frame_color_1 = Frame(self.frame_colors)
        self.frame_color_1.grid(column=0, row=0, sticky='news')
        self.frame_color_1.columnconfigure(0, weight=1)

        self.your_font = tkinter.font.nametofont("TkDefaultFont")
        self.your_font.actual()

        # label -- couleur A

        def clic_color_button(button, legend):
            choosen_color = askcolor(legend.cget('text'))
            print(choosen_color)
            print(button)
            button.config(bg=choosen_color[1])
            legend.config(text=choosen_color[1])

        def clic_pipette_button(color_to_pipette, hexa_legend_to_update, pipette_to_update, rgb_legend_to_update):

            def rgb_to_hex(r, g, b):
                return "#{:02x}{:02x}{:02x}".format(r, g, b)

            def pipette_move(x, y):
                print(x, y)
                x1, y1 = pyautogui.position()
                px = pyautogui.pixel(x1, y1)
                print(px[1])
                hexacolorvalue = rgb_to_hex(px[0], px[1], px[2])
                rgb_color_value = str(px[0]) + ", " + str(px[1]) + ", " + str(px[2])
                print("RGB VALUE : " + rgb_color_value)
                print(hexacolorvalue)
                color_to_pipette.config(bg=hexacolorvalue)
                hexa_legend_to_update.config(text=hexacolorvalue)
                rgb_legend_to_update.config(text=rgb_color_value)
                pipette_to_update.config(bg='white', image=self.pipette_logo_image)

            def pipette_click(x, y, button, pressed):
                print((x, y, button, pressed))
                if listener_is_on:
                    print('Click detected.')
                    pipette_to_update.config(bg='lightgrey')
                    pipette_listener.stop()
                else:
                    pass
                return

            pipette_listener = self.mouse.Listener(on_click=pipette_click, on_move=pipette_move)
            pipette_listener.start()

            listener_is_on = True

        # Color A

        self.label_couleur_A = Label(self.frame_color_1, relief='ridge', image=self.img_null, width=48, height=48,
                                     bg=self.couleur_A)
        self.label_couleur_A.grid(row=0, column=0, pady=5, padx=5, sticky='news')

        # Legende A

        self.legende_couleur_A = Label(self.frame_color_1, relief='ridge', image=self.img_null,
                                       bg='lightgrey', text='#bce3e0', compound=CENTER)
        self.legende_couleur_A.grid(row=1, column=0, pady=5, padx=5, sticky='news')
        self.legende_RGB_couleur_A = Label(self.frame_color_1, relief='ridge', image=self.img_null,
                                       bg='lightgrey', text='188, 227, 224', compound=CENTER)
        self.legende_RGB_couleur_A.grid(row=2, column=0, pady=5, padx=5, sticky='news')

        # Pipette A

        self.pipette_couleur_A = Label(self.frame_color_1, relief='ridge', image=self.pipette_logo_image,
                                       bg='lightgrey', compound=CENTER)
        self.pipette_couleur_A.grid(row=3, column=0, pady=5, padx=5, sticky='news')


        # Binding A

        self.legende_couleur_A.bind('<Button-1>', lambda label: copyclip_color(self.legende_couleur_A))

        self.pipette_couleur_A.bind('<Button-1>', lambda e: clic_pipette_button(self.label_couleur_A,
                                                                                self.legende_couleur_A,
                                                                                self.pipette_couleur_A, self.legende_RGB_couleur_A))
        self.pipette_couleur_A.bind('<Enter>', lambda pipette: change_label_color(self.pipette_couleur_A, 'lightblue', "Cliquez-glissez sur l'écran pour pipetter"))
        self.pipette_couleur_A.bind('<Leave>', lambda pipette: change_label_color(self.pipette_couleur_A, 'lightgrey', "Survolez un élément pour en décrire les fonctions"))
        self.label_couleur_A.bind('<Button-1>',
                                  lambda button: clic_color_button(self.label_couleur_A, self.legende_couleur_A))

        # frame [] couleur B

        self.frame_color_2 = Frame(self.frame_colors)
        self.frame_color_2.grid(column=1, row=0, sticky='news')
        self.frame_color_2.columnconfigure(0, weight=1)

        # label -- couleur B

        self.label_couleur_B = Label(self.frame_color_2, relief='ridge', image=self.img_null, width=48, height=48,
                                     bg=self.couleur_B)
        self.label_couleur_B.grid(pady=5, padx=5, sticky='news')

        # Légende B

        self.legende_couleur_B = Label(self.frame_color_2, relief='ridge', image=self.img_null,
                                       bg='lightgrey', text='#cfe3bc', compound=CENTER)
        self.legende_couleur_B.grid(row=1, column=0, pady=5, padx=5, sticky='news')
        self.legende_RGB_couleur_B = Label(self.frame_color_2, relief='ridge', image=self.img_null,
                                       bg='lightgrey', text='207, 227, 188', compound=CENTER)
        self.legende_RGB_couleur_B.grid(row=2, column=0, pady=5, padx=5, sticky='news')

        def copyclip_color(label):
            pyperclip.copy(label.cget("text"))
            notification.notify(title="Copie d'une couleur",
                                message='Vous avez copié la couleur ' + str(label.cget("text")) + " dans le "
                                                                                                  "presse-papier.",
                                app_name='Multi-Outil',
                                app_icon='',
                                timeout=1, ticker='Couleur copiée !')
            pass

        self.legende_couleur_B.bind('<Button-1>', lambda label: copyclip_color(self.legende_couleur_B))

        # Pipette B

        self.pipette_couleur_B = Label(self.frame_color_2, relief='ridge', image=self.pipette_logo_image,
                                       bg='lightgrey', compound=CENTER)
        self.pipette_couleur_B.grid(row=3, column=0, pady=5, padx=5, sticky='news')

        # Binding B

        self.label_couleur_B.bind('<Button-1>',
                                  lambda button: clic_color_button(self.label_couleur_B, self.legende_couleur_B))
        self.pipette_couleur_B.bind('<Button-1>', lambda e: clic_pipette_button(self.label_couleur_B,
                                                                                self.legende_couleur_B,
                                                                                self.pipette_couleur_B, self.legende_RGB_couleur_B))
        self.pipette_couleur_B.bind('<Enter>', lambda pipette: change_label_color(self.pipette_couleur_B, 'lightblue', "Cliquez-glissez sur l'écran pour pipetter"))
        self.pipette_couleur_B.bind('<Leave>', lambda pipette: change_label_color(self.pipette_couleur_B, 'lightgrey', "Survolez un élément pour en décrire les fonctions"))

        self.menu_test = Menu()

        # frame [] couleur C

        self.frame_color_3 = Frame(self.frame_colors)
        self.frame_color_3.grid(column=2, row=0, sticky='news')
        self.frame_color_3.columnconfigure(0, weight=1)

        # label -- couleur C

        self.label_couleur_C = Label(self.frame_color_3, relief='ridge', image=self.img_null, width=48, height=48,
                                     bg=self.couleur_C)
        self.label_couleur_C.grid(pady=5, padx=5, sticky='news')

        # Legende couleur C

        self.legende_couleur_C = Label(self.frame_color_3, relief='ridge', image=self.img_null,
                                       bg='lightgrey', text='#e3bcbc', compound=CENTER)
        self.legende_couleur_C.grid(row=1, column=0, pady=5, padx=5, sticky='news')
        self.legende_RGB_couleur_C = Label(self.frame_color_3, relief='ridge', image=self.img_null,
                                       bg='lightgrey', text='207, 227, 188', compound=CENTER)
        self.legende_RGB_couleur_C.grid(row=2, column=0, pady=5, padx=5, sticky='news')

        # Pipette C

        self.pipette_couleur_C = Label(self.frame_color_3, relief='ridge', image=self.pipette_logo_image,
                                       bg='lightgrey', compound=CENTER)
        self.pipette_couleur_C.grid(row=3, column=0, pady=5, padx=5, sticky='news')

        # Binding C

        self.legende_couleur_C.bind('<Button-1>', lambda label: copyclip_color(self.legende_couleur_C))

        self.label_couleur_C.bind('<Button-1>',
                                  lambda button: clic_color_button(self.label_couleur_C, self.legende_couleur_C))
        self.pipette_couleur_C.bind('<Button-1>', lambda e: clic_pipette_button(self.label_couleur_C,
                                                                                self.legende_couleur_C,
                                                                                self.pipette_couleur_C, self.legende_RGB_couleur_C))
        self.pipette_couleur_C.bind('<Enter>', lambda pipette: change_label_color(self.pipette_couleur_C, 'lightblue', "Cliquez-glissez sur l'écran pour pipetter"))
        self.pipette_couleur_C.bind('<Leave>', lambda pipette: change_label_color(self.pipette_couleur_C, 'lightgrey', "Survolez un élément pour en décrire les fonctions"))
        # Frame Options

        self.frame_options = LabelFrame(self, text='Options')
        self.frame_options.pack(fill=X, expand=True, padx=5, pady=(0, 5))
        self.slider_alpha = Scale(self.frame_options, from_=25, to=100, orient=HORIZONTAL,
                                  command=update_alpha_from_slider_value,
                                  label="Opacité de l'interface (%)", borderwidth=0)
        self.slider_alpha.set(100)
        self.slider_alpha.pack(padx=10, pady=10, fill=X, expand=True)
        self.slider_alpha.pack_propagate(False)

        self.dark_theme = False

        def change_theme():

            if not self.dark_theme:
                self.config(bg=self.dark_theme_bg_color)
                for i in self.winfo_children():
                    i.configure(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.label_informatif.config(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.label_nombre_de_clics.config(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.button_launch_listener.config(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.label_compteur.config(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.button_reinitialize_count.config(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.frame_color_1.config(bg=self.dark_theme_bg_color)
                self.frame_color_2.config(bg=self.dark_theme_bg_color)
                self.frame_color_3.config(bg=self.dark_theme_bg_color)
                self.frame_informative.config(bg=self.dark_theme_bg_color)
                self.radio_dark_theme.config(bg=self.dark_theme_bg_color, fg='#bbbbbb')
                self.slider_alpha.config(bg=self.dark_theme_bg_color, fg='#bbbbbb', borderwidth=0)
                self.dark_theme = True

            else:
                self.config(bg=self.general_bg_color)
                for i in self.winfo_children():
                    i.configure(bg=self.general_bg_color, fg='black')
                self.label_informatif.config(bg=self.general_bg_color, fg='black')
                self.label_nombre_de_clics.config(bg=self.general_bg_color, fg='black')
                self.button_launch_listener.config(bg=self.general_bg_color, fg='black')
                self.label_compteur.config(bg=self.general_bg_color, fg='black')
                self.button_reinitialize_count.config(bg=self.general_bg_color, fg='black')
                self.frame_color_1.config(bg=self.general_bg_color)
                self.frame_color_2.config(bg=self.general_bg_color)
                self.frame_color_3.config(bg=self.general_bg_color)
                self.frame_informative.config(bg=self.general_bg_color)
                self.radio_dark_theme.config(bg=self.general_bg_color, fg='black')
                self.slider_alpha.config(bg=self.general_bg_color, fg='black', borderwidth=0)
                self.dark_theme = False
            pass

        self.radio_dark_theme = Checkbutton(self.frame_options, text='Thème Sombre', relief='ridge',
                                            command=lambda: change_theme())
        self.radio_dark_theme.pack(padx=10, pady=10, fill=X, expand=True)

        # self.color_chooser = tkinter.colorchooser.Chooser(self).show()


App().mainloop()
