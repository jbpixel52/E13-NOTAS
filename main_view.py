from tkinter import *
import json
from tkinter.font import Font
from PIL import ImageTk, Image

FOLDERS = {
    'tarea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'proyectos':
        ['nota_0 de proyectos'],
    'ideas':
        []
}
folders_values = []
folders_keys = []


root = Tk()
root.geometry('360x640')
root.resizable(FALSE, FALSE)
root.title('NOTAS')

folder_icon = ImageTk.PhotoImage(Image.open('icon_folder.png'))


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
    global folders_keys, folders_values, folder_icon

    def __init__(self, master, title):
        super().__init__(master, title)
        make_lists(FOLDERS)
        self.show_lists()

    def show_lists(self):
        global folders_keys, folders_values
        for item in folders_keys:
            self.folder_frame = Frame(self.content_frame)
            self.folder_frame.place(relwidth=1, relheight=(1/4), anchor=NW)
            folder_image = Button(
                self.folder_frame, image=folder_icon, command=lambda: print('boton activado'))
            folder_image.pack(side=LEFT)
            folder_name = Button(self.folder_frame, text=str(item))
            folder_name.pack(side=LEFT)
            print(str(item))
            print(str(folders_keys))


class editor(build_frames):
    def __init__(self, master, title):
        super().__init__(master, title)


def raise_frame(frame):
    """ FUNCION DE AUXILIO PARA LEVANTAR FRAMES. """
    frame.cuadro.tkraise()


def make_lists(folder):
    global folders_keys, folders_values
    folders_keys = list(folder.keys())
    folders_values = list(folder.values())


Lista1 = listados(root, 'FOLDERS')
Notas = listados(root, 'Notas')
Editor = editor(root, 'Nota')

raise_frame(Lista1)


root.mainloop()
