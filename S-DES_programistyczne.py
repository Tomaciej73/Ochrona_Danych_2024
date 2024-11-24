P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_ODW = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permutuj(bity, tablica):
    return [bity[i - 1] for i in tablica]

def przesun_w_lewo(bity, n):
    return bity[n:] + bity[:n]

def generuj_klucze(klucz):
    klucz_p10 = permutuj(klucz, P10)
    lewa, prawa = klucz_p10[:5], klucz_p10[5:]
    lewa1 = przesun_w_lewo(lewa, 1)
    prawa1 = przesun_w_lewo(prawa, 1)
    K1 = permutuj(lewa1 + prawa1, P8)
    lewa2 = przesun_w_lewo(lewa1, 2)
    prawa2 = przesun_w_lewo(prawa1, 2)
    K2 = permutuj(lewa2 + prawa2, P8)
    return K1, K2

def sbox_pobierz(bity, sbox):
    wiersz = (bity[0] << 1) + bity[3]
    kolumna = (bity[1] << 1) + bity[2]
    wartosc = sbox[wiersz][kolumna]
    return [(wartosc >> 1) & 1, wartosc & 1]

def funkcja_fk(bity, klucz):
    lewa, prawa = bity[:4], bity[4:]
    prawa_exp = permutuj(prawa, EP)
    xor_bity = [b ^ k for b, k in zip(prawa_exp, klucz)]
    sbox0 = sbox_pobierz(xor_bity[:4], S0)
    sbox1 = sbox_pobierz(xor_bity[4:], S1)
    polaczone = permutuj(sbox0 + sbox1, P4)
    wynik = [l ^ p for l, p in zip(lewa, polaczone)]
    return wynik + prawa

def sdes_szyfruj(tekst_jawny, klucz):
    bity = permutuj(tekst_jawny, IP)
    K1, K2 = generuj_klucze(klucz)
    bity = funkcja_fk(bity, K1)
    bity = bity[4:] + bity[:4]
    bity = funkcja_fk(bity, K2)
    szyfrogram = permutuj(bity, IP_ODW)
    return szyfrogram

def bity_na_tekst(bity):
    return ''.join(str(bit) for bit in bity)

def tekst_na_bity(s):
    return [int(bit) for bit in s]

tekst_jawny_str = input("Podaj 8-bitowy tekst jawny: ")
klucz_str = input("Podaj 10-bitowy klucz: ")

bity_tekstu_jawnego = tekst_na_bity(tekst_jawny_str)
bity_klucza = tekst_na_bity(klucz_str)

bity_szyfrogramu = sdes_szyfruj(bity_tekstu_jawnego, bity_klucza)
print("===================================================")
#print("Tekst jawny: ", bity_na_tekst(bity_tekstu_jawnego))
#print("Klucz:       ", bity_na_tekst(bity_klucza))
print("Szyfrogram:  ", bity_na_tekst(bity_szyfrogramu))
print("===================================================")
