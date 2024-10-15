import re
from collections import Counter
'''1. Szyfr Cezara na podstawie twojego indeksu'''
def szyfrujCezar(tekst, klucz):
    zaszyfrowany = ""
    for znak in tekst:
        if znak.isupper():
            przesuniecie = (ord(znak) - ord('A') + klucz) % 26
            nowy_znak = chr(ord('A') + przesuniecie)
            zaszyfrowany += nowy_znak
        elif znak.islower():
            przesuniecie = (ord(znak) - ord('a') + klucz) % 26
            nowy_znak = chr(ord('a') + przesuniecie)
            zaszyfrowany += nowy_znak
        else:
            zaszyfrowany += znak
    return zaszyfrowany

def odszyfrujCezar(tekst, klucz):
    odszyfrowany = ""
    for znak in tekst:
        if znak.isupper():
            przesuniecie = (ord(znak) - ord('A') - klucz) % 26
            nowy_znak = chr(ord('A') + przesuniecie)
            odszyfrowany += nowy_znak
        elif znak.islower():
            przesuniecie = (ord(znak) - ord('a') - klucz) % 26
            nowy_znak = chr(ord('a') + przesuniecie)
            odszyfrowany += nowy_znak
        else:
            odszyfrowany += znak
    return odszyfrowany

'''2. Szyfr Vigenere na podstawie twojego indeksu'''
def szyfrujVigenere(tekst, klucz):
    zaszyfrowany = ''
    dlugosc_klucza = len(klucz)
    for i, znak in enumerate(tekst):
        if znak.isupper():
            kod_znaku = ord(znak) - ord('A')
            kod_klucza = ord(klucz[i % dlugosc_klucza].upper()) - ord('A')
            zaszyfrowany_kod = (kod_znaku + kod_klucza) % 26
            zaszyfrowany += chr(zaszyfrowany_kod + ord('A'))
        elif znak.islower():
            kod_znaku = ord(znak) - ord('a')
            kod_klucza = ord(klucz[i % dlugosc_klucza].lower()) - ord('a')
            zaszyfrowany_kod = (kod_znaku + kod_klucza) % 26
            zaszyfrowany += chr(zaszyfrowany_kod + ord('a'))
        else:
            zaszyfrowany += znak
    return zaszyfrowany

def odszyfrujVigenere(tekst, klucz):
    odszyfrowany = ''
    dlugosc_klucza = len(klucz)
    for i, znak in enumerate(tekst):
        if znak.isupper():
            kod_znaku = ord(znak) - ord('A')
            kod_klucza = ord(klucz[i % dlugosc_klucza].upper()) - ord('A')
            odszyfrowany_kod = (kod_znaku - kod_klucza + 26) % 26
            odszyfrowany += chr(odszyfrowany_kod + ord('A'))
        elif znak.islower():
            kod_znaku = ord(znak) - ord('a')
            kod_klucza = ord(klucz[i % dlugosc_klucza].lower()) - ord('a')
            odszyfrowany += chr((kod_znaku - kod_klucza + 26) % 26 + ord('a'))
        else:
            odszyfrowany += znak
    return odszyfrowany

'''3. Program do łamania szyfru Cezara'''
czestotliwosci_polskie = {
    'A': 8.91, 'Ą': 0.99, 'B': 1.47, 'C': 3.96, 'Ć': 0.40,
    'D': 3.25, 'E': 7.66, 'Ę': 1.11, 'F': 0.30, 'G': 1.42,
    'H': 1.08, 'I': 8.21, 'J': 2.28, 'K': 3.51, 'L': 2.10,
    'Ł': 1.82, 'M': 2.80, 'N': 5.52, 'Ń': 0.20, 'O': 7.75,
    'Ó': 0.85, 'P': 3.13, 'R': 4.69, 'S': 4.32, 'Ś': 0.66,
    'T': 3.98, 'U': 2.50, 'W': 4.65, 'Y': 3.76, 'Z': 5.64,
    'Ź': 0.06, 'Ż': 0.83
}

suma_czestotliwosci = sum(czestotliwosci_polskie.values())
for litera in czestotliwosci_polskie:
    czestotliwosci_polskie[litera] = czestotliwosci_polskie[litera] / suma_czestotliwosci * 100

alfabet_polski = [
    'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O',
    'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z',
    'Ź', 'Ż'
]

def wyczysc_tekst(tekst):
    return ''.join(re.findall('[A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż]', tekst)).upper()

