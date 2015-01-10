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
    '''Proda vstopnico za dani sedež na projekciji in vrne slovar podatkov za izpis vstopnice.'''

    # Preveri, da sta dvorani sedeža in projekcije enaki
    with baza:
        baza.execute("""SELECT dvorana FROM sedež WHERE id = ?""", [sedez])
        baza.execute("""SELECT dvorana FROM projekcija WHERE id = ?""", [projekcija])
        # dodamo še fetchone in preverimo, če se številki ujemata - takrat sta enaka sedeža
        
    # Sedež na vstopnici ni enak sedežu v dvorani
    if not sedez = številka_sedeža:
        raise Exception("Dvorani sedeža in projekcije nista enaki.")

    with baza:
        baza.execute("""INSERT INTO vstopnica (projekcija, sedež) VALUES (?, ?)""", [projekcija, sedez])

    # Poišči ime filma - vrnemo podatke o filmu oz. o projekciji
    slovarFilmov = {}
    
        

# v kateri dvorani je predstava - zapišemo na vstopnico
def kateraDvorana():
    with baza:
        baza.execute("""INSERT INTO vstopnica (dvorana) SELECT id FROM dvorana""")


# na katerem sedežu v dvorani sedimo - zapišemo na vstopnico
def kateriSedez():
    with baza:
        baza.execute("""INSERT INTO vstopnica (sedež) SELECT id FROM sedež""")
    

baza = sqlite3.connect(datoteka_baze, isolation_level = None)
