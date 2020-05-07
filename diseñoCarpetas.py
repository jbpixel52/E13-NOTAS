import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}


Carpetas = tk.Tk()
Carpetas.title('Carpetas')
Carpetas.minsize(screenSize['width'], screenSize['height'])
Carpetas.resizable(False, False)


seccion1 = tk.Frame(master=Carpetas, bg="gray")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)



label1 = tk.Label(master=seccion1,
                  bg="gray",
                  fg="black",
                  text="Carpetas",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.2, rely=0.2)

editar = tk.Button(master=seccion1, bg = 'gray', fg = 'black', text = 'Editar', font=tkFont.Font(family='Roboto', size=8))
editar.place(anchor = tk.NW, relx = 0.85, rely = 0.25)

seccion2 = tk.Frame(master=Carpetas, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

carpeta1 = tk.Button(master=seccion2, bg = 'white', fg = 'black', text = 'Compras', font=tkFont.Font(family='Roboto', size=14), width = 25)
carpeta1.place(anchor = tk.NW, relx = 0.05, rely = 0.1)

carpeta2 = tk.Button(master=seccion2, bg = 'white', fg = 'black', text = 'Tareas', font=tkFont.Font(family='Roboto', size=14), width = 25)
carpeta2.place(anchor = tk.NW, relx = 0.05, rely = 0.2)

carpeta2 = tk.Button(master=seccion2, bg = 'white', fg = 'black', text = 'Personal', font=tkFont.Font(family='Roboto', size=14), width = 25)
carpeta2.place(anchor = tk.NW, relx = 0.05, rely = 0.3)

boton = tk.Button(master=seccion2,
                  bg='black',
                  fg='white',
                  text='+',
                  font=tkFont.Font(family='Roboto', size=15),
                  width=5, command = Carpetas.destroy)
boton.place(anchor=tk.SE, relx=0.99, rely=0.99)

Carpetas.mainloop()

