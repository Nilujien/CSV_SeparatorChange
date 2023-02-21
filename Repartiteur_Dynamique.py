from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure


# noinspection PyTypeChecker
class MainWindow:

    def __init__(self):

        """ATTRIBUTS GÉNÉRIQUES DE LA CLASSE MAIN WINDOW"""

        '''ROOT ET CONFIGURATION'''

        self.root = Tk()
        self.root.wm_attributes('-topmost', True)
        self.root.rowconfigure((0, 1), weight=1)
        self.root.columnconfigure((0, 1), weight=1)
        # self.root.resizable(False, False)

        '''PAD GÉNÉRAUX'''

        self.general_padx = 5
        self.general_pady = 5

        '''FRAME TYPOLOGIES'''

        self.frame_typologie = LabelFrame(self.root, text="Typologies")
        self.frame_typologie.grid(row=1, column=0, sticky='news', padx=5, pady=5)

        '''FRAME GRAPHIQUE MATPLOTLIB'''

        self.frame_graphique = LabelFrame(self.root, text="Graphique")
        self.frame_graphique.grid(row=0, column=1, rowspan=2, sticky='news', padx=self.general_padx,
                                  pady=self.general_pady)
        self.frame_graphique.columnconfigure(0, weight=0)

        '''SELECT ALL IN ENTRY ON FOCUS'''

        def select_all_in_entry_on_focus(event):
            print('prout')
            event.widget.select_range(0, 'end')
            print('prout')

        '''SEQUENCE GET ALL THEN UPDATE'''

        def get_all_then_update():
            get_all_surfaces()
            update_pie_chart()
            self.frame_graphique.update_idletasks()

        '''TEST BUTTON'''
        # self.update_pie_button = Button(self.frame_graphique, text='Update Pie', command=get_all_then_update)
        # self.update_pie_button.pack()

        '''FRAME TOTAUX'''

        self.frame_totaux = LabelFrame(self.root, text='Totaux')
        self.frame_totaux.grid(row=0, column=0, sticky='news', pady=self.general_pady, padx=self.general_padx)
        self.frame_totaux.columnconfigure(0, weight=0)
        self.frame_totaux.rowconfigure(0, weight=0)

        '''FRAME TOTAUX CONTENEUR'''

        self.frame_totaux_conteneur = LabelFrame(self.frame_totaux, pady=5, padx=5)
        self.frame_totaux_conteneur.grid(row=0, column=0, sticky='news', padx=self.general_padx, pady=self.general_pady)

        self.typo_count = 1
        self.typologies_row_count = 1

        self.button_factice_1 = Button(self.frame_totaux_conteneur, text='+')
        self.button_factice_1.grid(column=0, row=0, padx=self.general_padx, pady=self.general_pady)

        self.button_factice_2 = Button(self.frame_totaux_conteneur, text='O')
        self.button_factice_2.grid(column=1, row=0, padx=self.general_padx, pady=self.general_pady)

        self.totaux_surfaces_var = DoubleVar()
        self.label_totaux_surfaces = Label(self.frame_totaux_conteneur, textvariable=self.totaux_surfaces_var)
        self.label_totaux_surfaces.grid(column=2, sticky='news', row=0, pady=self.general_pady, padx=self.general_padx)

        self.label_units_surface_totale = Label(self.frame_totaux_conteneur, justify=CENTER, text='m²', relief='ridge')
        self.label_units_surface_totale.grid(column=3, row=0, pady=5, padx=5, ipadx=5, ipady=5, sticky='news')

        self.nombre_de_typologies = IntVar()
        self.nombre_de_typologies.set(str(self.typo_count) + ' Typologie(s) actives')

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
        self.label_surface_a_peupler.grid(row=0, column=7)

        self.surface_a_peupler_var = DoubleVar()
        self.surface_a_peupler_var.set(100.0)
        # self.surface_a_peupler_var.trace_add('write', get_all_then_update())
        self.entry_surface_a_peupler = Entry(self.frame_totaux_conteneur, textvariable=self.surface_a_peupler_var,
                                             justify=CENTER)
        self.entry_surface_a_peupler.grid(row=0, column=8, sticky='news')
        self.entry_surface_a_peupler.bind("<FocusIn>", select_all_in_entry_on_focus)

        '''UPDATE DE LA TARTE'''

        def update_pie_chart():

            """OBTENTION DES NOUVELLES DONNES VIA GET ALL SURFACES"""

            new_sizes = get_all_surfaces()[3]
            new_labels = get_all_surfaces()[4]

            nombre_de_valeurs = len(new_labels)
            valeurs_explosion = []
            for i in new_sizes:
                valeurs_explosion.append(0.05)
            print(valeurs_explosion)

            print('Nombre de valeurs = ' + str(nombre_de_valeurs))

            '''RAPPEL DES AXES ET DU CANVAS'''

            axes = self.ax
            canvas = self.chart_1

            '''NETTOYAGE DES AXES'''

            axes.clear()
            axes.set_aspect('equal')

            '''DEFINITION DE LA NOUVELLE TARTE'''

            axes.pie(new_sizes, labels=new_labels, radius=self.pie_radius, autopct='%1.1f%%', normalize=True,
                     shadow=False, colors=["#bce3e0", "#6bb4da", "#547cda", "#324e98", "#badad7"],
                     frame=False, explode=valeurs_explosion)

            '''Need to set up a color set, that can respond to any number of typologies. A base color being
            declined through iterative mathematics and RGB values '''

            self.circle = plt.Circle((0, 0), self.white_circle_radius, color='white', fc='white', linewidth=1.25)
            self.ax.add_artist(self.circle)
            canvas.draw()
            canvas.get_tk_widget().update_idletasks()
            print(new_sizes)
            print(new_labels)
            print("Update completed")

        '''OBTENTION D'UN MAXIMUM DE DONNEES'''

        def get_all_surfaces():
            entry_values = []
            for child in self.frame_typologie.winfo_children():
                # print(str(child))
                entry_values.append(child)
            # print(entry_values)
            nephew_values = []
            for nephew in entry_values:
                # print(nephew.winfo_children())
                nephew_values.append(nephew.winfo_children())
            print('NEPHEW VALUES')
            print(nephew_values)
            list_of_surfaces = []
            list_of_percents = []
            list_of_typo_names = []
            list_of_max_units = []
            for descendants in nephew_values:
                my_var = IntVar()
                selected_widget = descendants[2]
                print('TEST')
                print(selected_widget.nametowidget(descendants[2]).get())

                # list_of_max_units.append(int(selected_widget.nametowidget(descendants[6]).get()))

                list_of_surfaces.append(float(selected_widget.nametowidget(descendants[2]).get()))
                list_of_typo_names.append(str(selected_widget.nametowidget(descendants[4]).get()))
                list_of_percents.append(float(selected_widget.nametowidget(descendants[7]).get()))

                widget_object = selected_widget.nametowidget(descendants[6])
                # print(widget_object)
                widget_object['textvariable'] = my_var
                my_var.set(int(self.surface_a_peupler_var.get()/float(selected_widget.nametowidget(descendants[2]).get())))

            for surfaces in list_of_surfaces:

                list_of_max_units.append(self.surface_a_peupler_var.get() / surfaces)
                # print('Maximums Unitaires : ')
                # print(list_of_max_units)

                # print(list_of_surfaces)
                # print(sum(list_of_surfaces))
                # print(list_of_percents)
                # print(list_of_typo_names)

            self.totaux_percent_var.set(sum(list_of_percents))
            self.totaux_surfaces_var.set(sum(list_of_surfaces))

            if self.totaux_percent_var.get() > 100:
                self.label_totaux_pourcents.configure(fg='red')
            else:
                self.label_totaux_pourcents.configure(fg='black')

            self.nombre_de_typologies.set(str(self.typo_count - 1) + ' Typologie(s) actives')
            self.root.update()
            self.frame_graphique.update()

            return sum(list_of_surfaces), sum(list_of_percents), list_of_surfaces, list_of_percents, list_of_typo_names

        # Création du graphique

        '''PREMIERE TARTE EN DUR'''

        self.white_circle_radius = 0.3
        self.pie_radius = 1.2

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111, label='Axes')

        self.tailles_tourtes = get_all_surfaces()[3]
        self.labels_tourtes = get_all_surfaces()[4]

        self.ax.pie(self.tailles_tourtes, radius=self.pie_radius, autopct='%1.1f%%', normalize=True,
                    labels=self.labels_tourtes,
                    shadow=False, colors=["#bce3e0", "#6bb4da", "#547cda", "#324e98", "#badad7"],
                    frame=False)

        self.circle = plt.Circle((0, 0), self.white_circle_radius, color='white', fc='white', linewidth=1.25)
        self.ax.add_artist(self.circle)

        self.chart_1 = FigureCanvasTkAgg(self.fig, self.frame_graphique)
        self.chart_1.get_tk_widget().pack(expand=True, fill=BOTH, side=TOP, padx=self.general_padx,
                                          pady=self.general_pady)

        self.chart_1.draw()

        def update_alpha_from_slider_value(slider):
            print(slider)
            alpha_slider_value = self.slider_alpha.get()
            print(self.slider_alpha.get())
            self.root.attributes('-alpha', alpha_slider_value / 100)

        self.slider_alpha = Scale(self.root, from_=25, to=100, orient=HORIZONTAL,
                                  command=update_alpha_from_slider_value,
                                  label="Opacité de l'interface (%)", borderwidth=0)
        self.slider_alpha.set(100)
        self.slider_alpha.grid(row=2, column=0, padx=10, pady=10, columnspan=7, sticky='news')

        def create_new_typo(islocked=False):

            def delete_typologie():
                print(new_delete_button.winfo_parent())
                frame_to_delete = self.frame_typologie.nametowidget(new_delete_button.winfo_parent())
                frame_to_delete.destroy()
                # self.frame_to_destroy = self.frame_typologie.nametowidget(self.new_frame_name)
                # self.frame_to_destroy.destroy()
                self.typo_count -= 1
                get_all_then_update()
                pass

            new_frame_name = str('newFrame_' + str(self.typo_count))
            new_frame = LabelFrame(self.frame_typologie,
                                   text=('T - ' + str(self.typo_count)),
                                   name=new_frame_name)
            new_frame.grid(row=self.typologies_row_count, padx=5, pady=5)
            new_create_button = Button(new_frame,
                                       text='+',
                                       name=str("bouton_new_typo_" + str(self.typo_count)),
                                       command=create_new_typo)
            new_create_button.grid(row=self.typologies_row_count,
                                   column=0,
                                   pady=5,
                                   padx=5, sticky='news', ipadx=5)
            new_delete_button = Button(new_frame, text='X',
                                       name=str("button_delete_typo_" + str(self.typo_count)),
                                       command=delete_typologie)
            new_delete_button.grid(row=self.typologies_row_count,
                                   column=1, sticky='news', pady=5, padx=5, ipadx=5)
            if not islocked:
                pass
            if islocked:
                new_delete_button.config(state="disabled")

            typo_surface_var = DoubleVar()

            typo_surface_entry = Entry(new_frame, justify=CENTER, textvariable=typo_surface_var,
                                       name=str('surfaceEntry_' + str(self.typo_count)))

            typo_surface_entry.grid(row=self.typologies_row_count,
                                    column=2,
                                    pady=5, padx=5, sticky='news')

            typo_surface_var.set("20.0")

            typo_surface_unit = Label(new_frame, justify=CENTER, text='m²', relief='ridge')
            typo_surface_unit.grid(row=self.typologies_row_count, column=3, pady=5, padx=5, ipadx=5, sticky='news')

            typo_name_entry = Entry(new_frame, name=str('nomSurface_' + str(self.typo_count)), justify=CENTER)
            typo_name_entry.insert(0, str('Nom Typo ' + str(self.typo_count)))
            typo_name_entry.grid(row=self.typologies_row_count,
                                 column=4,
                                 pady=5,
                                 padx=5,
                                 sticky='news')

            typo_maximum_unitaire_label = Label(new_frame, text='Maximum \n unitaire :')
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

            def test_trace(*args):
                print('Test_Trace')
                print(typo_surface_var.get())
                get_all_surfaces()
                get_all_then_update()

            def on_mousewheel_slider(event):
                current_value = typo_slider_percent.get()
                if event.delta > 0:
                    new_value = current_value + 1
                else:
                    new_value = current_value - 1
                typo_slider_percent.set(new_value)
                get_all_then_update()

            typo_name_entry.bind("<FocusIn>", select_all_in_entry_on_focus)
            typo_surface_entry.bind("<FocusIn>", select_all_in_entry_on_focus)
            typo_surface_var.trace_add('write', test_trace)

            typo_slider_percent = Scale(new_frame, from_=1, to=100, orient=HORIZONTAL, label="% de surface à peupler",
                                        length=150, command=lambda e: get_all_surfaces())
            typo_slider_percent.grid(row=self.typologies_row_count, column=5, padx=5, pady=5, sticky='news')
            typo_slider_percent.bind("<MouseWheel>", on_mousewheel_slider)
            typo_slider_percent.bind("<ButtonRelease-1>", lambda x: get_all_then_update())

            self.typo_count += 1
            self.typologies_row_count += 1
            get_all_surfaces()
            update_pie_chart()
            self.frame_typologie.grid(row=1, column=0, sticky='news', padx=5, pady=5)
            self.root.update()

        # self.button_get_all_surfaces_entry = Button(text='Get', command=get_all_surfaces)
        # self.button_get_all_surfaces_entry.grid()

        create_new_typo(islocked=True)
        create_new_typo(islocked=False)
        create_new_typo(islocked=False)
        get_all_surfaces()

        self.root.mainloop()


if __name__ == '__main__':
    MainWindow()
