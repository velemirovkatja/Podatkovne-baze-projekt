import sqlite3
import datetime
import hashlib

datoteka_baze = "kinospored.sqlite3"


# iskanje filmov, opisov in napovednikov po naslovu
# poišče tudi, če ne poznamo celega naslova, vendar samo ključne besede (v tem primeru nam vrne vse filme s to ključno besedo)
def poisci_filme(beseda = ""):
    """ Vrne seznam vseh filmov, ki dano besedo vsebuejo v naslovu. """
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT id, ime FROM Seznam_filmov WHERE ime LIKE ?""", ["%"+beseda+"%"])
        return cur.fetchall()


def izpisi_podatke(id):
    """ Vrne seznam opisov in napovednikov vseh filmov, ki vsebujejo dano besedo v naslovu. """
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT id, ime, opis, napovednik FROM Seznam_filmov WHERE id = ?""", [id])
        return cur.fetchall()
    

def id_filma(naslov):
    """ Vrne id filma."""
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT id FROM Seznam_filmov WHERE ime = ? """, [naslov])
        id_film = cur.fetchone()
        return id_film

# dodamo film (dodamo naslov filma)
def dodaj_film(naslov):
    """ V bazo doda nov film oz. naslov filma. """
    with baza:
        cur = baza.cursor()
        cur.execute("""INSERT INTO Seznam_filmov (ime) VALUES (?)""", [naslov])


def dodaj_opis(id_filma, opis_filma):
    """ V bazo dodamo opis filma, ki ustreta izbranemu naslovu. """
    with baza:
        cur = baza.cursor()
        cur.execute("""UPDATE Seznam_filmov SET opis = ? WHERE id = ?""", [opis_filma, id_filma])       

def dodaj_napovednik(id_filma, napovednik):
    """ V bazo dodamo napovednik filma, ki ustreta izbranemu naslovu. """
    with baza:
        cur = baza.cursor()
        cur.execute("""UPDATE Seznam_filmov SET napovednik = ? WHERE id = ?""", [napovednik, id_filma])
    

# projekcija za določen film
def dodaj_projekcijo(film, dvorana, termin, cena):
    """ Doda projekcijo danega filma. """
    with baza:
        cur = baza.cursor()
        cur.execute("""INSERT INTO projekcija (film, dvorana, termin_predstave, cena)
                        VALUES (?, ?, ?, ?)""", [film, dvorana, termin, cena])

def izpisi_podatke_projekcije(id_filma):
    """ Vrne podatke o projekciji."""
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT id, dvorana, termin_predstave, cena FROM projekcija WHERE film = ?""", [id_filma])
        return cur.fetchall()

import random
def izpisi_id_sedeza(st_dvorane):
    """ Vrne id sedeža."""
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT id FROM sedež WHERE dvorana = ?""", [st_dvorane])
        pod = cur.fetchall()
        nakljucni_id = random.choice(pod)
        return nakljucni_id

def izpisi_podatke_sedeza(st_dvorane, stVstopnic):
    """ Vrne številke sedeža. Vrne jih toliko, kolikor vstopnic želimo kupiti."""
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT številka_sedeža FROM sedež WHERE dvorana = ?""", [st_dvorane])
        pod = cur.fetchall()

        podatki = []
        for el in pod:
            podatki.append(el[0])
            
        sedezi = []
        for i in range(stVstopnic):
            sedezi.append(podatki[i])

        return sedezi

        
