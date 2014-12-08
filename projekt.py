import sqlite3

datoteka_baze = "kinospored.sqlite3"

# iskanje filmov po naslovu
# poišče tudi, če ne poznamo celega naslova, vendar samo ključne besede (v tem primeru nam vrne vse filme s to ključno besedo)
def poisciFilme(beseda):
    c = baza.cursor()
    c.execute("""SELECT id, ime FROM Seznam filmov WHERE ime LIKE %?%""", [beseda])
    filmi = c.fetchall()
    c.close()
    
    return filmi

# funkcija, ki prodaja vstopnice
def prodajanjeVstopnic():
    c = baza.cursor()
    #c.execute("""SELECT"""

baza = sqlite3.connect(datoteka_baze, isolation_level = None)
