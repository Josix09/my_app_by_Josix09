# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

Ventana_principal = Tk()

logo2=PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/my_app_by_Josix09/img/6126_177_10 (3) (2).png")

def abrir_toplevel_nacimiento():
    global toplevel_nacimiento
    toplevel_nacimiento = Toplevel()
    toplevel_nacimiento.title("Datos Nacimiento")
    toplevel_nacimiento.resizable(False, False)
    toplevel_nacimiento.geometry("500x200")
    toplevel_nacimiento.config(bg="light gray")

    subtitulon= Label(toplevel_nacimiento, text= "Fecha de Nacimiento: 8 de Octubre del 2009")
    subtitulon.config(bg="light gray",fg="Black", font=("Arial",12))
    subtitulon.place(x=5,y=150)

    subtitulon2= Label(toplevel_nacimiento, text= "Lugar de Nacimiento: Bucaramanga,Santander,Colombia")
    subtitulon2.config(bg="light gray",fg="Black", font=("Arial",12))
    subtitulon2.place(x=5,y=170)

    label_logo = Label(toplevel_nacimiento, image=logo2)
    label_logo.place(x=10,y=20)



def abrir_toplevel_medico():
    global toplevel_medico
    toplevel_medico = Toplevel()
    toplevel_medico.title("Datos Medicos")
    toplevel_medico.resizable(False, False)
    toplevel_medico.geometry("500x200")
    toplevel_medico.config(bg="light gray")

    subtitulom= Label(toplevel_medico, text= "Tipo de sangre: A+")
    subtitulom.config(bg="light gray",fg="Black", font=("Arial",12))
    subtitulom.place(x=5,y=30)



 

#####################################################################


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

#contenido ventana principal

logo=PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/my_app_by_Josix09/img/6126_177_10 (3).png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=40,y=60)

subtitulo1= Label(frame_1, text= "Jorge Luis Silva Morales")
subtitulo1.config(bg="light gray",fg="Black", font=("Arial",16))
subtitulo1.place(x=300,y=83)

subtitulo2= Label(frame_1, text= "Estudiante/Semi-Atleta")
subtitulo2.config(bg="light gray",fg="Black", font=("Arial",16))
subtitulo2.place(x=300,y=115)

subtitulo3= Label(frame_1, text= "Info adicional:")
subtitulo3.config(bg="light gray",fg="Black", font=("Arial",16))
subtitulo3.place(x=300,y=145)

subtitulo4= Label(frame_1, text= "Datos:")
subtitulo4.config(bg="light gray",fg="Black", font=("Arial",16))
subtitulo4.place(x=40,y=270)
#################################################################

# boton para abrir Toplevel nacimmiento
bt_nacimiento = Button(frame_1, text="Datos nacimiento", command=abrir_toplevel_nacimiento)
bt_nacimiento.place(x=40, y=345)

bt_medico = Button(frame_1, text="Datos Médicos", command=abrir_toplevel_medico)
bt_medico.place(x=40, y=310)


Ventana_principal.mainloop()