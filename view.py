import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# TODO: GRaficar los ultimos n eventos
# TODO: graficar en cierta fecha

class Datos(tk.LabelFrame):
    
    def __init__(self, master):
        super().__init__(master, text='Obtención de datos')
        self.master = master
        self.grid(row=0, column=0, padx=5)
        self.layout()
        
    def layout(self):
        # Agregaar Label
        self.agregar_label('Buscar datos', 0, 0)
        # Botón para buscar archivo
        self.buscar_button = self.agregar_button('Buscar...', 1, 0)
        # ? Decidir si dejar Labels o usar Treeview
        
        
    def agregar_label(self, text, row, column, padx=5, pady=5, **kwargs):
        label = ttk.Label(self, text=text)
        label.grid(kwargs, row=row, column=column, padx=padx, pady=pady)
        
    def agregar_button(self, text, row, column, padx=5, pady=5, **kwargs):
        button = ttk.Button(self, text=text)
        button.grid(kwargs, row=row, column=column, padx=padx, pady=pady)
        return button

class Configurar(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text='Configurar análisis')
        self.master = master
        self.grid(row=0, column=1, padx=5)
        self.layout()
        
    def layout(self):
        # Etiqueta de seleccionar Máquina
        self.agregar_label('Seleccionar Máquina', 1, 0, sticky='w')
        # Botones de seleccion de máquinas
        self.maq_var = tk.StringVar(self.master, value='todas')
        self.maquina1 = self.agregar_radiobutton('Máquina 1', 'maq1', self.maq_var, 2, 0,
                                                 padx=20, sticky='w')
        self.maquina2 = self.agregar_radiobutton('Máquina 2', 'maq2', self.maq_var, 2, 1,
                                                 padx=10, sticky='w')
        self.maquinab = self.agregar_radiobutton('Máquina Backup', 'maqb', self.maq_var, 3, 0,
                                                 padx=20, sticky='w')
        self.todas_maq = self.agregar_radiobutton('Todas', 'todas', self.maq_var, 3, 1,
                                                  padx=10, sticky='w')
        
        # Etiqueta de seleccionar columna
        self.agregar_label('Seleccionar variable', 4, 0, sticky='w')
        self.combobox = self.agregar_combobox(4, 1)     # Lista de columnas
        # TODO: Hacer dinámico el checbox para clima y frenos
        # Etiqueta de seleccionar el gas
        #self.agregar_label('Seleccionar gas', 4, 0, sticky='w')
        
        
        # TODO: Hacer para la gráfica controles que tambien dejen modificar la fecha
        # Etiqueta para seleccionar la fecha
        
        # Botón finales
        # ? Decidir si dejar Labels o usar Treeview
        
        
    def agregar_label(self, text, row, column, padx=5, pady=5,**kwargs):
        label = ttk.Label(self, text=text)
        label.grid(kwargs, row=row, column=column, padx=padx, pady=pady)
        return label
        
    def agregar_button(self, text, row, column, padx=5, pady=5,**kwargs):
        button = ttk.Button(self, text=text)
        button.grid(kwargs, row=row, column=column, padx=padx, pady=pady)
        return button
    
    def agregar_radiobutton(self, text, value, variable, row, column, padx=0, pady=0, **kwargs):
        radiobutton = ttk.Radiobutton(self,text=text, value=value, variable=variable)
        radiobutton.grid(kwargs, row=row, column=column, padx=padx, pady=pady)
        return radiobutton
    
    def agregar_combobox(self, row, column, padx=5, pady=5, **kwargs):
        combobox = ttk.Combobox(self)
        combobox.grid(kwargs, row=row, column=column, padx=padx, pady=pady)
        return combobox


master = tk.Tk()
master.title('Demo 1.1')
master['padx'] = 5
master['pady'] = 5
# Creando los LabelFrames
datos = Datos(master)
config = Configurar(master)
master.mainloop()