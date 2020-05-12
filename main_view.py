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
folder_index = 1
nota_index = 0

root.geometry('360x640')
root.resizable(FALSE, FALSE)
root.title('NOTAS')

folder_icon = ImageTk.PhotoImage(Image.open('icon_folder.png'))
note_icon = ImageTk.PhotoImage(Image.open('note.png'))
back_icon = ImageTk.PhotoImage(Image.open('back_arrow.png'))


class build_frames:
    def __init__(self, master, title):
        self.cuadro = Frame(master, bg='light goldenrod')
        self.cuadro.place(height=640, width=360, anchor=NW)

        self.title_bar = Frame(self.cuadro, bg='gold', padx=5, pady=5)
        self.title_bar.place(relwidth=1.0, relheight=(2/9))

        self.title = Label(self.title_bar, bg='gold',
                           text=title, font=Font(family='Comic Sans MS'))
        self.title.place(relwidth=.5, relheight=1)
        self.content_frame = Frame(
            self.cuadro, bg='pale goldenrod', padx=5, pady=0)
        self.content_frame.place(relwidth=1.0, relheight=.6, rely=.25)
        self.pagina = 0


class lista_folders(build_frames):
    global folders_keys, folders_values, folder_icon, folder_index, nota_index

    def __init__(self, master, title):
        super().__init__(master, title)
        make_lists(FOLDERS)

        self.pagina = 0
        self.show_folders()
        self.prev = Button(self.cuadro, text="PREV PAGE", command=lambda: self.turn_page(-1)).place(
            anchor=NW, rely=.8)
        self.next = Button(self.cuadro, text="NEXT PAGE", command=lambda: self.turn_page(1)).place(
            anchor=NW, rely=0.8, relx=.2)

    def turn_page(self, direccion):
        self.pagina += direccion
        if (self.pagina > len(folders_keys)//4) or (self.pagina < 0):
            self.pagina = 0
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
                item), command=lambda: print('boton activado'))
            self.folder_name.pack(side=LEFT)

            placement += (1/4)
            indice += 1


class lista_notas(build_frames):
    global folders_keys, folders_values, folder_icon, folder_index, folders_keys

    def __init__(self, master, title):
        super().__init__(master, title)
        make_lists(FOLDERS)
        self.key = folders_keys[folder_index]
        self.temp_list = FOLDERS[str(self.key)]
        self.pagina = 0
        self.show_notes()
        self.back = Button(self.title_bar, bg='gold', fg='black', image=back_icon,
                           command=lambda: self.cuadro.lower()).pack(side=LEFT)
        self.prev = Button(self.cuadro, text="PREV PAGE", command=lambda: self.turn_page(-1)).place(
            anchor=NW, rely=.8)
        self.next = Button(self.cuadro, text="NEXT PAGE", command=lambda: self.turn_page(1)).place(
            anchor=NW, rely=0.8, relx=.2)
        self.get_index()
    def transition(self):
        self.cuadro.lower()
        raise_frame(Lista1)

    def turn_page(self, direccion):
        self.pagina += direccion
        if (self.pagina > len(folders_keys)//4) or (self.pagina < 0):
            self.pagina = 0
        self.content_frame.update()
        self.show_notes()
        print(self.pagina)

    def show_notes(self):
        placement = 0
        indice = 0
        while indice < len(self.temp_list):

            item = self.temp_list[indice]
            page = 4*self.pagina
            indice = indice + page

            self.folder_frame = Frame(
                self.content_frame, bg='floral white', pady=0)
            self.folder_frame.place(rely=placement, relwidth=1/2)
            self.folder_image = Button(
                self.folder_frame, image=folder_icon, command=lambda: print('boton activado'))
            self.folder_image.pack(side=LEFT)
            self.folder_name = Button(self.folder_frame, text=str(
                item), command=lambda: print('boton activado'))
            self.folder_name.pack(side=LEFT)

            placement += (1/4)
            indice += 1
        self.notas_frame = Frame(self.content_frame, bg='floral white', pady=0)
        self.notas_frame.place(rely=placement, relwidth=1/2)
        self.label_note = Button(self.notas_frame, bg='floral white', text=str(
            self.key), command=lambda: print('boton activado'))
        self.label_note.pack(side=LEFT)
        placement += 1/4
        indice + 1

    def get_index(self):
        '''NO TERMINE ESTA FUNCION'''
        SLAVES=self.content_frame.slaves()
        print(SLAVES)

class editor(build_frames):
    global back_icon, folder_index, folders_keys, folders_values, FOLDERS

    def __init__(self, master, title):
        super().__init__(master, title)
        textoNotas2 = ""
        self.back = Button(self.title_bar, bg='gold', fg='black', image=back_icon,
                           command=lambda: self.back_save()).pack(side=LEFT)
        self.crear = Button(self.title_bar, bg='gold', text='Crear',
                            padx=5, command=self.add_nota).pack(side=RIGHT)
        self.Nota = Entry(self.content_frame, bg='light goldenrod')
        self.Nota.place(
            relx=0, rely=.05, relwidth=.9, relheight=.9)
        try:
            self.Nota.insert(END, 'Hola')
        except:
            Exception('Nota es NoneType')

    def add_nota(self):
        '''ESTA FUNCION SOLO AGREGA UNA NUEVA NO LA ACTUALIZA'''
        key = folders_keys[folder_index]
        temp_list = list(FOLDERS[str(key)])
        temp_list.append(self.Nota.get())
        FOLDERS[str(key)] = temp_list
        print('agregada')

    def back_save(self):
        '''GUARDA LA EDICION DE LA NOTA PRESENTA.'''
        key = folders_keys[folder_index]
        temp_list = list(FOLDERS[str(key)])
        temp_list[nota_index] = self.Nota.get()
        FOLDERS[str(key)] = temp_list
        Notas.cuadro.tkraise()

def raise_frame(frame):
    """ FUNCION DE AUXILIO PARA LEVANTAR FRAMES. """
    frame.cuadro.tkraise()



def make_lists(folder):
    global folders_keys, folders_values
    folders_keys = list(folder.keys())
    folders_values = list(folder.values())


Notas = lista_notas(root, 'Notas')
Lista1 = lista_folders(root, 'FOLDERS')
Editor = editor(root, 'Nota')


root.mainloop()
