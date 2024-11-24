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
    if not klucz.isalpha():
        raise ValueError("Klucz powinien zawierać tylko litery.")
    zaszyfrowany = ''
    klucz_indeks = 0
    dlugosc_klucza = len(klucz)
    for znak in tekst:
        if znak.isupper():
            kod_znaku = ord(znak) - ord('A')
            kod_klucza = ord(klucz[klucz_indeks % dlugosc_klucza].upper()) - ord('A')
            zaszyfrowany_kod = (kod_znaku + kod_klucza) % 26
            zaszyfrowany += chr(zaszyfrowany_kod + ord('A'))
            klucz_indeks += 1
        elif znak.islower():
            kod_znaku = ord(znak) - ord('a')
            kod_klucza = ord(klucz[klucz_indeks % dlugosc_klucza].lower()) - ord('a')
            zaszyfrowany_kod = (kod_znaku + kod_klucza) % 26
            zaszyfrowany += chr(zaszyfrowany_kod + ord('a'))
            klucz_indeks += 1
        else:
            zaszyfrowany += znak
    return zaszyfrowany

def odszyfrujVigenere(tekst, klucz):
    if not klucz.isalpha():
        raise ValueError("Klucz powinien zawierać tylko litery.")
    odszyfrowany = ''
    klucz_indeks = 0
    dlugosc_klucza = len(klucz)
    for znak in tekst:
        if znak.isupper():
            kod_znaku = ord(znak) - ord('A')
            kod_klucza = ord(klucz[klucz_indeks % dlugosc_klucza].upper()) - ord('A')
            odszyfrowany_kod = (kod_znaku - kod_klucza + 26) % 26
            odszyfrowany += chr(odszyfrowany_kod + ord('A'))
            klucz_indeks += 1
        elif znak.islower():
            kod_znaku = ord(znak) - ord('a')
            kod_klucza = ord(klucz[klucz_indeks % dlugosc_klucza].lower()) - ord('a')
            odszyfrowany_kod = (kod_znaku - kod_klucza + 26) % 26
            odszyfrowany += chr(odszyfrowany_kod + ord('a'))
            klucz_indeks += 1
        else:
            odszyfrowany += znak
    return odszyfrowany

'''3. Program do łamania szyfru Cezara'''
def wybierz_alfabet_i_czestotliwosci(jezyk):
    if jezyk.lower() == 'polski':
        alfabet = [
            'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O',
            'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z',
            'Ź', 'Ż'
        ]
        czestotliwosci = {
            'A': 8.91, 'Ą': 0.99, 'B': 1.47, 'C': 3.96, 'Ć': 0.40,
            'D': 3.25, 'E': 7.66, 'Ę': 1.11, 'F': 0.30, 'G': 1.42,
            'H': 1.08, 'I': 8.21, 'J': 2.28, 'K': 3.51, 'L': 2.10,
            'Ł': 1.82, 'M': 2.80, 'N': 5.52, 'Ń': 0.20, 'O': 7.75,
            'Ó': 0.85, 'P': 3.13, 'R': 4.69, 'S': 4.32, 'Ś': 0.66,
            'T': 3.98, 'U': 2.50, 'W': 4.65, 'Y': 3.76, 'Z': 5.64,
            'Ź': 0.06, 'Ż': 0.83
        }
    elif jezyk.lower() == 'angielski':
        alfabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        czestotliwosci = {
            'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70,
            'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15,
            'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
            'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
            'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97,
            'Z': 0.07
        }
    else:
        raise ValueError("Nieobsługiwany język.")
    return alfabet, czestotliwosci

def normalizuj_czestotliwosci(czestotliwosci):
    suma_czestotliwosci = sum(czestotliwosci.values())
    for litera in czestotliwosci:
        czestotliwosci[litera] = czestotliwosci[litera] / suma_czestotliwosci * 100
    return czestotliwosci

