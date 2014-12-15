import sqlite3

datoteka_baze = "kinospored.sqlite3"

# iskanje filmov po naslovu
# poišče tudi, če ne poznamo celega naslova, vendar samo ključne besede (v tem primeru nam vrne vse filme s to ključno besedo)
def poisciFilme(beseda):
    with baza:
        baza.execute("""SELECT id, ime FROM Seznam filmov WHERE ime LIKE %?%""", [beseda])
    filmi = c.fetchall()
    
    return filmi

# projekcija za določen film
def projekcjaKateregaFilma(): # id v parametru???? kaj mi vrne???
    with baza:
        baza.execute("""INSERT INTO projekcija (film) SELECT id FROM Seznam filmov""")
        

# vstopnica za določen film
def vstopnicaKatereProjekcije():
    with baza:
        baza.execute("""INSERT INTO vstopnica (projekcija) SELECT id FROM projekcija""")
        


baza = sqlite3.connect(datoteka_baze, isolation_level = None)
