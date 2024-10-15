'''Szyfr Cezara na podstawie twojego indeksu'''
def cezar_szyfruj(tekst, klucz):
    zaszyfrowany = ""
    for znak in tekst:
        if znak.isalpha():
            przesuniecie = (ord(znak.upper()) - ord('A') + klucz) % 26
            nowy_znak = chr(ord('A') + przesuniecie)
            zaszyfrowany += nowy_znak
        else:
            zaszyfrowany += znak
    return zaszyfrowany

def cezar_odszyfruj(tekst, klucz):
    odszyfrowany = ""
    for znak in tekst:
        if znak.isalpha():
            przesuniecie = (ord(znak.upper()) - ord('A') - klucz) % 26
            nowy_znak = chr(ord('A') + przesuniecie)
            odszyfrowany += nowy_znak
        else:
            odszyfrowany += znak
    return odszyfrowany

def main():
    tekst = input("Wprowadź tekst do zaszyfrowania: ")
    liczba = 163105 #zmien indeks
    klucz = liczba % 26

    for znak in tekst:
        if znak.isalpha():
            print(f"{znak}+({klucz})")

    zaszyfrowany_tekst = cezar_szyfruj(tekst, klucz)
    print(f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")

    odszyfrowany_tekst = cezar_odszyfruj(zaszyfrowany_tekst, klucz)
    print(f"Odszyfrowany tekst: {odszyfrowany_tekst}")

if __name__ == "__main__":
    main()