def policz_czestotliwosci(tekst):
    licznik = Counter(tekst)
    suma = sum(licznik.values())
    czestotliwosci = {}
    for litera in alfabet_polski:
        czestotliwosc = (licznik.get(litera, 0) / suma) * 100
        czestotliwosci[litera] = czestotliwosc
    return czestotliwosci

def przesun_litery(tekst, przesuniecie):
    wynik = ''
    for znak in tekst:
        if znak in alfabet_polski:
            indeks = alfabet_polski.index(znak)
            nowy_indeks = (indeks + przesuniecie) % len(alfabet_polski)
            wynik += alfabet_polski[nowy_indeks]
        else:
            wynik += znak
    return wynik

def chi_kwadrat(obserwowane, oczekiwane):
    chi2 = 0
    for litera in alfabet_polski:
        o = obserwowane.get(litera, 0)
        e = oczekiwane.get(litera, 0)
        chi2 += ((o - e) ** 2) / (e + 1e-6)
    return chi2

def rozszyfruj_szyfr_cezara(szyfrogram, liczba_najlepszych=5):
    szyfrogram_czysty = wyczysc_tekst(szyfrogram)
    wyniki = []
    for przesuniecie in range(len(alfabet_polski)):
        tekst_probny = przesun_litery(szyfrogram_czysty, -przesuniecie)
        czestotliwosci_tekst = policz_czestotliwosci(tekst_probny)
        chi2 = chi_kwadrat(czestotliwosci_tekst, czestotliwosci_polskie)
        wyniki.append((chi2, przesuniecie, tekst_probny))
    wyniki.sort()
    return wyniki[:liczba_najlepszych]

def lamanieCezar():
    szyfrogram = input("Wprowadź tekst zaszyfrowany szyfrem Cezara: ")
    liczba_najlepszych = input("Ile najbardziej prawdopodobnych kombinacji wyświetlić (1-10): ")
    try:
        liczba_najlepszych = int(liczba_najlepszych)
        if liczba_najlepszych < 1 or liczba_najlepszych > 10:
            raise ValueError
    except ValueError:
        print("Niepoprawna liczba. Ustawiono domyślną wartość 5.")
        liczba_najlepszych = 5

    wyniki = rozszyfruj_szyfr_cezara(szyfrogram, liczba_najlepszych)

    print("\nNajbardziej prawdopodobne odszyfrowania:")
    for i, (chi2, przesuniecie, tekst) in enumerate(wyniki, 1):
        print(f"{i}. Przesunięcie: {przesuniecie}, Chi-kwadrat: {chi2:.2f}")
        print(f"Odszyfrowany tekst: {tekst}\n")

def cezar():
    tekst = input("Wprowadź tekst do zaszyfrowania: ")
    liczba = 163105  # zmień indeks na swój
    klucz = liczba % 26

    print(f"\nUżyty klucz: {klucz}")

    naglowek = "|"
    for znak in tekst:
        naglowek += f"{znak}|"
    przesuniecia = "|"
    for znak in tekst:
        if znak.isalpha():
            przesuniecia += f"{klucz}|"
        else:
            przesuniecia += " |"

    print(naglowek)
    print(przesuniecia)

    zaszyfrowany_tekst = szyfrujCezar(tekst, klucz)
    print(f"\nZaszyfrowany tekst: {zaszyfrowany_tekst}")

    odszyfrowany_tekst = odszyfrujCezar(zaszyfrowany_tekst, klucz)
    print(f"Odszyfrowany tekst: {odszyfrowany_tekst}")

def vigenere():
    tekst = input("Wprowadź tekst do zaszyfrowania: ")
    liczba = 163105  # zmień indeks na swój
    klucz_num = liczba % 26

    klucz_znak = chr(klucz_num + ord('A'))
    klucz_podstawowy = klucz_znak * len(tekst)
    klucz = klucz_podstawowy

    print(f"\nUżyty klucz: {klucz_podstawowy}")

    naglowek = "|"
    for znak in tekst:
        naglowek += f"{znak}|"
    klucz_wartosci = "|"
    for znak in klucz:
        klucz_wartosci += f"{znak}|"

    print(naglowek)
    print(klucz_wartosci)

    zaszyfrowany_tekst = szyfrujVigenere(tekst, klucz)
    print(f"\nZaszyfrowany tekst: {zaszyfrowany_tekst}")

    odszyfrowany_tekst = odszyfrujVigenere(zaszyfrowany_tekst, klucz)
    print(f"Odszyfrowany tekst: {odszyfrowany_tekst}")

if __name__ == "__main__":
    #cezar()
    #vigenere()
    lamanieCezar()
