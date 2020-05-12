from tkinter import *
import json
from tkinter.font import Font
from PIL import ImageTk, Image

root = Tk()

FOLDERS = {
    'tarea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'proyectos':
        ['nota_0 de proyectos'],
    'ideas':
        [],
    'planes':
    [],
    'memes':
    [],
    'mandado':
    [],
    'vacadacione2s': [],
    'tar2ea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'dproyect2os':
        ['nota_0 de proyectos'],
    'ide2as':
        [],
    'pla1dsadsandases':
    [],
    'mem2es':
    [],
    'mandaas3do':
    [],
    'vacac1iodanes': [],
    'tar2ea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'proyecast2os':
        ['nota_0 de proyectos'],
    'ide2as':
        [],
    'pla1ncfzsaes':
    [],
    'mexcm2es':
    [],
    'mandazx3do':
    [],
    'vacacx1iones': [],
    'tar2xea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'proyevcxctx2os':
        ['nota_0 de proyectos'],
    'idxe2as':
        [],
    'pla1cznxs':
    [],
    'mem2 zcx eas':
    [],
    'mandaczx 3ado':
    [],
    'vacac1ia cxzones': [],
    'tar2ea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'proyectzxc2os':
        ['nota_0 de proyectos'],
    'idasde2as':
        [],
    'pla1nfdeas':
    [],
    'mem2easas':
    [],
    'mandasda3ado':
    [], 'aes': [],
    'tasar2ea':
        ['nota_0 de tarea', 'nota_1 de tarea'],
    'prosadyeact2os':
        ['nota_0 de proyectos'],
    'idasea2as':
        [],
    'pla1anefs':
    [],
    'mem2aseas':
    [],
    'mandaas3ado':
    [],
    'vacac1ia ones': []
}
folders_values = []
folders_keys = []


root.geometry('360x640')
root.resizable(FALSE, FALSE)
root.title('NOTAS')

folder_icon = ImageTk.PhotoImage(Image.open('icon_folder.png'))
note_icon = ImageTk.PhotoImage(Image.open('note.png'))


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
            self.cuadro, bg='floral white', padx=5, pady=0)
        self.content_frame.place(relwidth=1.0, relheight=.6, rely=.25)
        self.pagina = 0


class listados(build_frames):
    global folders_keys, folders_values, folder_icon

    def __init__(self, master, title):
        super().__init__(master, title)
        self.pagina = 0
        make_lists(FOLDERS)

        self.show_folders()
        self.prev = Button(self.cuadro, text="PREV PAGE", command=lambda: self.turn_page(-1)).place(
            anchor=NW, rely=.8)
        self.next = Button(self.cuadro, text="NEXT PAGE", command=lambda: self.turn_page(1)).place(
            anchor=NW, rely=0.8, relx=.2)

    def turn_page(self, direccion):
        if (self.pagina > len(folders_keys)//4) or (self.pagina == -1):
            self.pagina = 0
        else:
            self.pagina += direccion

        self.content_frame.update()
        self.show_folders()
        print(self.pagina)

    def show_folders(self):
        global folders_keys, folders_values
        placement = 0
        indice = 0
        while indice < len(folders_keys):

            item = folders_keys[indice]
            page = 4*self.pagina
            indice = indice + page

            self.folder_frame = Frame(
                self.content_frame, bg='floral white', pady=0)
            self.folder_frame.place(rely=placement, relwidth=1/2)
            self.folder_image = Button(
                self.folder_frame, image=folder_icon, command=lambda: print('boton activado'))
            self.folder_image.pack(side=LEFT)
            self.folder_name = Button(self.folder_frame, text=str(
                item), command=lambda: self.transition(int(page)))
            self.folder_name.pack(side=LEFT)

            placement += (1/4)
            indice += 1

    def transition(self, indice):
        global folders_keys, folders_values, folder_icon, note_icon
        placement = 0
        Notas = listados(root, 'NOTAS')
        make_lists(FOLDERS)
        raise_frame(Notas)
        Lista1.cuadro.lower()
        unmap = self.content_frame.place_slaves()

        for each in unmap:
            each.forget()

        self.lista_notas = []
        self.lista_notas = folders_values[indice]  # esta saca la lista de las notas

        for nota in self.lista_notas:
            self.nota_f = Frame(self.content_frame, bg='floralwhite', pady=0).pack()
            self.nota_icon = Button(self.nota_f, image=note_icon, command=lambda: print(
                'boton activado')).pack(side=LEFT)
            self.breve = Button(self.nota_f,
                                text=str(nota[:len(nota)//2])).pack(side=LEFT)
            placement += (1/4)


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
"""Notas = listados(root, 'Notas')
Editor = editor(root, 'Nota')"""

raise_frame(Lista1)


root.mainloop()
