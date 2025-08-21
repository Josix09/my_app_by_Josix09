# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

Ventana_principal = Tk()



#Titulo de la ventana

Ventana_principal.title("Jorge Luis Silva Morales")

#tamaño de la ventana
Ventana_principal.geometry("700x400")

#Deshabilitar el botón de maximizar de la ventana
Ventana_principal.resizable(0,0)

#color de fondo de la ventana

Ventana_principal.config(bg="gray")

#frames

#frame 1 
frame_1 = Frame(Ventana_principal)
frame_1.config(bg="light gray",width=680, height=380)
frame_1.place(x=10,y=10)

#contenido (texto ) ventana principal
subtitulo1= Label(frame_1, text= "Jorge Luis Silva Morales")
subtitulo1.config(bg="light gray",fg="Black", font=("Arial",16))
subtitulo1.place(x=320,y=83)

Ventana_principal.mainloop()