def wyczysc_tekst(tekst, alfabet):
    wzorzec = ''.join(alfabet)
    return ''.join(re.findall(f'[{wzorzec}]', tekst.upper()))

def policz_czestotliwosci(tekst, alfabet):
    licznik = Counter(tekst)
    suma = sum(licznik.values())
    czestotliwosci = {}
    for litera in alfabet:
        czestotliwosc = (licznik.get(litera, 0) / suma) * 100
        czestotliwosci[litera] = czestotliwosc
    return czestotliwosci

def przesun_litery(tekst, przesuniecie, alfabet):
    wynik = ''
    n = len(alfabet)
    for znak in tekst:
        if znak in alfabet:
            indeks = alfabet.index(znak)
            nowy_indeks = (indeks + przesuniecie) % n
            wynik += alfabet[nowy_indeks]
        else:
            wynik += znak
    return wynik

def chi_kwadrat(obserwowane, oczekiwane, alfabet):
    chi2 = 0
    for litera in alfabet:
        o = obserwowane.get(litera, 0)
        e = oczekiwane.get(litera, 0)
        chi2 += ((o - e) ** 2) / (e + 1e-6)
    return chi2

def rozszyfruj_szyfr_cezara(szyfrogram, alfabet, czestotliwosci, liczba_najlepszych=5):
    szyfrogram_czysty = wyczysc_tekst(szyfrogram, alfabet)
    wyniki = []
    n = len(alfabet)
    for przesuniecie in range(n):
        tekst_probny = przesun_litery(szyfrogram_czysty, -przesuniecie, alfabet)
        czestotliwosci_tekst = policz_czestotliwosci(tekst_probny, alfabet)
        chi2 = chi_kwadrat(czestotliwosci_tekst, czestotliwosci, alfabet)
        wyniki.append((chi2, przesuniecie, tekst_probny))
    wyniki.sort()
    return wyniki[:liczba_najlepszych]

'''================================================================================================='''

def lamanieCezar():
    jezyk = input("Wybierz język (polski/angielski): ")
    alfabet, czestotliwosci = wybierz_alfabet_i_czestotliwosci(jezyk)
    czestotliwosci = normalizuj_czestotliwosci(czestotliwosci)

    szyfrogram = input("Wprowadź tekst zaszyfrowany szyfrem Cezara: ")
    liczba_najlepszych = input("Ile najbardziej prawdopodobnych kombinacji wyświetlić (1-10): ")
    try:
        liczba_najlepszych = int(liczba_najlepszych)
        if liczba_najlepszych < 1 or liczba_najlepszych > 10:
            raise ValueError
    except ValueError:
        print("Niepoprawna liczba. Ustawiono domyślną wartość 5.")
        liczba_najlepszych = 5

    wyniki = rozszyfruj_szyfr_cezara(szyfrogram, alfabet, czestotliwosci, liczba_najlepszych)

    print("\nNajbardziej prawdopodobne odszyfrowania:")
    for i, (chi2, przesuniecie, tekst) in enumerate(wyniki, 1):
        print(f"{i}. Przesunięcie: {przesuniecie}, Chi-kwadrat: {chi2:.2f}")
        print(f"Odszyfrowany tekst: {tekst}\n")

def cezar():
    tekst = input("Wprowadź tekst do zaszyfrowania: ")
    klucz = int(input("Podaj klucz (liczba przesunięć 1-25): "))

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
    klucz = input("Podaj literę alfabetu (A=0,B=1,...): ")

    print(f"\nUżyty klucz: {klucz}")

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
    wybor = input("Wybierz szyfr: \n1 - Caesar, \n2 - Vigenere, \n3 - Lamanie hasla Cezar\nWpisz: ")
    if wybor == "1":
        cezar()
    elif wybor == "2":
        vigenere()
    elif wybor == "3":
        lamanieCezar()
    else:
        print("Nieprawidłowy wybór.")
