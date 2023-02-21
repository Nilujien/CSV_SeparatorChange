# pourcentages en input
# surfaces en input

import math
from tkinter import *
import tkinter.ttk as ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure


def callback(aba, bab, cac):
    print((aba, bab, cac))
    liste_de_resultats_unitaire_pourcentages = []
    liste_de_resultats_unitaires_maximums = []
    liste_des_modulos = []
    count = 0

    for o, s, ef in zip(ensemble_des_resultats_unitaires_pourcentages, total_des_unites_max, modulo_total_var):
        for q, r in zip(ensemble_stringvar_surfaces, ensemble_des_pourcentages_input):
            surface_de_la_typologie = q.get()
            print('Surface de la typologie : ' + str(surface_de_la_typologie))
            surface_totale = valeur_surface_a_peupler.get()
            pourcentage_unitaire = r.get()
            calcul_unites_par_pourcentages = math.ceil(
                (float(surface_totale) * pourcentage_unitaire / 100) / surface_de_la_typologie)
            calcul_du_modulo_par_pourcentages = (float(
                surface_totale) * pourcentage_unitaire / 100) / surface_de_la_typologie % 1
            calcul_du_maximum_unitaire = math.ceil(float(surface_totale) / surface_de_la_typologie)
            print("Modulo : " + str(calcul_du_modulo_par_pourcentages))
            liste_de_resultats_unitaire_pourcentages.append(calcul_unites_par_pourcentages)
            liste_de_resultats_unitaires_maximums.append(calcul_du_maximum_unitaire)
            liste_des_modulos.append(calcul_du_modulo_par_pourcentages)
            liste_des_valeurs_de_pourcentages.append(pourcentage_unitaire)
            valeur_Pourcentage_total.set(math.fsum(liste_des_valeurs_de_pourcentages))

        print(liste_des_modulos)
        print("liste des résultats unitaires par pourcentages : " + str(liste_de_resultats_unitaire_pourcentages))
        # total_des_modulos = math.fsum(liste_des_modulos)
        o.set(liste_de_resultats_unitaire_pourcentages[count])
        s.set(str(liste_de_resultats_unitaires_maximums[count]))
        ef.set(round(liste_des_modulos[count], 3))
        count += 1

        liste_de_resultats_unitaire_pourcentages.clear()
        liste_de_resultats_unitaires_maximums.clear()
        liste_des_modulos.clear()
        liste_des_valeurs_de_pourcentages.clear()
    inital_donut.update()
    pass


root = Tk()

ttk.Style().configure('pad.TEntry', padding='5 5 5 5')
ttk.Style().configure('border.TLabel', border='sunken')

root.title("Aghiles - Répartiteur de Typologies")
# root.attributes('-topmost', True)
# noinspection PyTypeChecker
root.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
# noinspection PyTypeChecker
root.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

padx_general = 1
pady_general = 1

modulo_1_var = DoubleVar()
modulo_2_var = DoubleVar()
modulo_3_var = DoubleVar()
modulo_4_var = DoubleVar()
modulo_5_var = DoubleVar()

modulo_total_var = (modulo_5_var, modulo_4_var, modulo_3_var, modulo_2_var, modulo_1_var)

label_modulo_1 = ttk.Label(root, textvariable=modulo_1_var)
label_modulo_2 = ttk.Label(root, textvariable=modulo_2_var)
label_modulo_3 = ttk.Label(root, textvariable=modulo_3_var)
label_modulo_4 = ttk.Label(root, textvariable=modulo_4_var)
label_modulo_5 = ttk.Label(root, textvariable=modulo_5_var)

label_modulo_total = (label_modulo_1, label_modulo_5, label_modulo_4, label_modulo_3, label_modulo_2)

row_modulo = 1
for h in label_modulo_total:
    h.grid(row=row_modulo, column=6, padx=padx_general, pady=pady_general)
    row_modulo += 1

