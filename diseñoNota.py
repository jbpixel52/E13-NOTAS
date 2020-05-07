import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}



Nota = tk.Tk()
Nota.title('Carpetas')
Nota.minsize(screenSize['width'], screenSize['height'])
Nota.resizable(False, False)
im = ImageTk.PhotoImage( Image.open('ic_arrow_back.png').resize((24,24)) )


seccion1 = tk.Frame(master=Nota, bg="gray")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)



label1 = tk.Label(master=seccion1,
                  bg="gray",
                  fg="black",
                  text="Proyecto",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.2, rely=0.2)

back = tk.Button(master=seccion1, bg = 'gray', image = im, height = 30, width = 30)
back.place(anchor = tk.NW, relx = 0.05, rely = 0.2)

crear = tk.Button(master=seccion1, bg = 'gray', fg = 'black', text = 'Crear', font=tkFont.Font(family='Roboto', size=8))
crear.place(anchor = tk.NW, relx = 0.85, rely = 0.25)

seccion2 = tk.Frame(master=Nota, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

texto = tk.Message(master=seccion2, bg = 'white', fg = 'black', text = 'Esta nota es un ejemplo de una aplicacion hecha en python 3 en el editor Visual Studio Code con el fin de seguir practicando el diseño de interfaces graficas con Tkinter', font=tkFont.Font(family='Roboto', size=14))
texto.place(anchor = tk.NW, relx = 0.05, rely = 0.05)



Nota.mainloop()