# vstopnica za določeno projekcijo
def prodajVstopnico(id_projekcije, datum_nakupa, id_sedeza):
    """ Proda vstopnico za dani sedež na projekciji in vrne id vstopnice. """

    # Preveri, da sta dvorani sedeža in projekcije enaki
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT dvorana FROM sedež WHERE id = ?""", [id_sedeza])
        dvorana_sedez = cur.fetchone()
        cur = baza.cursor()
        cur.execute("""SELECT dvorana FROM projekcija WHERE id = ?""", [id_projekcije])
        dvorana_projekcija = cur.fetchone()
        
    # dvorana sedeža ni enaka dvorani, v kateri je projekcija
    if dvorana_sedez[0] != int(dvorana_projekcija[0]):
        raise Exception("Dvorani sedeža in projekcije nista enaki.")

    cur = baza.cursor()
    cur.execute("""INSERT INTO vstopnica (projekcija, datum_nakupa, sedež) VALUES (?, ?, ?)""", [id_projekcije, datum_nakupa, id_sedeza])
    id = cur.lastrowid

    # vrne id vstopnice
    return id

    

def podatkiZaIzpisVstopnice(vstopnica):
    """ Podatki o filmu, ki so zapisani na vstopnici. """
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT Seznam_filmov.ime, dvorana.številka_dvorane, projekcija.termin_predstave, projekcija.cena, sedež.številka_sedeža
                     FROM vstopnica
                     JOIN projekcija ON projekcija.id = vstopnica.projekcija
                     JOIN sedež ON sedež.id = vstopnica.sedež
                     JOIN Seznam_filmov ON Seznam_filmov.id = projekcija.film
                     JOIN dvorana ON dvorana.številka_dvorane = projekcija.dvorana
                     WHERE vstopnica.id = ?
                     """, [vstopnica])    

        return cur.fetchall()

def cenaNakupaVstopnic(film):
    """ Vrne ceno vstopnice."""
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT cena FROM projekcija WHERE film = ?""", [film])
        cena = cur.fetchone()

    return cena


def zakodiraj(geslo):
    """ Zakodiramo geslo, ki ga poda uporabnik. """
    return hashlib.md5(geslo.encode()).hexdigest()

    
def preveri_geslo(uporabnisko_ime, geslo):
    """ Preverimo, če v bazi obstaja uporabnik z določenim geslom. """
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT 1 FROM uporabniki WHERE uporabnisko_ime = ? AND geslo = ?""", [uporabnisko_ime, zakodiraj(geslo)])
        pravo = cur.fetchone()
    return pravo

        
def dodaj_uporabnika(uporabnisko_ime, geslo, ime):
    """ V bazo dodamo novega uporabnika z njegovim uporabniškim imenom in geslom. """
    with baza:
        cur = baza.cursor()
        cur.execute("""INSERT INTO uporabniki (uporabnisko_ime, geslo, ime) VALUES (?, ?, ?)""", [uporabnisko_ime, zakodiraj(geslo), ime])
            
        id = cur.lastrowid  # id uporabnika

    return id

def ali_ze_obstaja(uporabnisko_ime):
    """ Preverimo, ali uporabniško ime, ki ga želimo dodati, že obstaja. """
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT 1 FROM uporabniki WHERE uporabnisko_ime = ?""", [uporabnisko_ime])
        obstaja = cur.fetchone()
    return obstaja


def id_uporabnika(uporabnisko_ime):
    """ Vrnemo id uporabnika z določenim uporabniškim imenom."""
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT id FROM uporabniki WHERE uporabnisko_ime = ?""", [uporabnisko_ime])
        id_uporabnika = cur.fetchone()
        return id_uporabnika


def dodaj_komentar(id_filma, komentar, uporabnisko_ime):
    """ V bazo dodamo komentar nekega uporabnika."""
    with baza:
        cur = baza.cursor()
        cur.execute("""INSERT INTO komentarji (id_filma, komentar, uporabnisko_ime) VALUES (?, ?, ?)""", [id_filma, komentar, uporabnisko_ime])
        
        id = cur.lastrowid  # id komentarja

    return id


def komentarji_film(id):
    """ Izpiše vse komentarje za določen film."""
    cur = baza.cursor()
    cur.execute("""SELECT uporabnisko_ime, komentar FROM komentarji WHERE id_filma = ?""", [id])
    komentarji = cur.fetchall()

    return komentarji


def cookies(username):
    with baza:
        cur = baza.cursor()
        cur.execute("""SELECT uporabnisko_ime FROM uporabniki WHERE uporabnisko_ime = ?""", [username])
        r = cur.fetchone()
    return r


baza = sqlite3.connect(datoteka_baze, isolation_level = None, detect_types=sqlite3.PARSE_DECLTYPES)
