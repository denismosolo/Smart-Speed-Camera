import io
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from get_from_DB import get_data

class DataDisplayer(Frame):
    """Main window section"""
    def __init__(self, master, targa, codice):
        master.title('AUTOVELOX')
        master.state('zoomed')
        master.resizable(False,False)

        # Get data from DB
        data = get_data(codice)


        # Layout Manager
        width = 25
        height = 1
        desc_font = 'Georgia 10 bold'
        text_font = 'CourierNew 13'


        """create the velox display frame"""
        fVelox = Frame(master, bd=3, relief=RIDGE)#, background='red')

        fAuto = Frame(fVelox)#, background='orange')
        lAuto = Label(fAuto, text="Foto Velox", font=desc_font)
        lAuto.pack()
        cAuto = Canvas(fAuto, width=412, height=287, bd=3, relief=SUNKEN)#, background='black')
        cAuto.pack(padx=20)
        self.img1 = Image.open(f'auto_images\{targa}.png')
        self.resized_image1= self.img1.resize((420,300), Image.ANTIALIAS)
        self.new_img1=ImageTk.PhotoImage(self.resized_image1)
        cAuto.create_image(0, 0, anchor=NW, image=self.new_img1)
        fAuto.pack(side=LEFT, padx=100, pady=20)

        fTarga = Frame(fVelox)#, background='pink')
        fTarga.pack(side=RIGHT, padx=150)
        lTarga = Label(fTarga, text="Targa", font=desc_font)
        lTarga.pack()
        tTarga = Text(fTarga, height=1*height, width=2*width, font='CourierNew 24', bd=2, relief=SUNKEN)
        tTarga.tag_configure("center", justify='center')
        tTarga.insert("1.0", targa)
        tTarga.tag_add("center", "1.0", "end")
        tTarga.pack(pady=5)
        
        tTarga.config(state=DISABLED)

        fVelox.pack(side=TOP,padx=20, pady=20)



        

        """ Create data display frame """
        fDB = Frame(master, bd=3, relief=RIDGE)#, background='blue')

        # Create the empty textboxes
        fAnagrafica = Frame(fDB)#, background='pink')
        lAnagrafica = Label(fAnagrafica, text="Anagrafica", font=desc_font)
        lAnagrafica.pack(side=TOP, padx=50, pady=5)

        fNomeCognome = Frame(fAnagrafica)#, background="blue")
        fCognome = Frame(fNomeCognome)#, background="yellow")
        lCognome = Label(fCognome, text="Cognome", font=desc_font)
        lCognome.pack(pady=5)
        tCognome = Text(fCognome, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tCognome.pack(pady=5)
        tCognome.insert(END,' '+data[2])
        tCognome.config(state=DISABLED)
        fCognome.pack(side=LEFT, padx=50)

        fNome = Frame(fNomeCognome)#, background="red")
        lNome = Label(fNome, text="Nome", font=desc_font)
        lNome.pack(pady=5)
        tNome = Text(fNome, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tNome.pack(pady=5)
        tNome.insert(END,' '+data[1])
        tNome.config(state=DISABLED)
        fNome.pack(side=RIGHT, padx=50)
        fNomeCognome.pack(anchor=W, pady=7)



        fNascita = Frame(fAnagrafica)#, background='blue')
        fDataNascita = Frame(fNascita)#, background='red')
        lDataNascita = Label(fDataNascita, text="Data Nascita", font=desc_font)
        lDataNascita.pack(pady=5)
        tDataNascita = Text(fDataNascita, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tDataNascita.pack(pady=5)
        tDataNascita.insert(END,' '+data[3].strftime("%d/%m/%Y"))
        tDataNascita.config(state=DISABLED)
        fDataNascita.pack(side=LEFT, padx=50)

        fLuogoNascita = Frame(fNascita)#, background='yellow')
        lLuogoNascita = Label(fLuogoNascita, text="Luogo Nascita", font=desc_font)
        lLuogoNascita.pack(pady=5)
        tLuogoNascita = Text(fLuogoNascita, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tLuogoNascita.pack(pady=5)
        tLuogoNascita.insert(END,' '+data[4])
        tLuogoNascita.config(state=DISABLED)
        fLuogoNascita.pack(side=RIGHT, padx=50)
        fNascita.pack(anchor=W, pady=7)



        fPatente = Frame(fAnagrafica)#, background='blue')
        fCodice = Frame(fPatente)#, background='yellow')
        lCodice = Label(fCodice, text="Codice Patente", font=desc_font)
        lCodice.pack(pady=5)
        tCodice = Text(fCodice, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tCodice.pack(pady=5)
        tCodice.insert(END,' '+data[0])
        tCodice.config(state=DISABLED)
        fCodice.pack(side=LEFT, padx=50)

        fEnte = Frame(fPatente)#, background='red')
        lEnte = Label(fEnte, text="Ente Emettitore", font=desc_font)
        lEnte.pack(pady=5)
        tEnte = Text(fEnte, height=height, width=int(width/2), font=text_font, bd=2, relief=SUNKEN)
        tEnte.pack(pady=5)
        tEnte.insert(END,' '+data[6])
        tEnte.config(state=DISABLED)
        fEnte.pack(side=RIGHT, padx=50)

        fTipo = Frame(fPatente)#, background='green')
        lTipo = Label(fTipo, text="Tipo Patente", font=desc_font)
        lTipo.pack(pady=5)
        tTipo = Text(fTipo, height=height, width=int(width/2), font=text_font, bd=2, relief=SUNKEN)
        tTipo.pack(pady=5)
        tTipo.insert(END,' '+data[5])
        tTipo.config(state=DISABLED)
        fTipo.pack(side=LEFT)
        fPatente.pack(anchor=W, pady=7)

        

        fDatePatente = Frame(fAnagrafica)#, background='blue')
        fDataEmissione = Frame(fDatePatente)#, background='red')
        lDataEmissione = Label(fDataEmissione, text="Data Emissione", font=desc_font)
        lDataEmissione.pack(pady=5)
        tDataEmissione = Text(fDataEmissione, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tDataEmissione.pack(pady=5)
        tDataEmissione.insert(END,' '+data[7].strftime("%d/%m/%Y"))
        tDataEmissione.config(state=DISABLED)
        fDataEmissione.pack(side=LEFT, padx=50)

        fDataScadenza = Frame(fDatePatente)#, background='yellow')
        lDataScadenza = Label(fDataScadenza, text="Data Scadenza", font=desc_font)
        lDataScadenza.pack(pady=5)
        tDataScadenza = Text(fDataScadenza, height=height, width=width, font=text_font, bd=2, relief=SUNKEN)
        tDataScadenza.pack(pady=5)
        tDataScadenza.insert(END,' '+data[8].strftime("%d/%m/%Y"))
        tDataScadenza.config(state=DISABLED)
        fDataScadenza.pack(side=RIGHT, padx=50)
        fDatePatente.pack(anchor=NW, pady=7)

        fAnagrafica.pack(side=RIGHT, padx=100)

        
        """ Create photo frame """
        fFoto = Frame(fDB)#, background='orange')
        lFoto = Label(fFoto, text="Foto ID", font=desc_font)
        lFoto.pack()
        cFoto = Canvas(fFoto, width=213, height=313, bd=3, relief=SUNKEN)#, background='black')
        cFoto.pack()
        self.img = Image.open(io.BytesIO(data[9]))
        self.resized_image= self.img.resize((220,320), Image.ANTIALIAS)
        self.new_img=ImageTk.PhotoImage(self.resized_image)
        cFoto.create_image(0, 0, anchor=NW, image=self.new_img)
        fFoto.pack(side=LEFT, padx=200,pady=20)

        fDB.pack(side=BOTTOM, padx=20, pady=20)



# Main
#root=Tk()
#App=DataDisplayer(root)
#root.mainloop()

