# !/usr/bin/python3
from tkinter import *
from tkinter import ttk

# libraria pint modificată
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity


root = Tk()
root.title("Convertor")
categorie = StringVar()
unitatea_neconvertita = StringVar()
unitatea_convertita = StringVar()
prefixe = ('yocto', 'zepto', 'atto', 'femto', 'pico', 'nano', 'micro', 'mili', 'centi', 'deci', '', 'deca', 'hecto', 'kilo', 'giga', 'tera', 'exa', 'zetta', 'yotta')
prefix_unitate_intrare = StringVar()
prefix_unitate_iesire = StringVar()
unitate_intrare = StringVar()
unitate_iesire = StringVar()
unitati_grupate = {
    'lungime': ('metri', 'mile terestre', 'mile marine', 'țoli', 'lănțișori', 'picioare', 'yarzi'),
    'timp': ('secunde', 'minute', 'ore', 'zile', 'săptămâni', 'luni iuliane', 'ani iuliani', 'luni gregoriene', 'ani gregorieni'),
    'temperatura': ('grade Celsius', 'grade Kelvin', 'grade Fahrenheit', 'grade Rankine'),
    'masa': ('grame'),
    'sarcina electrica': ('columb', 'statcolumb'),
    'curent electric': ('amper', 'statamper'),
    'camp electric': ('volți/metru', 'statvolți/centimetru'),
    'camp magnetic': ('tesla', 'gauss'),
    'inducție electrică': ('columb/metru^2', 'statcolomb/centimetru^2'),
    'flux magnetic':('maxwell','weber')
}

dictionar = {
    'metri':'meter',
    'mile terestre':'mile', 
    'mile marine':'nautical_mile', 
    'țoli':'inch', 
    'lănțișori':'link', 
    'picioare':'foot', 
    'yarzi':'yard',
    'secunde':'second', 
    'minute':'minute', 
    'ore':'hour', 
    'zile':'day', 
    'săptămâni':'week', 
    'luni iuliane':'julian_month', 
    'ani iuliani':'julian_year', 
    'luni gregoriene':'gregorian_month', 
    'ani gregorieni':'gregorian_year',
    'grade Celsius':'celsius',
    'grade Kelvin':'kelvin', 
    'grade Fahrenheit':'fahrenheit', 
    'grade Rankine':'rankine',
    'grame':'gram',
    'moli':'mole',
    'columb':'coulomb', 
    'statcolumb':'statC',
    'amper':'ampere', 
    'statamper':'statA',
    'volți/metru':'volt/meter', 
    'statvolți/centimetru':'statvolt/meter',
    'tesla':'tesla',
    'gauss':'gauss',
    'columb/metru^2':'coulomb / meter**2', 
    'statcolumb/centimetru^2':'statC / centimeter**2',
    'maxwell':'maxwell',
    'weber':'weber'
}

combobox_categorie = ttk.Combobox(
    root, textvariable=categorie, state='readonly')
combobox_categorie.grid(row=0)

combobox_prefix_i = ttk.Combobox(
    root, textvariable=prefix_unitate_intrare, state='readonly')
combobox_prefix_i.grid(row=3)
combobox_i = ttk.Combobox(
    root, textvariable=unitate_intrare, state='readonly')
combobox_i.grid(row=4)

label_to=Label(root, text='în')
label_to.grid(row=5)

combobox_prefix_o = ttk.Combobox(
    root, textvariable=prefix_unitate_iesire, state='readonly')
combobox_prefix_o.grid(row=6)
combobox_o = ttk.Combobox(
    root, textvariable=unitate_iesire, state='readonly')
combobox_o.grid(row=7)

entry_i=ttk.Entry(root)
entry_i.grid(row=2, sticky=W+E+N+S)

label_o=ttk.Label(root, text = "")
label_o.grid(row=9, sticky=W+E+N+S)

def selecteaza_categoria():
    print(categorie.get())
    combobox_i.config(values=unitati_grupate[categorie.get()])
    combobox_o.config(values=unitati_grupate[categorie.get()])
    unitate_intrare.set('')
    unitate_iesire.set('')


b_selectare = Button(root, text="Selectează", command=selecteaza_categoria)
b_selectare.grid(row=1, sticky=W+E+N+S)

def converteste():
    label_o.config(text = Q_(float(entry_i.get()), prefix_unitate_intrare.get()+dictionar[unitate_intrare.get()]).to(prefix_unitate_iesire.get()+dictionar[unitate_iesire.get()]).magnitude)
    

b_convertire = Button(root, text="Convertește", command= lambda: converteste())
b_convertire.grid(row=8, sticky=W+E+N+S)

combobox_categorie.config(values=tuple(unitati_grupate.keys()))
combobox_prefix_i.config(values=prefixe)
combobox_prefix_o.config(values=prefixe)



root.mainloop()
