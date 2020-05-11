from tkinter import *
import json
from tkinter.font import Font
"""EN EL JSON DE LAS NOTAS LA JERARQUIA SERA FOLDER/OBJETO DE LA NOTA"""

folders = {
    'tarea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'proyectos':
        ['nota_0 de proyectos'],
    'ideas':
        []
}


root = Tk()
root.geometry('360x640')
root.resizable(FALSE, FALSE)
root.title('NOTAS')


class build_frames:
    def __init__(self, master, title):
        self.cuadro = Frame(master, bg='light goldenrod')
        self.cuadro.place(height=640, width=360, anchor=NW)

        self.title_bar = Frame(self.cuadro, bg='snow3', padx=5, pady=5)
        self.title_bar.place(relwidth=1.0, relheight=(2/9))

        self.title = Label(self.title_bar, bg='snow3',
                           text=title, font=Font(family='Comic Sans MS'))
        self.title.place(relwidth=.5, relheight=1)
        self.content_frame = Frame(
            self.cuadro, bg='floral white', padx=5, pady=5)
        self.content_frame.place(relwidth=1.0, relheight=(3/4)-.15, rely=.25)


class listados(build_frames):
    def __init__(self, master, title):
        super().__init__(master, title)


class editor(build_frames):
    def __init__(self, master, title):
        super().__init__(master, title)


def make_lists(folder):
    l_keys = list(folder.keys())
    l_values = list(folder.values())


def raise_frame(frame):
    """ FUNCION DE AUXILIO PARA LEVANTAR FRAMES. """
    frame.tkraise()


Lista1 = listados(root, 'Folders')
Notas = listados(root, 'Notas')
Editor = editor(root, 'Nota')

Lista1.cuadro.tkraise()
root.mainloop()
