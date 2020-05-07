import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}



Notas = tk.Tk()
Notas.title('Carpetas')
Notas.minsize(screenSize['width'], screenSize['height'])
Notas.resizable(False, False)
im = ImageTk.PhotoImage( Image.open('ic_arrow_back.png').resize((24,24)) )


seccion1 = tk.Frame(master=Notas, bg="gray")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)



label1 = tk.Label(master=seccion1,
                  bg="gray",
                  fg="black",
                  text="Notas",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.2, rely=0.2)

back = tk.Button(master=seccion1, bg = 'gray', image = im, height = 30, width = 30)
back.place(anchor = tk.NW, relx = 0.05, rely = 0.2)

editar = tk.Button(master=seccion1, bg = 'gray', fg = 'black', text = 'Editar', font=tkFont.Font(family='Roboto', size=8))
editar.place(anchor = tk.NW, relx = 0.85, rely = 0.25)

seccion2 = tk.Frame(master=Notas, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)


##Primera nota
Nota1 = tk.Button(master=seccion2, bg = 'white', fg = 'black', text = 'Proyecto', font=tkFont.Font(family='Roboto', size=12), width = 25)
Nota1.place(anchor = tk.NW, relx = 0.05, rely = 0.1)

fecha1 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = '05/05/2020- 19:00', font=tkFont.Font(family='Roboto', size=8))
fecha1.place(anchor = tk.NW, relx = 0.05, rely = 0.17)

##Segunda nota
Nota2 = tk.Button(master=seccion2, bg = 'white', fg = 'black', text = 'Decripcion de auto', font=tkFont.Font(family='Roboto', size=12), width = 25)
Nota2.place(anchor = tk.NW, relx = 0.05, rely = 0.25)

fecha2 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = '05/05/2020- 19:00', font=tkFont.Font(family='Roboto', size=8))
fecha2.place(anchor = tk.NW, relx = 0.05, rely = 0.32)

##Tercera nota
Nota3 = tk.Button(master=seccion2, bg = 'white', fg = 'black', text = 'Libros para comprar', font=tkFont.Font(family='Roboto', size=12), width = 25)
Nota3.place(anchor = tk.NW, relx = 0.05, rely = 0.4)

fecha3 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = '05/05/2020- 19:00', font=tkFont.Font(family='Roboto', size=8))
fecha3.place(anchor = tk.NW, relx = 0.05, rely = 0.47)

boton = tk.Button(master=seccion2,
                  bg='black',
                  fg='white',
                  text='+',
                  font=tkFont.Font(family='Roboto', size=15),
                  width=5, command = Notas.destroy)
boton.place(anchor=tk.SE, relx=0.99, rely=0.99)

numero = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = '3 notas', font=tkFont.Font(family='Roboto', size=9))
numero.place(anchor=tk.NW, relx=0.45, rely=0.95)

Notas.mainloop()

