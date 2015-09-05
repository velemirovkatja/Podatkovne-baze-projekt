import bottle
import modeli
import random
import hashlib
import sqlite3

bottle.debug(True)

################################################

static_dir = "./static"

@bottle.route("/static/<filename:path>")
def static(filename):
    """Splošna funkcija, ki servira vse statične datoteke iz naslova /static/..."""
    
    return bottle.static_file(filename, root=static_dir)

@bottle.route("/")
@bottle.view("homepage")
def homepage():
    """ Naslovna stran aplikacije."""
    
    uporabnisko_ime = get_user()
    id_uporabnika = modeli.id_uporabnika(uporabnisko_ime)
    filmi = modeli.poisci_filme(beseda = "")
    odKje = random.randint(0, len(filmi)-30)
    return {
        "uporabnisko_ime": uporabnisko_ime,
        "id_uporabnika": id_uporabnika,
        "filmi": filmi[odKje:odKje+5]
    }

@bottle.route("/vsi/")
@bottle.view("vsi")
def vsi():
    """ Izpis vseh filmov."""
    
    filmi = modeli.poisci_filme(beseda = "")
    uporabnisko_ime = get_user()
    id_uporabnika = modeli.id_uporabnika(uporabnisko_ime)
    return {
        "uporabnisko_ime": uporabnisko_ime,
        "id_uporabnika": id_uporabnika,
        "filmi": filmi
        }
    

@bottle.route("/iskanje/")
@bottle.view("iskanje")
def iskanje():
    """ Poišče vse filme, ki vsebujejo dani niz, ki ga vnesemo. """
    
    ime = bottle.request.query.ime
    filmi = modeli.poisci_filme(beseda = ime)
    uporabnisko_ime = get_user()
    id_uporabnika = modeli.id_uporabnika(uporabnisko_ime)
    return {
        "uporabnisko_ime": uporabnisko_ime,
        "id_uporabnika": id_uporabnika,
        "iskano_ime": ime,
        "filmi": filmi
    }

@bottle.route("/Seznam_filmov/<id>")
@bottle.view("film")
def izpis_podatkov(id):
    """ Izpis vseh podatkov o filmu."""
    
    uporabnisko_ime = get_user()
    id_uporabnika = modeli.id_uporabnika(uporabnisko_ime)
    podatki = modeli.izpisi_podatke(id)
    komentarji = modeli.komentarji_film(id)
    podatki_projekcije = modeli.izpisi_podatke_projekcije(id)
    return {
        "uporabnisko_ime": uporabnisko_ime,
        "id_uporabnika": id_uporabnika,
        "podatki": podatki,
        "komentarji": komentarji,
        "podatki_projekcije": podatki_projekcije
    }


@bottle.post("/<id>/dodaj_opis/")
def dodaj_opis(id):
    """ Če dani film še ne vsebuje opisa, ga lahko dodamo."""
    
    opis = bottle.request.forms.get("opis")
    modeli.dodaj_opis(id, opis)
    naslov = "/Seznam_filmov/" + str(id)
    bottle.redirect(naslov)

@bottle.post("/<id>/dodaj_napovednik/")
def dodaj_napovednik(id):
    """ Če dani film še ne vsebuje napovednika, ga lahko dodamo."""
    
    napovednik = bottle.request.forms.get("napovednik")
    modeli.dodaj_napovednik(id, napovednik)
    naslov = "/Seznam_filmov/" + str(id)
    bottle.redirect(naslov)

