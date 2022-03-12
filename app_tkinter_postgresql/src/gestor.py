from cgitb import text
import tkinter as tk
from tkinter import PhotoImage, ttk
import psycopg2 as db
import sys
class Aplication:
    def __init__(self):
        # Setting of the main window
        self.window = tk.Tk()
        self.window.title('Gestor de Plantilla de Club Atletico River Plate')
        self.center_window(window=self.window, width=420, height=400)
        # Page Conteiner
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack()
        # Page Menu
        self.page_menu = ttk.Frame(self.notebook)
        self.notebook.add(self.page_menu, text='Menú')
        self.image_main = PhotoImage(file ='img/logo_carp_mini.png')
        self.image_label = tk.Label(self.page_menu, image=self.image_main)
        self.image_label.pack(pady=10)
        #self.image_label.grid(column=0, row=0)
        self.text_information = ttk.Label(self.page_menu, text='Información de la aplicacion de gestión de CARP')
        #self.text_information.grid(column=0, row=1)
        self.text_information.pack()
        # Page Create
        self.page_create = ttk.Frame(self.notebook)
        self.notebook.add(self.page_create, text='Create Person')
        self.elements_create(window=self.page_create)
        # Page Search
        self.page_search = ttk.Frame(self.notebook)
        self.notebook.add(self.page_search, text='Search Person')
        self.elements_search(window=self.page_search)
        # Page Update
        self.page_update = tk.Frame(self.notebook)
        self.notebook.add(self.page_update, text='Update Person')
        self.elements_update(window=self.page_update)
        # Page Delete
        self.page_delete = tk.Frame(self.notebook)
        self.notebook.add(self.page_delete, text='Delete Person')
        self.elements_delete(window=self.page_delete)
        # Page about app
        self.page_about = tk.Frame(self.notebook)
        self.notebook.add(self.page_about, text='About ...')
        self.version_label = tk.Label(self.page_about, text='Version 1.0')
        self.version_label.pack(pady=10)
        self.developer_label = tk.Label(self.page_about, text='Desarrollador: ERSP')
        self.developer_label.pack(pady=5)
        self.property_org_label = tk.Label(self.page_about, text='Propiedad de CARP')
        self.property_org_label.pack(pady=5)
        self.window.mainloop()
        # self.elements_delete(window=self.window)
        # self.elements_update(window=self.window)
        # self.elements_search(window=self.window)
        # self.elements_crud(window=self.window)
        # self.exit_button = tk.Button(self.window, text='Salir', command=self.exit)
        # self.exit_button.grid(column=0, row=5, padx=5, pady=5)
    
    # Functions
    def center_window(self, window, width, height):
        print("Width", width, "Height", height)
        window.geometry('{}x{}'.format(width, height))
        # Gets the requested values of the height and widht.
        x = window.winfo_screenwidth()
        y = window.winfo_screenheight()
        print('x:', x, 'y:', y)
        # Gets both half the screen width/height and window width/height
        position_right = int(window.winfo_screenwidth() / 2 - width / 2)
        position_down = int(window.winfo_screenheight() / 2 - height / 2)
        print('Right:', position_right, 'Down:', position_down)
        # Positions the window in the center of the page.
        window.geometry("+{}+{}".format(position_right, position_down))
    def create_person_f(self, name, surname, age, nationality, role, position, shirtnumber):
        conn = self.connection_db()
        cursor = conn.cursor()
        query = '''INSERT INTO first_team_squad(name, surname, age, nationality, role, position, shirtnumber) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (name, surname, age, nationality, role, position, shirtnumber))
        print('Saved Person')
        conn.commit()
        conn.close()
    def delete_person_f(self, name, surname):
        conn = self.connection_db()
        cursor = conn.cursor()
        query = '''DELETE FROM first_team_squad WHERE name=%s AND surname=%s'''
        cursor.execute(query, (name, surname))
        print('Delete Person')
        conn.commit()
        conn.close()
    def connection_db(self):
        try:
            conn = db.connect(user='postgres',
                          password='20postgresql21',
                          host='localhost',
                          port='5432',
                          database='first_team_squad_CARP')
        except Exception as e:
            print(e)
        finally:
            return conn
    def elements_create(self, window):
        # LabelFrame create --------------------------------------------------
        self.create_labelframe = tk.LabelFrame(window, text='Agregar Persona', foreground='blue')
        #self.create_labelframe.grid(column=0, row=0, padx=5, pady=10)
        self.create_labelframe.pack(pady=10)
        # name
        self.name_label = tk.Label(self.create_labelframe, text='Nombres:')
        self.name_label.grid(column=0, row=0, padx=5, pady=5)
        #self.name_label.pack(padx=5, pady=5)
        self.name_string = tk.StringVar()
        self.name_entry = tk.Entry(self.create_labelframe, textvariable=self.name_string)
        self.name_entry.grid(column=1, row=0, padx=5, pady=5)
        # surname
        self.surname_label = tk.Label(self.create_labelframe, text='Apellidos:')
        self.surname_label.grid(column=0, row=1, padx=5, pady=5)
        self.surname_string = tk.StringVar()
        self.surname_entry = tk.Entry(self.create_labelframe, textvariable=self.surname_string)
        self.surname_entry.grid(column=1, row=1, padx=5, pady=5)
        # age
        self.age_label = tk.Label(self.create_labelframe, text='Edad:')
        self.age_label.grid(column=0, row=2, padx=5, pady=5)
        self.age_string = tk.StringVar()
        self.age_entry = tk.Entry(self.create_labelframe, textvariable=self.age_string)
        self.age_entry.grid(column=1, row=2, padx=5, pady=5)
        # nationality
        self.nationality = tk.Label(self.create_labelframe, text='Nacionalidad:')
        self.nationality.grid(column=0, row=3, padx=5, pady=5)
        self.nationatilty_string = tk.StringVar()
        self.nationality_entry = tk.Entry(self.create_labelframe, textvariable=self.nationatilty_string)
        self.nationality_entry.grid(column=1, row=3, padx=5, pady=5)
        # role
        self.role_label = tk.Label(self.create_labelframe, text='Rol de la persona:')
        self.role_label.grid(column=0, row=4, padx=5, pady=5) # sticky='e'
        self.role_string = tk.StringVar()
        self.role_entry = tk.Entry(self.create_labelframe, textvariable=self.role_string)
        self.role_entry.grid(column=1, row=4, padx=5, pady=5)
        # position
        self.position_label = tk.Label(self.create_labelframe, text='Posicion del jugador:')
        self.position_label.grid(column=0, row=5, padx=6, pady=5)
        self.position_string = tk.StringVar()
        self.position_entry = tk.Entry(self.create_labelframe, textvariable=self.position_string)
        self.position_entry.grid(column=1, row=5, padx=5, pady=5)
        # shirtnumber
        self.shirtnumber_label = tk.Label(self.create_labelframe, text='Numero de camiseta:')
        self.shirtnumber_label.grid(column=0, row=6, padx=5, pady=5)
        self.shirtnumber_string = tk.StringVar()
        self.shirtnumber_entry = tk.Entry(self.create_labelframe, textvariable=self.shirtnumber_string)
        self.shirtnumber_entry.grid(column=1, row=6, padx=5, pady=5)
        # Label add_ok
        self.add_ok_label = tk.Label(self.create_labelframe, text='')
        self.add_ok_label.grid(column=0, row=4, padx=5, pady=5)
        # Create Button
        self.create_person_b = tk.Button(self.page_create, text='Create person',
                                         command=lambda:self.create_person_f(
                                             self.name_string.get(), 
                                             self.surname_string.get(), 
                                             self.age_string.get(),
                                             self.nationatilty_string.get(),
                                             self.role_string.get(),
                                             self.position_string.get(),
                                             self.shirtnumber_string.get()))
        #self.create_person_b.grid(column=0, row=4, padx=5, pady=5)
        self.create_person_b.pack(pady=5)
    def elements_search(self, window):
        # Frame search
        self.search_labelframe = tk.LabelFrame(window, text='Buscar segun su rol', foreground='grey')
        #self.search_labelframe.grid(column=0, row=0)
        self.search_labelframe.pack(pady=10)
        # role
        self.role_label_s = tk.Label(self.search_labelframe, text='Rol')
        self.role_label_s.grid(column=0, row=0, padx=5, pady=5)
        self.role_string_s = tk.StringVar()
        self.role_entry_s = tk.Entry(self.search_labelframe, textvariable=self.role_string_s)
        self.role_entry_s.grid(column=1, row=0, padx=5, pady=5)
        # Label result
        self.persons_label = tk.Label(self.search_labelframe)
        self.persons_label.grid(column=0, row=1)
        # Search Button
        self.search_person_b = tk.Button(self.page_search, text='Search person', command=lambda:self.search_person_f(self.role_string_s.get()))
        #self.search_person_b.grid(column=0, row=1, padx=5, pady=5)
        self.search_person_b.pack(pady=5)
    def elements_update(self, window):
        # Frame update
        self.update_labelframe = tk.LabelFrame(window, text='Modificar Rol de Persona', foreground='pink')
        #self.update_labelframe.grid(column=0, row=0, padx=5, pady=10)
        self.update_labelframe.pack(pady=10)
        # name
        self.name_label_u = tk.Label(self.update_labelframe, text='Nombre:')
        self.name_label_u.grid(column=0, row=0)
        self.name_string_u = tk.StringVar()
        self.name_entry_u = tk.Entry(self.update_labelframe, textvariable=self.name_string_u)
        self.name_entry_u.grid(column=1, row=0, padx=5, pady=5)
        # surname
        self.surname_label_u = tk.Label(self.update_labelframe, text='Apellido:')
        self.surname_label_u.grid(column=0, row=1)
        self.surname_string_u = tk.StringVar()
        self.surname_entry_u = tk.Entry(self.update_labelframe, textvariable=self.surname_string_u)
        self.surname_entry_u.grid(column=1, row=1, padx=5, pady=5)
        # Update Button
        self.update_person_b = tk.Button(self.page_update, text='Update person', command=lambda:self.update_person_f(self.name_string_u.get(), self.surname_string_u.get()))
        #self.update_person_b.grid(column=0, row=1, padx=5, pady=5)
        self.update_person_b.pack(pady=10)
    def elements_delete(self, window):
        # LabelFrame detele ------------------------------------------------
        self.detele_labelframe = tk.LabelFrame(window, text='Eliminar Persona', foreground='green')
        #self.detele_labelframe.grid(column=0, row=0, padx=5, pady=5)
        self.detele_labelframe.pack(pady=10)
        # name
        self.name_label_d = tk.Label(self.detele_labelframe, text='Nombre:')
        self.name_label_d.grid(column=0, row=0, padx=5, pady=5)
        self.name_string_d = tk.StringVar()
        self.name_entry_d = tk.Entry(self.detele_labelframe, textvariable=self.name_string_d)
        self.name_entry_d.grid(column=1, row=0, padx=5, pady=5)
        # surname
        self.surname_label_d = tk.Label(self.detele_labelframe, text='Apellido:')
        self.surname_label_d.grid(column=0, row=1, padx=5, pady=5)
        self.surname_string_d = tk.StringVar()
        self.surname_entry_d = tk.Entry(self.detele_labelframe, textvariable=self.surname_string_d)
        self.surname_entry_d.grid(column=1, row=1, padx=5, pady=5)
        # Label messaje_ok
        self.delete_ok_label = tk.Label(self.detele_labelframe, text='')
        self.delete_ok_label.grid(column=1, row=2, padx=5, pady=5)
        # Delete Button
        self.delete_person_b = tk.Button(self.page_delete, text='Delete person', command=lambda:self.delete_person_f(self.name_string_d.get(), self.surname_string_d.get()))
        #self.delete_person_b.grid(column=0, row=1, padx=5, pady=5)
        self.delete_person_b.pack(pady=5)
    def elements_crud(self, window):
        # LabelFrame crud ------------------------------------------------
        self.crud_frame = tk.LabelFrame(window, text='Opciones', foreground='blue')
        self.crud_frame.grid(column=0, row=1, padx=5, pady=10)
        # Buttons operations
        self.search_person_b = tk.Button(self.crud_frame, text='Search person', command=lambda:self.search_person_f(self.role_string_s.get()))
        self.search_person_b.grid(column=1, row=0, padx=5, pady=5)
        self.update_person_b = tk.Button(self.crud_frame, text='Update person', command=lambda:self.update_person_f(self.name_string_u.get(), self.surname_string_u.get()))
        self.update_person_b.grid(column=2, row=0, padx=5, pady=5)
        self.delete_person_b = tk.Button(self.crud_frame, text='Delete person', command=lambda:self.delete_person_f(self.name_string_d.get(), self.surname_string_d.get()))
        self.delete_person_b.grid(column=3, row=0, padx=5, pady=5)  
    def search_person_f(self, role):
        conn = self.connection_db()
        cursor = conn.cursor()
        query = '''SELECT * FROM first_team_squad WHERE role=%s'''
        cursor.execute(query, (role,))
        persons = cursor.fetchall()
        for person in persons:
            print(person)
        conn.commit()
        conn.close()
    def update_person_f(self, name, surname):
        conn = self.connection_db()
        cursor = conn.cursor()
        query = '''UPDATE first_team_squad SET surname=%s WHERE name=%s;'''
        cursor.execute(query, (surname, name))
        query = '''SELECT * FROM first_team_squad WHERE name=%s;'''
        cursor.execute(query, (name,))
        person = cursor.fetchone()
        print('update {}'.format(str(person)))
        conn.commit()
        conn.close()
    def exit(self):
        sys.exit()

ventana1 = Aplication()