label_typologies = Label(root, text="Typologies", padx=padx_general, pady=pady_general)
label_pourcentages = Label(root, text="Pourcentages \n de surface totale à peupler",
                           padx=padx_general, pady=pady_general)
label_surface_a_peupler = Label(root, text="Surface à peupler (m²)", padx=padx_general, pady=pady_general)
label_surface_typologie = Label(root, text="Surface (m²)", padx=padx_general, pady=pady_general)
label_resultats_unitaires = Label(root, text="Maximums \n unitaires", padx=padx_general,
                                  pady=pady_general)
label_resultats_unitaires_pourcentages = Label(root, text="Nombre de typologies\n implémentées")
label_modulo = Label(root, text="Surface restante (m²)", padx=padx_general, pady=pady_general)

label_typologies.grid(column=0, row=0, sticky='nsew')
label_surface_typologie.grid(column=1, row=0, sticky='nsew')
label_pourcentages.grid(column=2, row=0, sticky='nsew')
label_surface_a_peupler.grid(column=3, row=0, sticky='nsew')
label_resultats_unitaires.grid(column=4, row=0, sticky='nsew')
label_resultats_unitaires_pourcentages.grid(column=5, row=0, sticky='nsew')
label_modulo.grid(column=6, row=0, sticky='nsew')

Resultat_T1_unitaire = DoubleVar()
Resultat_T1_unitaire.set(0)
Resultat_T2_unitaire = DoubleVar()
Resultat_T2_unitaire.set(0)
Resultat_T3_unitaire = DoubleVar()
Resultat_T3_unitaire.set(0)
Resultat_T4_unitaire = DoubleVar()
Resultat_T4_unitaire.set(0)
Resultat_T5_unitaire = DoubleVar()
Resultat_T5_unitaire.set(0)

ensemble_des_resultats_unitaires_pourcentages = (Resultat_T1_unitaire, Resultat_T2_unitaire, Resultat_T3_unitaire,
                                                 Resultat_T4_unitaire, Resultat_T5_unitaire)

entry_resultat_unitaire_p1 = ttk.Entry(root, textvariable=Resultat_T1_unitaire, style='pad.TEntry', justify=CENTER)
entry_resultat_unitaire_p2 = ttk.Entry(root, textvariable=Resultat_T2_unitaire, style='pad.TEntry', justify=CENTER)
entry_resultat_unitaire_p3 = ttk.Entry(root, textvariable=Resultat_T3_unitaire, style='pad.TEntry', justify=CENTER)
entry_resultat_unitaire_p4 = ttk.Entry(root, textvariable=Resultat_T4_unitaire, style='pad.TEntry', justify=CENTER)
entry_resultat_unitaire_p5 = ttk.Entry(root, textvariable=Resultat_T5_unitaire, style='pad.TEntry', justify=CENTER)

ensemble_des_entrees_de_pourcentages_unitaires = (entry_resultat_unitaire_p1, entry_resultat_unitaire_p2,
                                                  entry_resultat_unitaire_p3, entry_resultat_unitaire_p4,
                                                  entry_resultat_unitaire_p5)
pu_rows = 1

for m in ensemble_des_entrees_de_pourcentages_unitaires:
    m.grid(column=5, row=pu_rows, pady=pady_general, padx=padx_general)
    m.config(state='disabled')
    pu_rows += 1

label_typo_1 = Label(root, text="T-1", padx=padx_general, pady=pady_general)
label_typo_2 = Label(root, text="T-2", padx=padx_general, pady=pady_general)
label_typo_3 = Label(root, text="T-3", padx=padx_general, pady=pady_general)
label_typo_4 = Label(root, text="T-4", padx=padx_general, pady=pady_general)
label_typo_5 = Label(root, text="T-5", padx=padx_general, pady=pady_general)

ensemble_des_typos_de_base = (label_typo_1, label_typo_2, label_typo_3, label_typo_4, label_typo_5)

test_row = 1
for i in ensemble_des_typos_de_base:
    i.grid(column=0, row=test_row)
    test_row += 1