import datetime   
@bottle.route("/Seznam_filmov/<id>/nakup_vstopnice/")
@bottle.view("nakup_vstopnice")
def nakup_vstopnice(id):
    """ Izpis podatkov za nakup vstopnice."""

    podatki_projekcije = modeli.izpisi_podatke_projekcije(id)
    id_projekcije = podatki_projekcije[0][0]
    dvorana_projekcije = podatki_projekcije[0][1]
    podatki_sedeza = modeli.izpisi_id_sedeza(dvorana_projekcije)
    id_sedeza = podatki_sedeza[0]
    vstopnica = modeli.prodajVstopnico(id_projekcije, datetime.datetime.today(), id_sedeza)
    podatki_vstopnice = modeli.podatkiZaIzpisVstopnice(vstopnica)
    uporabnisko_ime = get_user()
    id_uporabnika = modeli.id_uporabnika(uporabnisko_ime)

    return {
        "uporabnisko_ime": uporabnisko_ime,
        "id_uporabnika": id_uporabnika,
        "podatki_vstopnice" : podatki_vstopnice,
        "id_projekcije" : id_projekcije
        }


@bottle.route("/<id>/nakup_vstopnice/")
@bottle.view("nakup_vstopnice")
@bottle.view("nakupljeno_film")
def nakupljeno_film(id):
    """ Izpis podatkov za nakup vstopnice. Izpiše še koliko vstopnic smo kupili
        in kolikšna je skupna cena."""

    stVstopnic = bottle.request.query.stVstopnic
    
    cena = modeli.cenaNakupaVstopnic(id)
    skupnaCena = round(cena[0]*int(stVstopnic), 2)

    podatki_projekcije = modeli.izpisi_podatke_projekcije(id)
    id_projekcije = podatki_projekcije[0][0]
    dvorana_projekcije = podatki_projekcije[0][1]
    podatki_sedeza = modeli.izpisi_podatke_sedeza(dvorana_projekcije, int(stVstopnic))

    id_sedeza = modeli.izpisi_id_sedeza(dvorana_projekcije)[0]
    vstopnica = modeli.prodajVstopnico(id_projekcije, datetime.datetime.today(), id_sedeza)
    podatki_vstopnice = modeli.podatkiZaIzpisVstopnice(vstopnica)

    uporabnisko_ime = get_user()
    id_uporabnika = modeli.id_uporabnika(uporabnisko_ime)
    
    return {
        "stVstopnic": stVstopnic,
        "skupnaCena": skupnaCena,
        "podatki_sedeza": podatki_sedeza,
        "dvorana_projekcije": dvorana_projekcije,
        "podatki_vstopnice": podatki_vstopnice,
        "uporabnisko_ime": uporabnisko_ime,
        "id_uporabnika": id_uporabnika,
        }


@bottle.route("/<id>/dodaj_komentar/")
def dodaj_komentar(id):
    """ Dodajanje komentarja določenemu filmu."""
    
    uporabnisko_ime = get_user()
    komentar = bottle.request.query.komentar
    modeli.dodaj_komentar(id, komentar, uporabnisko_ime)
    naslov = "/Seznam_filmov/" +str(id)
    bottle.redirect(naslov)


@bottle.route("/iskanje/Seznam_filmov/<id>")
@bottle.view("film")
def izpis_podatkov(id):
    """ Izpis podatkov, ko iščemo filme."""
    
    podatki = modeli.izpisi_podatke(id)
    komentarji = modeli.komentarji_film(id)
    return {
        "podatki": podatki,
        "komentarji": komentarji
    }

@bottle.post("/dodaj_film/")
def dodaj_film():
    """ Možnost dodajanja filma."""
    
    naslov = bottle.request.forms.get("naslov")
    modeli.dodaj_film(naslov)
    bottle.redirect("/vsi/")



#### REGISTRACIJA IN  PRIJAVA ####

# Skrivnost za kodiranje cookiejev
skrivnost = "To je najbolj skrivna skrivnost na svetu 40kdsjfh39zurbeu29rinsj"

# Funkcija, ki v cookie spravi sporočilo
def set_sporocilo(tip, vsebina):
    bottle.response.set_cookie("message", (tip, vsebina), path="/", secret = skrivnost)

# Funkcija, ki iz cookieja dobi sporočilo
def get_sporocilo():
    sporocilo = bottle.request.get_cookie("message", default = None, secret = skrivnost)


