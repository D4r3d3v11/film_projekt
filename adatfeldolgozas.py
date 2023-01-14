from Film import Film
film_adatok = []
def beolvas():
    f = open("film.txt", "r", encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    feldolgoz(sorok)

def feldolgoz(sorok):
    i = 0
    while i < len(sorok):
        sor_lista = sorok[i].strip().split(";")
        filmek = Film(sor_lista)
        film_adatok.append(filmek)
        i += 1


"""Olvasd be a mellékelt file (film.txt) tartalmát, majd 
add meg az adatok sorainak a számát (az első sor nélkül)!"""
def filmek_szamok():
    return len(film_adatok)


"""Melyik a legrövidebb film címe?"""
def legrovidebb_film():
    min = film_adatok[0].Perc
    min_hely = 0
    i = 0
    while i < len(film_adatok):
        if film_adatok[i].Perc < min:
            min = film_adatok[i].Perc
            min_hely = i
        i += 1
    return film_adatok[min_hely].Cim



"""Hány darab legalább 110 perces film van?"""

def filmek_szaztizperc_van():
    i = 0
    szaztiz = 0
    while i < len(film_adatok):
        if film_adatok[i].Perc >= 110:
           szaztiz += 1
        i += 1
    return szaztiz



"""Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből,
 ha tudsz (film címét íratjuk ki, ha van ilyen)! Ha nincs ilyen nevű 
 színész, akkor azt is tudasd!"""
def film_ajanlo():
    film_cime = []
    szinesz_neve = input("Kérem adjon meg egy szinészt a kereséshez: ")
    i = 0
    while i < len(film_adatok):
        if film_adatok[i].Foszereplo == szinesz_neve:
            film_cime.append(film_adatok[i].Cim)

        i +=1
    if len(film_cime) <= 0:
        return "Nincs ilyen szinész"
    else:
        return film_cime


"""A 4-es feladat eredményét írasd ki fájlba is! """

def fajl_beiras(eredmeny):
    f = open("feladat4.txt", "w", encoding="utf-8")
    f.write(str(eredmeny))
    f.close()

