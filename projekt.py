import sqlite3

datoteka_baze = "kinospored.sqlite3"

# iskanje filmov po naslovu
# poišče tudi, če ne poznamo celega naslova, vendar samo ključne besede (v tem primeru nam vrne vse filme s to ključno besedo)
def poisci_filme(beseda):
    '''Vrne seznam vseh filmov, ki dano besedo vsebuejo v naslovu.'''
    with baza:
        baza.execute("""SELECT id, ime FROM Seznam_filmov WHERE ime LIKE %?%""", [beseda])
        return baza.fetchall()


# projekcija za določen film
def dodaj_projekcijo(film, termin, cena):
    '''Doda projekcijo danega filma.'''
    with baza:
        baza.execute("""INSERT INTO projekcija (film, termin_predstave, cena)
                        VALUES (?, ?, ?)""", [film, termin, cena])
        

# vstopnica za določeno projekcijo
def prodajVstopnico(projekcija, sedez):
    '''Proda vstopnico za dani sedež na projekciji in vrne id vstopnice.'''

    # Preveri, da sta dvorani sedeža in projekcije enaki
    with baza:
        baza.execute("""SELECT dvorana FROM sedež WHERE id = ?""", [sedez])
        dvorana_sedez = baza.fetchone()
        baza.execute("""SELECT dvorana FROM projekcija WHERE id = ?""", [projekcija])
        dvorana_projekcija = baza.fetchone()
        
    # dvorana sedeža ni enaka dvorani, v kateri je projekcija
    if dvorana_sedez != dvorana_projekcija:
        raise Exception("Dvorani sedeža in projekcije nista enaki.")

    cur = baza.cursor()
    cur.execute("""INSERT INTO vstopnica (projekcija, sedež) VALUES (?, ?)""", [projekcija, sedez])
    id = cur.lastrowid

    # vrne id vstopnice
    return id

def podatkiZaIzpisVstopnice(vstopnica):
    ''' Podatki o filmu, ki so zapisani na vstopnici.'''

    with baza:
        baza.execute("""SELECT film FROM projekcija""")
        naslov = baza.fetchone()
        baza.execute("""SELECT dvorana FROM projekcija""")
        dvorana = baza.fetchone()
        baza.execute("""SELECT sedež FROM vstopnica""")
        sedez = baza.fetchone()
        baza.execute("""SELECT termin_predstave FROM projekcija""")
        termin = baza.fetchone()
        baza.execute("""SELECT cena FROM projekcija""")
        cena = baza.fetchone()

    potatkiNaVstopnici = {
        "naslov_filma": naslov
        "dvorana": dvorana
        "sedez": sedez
        "termin_predstave": termin
        "cena": cena
    }

    return podatkiNaVstopnici
 
    

baza = sqlite3.connect(datoteka_baze, isolation_level = None)

# bottle:

def nakup():
    vstopnica = prodajVstopnico()
    podatki = prodatkiZaIzpis(vstopnica)
    #podatke daj v HTML
    
