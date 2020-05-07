import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}


sinNotas = tk.Tk()
sinNotas.title('Notas')
sinNotas.minsize(screenSize['width'], screenSize['height'])
sinNotas.resizable(False, False)
im = ImageTk.PhotoImage(Image.open('not_found.png').resize((200, 200)))
im2 = ImageTk.PhotoImage( Image.open('ic_arrow_back.png').resize((24,24)) )


seccion1 = tk.Frame(master=sinNotas, bg="gray")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)



label1 = tk.Label(master=seccion1,
                  bg="gray",
                  fg="black",
                  text="Notas",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.2, rely=0.2)

back = tk.Button(master=seccion1, bg = 'gray', image = im2, height = 30, width = 30)
back.place(anchor = tk.NW, relx = 0.05, rely = 0.2)

editar = tk.Button(master=seccion1, bg = 'gray', fg = 'black', text = 'Editar', font=tkFont.Font(family='Roboto', size=8))
editar.place(anchor = tk.NW, relx = 0.85, rely = 0.25)

seccion2 = tk.Frame(master=sinNotas, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

canvas = tk.Canvas(master=seccion2,
                   bd=2,
                   bg='white',
                   height=300,
                   width=300,
                   highlightbackground='white'
                   )
canvas.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
canvas.create_image(60, 40, image=im, anchor=tk.NW)
label3 = tk.Label(master=canvas,
                  text="Sin Notas",
                  bg='white',
                  fg='gray',
                  font=tkFont.Font(family='Roboto', size=15)
                  )
label3.place(anchor=tk.CENTER, relx=0.5, rely=0.8)

boton = tk.Button(master=seccion2,
                  bg='gray',
                  fg='black',
                  text='+',
                  font=tkFont.Font(family='Roboto', size=15),
                  width=5, command = sinNotas.destroy)
boton.place(anchor=tk.SE, relx=0.99, rely=0.99)

sinNotas.mainloop()