surface_T1 = DoubleVar()
surface_T1.set(12)
surface_T2 = DoubleVar()
surface_T2.set(20)
surface_T3 = DoubleVar()
surface_T3.set(30)
surface_T4 = DoubleVar()
surface_T4.set(40)
surface_T5 = DoubleVar()
surface_T5.set(50)

ensemble_stringvar_surfaces = (surface_T1, surface_T2, surface_T3, surface_T4, surface_T5)

entry_surface_T1 = ttk.Entry(root, textvariable=surface_T1, justify=CENTER, style='pad.TEntry')
entry_surface_T2 = ttk.Entry(root, textvariable=surface_T2, justify=CENTER, style='pad.TEntry')
entry_surface_T3 = ttk.Entry(root, textvariable=surface_T3, justify=CENTER, style='pad.TEntry')
entry_surface_T4 = ttk.Entry(root, textvariable=surface_T4, justify=CENTER, style='pad.TEntry')
entry_surface_T5 = ttk.Entry(root, textvariable=surface_T5, justify=CENTER, style='pad.TEntry')

ensemble_des_entrees_de_surfaces = (entry_surface_T1, entry_surface_T2,
                                    entry_surface_T3, entry_surface_T4, entry_surface_T5)
a = 1
for i in ensemble_des_entrees_de_surfaces:
    i.grid(column=1, row=a, padx=padx_general, pady=pady_general)
    a += 1

valeur_Pourcentage_1 = DoubleVar()
valeur_Pourcentage_1.set(10)
valeur_Pourcentage_2 = DoubleVar()
valeur_Pourcentage_2.set(20)
valeur_Pourcentage_3 = DoubleVar()
valeur_Pourcentage_3.set(30)
valeur_Pourcentage_4 = DoubleVar()
valeur_Pourcentage_4.set(20)
valeur_Pourcentage_5 = DoubleVar()
valeur_Pourcentage_5.set(20)

ensemble_des_pourcentages_input = (valeur_Pourcentage_1, valeur_Pourcentage_2, valeur_Pourcentage_3,
                                   valeur_Pourcentage_4, valeur_Pourcentage_5)

liste_des_valeurs_de_pourcentages = []
count_liste_valeurs_pourcentages = 0
for v in ensemble_des_pourcentages_input:
    liste_des_valeurs_de_pourcentages.append(v.get())

valeur_Pourcentage_total = DoubleVar()
valeur_Pourcentage_total.set(math.fsum(liste_des_valeurs_de_pourcentages))

label_total_pourcentages = ttk.Label(root, textvariable=valeur_Pourcentage_total, borderwidth=2)
label_total_pourcentages.grid(column=2, row=6)

for i in ensemble_des_pourcentages_input:
    i.trace_add("write", callback)

for i in ensemble_stringvar_surfaces:
    i.trace_add("write", callback)

entry_pourcentage_P1 = ttk.Entry(root, textvariable=valeur_Pourcentage_1, justify=CENTER, style='pad.TEntry')
entry_pourcentage_P2 = ttk.Entry(root, textvariable=valeur_Pourcentage_2, justify=CENTER, style='pad.TEntry')
entry_pourcentage_P3 = ttk.Entry(root, textvariable=valeur_Pourcentage_3, justify=CENTER, style='pad.TEntry')
entry_pourcentage_P4 = ttk.Entry(root, textvariable=valeur_Pourcentage_4, justify=CENTER, style='pad.TEntry')
entry_pourcentage_P5 = ttk.Entry(root, textvariable=valeur_Pourcentage_5, justify=CENTER, style='pad.TEntry')

ensemble_des_entrees_de_pourcentages = (entry_pourcentage_P1, entry_pourcentage_P2,
                                        entry_pourcentage_P3, entry_pourcentage_P4, entry_pourcentage_P5)
b = 1
for i in ensemble_des_entrees_de_pourcentages:
    i.grid(column=2, row=b, padx=padx_general, pady=pady_general)
    b += 1