def get_user():
    """Poglej cookie in ugotovi, kdo je prijavljen uporabnik, vrni njegovo uporabniško ime in ime.
       Če ni prijavljen, preusmeri na stran za prijavo ali vrni None."""
    
    # Dobimo username iz cookieja
    username = bottle.request.get_cookie("username", secret = skrivnost)
    
    # Preverimo, ali ta uporabnik obstaja
    if username is not None:
        r = modeli.cookies(username)
        if r is not None:   # uporabnik obstaja, vrnemo njegove podatke
            return r[0]
    # Sicer uporabnik ni prijavljen
    else:
        return None


### Funkciji za prijavo ###
@bottle.get("/prijava/")
@bottle.view("prijava")
def login_get():
    """Prikaži formo za registracijo."""
    
    return {
        "napaka" : None,
        "uporabnisko_ime" : None
        }

@bottle.post("/prijava/")
@bottle.view("prijava")
def login_post():
    """Obdelaj izpolnjeno formo za prijavo."""
    
    # Uporabniško ime in geslo, ki ju je uporabnik vpisal v formo
    uporabnisko_ime = bottle.request.forms.uporabnisko_ime    
    geslo = bottle.request.forms.geslo
        
    # Preverimo, ali se je uporabnik pravilno prijavil
    preveriGeslo = modeli.preveri_geslo(uporabnisko_ime, geslo)
    if preveriGeslo is None:        # uporabniško ime in geslo se ne ujemata
        return {
            "napaka": "Uporabniško ime in geslo se ne ujemata",
            "uporabnisko_ime": uporabnisko_ime
            }
    else:
        # Vse je v redu, nastavimo cookie in preusmerimo na glavno stran
        bottle.response.set_cookie("username", uporabnisko_ime, path="/", secret = skrivnost)
        bottle.redirect("/")


### Funkciji za registracijo ###
@bottle.get("/registracija/")
@bottle.view("registracija")
def registracija_get():
    """Prikaži formo za registracijo."""
    
    return {
        "napaka" : None,
        "uporabnisko_ime" : None,
        "ime" : None
        }

@bottle.post("/registracija/")
@bottle.view("registracija")
def registracija_post():
    """ Obdelaj izpolnjeno formo za registracijo. """

    # uporabniško ime in polno ime, ki ju je uporabnik vpisal v formo
    uporabnisko_ime = bottle.request.forms.uporabnisko_ime
    ime = bottle.request.forms.ime
    # vnesemo dve gesli - drugo za potrditev gesla
    geslo1 = bottle.request.forms.geslo1
    geslo2 = bottle.request.forms.geslo2
    
    print("ime:" + ime)
    print("uporabnisko_ime:" + uporabnisko_ime)
    print("geslo:" + geslo1)

    # Preverimo, ali uporabniško ime, ki ga želimo dodati, že obstaja
    obstaja = modeli.ali_ze_obstaja(uporabnisko_ime)
    if obstaja is not None:
 
        return {
            "napaka" : "Uporabniško ime že obstaja!",
            "uporabnisko_ime" : uporabnisko_ime,
            "ime": ime
            }
    else:
        modeli.dodaj_uporabnika(uporabnisko_ime, geslo1, ime)

    # Preverimo, ali se vnešeni gesli ujemata
    if geslo1 != geslo2:
        return {
            "napaka" : "Gesli se ne ujemata!",
            "uporabnisko_ime" : uporabnisko_ime,
            "ime" : ime
            }
                    
    else:
        bottle.response.set_cookie("username", uporabnisko_ime, path="/", secret = skrivnost)
        bottle.redirect("/")


### Funkcija za odjavo ###  
@bottle.get("/odjava/")
def odjava():
    """Pobriši cookie in preusmeri na login."""
    
    bottle.response.delete_cookie("username", path="/")
    bottle.redirect("/")



################################################

bottle.run(host="localhost", port=8080)
