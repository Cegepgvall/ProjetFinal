# Gabriel Vallieres, 1536504
import sys
import tkinter as tk
import tkinter.ttk as ttk
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _ana2color)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Treeview',  font="TkDefaultFont")
    _style_code_ran = 1

class ProjetFinalUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("ProjetFinalUI")
        top.configure(background="#d9d9d9")

        self.top = top
        self.combobox = tk.StringVar()

        _style_code()
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Garage''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t1.configure(background="#c681fe")
        self.TNotebook1_t1.configure(highlightbackground="#ff80ff")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Voitures''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2.configure(background="#ffff00")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Réparations''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3.configure(background="#ff80c0")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(3, text='''Consultations''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t4.configure(background="#00ffff")
        self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4.configure(highlightcolor="black")
        self.InfogarageLabelframe = tk.LabelFrame(self.TNotebook1_t1)
        self.InfogarageLabelframe.place(relx=0.034, rely=0.071, relheight=0.507
                , relwidth=0.923)
        self.InfogarageLabelframe.configure(relief='groove')
        self.InfogarageLabelframe.configure(foreground="#000000")
        self.InfogarageLabelframe.configure(text='''Infos garage''')
        self.InfogarageLabelframe.configure(background="#ff0000")
        self.Label1 = tk.Label(self.InfogarageLabelframe)
        self.Label1.place(relx=0.036, rely=0.093, height=41, width=104
                , bordermode='ignore')
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Nom :''')
        self.Label1_1 = tk.Label(self.InfogarageLabelframe)
        self.Label1_1.place(relx=0.036, rely=0.326, height=41, width=104
                , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Adresse :''')
        self.Label1_1_1 = tk.Label(self.InfogarageLabelframe)
        self.Label1_1_1.place(relx=0.036, rely=0.558, height=41, width=104
                , bordermode='ignore')
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#d9d9d9")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Téléphone :''')
        self.GarageEntryNom = tk.Entry(self.InfogarageLabelframe)
        self.GarageEntryNom.place(relx=0.273, rely=0.093, height=40
                , relwidth=0.498, bordermode='ignore')
        self.GarageEntryNom.configure(background="white")
        self.GarageEntryNom.configure(disabledforeground="#a3a3a3")
        self.GarageEntryNom.configure(font="TkFixedFont")
        self.GarageEntryNom.configure(foreground="#000000")
        self.GarageEntryNom.configure(insertbackground="black")
        self.GarageEntryAdresse = tk.Entry(self.InfogarageLabelframe)
        self.GarageEntryAdresse.place(relx=0.273, rely=0.326, height=40
                , relwidth=0.589, bordermode='ignore')
        self.GarageEntryAdresse.configure(background="white")
        self.GarageEntryAdresse.configure(disabledforeground="#a3a3a3")
        self.GarageEntryAdresse.configure(font="TkFixedFont")
        self.GarageEntryAdresse.configure(foreground="#000000")
        self.GarageEntryAdresse.configure(highlightbackground="#d9d9d9")
        self.GarageEntryAdresse.configure(highlightcolor="black")
        self.GarageEntryAdresse.configure(insertbackground="black")
        self.GarageEntryAdresse.configure(selectbackground="#c4c4c4")
        self.GarageEntryAdresse.configure(selectforeground="black")
        self.GarageEntryTelephone = tk.Entry(self.InfogarageLabelframe)
        self.GarageEntryTelephone.place(relx=0.273, rely=0.558, height=40
                , relwidth=0.407, bordermode='ignore')
        self.GarageEntryTelephone.configure(background="white")
        self.GarageEntryTelephone.configure(disabledforeground="#a3a3a3")
        self.GarageEntryTelephone.configure(font="TkFixedFont")
        self.GarageEntryTelephone.configure(foreground="#000000")
        self.GarageEntryTelephone.configure(highlightbackground="#d9d9d9")
        self.GarageEntryTelephone.configure(highlightcolor="black")
        self.GarageEntryTelephone.configure(insertbackground="black")
        self.GarageEntryTelephone.configure(selectbackground="#c4c4c4")
        self.GarageEntryTelephone.configure(selectforeground="black")
        self.GarageButtonCreerGarage = tk.Button(self.InfogarageLabelframe)
        self.GarageButtonCreerGarage.place(relx=0.345, rely=0.791, height=34
                , width=177, bordermode='ignore')
        self.GarageButtonCreerGarage.configure(activebackground="beige")
        self.GarageButtonCreerGarage.configure(activeforeground="black")
        self.GarageButtonCreerGarage.configure(background="#d9d9d9")
        self.GarageButtonCreerGarage.configure(compound='left')
        self.GarageButtonCreerGarage.configure(disabledforeground="#a3a3a3")
        self.GarageButtonCreerGarage.configure(foreground="#000000")
        self.GarageButtonCreerGarage.configure(highlightbackground="#d9d9d9")
        self.GarageButtonCreerGarage.configure(highlightcolor="black")
        self.GarageButtonCreerGarage.configure(pady="0")
        self.GarageButtonCreerGarage.configure(text='''Créer garage''')
        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.05, rely=0.613, height=41, width=134)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Fichier :''')
        self.GarageEntryFichier = ttk.Entry(self.TNotebook1_t1)
        self.GarageEntryFichier.place(relx=0.302, rely=0.613, relheight=0.097
                , relwidth=0.547)
        self.GarageEntryFichier.configure(takefocus="")
        self.GarageEntryFichier.configure(cursor="ibeam")
        self.GarageButtonDeserialiser = tk.Button(self.TNotebook1_t1)
        self.GarageButtonDeserialiser.place(relx=0.05, rely=0.825, height=44
                , width=197)
        self.GarageButtonDeserialiser.configure(activebackground="beige")
        self.GarageButtonDeserialiser.configure(activeforeground="black")
        self.GarageButtonDeserialiser.configure(background="#d9d9d9")
        self.GarageButtonDeserialiser.configure(compound='left')
        self.GarageButtonDeserialiser.configure(disabledforeground="#a3a3a3")
        self.GarageButtonDeserialiser.configure(foreground="#000000")
        self.GarageButtonDeserialiser.configure(highlightbackground="#d9d9d9")
        self.GarageButtonDeserialiser.configure(highlightcolor="black")
        self.GarageButtonDeserialiser.configure(pady="0")
        self.GarageButtonDeserialiser.configure(text='''Désérialiser''')
        self.GarageButtonSerialiser = tk.Button(self.TNotebook1_t1)
        self.GarageButtonSerialiser.place(relx=0.621, rely=0.825, height=44
                , width=197)
        self.GarageButtonSerialiser.configure(activebackground="beige")
        self.GarageButtonSerialiser.configure(activeforeground="black")
        self.GarageButtonSerialiser.configure(background="#d9d9d9")
        self.GarageButtonSerialiser.configure(compound='left')
        self.GarageButtonSerialiser.configure(disabledforeground="#a3a3a3")
        self.GarageButtonSerialiser.configure(foreground="#000000")
        self.GarageButtonSerialiser.configure(highlightbackground="#d9d9d9")
        self.GarageButtonSerialiser.configure(highlightcolor="black")
        self.GarageButtonSerialiser.configure(pady="0")
        self.GarageButtonSerialiser.configure(text='''Sérialiser''')
        self.VoituresLabelframeVoiture = tk.LabelFrame(self.TNotebook1_t2)
        self.VoituresLabelframeVoiture.place(relx=0.0, rely=0.024
                , relheight=0.342, relwidth=0.99)
        self.VoituresLabelframeVoiture.configure(relief='groove')
        self.VoituresLabelframeVoiture.configure(foreground="#000000")
        self.VoituresLabelframeVoiture.configure(text='''Infos voiture''')
        self.VoituresLabelframeVoiture.configure(background="#ff8000")
        self.Label3 = tk.Label(self.VoituresLabelframeVoiture)
        self.Label3.place(relx=0.017, rely=0.138, height=31, width=94
                , bordermode='ignore')
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Num. Plaque :''')
        self.Label4 = tk.Label(self.VoituresLabelframeVoiture)
        self.Label4.place(relx=0.017, rely=0.414, height=31, width=94
                , bordermode='ignore')
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Marque :''')
        self.Label5 = tk.Label(self.VoituresLabelframeVoiture)
        self.Label5.place(relx=0.017, rely=0.69, height=31, width=94
                , bordermode='ignore')
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Couleur :''')
        self.VoitureEntryPlaque = tk.Entry(self.VoituresLabelframeVoiture)
        self.VoitureEntryPlaque.place(relx=0.203, rely=0.138, height=30
                , relwidth=0.227, bordermode='ignore')
        self.VoitureEntryPlaque.configure(background="white")
        self.VoitureEntryPlaque.configure(disabledforeground="#a3a3a3")
        self.VoitureEntryPlaque.configure(font="TkFixedFont")
        self.VoitureEntryPlaque.configure(foreground="#000000")
        self.VoitureEntryPlaque.configure(insertbackground="black")
        self.VoitureEntryMarque = tk.Entry(self.VoituresLabelframeVoiture)
        self.VoitureEntryMarque.place(relx=0.203, rely=0.414, height=30
                , relwidth=0.278, bordermode='ignore')
        self.VoitureEntryMarque.configure(background="white")
        self.VoitureEntryMarque.configure(disabledforeground="#a3a3a3")
        self.VoitureEntryMarque.configure(font="TkFixedFont")
        self.VoitureEntryMarque.configure(foreground="#000000")
        self.VoitureEntryMarque.configure(insertbackground="black")
        self.VoitureEntryCouleur = tk.Entry(self.VoituresLabelframeVoiture)
        self.VoitureEntryCouleur.place(relx=0.203, rely=0.69, height=30
                , relwidth=0.278, bordermode='ignore')
        self.VoitureEntryCouleur.configure(background="white")
        self.VoitureEntryCouleur.configure(disabledforeground="#a3a3a3")
        self.VoitureEntryCouleur.configure(font="TkFixedFont")
        self.VoitureEntryCouleur.configure(foreground="#000000")
        self.VoitureEntryCouleur.configure(insertbackground="black")
        self.Label6 = tk.Label(self.VoituresLabelframeVoiture)
        self.Label6.place(relx=0.508, rely=0.414, height=31, width=94
                , bordermode='ignore')
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(cursor="fleur")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Modele :''')
        self.Label7 = tk.Label(self.VoituresLabelframeVoiture)
        self.Label7.place(relx=0.508, rely=0.69, height=31, width=94
                , bordermode='ignore')
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Année :''')
        self.VoitureEntryModele = tk.Entry(self.VoituresLabelframeVoiture)
        self.VoitureEntryModele.place(relx=0.695, rely=0.414, height=30
                , relwidth=0.278, bordermode='ignore')
        self.VoitureEntryModele.configure(background="white")
        self.VoitureEntryModele.configure(disabledforeground="#a3a3a3")
        self.VoitureEntryModele.configure(font="TkFixedFont")
        self.VoitureEntryModele.configure(foreground="#000000")
        self.VoitureEntryModele.configure(insertbackground="black")
        self.VoitureEntryAnnee = tk.Entry(self.VoituresLabelframeVoiture)
        self.VoitureEntryAnnee.place(relx=0.695, rely=0.69, height=30
                , relwidth=0.244, bordermode='ignore')
        self.VoitureEntryAnnee.configure(background="white")
        self.VoitureEntryAnnee.configure(disabledforeground="#a3a3a3")
        self.VoitureEntryAnnee.configure(font="TkFixedFont")
        self.VoitureEntryAnnee.configure(foreground="#000000")
        self.VoitureEntryAnnee.configure(insertbackground="black")
        self.VoituresLabelframeProprietaire = tk.LabelFrame(self.TNotebook1_t2)
        self.VoituresLabelframeProprietaire.place(relx=0.0, rely=0.377
                , relheight=0.507, relwidth=0.99)
        self.VoituresLabelframeProprietaire.configure(relief='groove')
        self.VoituresLabelframeProprietaire.configure(foreground="#000000")
        self.VoituresLabelframeProprietaire.configure(text='''Infos propriétaire''')
        self.VoituresLabelframeProprietaire.configure(background="#ff8000")
        self.Label8 = tk.Label(self.VoituresLabelframeProprietaire)
        self.Label8.place(relx=0.068, rely=0.093, height=41, width=104
                , bordermode='ignore')
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Nom :''')
        self.Label9 = tk.Label(self.VoituresLabelframeProprietaire)
        self.Label9.place(relx=0.068, rely=0.326, height=41, width=104
                , bordermode='ignore')
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Prénom :''')
        self.Label10 = tk.Label(self.VoituresLabelframeProprietaire)
        self.Label10.place(relx=0.068, rely=0.558, height=41, width=104
                , bordermode='ignore')
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Courriel :''')
        self.Label11 = tk.Label(self.VoituresLabelframeProprietaire)
        self.Label11.place(relx=0.068, rely=0.791, height=41, width=104
                , bordermode='ignore')
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Téléphone :''')
        self.ProprietaireEntryNom = tk.Entry(self.VoituresLabelframeProprietaire)
        self.ProprietaireEntryNom.place(relx=0.288, rely=0.093, height=40
                , relwidth=0.397, bordermode='ignore')
        self.ProprietaireEntryNom.configure(background="white")
        self.ProprietaireEntryNom.configure(disabledforeground="#a3a3a3")
        self.ProprietaireEntryNom.configure(font="TkFixedFont")
        self.ProprietaireEntryNom.configure(foreground="#000000")
        self.ProprietaireEntryNom.configure(insertbackground="black")
        self.ProprietaireEntryPrenom = tk.Entry(self.VoituresLabelframeProprietaire)
        self.ProprietaireEntryPrenom.place(relx=0.288, rely=0.326, height=40
                , relwidth=0.464, bordermode='ignore')
        self.ProprietaireEntryPrenom.configure(background="white")
        self.ProprietaireEntryPrenom.configure(disabledforeground="#a3a3a3")
        self.ProprietaireEntryPrenom.configure(font="TkFixedFont")
        self.ProprietaireEntryPrenom.configure(foreground="#000000")
        self.ProprietaireEntryPrenom.configure(insertbackground="black")
        self.ProprietaireEntryCourriel = tk.Entry(self.VoituresLabelframeProprietaire)
        self.ProprietaireEntryCourriel.place(relx=0.288, rely=0.558, height=40
                , relwidth=0.515, bordermode='ignore')
        self.ProprietaireEntryCourriel.configure(background="white")
        self.ProprietaireEntryCourriel.configure(disabledforeground="#a3a3a3")
        self.ProprietaireEntryCourriel.configure(font="TkFixedFont")
        self.ProprietaireEntryCourriel.configure(foreground="#000000")
        self.ProprietaireEntryCourriel.configure(insertbackground="black")
        self.ProprietaireEntryTelephone = tk.Entry(self.VoituresLabelframeProprietaire)
        self.ProprietaireEntryTelephone.place(relx=0.288, rely=0.791, height=40
                , relwidth=0.414, bordermode='ignore')
        self.ProprietaireEntryTelephone.configure(background="white")
        self.ProprietaireEntryTelephone.configure(disabledforeground="#a3a3a3")
        self.ProprietaireEntryTelephone.configure(font="TkFixedFont")
        self.ProprietaireEntryTelephone.configure(foreground="#000000")
        self.ProprietaireEntryTelephone.configure(insertbackground="black")
        self.VoitureButtonAjouter = tk.Button(self.TNotebook1_t2)
        self.VoitureButtonAjouter.place(relx=0.185, rely=0.896, height=34
                , width=147)
        self.VoitureButtonAjouter.configure(activebackground="beige")
        self.VoitureButtonAjouter.configure(activeforeground="black")
        self.VoitureButtonAjouter.configure(background="#d9d9d9")
        self.VoitureButtonAjouter.configure(compound='left')
        self.VoitureButtonAjouter.configure(disabledforeground="#a3a3a3")
        self.VoitureButtonAjouter.configure(foreground="#000000")
        self.VoitureButtonAjouter.configure(highlightbackground="#d9d9d9")
        self.VoitureButtonAjouter.configure(highlightcolor="black")
        self.VoitureButtonAjouter.configure(pady="0")
        self.VoitureButtonAjouter.configure(text='''Ajouter''')
        self.VoitureButtonRechercher = tk.Button(self.TNotebook1_t2)
        self.VoitureButtonRechercher.place(relx=0.554, rely=0.896, height=34
                , width=147)
        self.VoitureButtonRechercher.configure(activebackground="beige")
        self.VoitureButtonRechercher.configure(activeforeground="black")
        self.VoitureButtonRechercher.configure(background="#d9d9d9")
        self.VoitureButtonRechercher.configure(compound='left')
        self.VoitureButtonRechercher.configure(disabledforeground="#a3a3a3")
        self.VoitureButtonRechercher.configure(foreground="#000000")
        self.VoitureButtonRechercher.configure(highlightbackground="#d9d9d9")
        self.VoitureButtonRechercher.configure(highlightcolor="black")
        self.VoitureButtonRechercher.configure(pady="0")
        self.VoitureButtonRechercher.configure(text='''Rechercher''')
        self.Label12 = tk.Label(self.TNotebook1_t3)
        self.Label12.place(relx=0.034, rely=0.165, height=41, width=124)
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''Numéro technicien :''')
        self.Label13 = tk.Label(self.TNotebook1_t3)
        self.Label13.place(relx=0.034, rely=0.047, height=41, width=124)
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Numéro Plaque :''')
        self.ReparationEntryPlaque = tk.Entry(self.TNotebook1_t3)
        self.ReparationEntryPlaque.place(relx=0.268, rely=0.047, height=40
                , relwidth=0.443)
        self.ReparationEntryPlaque.configure(background="white")
        self.ReparationEntryPlaque.configure(disabledforeground="#a3a3a3")
        self.ReparationEntryPlaque.configure(font="TkFixedFont")
        self.ReparationEntryPlaque.configure(foreground="#000000")
        self.ReparationEntryPlaque.configure(insertbackground="black")
        self.ReparationEntryTechnicien = tk.Entry(self.TNotebook1_t3)
        self.ReparationEntryTechnicien.place(relx=0.268, rely=0.165, height=40
                , relwidth=0.376)
        self.ReparationEntryTechnicien.configure(background="white")
        self.ReparationEntryTechnicien.configure(disabledforeground="#a3a3a3")
        self.ReparationEntryTechnicien.configure(font="TkFixedFont")
        self.ReparationEntryTechnicien.configure(foreground="#000000")
        self.ReparationEntryTechnicien.configure(insertbackground="black")
        self.ReparationLabelframe = tk.LabelFrame(self.TNotebook1_t3)
        self.ReparationLabelframe.place(relx=0.017, rely=0.307, relheight=0.46
                , relwidth=0.973)
        self.ReparationLabelframe.configure(relief='groove')
        self.ReparationLabelframe.configure(foreground="#000000")
        self.ReparationLabelframe.configure(text='''Infos réparation''')
        self.ReparationLabelframe.configure(background="#ff8000")
        self.Label14 = tk.Label(self.ReparationLabelframe)
        self.Label14.place(relx=0.034, rely=0.103, height=41, width=114
                , bordermode='ignore')
        self.Label14.configure(anchor='w')
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(compound='left')
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Code :''')
        self.Label15 = tk.Label(self.ReparationLabelframe)
        self.Label15.place(relx=0.034, rely=0.359, height=41, width=114
                , bordermode='ignore')
        self.Label15.configure(anchor='w')
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(compound='left')
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Description :''')
        self.ReparationEntryCode = tk.Entry(self.ReparationLabelframe)
        self.ReparationEntryCode.place(relx=0.259, rely=0.103, height=40
                , relwidth=0.283, bordermode='ignore')
        self.ReparationEntryCode.configure(background="white")
        self.ReparationEntryCode.configure(disabledforeground="#a3a3a3")
        self.ReparationEntryCode.configure(font="TkFixedFont")
        self.ReparationEntryCode.configure(foreground="#000000")
        self.ReparationEntryCode.configure(insertbackground="black")
        self.ReparationEntryDescription = tk.Entry(self.ReparationLabelframe)
        self.ReparationEntryDescription.place(relx=0.259, rely=0.359, height=40
                , relwidth=0.714, bordermode='ignore')
        self.ReparationEntryDescription.configure(background="white")
        self.ReparationEntryDescription.configure(disabledforeground="#a3a3a3")
        self.ReparationEntryDescription.configure(font="TkFixedFont")
        self.ReparationEntryDescription.configure(foreground="#000000")
        self.ReparationEntryDescription.configure(insertbackground="black")
        self.Label16 = tk.Label(self.ReparationLabelframe)
        self.Label16.place(relx=0.034, rely=0.718, height=41, width=94
                , bordermode='ignore')
        self.Label16.configure(anchor='w')
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Date :''')
        self.Label17 = tk.Label(self.ReparationLabelframe)
        self.Label17.place(relx=0.517, rely=0.718, height=41, width=114
                , bordermode='ignore')
        self.Label17.configure(anchor='w')
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''Montant :''')
        self.ReparationEntryDate = tk.Entry(self.ReparationLabelframe)
        self.ReparationEntryDate.place(relx=0.224, rely=0.718, height=40
                , relwidth=0.266, bordermode='ignore')
        self.ReparationEntryDate.configure(background="white")
        self.ReparationEntryDate.configure(disabledforeground="#a3a3a3")
        self.ReparationEntryDate.configure(font="TkFixedFont")
        self.ReparationEntryDate.configure(foreground="#000000")
        self.ReparationEntryDate.configure(insertbackground="black")
        self.ReparationEntryMontant = tk.Entry(self.ReparationLabelframe)
        self.ReparationEntryMontant.place(relx=0.741, rely=0.718, height=40
                , relwidth=0.231, bordermode='ignore')
        self.ReparationEntryMontant.configure(background="white")
        self.ReparationEntryMontant.configure(disabledforeground="#a3a3a3")
        self.ReparationEntryMontant.configure(font="TkFixedFont")
        self.ReparationEntryMontant.configure(foreground="#000000")
        self.ReparationEntryMontant.configure(insertbackground="black")
        self.ReparationButtonAjouter = tk.Button(self.TNotebook1_t3)
        self.ReparationButtonAjouter.place(relx=0.084, rely=0.778, height=54
                , width=177)
        self.ReparationButtonAjouter.configure(activebackground="beige")
        self.ReparationButtonAjouter.configure(activeforeground="black")
        self.ReparationButtonAjouter.configure(background="#d9d9d9")
        self.ReparationButtonAjouter.configure(compound='left')
        self.ReparationButtonAjouter.configure(disabledforeground="#a3a3a3")
        self.ReparationButtonAjouter.configure(foreground="#000000")
        self.ReparationButtonAjouter.configure(highlightbackground="#d9d9d9")
        self.ReparationButtonAjouter.configure(highlightcolor="black")
        self.ReparationButtonAjouter.configure(pady="0")
        self.ReparationButtonAjouter.configure(text='''Ajouter''')
        self.ReparationButtonSupprimer = tk.Button(self.TNotebook1_t3)
        self.ReparationButtonSupprimer.place(relx=0.587, rely=0.778, height=54
                , width=177)
        self.ReparationButtonSupprimer.configure(activebackground="beige")
        self.ReparationButtonSupprimer.configure(activeforeground="black")
        self.ReparationButtonSupprimer.configure(background="#d9d9d9")
        self.ReparationButtonSupprimer.configure(compound='left')
        self.ReparationButtonSupprimer.configure(disabledforeground="#a3a3a3")
        self.ReparationButtonSupprimer.configure(foreground="#000000")
        self.ReparationButtonSupprimer.configure(highlightbackground="#d9d9d9")
        self.ReparationButtonSupprimer.configure(highlightcolor="black")
        self.ReparationButtonSupprimer.configure(pady="0")
        self.ReparationButtonSupprimer.configure(text='''Supprimer''')
        self.Label18 = tk.Label(self.TNotebook1_t4)
        self.Label18.place(relx=0.034, rely=0.047, height=41, width=104)
        self.Label18.configure(anchor='w')
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(compound='left')
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(text='''Numéro plaque :''')
        self.Label19 = tk.Label(self.TNotebook1_t4)
        self.Label19.place(relx=0.034, rely=0.165, height=41, width=104)
        self.Label19.configure(anchor='w')
        self.Label19.configure(background="#d9d9d9")
        self.Label19.configure(compound='left')
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(text='''Marque Voiture :''')
        self.ConsultationsButtonAfficher = tk.Button(self.TNotebook1_t4)
        self.ConsultationsButtonAfficher.place(relx=0.671, rely=0.047, height=44
                , width=177)
        self.ConsultationsButtonAfficher.configure(activebackground="beige")
        self.ConsultationsButtonAfficher.configure(activeforeground="black")
        self.ConsultationsButtonAfficher.configure(background="#d9d9d9")
        self.ConsultationsButtonAfficher.configure(compound='left')
        self.ConsultationsButtonAfficher.configure(disabledforeground="#a3a3a3")
        self.ConsultationsButtonAfficher.configure(foreground="#000000")
        self.ConsultationsButtonAfficher.configure(highlightbackground="#d9d9d9")
        self.ConsultationsButtonAfficher.configure(highlightcolor="black")
        self.ConsultationsButtonAfficher.configure(pady="0")
        self.ConsultationsButtonAfficher.configure(text='''Afficher réparations''')
        self.ConsultationsEntryMarque = tk.Entry(self.TNotebook1_t4)
        self.ConsultationsEntryMarque.place(relx=0.235, rely=0.165, height=40
                , relwidth=0.258)
        self.ConsultationsEntryMarque.configure(background="white")
        self.ConsultationsEntryMarque.configure(disabledforeground="#a3a3a3")
        self.ConsultationsEntryMarque.configure(font="TkFixedFont")
        self.ConsultationsEntryMarque.configure(foreground="#000000")
        self.ConsultationsEntryMarque.configure(insertbackground="black")
        self.ConsultationsCombobox = ttk.Combobox(self.TNotebook1_t4)
        self.ConsultationsCombobox.place(relx=0.235, rely=0.047, relheight=0.097
                , relwidth=0.408)
        self.ConsultationsCombobox.configure(textvariable=self.combobox)
        self.ConsultationsCombobox.configure(takefocus="")
        self.Scrolledtreeview1 = ScrolledTreeView(self.TNotebook1_t4)
        self.Scrolledtreeview1.place(relx=0.034, rely=0.307, relheight=0.557
                , relwidth=0.941)
        self.Scrolledtreeview1.configure(columns="Col1 Col2 Col3 Col4")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0",text="Code réparation")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="99")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Description")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="151")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")
        self.Scrolledtreeview1.heading("Col2",text="Intervenant")
        self.Scrolledtreeview1.heading("Col2",anchor="center")
        self.Scrolledtreeview1.column("Col2",width="120")
        self.Scrolledtreeview1.column("Col2",minwidth="20")
        self.Scrolledtreeview1.column("Col2",stretch="1")
        self.Scrolledtreeview1.column("Col2",anchor="w")
        self.Scrolledtreeview1.heading("Col3",text="Date")
        self.Scrolledtreeview1.heading("Col3",anchor="center")
        self.Scrolledtreeview1.column("Col3",width="103")
        self.Scrolledtreeview1.column("Col3",minwidth="20")
        self.Scrolledtreeview1.column("Col3",stretch="1")
        self.Scrolledtreeview1.column("Col3",anchor="w")
        self.Scrolledtreeview1.heading("Col4",text="Montant")
        self.Scrolledtreeview1.heading("Col4",anchor="center")
        self.Scrolledtreeview1.column("Col4",width="69")
        self.Scrolledtreeview1.column("Col4",minwidth="20")
        self.Scrolledtreeview1.column("Col4",stretch="1")
        self.Scrolledtreeview1.column("Col4",anchor="w")

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    root=tk.Tk()
    projetfinalui:ProjetFinalUI=ProjetFinalUI(root)
    root.mainloop()