def update_alpha_from_slider_value(slider):
    print(slider)
    alpha_slider_value = slider_alpha.get()
    print(slider_alpha.get())
    root.attributes('-alpha', alpha_slider_value / 100)


slider_alpha = Scale(root, from_=25, to=100, orient=HORIZONTAL,
                     command=update_alpha_from_slider_value,
                     label="Opacité de l'interface (%)", borderwidth=0)
slider_alpha.set(100)
slider_alpha.grid(padx=10, pady=10, columnspan=7, sticky='news')

valeur_surface_a_peupler = DoubleVar()
valeur_surface_a_peupler.set(float(100))
valeur_surface_a_peupler.trace_add("write", callback)

entry_surface_a_peupler = ttk.Entry(root, textvariable=valeur_surface_a_peupler, justify=CENTER)
entry_surface_a_peupler.grid(row=1, column=3, rowspan=6, sticky='nsew', padx=padx_general, pady=pady_general)

total_des_unites_maximum_1 = StringVar()
total_des_unites_maximum_1.set('--')

total_des_unites_maximum_2 = StringVar()
total_des_unites_maximum_2.set('--')

total_des_unites_maximum_3 = StringVar()
total_des_unites_maximum_3.set('--')

total_des_unites_maximum_4 = StringVar()
total_des_unites_maximum_4.set('--')

total_des_unites_maximum_5 = StringVar()
total_des_unites_maximum_5.set('--')

total_des_unites_max = (
    total_des_unites_maximum_1, total_des_unites_maximum_2, total_des_unites_maximum_3, total_des_unites_maximum_4,
    total_des_unites_maximum_5)

label_max_1 = Label(root, textvariable=total_des_unites_maximum_1, padx=padx_general, pady=pady_general)
label_max_2 = Label(root, textvariable=total_des_unites_maximum_2, padx=padx_general, pady=pady_general)
label_max_3 = Label(root, textvariable=total_des_unites_maximum_3, padx=padx_general, pady=pady_general)
label_max_4 = Label(root, textvariable=total_des_unites_maximum_4, padx=padx_general, pady=pady_general)
label_max_5 = Label(root, textvariable=total_des_unites_maximum_5, padx=padx_general, pady=pady_general)

ensemble_des_maximums = (label_max_1, label_max_2, label_max_3, label_max_4, label_max_5)

c = 1
for i in ensemble_des_maximums:
    i.grid(column=4, row=c)
    c += 1

frameChartsLT = LabelFrame(root, text='Graphique récapitulatif', width=50, height=50)
frameChartsLT.grid(row=0, column=7, rowspan=8)

liste_des_valeurs_input_percent = []
ni_count = 0
for ni in ensemble_des_pourcentages_input:
    liste_des_valeurs_input_percent.append(ni.get())
    ni_count += 1

stockListExp = ['T-1', 'T-2', 'T-3', 'T-4', 'T-5']
stockSplitExp = liste_des_valeurs_input_percent


def create_matplotlib_donut():
    fig = Figure()  # create a figure object

    ax = fig.add_subplot(111, label='Axes')  # add an Axes to the figure

    tourte = ax.pie(stockSplitExp, radius=1.5, labels=stockListExp, autopct='%1.1f%%', shadow=False,
                    colors=["#bce3e0", "#6bb4da", "#547cda", "#324e98", "#badad7"], explode=[0, 0, 0, 0, 0],
                    frame=False)

    circle = plt.Circle((0, 0), 0.6, color='white', fc='white', linewidth=1.25)
    ax.add_artist(circle)

    chart1 = FigureCanvasTkAgg(fig, frameChartsLT)

    chart1.draw()
    return chart1


inital_donut = create_matplotlib_donut().get_tk_widget()
inital_donut.pack()
toolbar = NavigationToolbar2Tk(create_matplotlib_donut(), frameChartsLT)
toolbar.update()
root.mainloop()
