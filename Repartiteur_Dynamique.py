import math
from tkinter import *
from tkinter import font

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure
from PIL import ImageTk, Image


# noinspection PyTypeChecker
class MainWindow:

    def __init__(self):

        """ATTRIBUTS GÉNÉRIQUES DE LA CLASSE MAIN WINDOW"""

        '''ROOT ET CONFIGURATION'''

        self.root = Tk()
        self.root.wm_attributes('-topmost', False)
        self.root.wm_attributes(())
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(4, weight=1)
        # self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.title('Répartiteur de Typologies de Surfaces - RTS')
        # self.root.resizable(False, False)

        self.bold_font = font.Font()
        self.bold_font.configure(weight='bold', size=9)

        '''PAD GÉNÉRAUX'''

        self.general_padx = 5
        self.general_pady = 5
        self.false_init_string_var = StringVar()

        '''FRAME TYPOLOGIES'''

        self.frame_typologie = LabelFrame(self.root, text="Typologies")
        self.frame_typologie.grid(row=1, column=0, sticky='news', padx=5, pady=5)

        '''FRAME GRAPHIQUE MATPLOTLIB'''

        self.frame_graphique = LabelFrame(self.root, text='Graphique')
        self.frame_graphique.grid(row=0, column=1, rowspan=2, sticky='news', padx=self.general_padx,
                                  pady=self.general_pady)
        self.frame_graphique.columnconfigure(0, weight=0)

        '''FRAME LEGENDE MATPLOTLIB'''
        self.frame_legende_matplotlib = LabelFrame(self.root, text="Légende")
        self.frame_legende_matplotlib.grid(row=0, column=2, rowspan=2, sticky='news', padx=self.general_padx,
                                           pady=self.general_pady)
        self.frame_graphique.columnconfigure(0, weight=0)

        self.img = ImageTk.PhotoImage(Image.open("Aguiles_Logo.png"))

        '''FRAME LOGO'''
        self.frame_logo = LabelFrame(self.root, text='Test')
        self.frame_logo.grid(row=4, column=0, rowspan=8, columnspan=8, sticky='news')
        self.label_logo_u = Label(self.frame_logo, image=self.img)
        self.label_logo_u.pack(side=LEFT, fill=BOTH)


        '''SELECT ALL IN ENTRY ON FOCUS'''

        def select_all_in_entry_on_focus(event):
            event.widget.select_range(0, 'end')


        '''SEQUENCE GET ALL THEN UPDATE'''

        def obtain_all_then_update():
            obtain_all_data()
            update_pie_chart()
            self.frame_graphique.update_idletasks()

        '''FRAME TOTAUX'''

        self.frame_totaux = LabelFrame(self.root, text='Totaux')
        self.frame_totaux.grid(row=0, column=0, sticky='news', pady=self.general_pady, padx=self.general_padx)
        self.frame_totaux.columnconfigure(0, weight=1)
        self.frame_totaux.rowconfigure(0, weight=1)

        '''FRAME TOTAUX CONTENEUR'''

        self.frame_totaux_conteneur = LabelFrame(self.frame_totaux, pady=5, padx=5, bg='#d6d6d6')
        self.frame_totaux_conteneur.grid(row=0, column=0, sticky='news', padx=self.general_padx, pady=self.general_pady)

        self.typo_count = 1
        self.typologies_row_count = 1

        self.button_factice_1 = Button(self.frame_totaux_conteneur, text='+')
        self.button_factice_1.grid(column=0, row=0, padx=self.general_padx, pady=self.general_pady,
                                   ipady=self.general_pady, ipadx=self.general_padx, sticky='news')

        self.button_factice_2 = Button(self.frame_totaux_conteneur, text='O')
        self.button_factice_2.grid(column=1, row=0, padx=self.general_padx, pady=self.general_pady,
                                   ipady=self.general_pady, ipadx=self.general_padx, sticky='news')

        self.totaux_surfaces_var = DoubleVar()
        self.label_totaux_surfaces = Label(self.frame_totaux_conteneur, textvariable=self.totaux_surfaces_var)
        self.label_totaux_surfaces.grid(column=2, sticky='news', row=0, pady=self.general_pady, padx=self.general_padx)

        self.label_units_surface_totale = Label(self.frame_totaux_conteneur, justify=CENTER, text='m²', relief='ridge')
        self.label_units_surface_totale.grid(column=3, row=0, pady=self.general_pady, padx=self.general_padx, ipadx=self.general_padx, ipady=self.general_pady, sticky='news')

        self.nombre_de_typologies = IntVar()
        self.nombre_de_typologies.set(str(self.typo_count) + ' Typologie(s) active(s)')

        self.label_nombre_de_typologies_totales = Label(self.frame_totaux_conteneur, justify=CENTER,
                                                        textvariable=self.nombre_de_typologies, relief='groove')
        self.label_nombre_de_typologies_totales.grid(column=4, row=0, sticky='news', pady=self.general_pady,
                                                     padx=self.general_padx, ipadx=5)

        '''TOTAL DES POURCENTAGES'''
        self.label_litteral_totaux_pourcents = Label(self.frame_totaux_conteneur, text='Pourcentage Total :',
                                                     relief='ridge')
        self.label_litteral_totaux_pourcents.grid(column=5, sticky='news', row=0, pady=self.general_pady,
                                                  padx=self.general_padx, ipadx=self.general_padx,
                                                  ipady=self.general_pady)

        self.totaux_percent_var = DoubleVar()
        self.label_totaux_pourcents = Label(self.frame_totaux_conteneur, textvariable=self.totaux_percent_var,
                                            relief='groove')
        self.label_totaux_pourcents.grid(column=6, sticky='news', row=0, pady=self.general_pady, padx=self.general_padx,
                                         ipadx=self.general_padx, ipady=self.general_pady)

        '''SURFACE A PEUPLER'''

        self.label_surface_a_peupler = Label(self.frame_totaux_conteneur, text='Surface à peupler :', justify=CENTER,
                                             pady=self.general_pady, padx=self.general_padx)
        self.label_surface_a_peupler.grid(row=0, column=7, sticky='news', ipady=self.general_pady, ipadx=self.general_padx)

        self.surface_a_peupler_var = DoubleVar()
        self.surface_a_peupler_var.set(100.0)
        '''ENTREE DE SURFACE A PEUPLER'''
        self.entry_surface_a_peupler = Entry(self.frame_totaux_conteneur, textvariable=self.surface_a_peupler_var,
                                             justify=CENTER)
        self.entry_surface_a_peupler.grid(row=0, column=8, sticky='news')
        self.entry_surface_a_peupler.bind("<FocusIn>", select_all_in_entry_on_focus)

        self.label_surface_totale_restante = Label(self.frame_totaux_conteneur, text='Surface totale\nnon allouée :',
                                                   justify=CENTER, padx=self.general_padx, pady=self.general_pady)
        self.label_surface_totale_restante.grid(row=0, column=9, sticky='news', ipadx=self.general_padx,
                                                ipady=self.general_pady)
        self.surface_totale_non_allouee_var = DoubleVar()
        self.label_surface_totale_restante_view = Label(self.frame_totaux_conteneur, relief='ridge',
                                                        textvariable=self.surface_totale_non_allouee_var)
        self.label_surface_totale_restante_view.grid(row=0, column=10, sticky='news', ipadx=self.general_padx,
                                                ipady=self.general_pady)

        '''UPDATE DE LA TARTE'''

        def update_pie_chart():

            """OBTENTION DES NOUVELLES DONNES VIA GET ALL SURFACES"""

            '''Valeurs des tranches de la tourte'''
            new_sizes = obtain_all_data()[7] + [sum(obtain_all_data()[5])]
            new_units = obtain_all_data()[6] + ['']

            '''Nouveaux Labels'''
            new_labels = obtain_all_data()[4] + ['Surface restante']
            new_labels_renamed = []

            "Concaténation des infos de la légende"
            for ig, ug, og in zip(new_labels, new_sizes, new_units):
                if ig == 'Surface restante':
                    ig = ig + ' : ' + str(round(sum(obtain_all_data()[5]),2)) + ' (m²)'
                    new_labels_renamed.append(ig)
                else:
                    ig = ig + ' : ' + str(ug) + ' (m²) / ' + str(og) + ' (u)'
                    new_labels_renamed.append(ig)

            '''RAPPEL DES AXES ET DU CANVAS'''

            axes = self.ax
            axes_2 = self.ax_2
            canvas = self.canvas_pie
            canvas_legend = self.canvas_legend

            '''NETTOYAGE DES AXES'''

            axes.clear()
            axes_2.clear()

            '''DEFINITION DE LA NOUVELLE TARTE'''

            wedges, texts, autotexts = axes.pie(new_sizes, radius=self.pie_radius, autopct='%1.1f%%', normalize=True,
                                                shadow=False,
                                                colors=["#bce3e0", "#6bb4da", "#547cda", "#324e98", "#badad7"],
                                                frame=False)

            for autotext in autotexts:
                autotext.set_bbox({'facecolor': 'white', 'edgecolor': 'white', 'alpha': 0.7})

            '''Coloriage de la part restante en rouge pâle'''
            label_to_color = {'Surface restante': '#e3bcbc'}
            for wedge, label in zip(wedges, new_labels):
                if label in label_to_color:
                    wedge.set_facecolor(label_to_color[label])

            '''Ajout du cercle blanc du donut'''
            self.circle = plt.Circle((0, 0), self.white_circle_radius, color='white', fc='white', linewidth=1.25)
            self.ax.add_artist(self.circle)

            axes.legend(wedges, labels=new_labels_renamed, loc='lower left', bbox_to_anchor=(0, 1.2, 0, 1.2))

            '''Need to set up a color set, that can respond to any number of typologies. A base color being
            declined through iterative mathematics and RGB values '''


            canvas.draw()
            canvas_legend.draw()

            return canvas, canvas_legend

        '''OBTENTION D'UN MAXIMUM DE DONNEES'''

        def obtain_all_data():
            frames_values = []
            '''Recherche les frames contenues dans self.frame_typologie, avec winfo_children'''
            for child in self.frame_typologie.winfo_children():
                '''Append les frames trouvées dans une liste frames_values'''
                frames_values.append(child)

            widgets_values = []
            for grand_child in frames_values:

                widgets_values.append(grand_child.winfo_children())
            '''Pré déclarations des différentes listes'''
            list_of_surfaces = []
            list_of_percents = []
            list_of_typo_names = []
            list_of_max_units = []
            list_of_surfaces_restantes = []
            list_of_implanted_units_values = []
            list_of_surfaces_allouees_utilisees = []
            for descendants in widgets_values:
                max_units_var = IntVar()
                surface_restante = DoubleVar()
                surface_allouee_utilisee = 0
                name_of_typo = StringVar()
                surface_totale_allouee = DoubleVar()
                implanted_units_var = IntVar()
                selected_widget = descendants[2]




                # list_of_max_units.append(int(selected_widget.nametowidget(descendants[6]).get()))

                name_of_typo_entry = selected_widget.nametowidget(descendants[4])
                name_of_typo_entry_value = str(selected_widget.nametowidget(descendants[4]).get())
                name_of_typo_entry['textvariable'] = name_of_typo
                name_of_typo.set(name_of_typo_entry_value)

                '''Agrégation des différentes listes'''
                ''' -Surfaces'''
                list_of_surfaces.append(float(selected_widget.nametowidget(descendants[2]).get()))
                '''-Noms'''
                list_of_typo_names.append(str(name_of_typo_entry_value))
                '''-Pourcentages'''
                list_of_percents.append(float(selected_widget.nametowidget(descendants[11]).get()))
                '''Surface totale allouée de la typologie'''
                surface_totale_allouee_value = self.surface_a_peupler_var.get() * float(
                    selected_widget.nametowidget(descendants[11]).get()) / 100
                '''Surface de la typologie'''
                surface_typo_atteinte = float(selected_widget.nametowidget(descendants[2]).get())
                '''Pourcentage de la typologie'''
                pourcentage_atteint = float(selected_widget.nametowidget(descendants[11]).get())

                '''UPDATE UNITES MAX'''


                max_units_var_label = selected_widget.nametowidget(descendants[6])
                max_units_var_label['textvariable'] = max_units_var
                max_units_var.set(
                    int(self.surface_a_peupler_var.get() / float(selected_widget.nametowidget(descendants[2]).get())))

                '''UPDATE IMPLANTED UNITS'''

                implanted_units_var_label = selected_widget.nametowidget(descendants[8])
                implanted_units_var_label['textvariable'] = implanted_units_var
                implanted_units_value = math.floor(
                    ((self.surface_a_peupler_var.get() * pourcentage_atteint) / 100) / surface_typo_atteinte)
                implanted_units_var.set(implanted_units_value)
                list_of_implanted_units_values.append(implanted_units_value)

                try:
                    surface_modulo_restant_value = (
                            surface_totale_allouee_value - (implanted_units_value * surface_typo_atteinte))
                    surface_allouee_utilisee = implanted_units_value * surface_typo_atteinte

                except ZeroDivisionError as e:
                    surface_modulo_restant_value = 0.0


                '''SURFACES RESTANTES'''

                '''Agrégation en liste des surfaces restantes'''
                list_of_surfaces_restantes.append(surface_modulo_restant_value)
                '''Agrégation en liste des surfaces utilisées'''
                list_of_surfaces_allouees_utilisees.append(surface_allouee_utilisee)

                surface_restante_var_label = selected_widget.nametowidget(descendants[10])
                surface_restante_var_label['textvariable'] = surface_restante
                surface_restante.set(str(round(surface_modulo_restant_value, 2)) + ' | ' + str(
                    round(surface_totale_allouee_value, 2)) + " m²")


                implanted_units_var_label['textvariable'] = implanted_units_var

            '''LISTE DES UNITES MAX'''

            for surfaces in list_of_surfaces:
                list_of_max_units.append(self.surface_a_peupler_var.get() / surfaces)


            self.totaux_percent_var.set(sum(list_of_percents))
            self.totaux_surfaces_var.set(round(sum(list_of_surfaces), 2))

            if self.totaux_percent_var.get() > 100:
                self.label_totaux_pourcents.configure(fg='red')
                self.label_totaux_pourcents.configure(bg='#e3bcbc')
            elif self.totaux_percent_var.get() == 100:
                self.label_totaux_pourcents.configure(fg='green')
                self.label_totaux_pourcents.configure(bg='#cfe3bc')
            else:
                self.label_totaux_pourcents.configure(fg='black')
                self.label_totaux_pourcents.configure(bg='#bce3e0')

            self.nombre_de_typologies.set(str(self.typo_count - 1) + ' Typologie(s) active(s)')
            self.root.update()
            self.frame_graphique.update_idletasks()

            return sum(list_of_surfaces), sum(
                list_of_percents), list_of_surfaces, list_of_percents, list_of_typo_names, list_of_surfaces_restantes, list_of_implanted_units_values, list_of_surfaces_allouees_utilisees

        def update_alpha_from_slider_value(slider):

            alpha_slider_value = self.slider_alpha.get()

            self.root.attributes('-alpha', alpha_slider_value / 100)

        def on_enter_create_button(event):
            event.widget.config(bg='#cfe3bc')

        def on_enter_delete_button(event, islocked):
            if islocked:
                event.widget.config(bg='#b4b4b4')

            else:
                event.widget.config(bg='#ffbfbf')

        def on_leave(event):
            event.widget.config(bg='SystemButtonFace')

        # Création du graphique

        '''PREMIERE TARTE EN DUR'''

        self.white_circle_radius = 0.3
        self.pie_radius = 1.5

        '''FIGURES MATPLOTLIB'''

        self.fig = Figure(figsize=(4, 4), tight_layout=True)
        self.fig_2 = Figure(figsize=(3, 5))

        self.ax = self.fig.add_subplot(111, label='Axes')
        self.ax_2 = self.fig_2.add_subplot(111)
        self.ax_2.axis('off')

        self.tailles_tourtes = obtain_all_data()[3]
        self.labels_tourtes = obtain_all_data()[4]

        self.ax.pie(self.tailles_tourtes, radius=self.pie_radius, autopct='%1.1f%%', normalize=True,
                    shadow=False, colors=["#bce3e0", "#6bb4da", "#547cda", "#324e98", "#badad7"],
                    frame=False)

        self.circle = plt.Circle((0, 0), self.white_circle_radius, color='white', fc='white', linewidth=1.25)
        self.ax.add_artist(self.circle)

        self.canvas_pie = FigureCanvasTkAgg(self.fig, master=self.frame_graphique)
        self.canvas_legend = FigureCanvasTkAgg(self.fig_2, master=self.frame_legende_matplotlib)

        self.canvas_pie.draw()
        self.canvas_pie.get_tk_widget().pack(expand=True, fill=BOTH, side=TOP)
        self.canvas_legend.draw()

        self.surface_a_peupler_var.trace_add('write', lambda x, y, z: obtain_all_then_update())

        self.slider_alpha = Scale(self.root, from_=25, to=100, orient=HORIZONTAL,
                                  command=update_alpha_from_slider_value, borderwidth=0)
        self.slider_alpha.set(100)
        self.slider_alpha.grid(row=2, column=0, columnspan=7, sticky='news')

        ''' CREATION DE TYPOLOGIES ----- !'''

        def create_new_typo(islocked=False):

            def delete_typologie():

                """utilise le parent du bouton delete pour accéder à la frame à supprimer"""
                frame_to_delete = self.frame_typologie.nametowidget(new_delete_button.winfo_parent())
                '''supprime la frame'''
                frame_to_delete.destroy()

                # self.frame_to_destroy = self.frame_typologie.nametowidget(self.new_frame_name)
                # self.frame_to_destroy.destroy()
                '''altère le compte de typologie de -1'''
                self.typo_count -= 1
                '''update les données et le donut'''
                obtain_all_then_update()
                pass

            new_frame_name = str('newFrame_' + str(self.typo_count))
            new_frame = LabelFrame(self.frame_typologie,
                                   name=new_frame_name)
            new_frame.grid(row=self.typologies_row_count, padx=5, pady=5)
            new_frame.configure(bg='#d6d6d6')

            '''CREATE TYPO BUTTON'''
            new_create_button = Button(new_frame,
                                       text='+',
                                       name=str("bouton_new_typo_" + str(self.typo_count)),
                                       command=create_new_typo)
            new_create_button.grid(row=self.typologies_row_count,
                                   column=0,
                                   pady=5,
                                   padx=5, sticky='news', ipadx=5)
            new_create_button.bind('<Enter>', on_enter_create_button)
            new_create_button.bind('<Leave>', on_leave)

            '''DELETE BUTTON'''

            new_delete_button = Button(new_frame, text='X',
                                       name=str("button_delete_typo_" + str(self.typo_count)),
                                       command=delete_typologie)
            new_delete_button.grid(row=self.typologies_row_count,
                                   column=1, sticky='news', pady=5, padx=5, ipadx=5)
            new_delete_button.bind('<Enter>', lambda event: on_enter_delete_button(event, islocked=islocked))
            new_delete_button.bind('<Leave>', on_leave)

            '''Si le widget est appelé locké, le bouton de suppression est désactivé'''
            if not islocked:
                pass
            if islocked:
                new_delete_button.config(state="disabled")

            '''Variable Tkinter de la surface de la typologie'''
            typo_surface_var = DoubleVar()
            typo_surface_entry = Entry(new_frame, justify=CENTER, textvariable=typo_surface_var,
                                       name=str('surfaceEntry_' + str(self.typo_count)))
            typo_surface_entry.grid(row=self.typologies_row_count,
                                    column=2,
                                    pady=5, padx=5, sticky='news')
            '''Valeur initiale de la variable de surface de typologie'''
            typo_surface_var.set("20.0")

            '''Label des unités de typologies placées'''
            typo_surface_unit = Label(new_frame, justify=CENTER, text='m²', relief='ridge')
            typo_surface_unit.grid(row=self.typologies_row_count, column=3, pady=5, padx=5, ipadx=5, sticky='news')
            '''Variable du nom de la typologie'''
            typo_name_entry_string_var = StringVar()
            '''Entrée du nom de la typologie'''
            typo_name_entry = Entry(new_frame, textvariable=typo_name_entry_string_var,
                                    name=str('nomSurface_' + str(self.typo_count)), justify=CENTER)
            typo_name_entry.grid(row=self.typologies_row_count,
                                 column=4,
                                 pady=5,
                                 padx=5,
                                 sticky='news')
            '''Valeur initiale de la variable du nom de la typologie'''
            typo_name_entry_string_var.set('Nom Typo ' + str(self.typo_count))

            '''Label informatif du maximum unitaire par typologies'''
            typo_maximum_unitaire_label = Label(new_frame, text="Maximum \n d'unités :")
            typo_maximum_unitaire_label.grid(row=self.typologies_row_count,
                                             column=6,
                                             pady=5,
                                             padx=5,
                                             sticky='news')

            typo_maximum_unitaire_var = IntVar()
            typo_maximum_unitaire_var.set(self.surface_a_peupler_var.get() / typo_surface_var.get())
            typo_maximum_unitaire_view = Label(new_frame, justify=CENTER, textvariable=typo_maximum_unitaire_var,
                                               relief='ridge')
            typo_maximum_unitaire_view.grid(row=self.typologies_row_count, column=7, pady=5, padx=5, ipadx=5,
                                            sticky='news')

            '''QUANTITE IMPLANTEE'''

            typo_qut_implante_label = Label(new_frame, justify=CENTER, text="Unités \n implantées : ")
            typo_qut_implante_label.grid(row=self.typologies_row_count, column=8, pady=5, padx=5, ipadx=5,
                                         sticky='news')

            typo_quantite_implante_var = IntVar()
            typo_quantite_implante_view = Label(new_frame, justify=CENTER, textvariable=typo_quantite_implante_var,
                                                relief='ridge', name='qt_implantee', font=self.bold_font)
            typo_quantite_implante_view.grid(row=self.typologies_row_count, column=9, pady=5, padx=5, ipadx=5,
                                             sticky='news')

            '''SURFACE RESTANTE (MODULO)'''

            typo_surface_restante_label = Label(new_frame, justify=CENTER, text="Surface allouée \nrestante | totale :")
            typo_surface_restante_label.grid(row=self.typologies_row_count, column=10, pady=5, padx=5, ipadx=5,
                                             sticky='news')

            typo_surface_renstante_var = DoubleVar()
            typo_surface_renstante_view = Label(new_frame, justify=CENTER, textvariable=typo_surface_renstante_var,
                                                relief='ridge', name='surface_restante')
            typo_surface_renstante_view.grid(row=self.typologies_row_count, column=11, pady=5, padx=5, ipadx=5,
                                             sticky='news')

            def test_trace(*args):

                obtain_all_data()
                obtain_all_then_update()

            def on_mousewheel_slider(event):
                current_value = typo_slider_percent.get()
                if event.delta > 0:
                    new_value = current_value + 1
                else:
                    new_value = current_value - 1
                typo_slider_percent.set(new_value)
                obtain_all_then_update()


            typo_name_entry.bind("<FocusIn>", select_all_in_entry_on_focus)
            typo_name_entry.bind("<Return>", test_trace)
            typo_surface_entry.bind("<FocusIn>", select_all_in_entry_on_focus)
            typo_surface_var.trace_add('write', lambda x, y, z: test_trace())
            typo_name_entry_string_var.trace_add('write', lambda x, y, z: test_trace())

            typo_slider_percent = Scale(new_frame, from_=1.00, to=100.00, orient=HORIZONTAL, label="% de surface à peupler",
                                        length=150, digits=2, command=lambda e: obtain_all_data())
            typo_slider_percent.grid(row=self.typologies_row_count, column=5, padx=5, pady=5, sticky='news')
            typo_slider_percent.set(20.0)
            typo_slider_percent.bind("<MouseWheel>", on_mousewheel_slider)
            typo_slider_percent.bind("<ButtonRelease-1>", lambda x: obtain_all_then_update())

            # self.typo_name_entry_string_var.trace_add('write', test_trace_bis)

            self.typo_count += 1
            self.typologies_row_count += 1
            obtain_all_data()
            update_pie_chart()
            self.frame_typologie.grid(row=1, column=0, sticky='news', padx=5, pady=5)
            self.root.update()

        # self.button_get_all_surfaces_entry = Button(text='Get', command=obtain_all_data)
        # self.button_get_all_surfaces_entry.grid()

        create_new_typo(islocked=True)
        create_new_typo(islocked=False)
        create_new_typo(islocked=False)
        create_new_typo(islocked=False)
        obtain_all_data()
        self.root.mainloop()


if __name__ == '__main__':
    MainWindow()
