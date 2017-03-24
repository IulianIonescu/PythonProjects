import string
import random
from clase import *

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def Autentificare_Cont(banca):
    print('---Autentificare---')
    print("Nume: ")
    nume = input()
    print('Parola: ')
    pin = input()
    for i in range(len(banca)):
        if nume == banca[i].get_name() and pin == banca[i].get_pin():
            print('Autentificare reusita!')
            return i
    else:
        print('Autentificare esuata!')
        return -1


def Creare_Profil(banca):
    print('---Creare Profil---')
    print('Setati un nume :')
    x = input()
    print('Setati o parola de acces: ')
    y = input()
    profil = Profil(x, y)
    client = Client(profil)
    banca.append(client)


def Deschidere_Cont(banca,sold,exista):
    banca[exista].adauga_cont(sold,id_generator())
    print('---Contul a fost creat---')
    print('Detalii')
    banca[exista].afisare_extrase()


def Inchidere_Cont(banca,exista):
    cont_de_inchis = -1
    while cont_de_inchis == -1:
        print('Dati codul contului de inchis:')
        cod = input()
        cont_de_inchis = banca[exista].cauta_cont(cod)
        if cont_de_inchis != -1:
            cod_cont_inchis = banca[exista].conturi[cont_de_inchis].get_cod()
            banca[exista].inchidere_cont(cont_de_inchis)
            print('---Contul cu ID-ul', cod_cont_inchis, ' a fost inchis!---')
            Afisare_Raport(banca,exista)
        else:
            print('Cont negasit!')


def Depunere_Bani(banca):
    pozitie_client = -1
    pozitie_cont = -1
    while pozitie_cont == -1:
        print('Dati codul contului in care doriti sa depuneti: ')
        cod = input()
        for i in range(len(banca)):
            pozitie_cont = banca[i].cauta_cont(cod)
            if pozitie_cont != -1:
                pozitie_client = i
                break
        if pozitie_cont != -1:
            print('Dati suma: ')
            suma = float(input())
            suma_initiala = banca[pozitie_client].conturi[pozitie_cont].get_sold()
            banca[pozitie_client].conturi[pozitie_cont].set_sold(suma + suma_initiala)
            print('Extrasul contului in care s-au depus banii')
            banca[pozitie_client].conturi[pozitie_cont].afisare_cont()
        else:
            print('Cont Inexistent!')


def Extragere_Bani(banca,exista):
    plafon = 5000.00
    suma = 5001.00
    if len(banca[exista].conturi) > 0:
        print('Dati codul contului dumneavoastra din care se vor extrage banii')
        cod_cont = input()
        pozitie_cont = banca[exista].cauta_cont(cod_cont)
        if pozitie_cont != -1:
            suma_initiala = banca[exista].conturi[pozitie_cont].get_sold()
            while suma > plafon or suma > suma_initiala: #va intra cel putin o data , prima suma e mereu mai mare decat plafonul
                print('Dati suma: ')
                suma = float(input())
                if suma > plafon:
                    print('Suma depasteste plafonul zilnic, dati o suma mai mica')
                elif suma > suma_initiala:
                    print('Fonduri insuficiente!')
                else:
                    banca[exista].conturi[pozitie_cont].set_sold(suma_initiala - suma)
        else:
            print('Cont negasit')
    else:
        print('Nu aveti un cont deschis deocamdata')



def Transfer_Bani(banca,exista):
    pozitie_cont_primitor = -1
    pozitie_client_primitor = -1
    if len(banca[exista].conturi) > 0:
        print('Dati codul contului dumneavoastra din care vor fi transferati banii:')
        cod_cont_extras = input()
        pozitie_cont_extras = banca[exista].cauta_cont(cod_cont_extras)
        while pozitie_cont_primitor == -1:
            print('Dati codul contului in care vor fi transferati banii:')
            cod_cont_primitor = input()
            for i in range(len(banca)):
                pozitie_cont_primitor = banca[i].cauta_cont(cod_cont_primitor)
                if pozitie_cont_primitor != -1:
                    pozitie_client_primitor = i
                    break
            if pozitie_cont_primitor != -1:
                suma = 5001.00
                while suma > banca[exista].conturi[pozitie_cont_extras].get_sold():
                    print('Dati suma pe care doriti s-o transferati:')
                    suma = float(input())
                    if suma > banca[exista].conturi[pozitie_cont_extras].get_sold():
                        print('Fonduri Insuficiente!')
                suma_initiala_donator = banca[exista].conturi[pozitie_cont_extras].get_sold()
                suma_initiala_primitor = banca[pozitie_client_primitor].conturi[pozitie_cont_primitor].get_sold()
                banca[exista].conturi[pozitie_cont_extras].set_sold(suma_initiala_donator - suma)
                banca[pozitie_client_primitor].conturi[pozitie_cont_primitor].set_sold(suma_initiala_primitor + suma)
            else:
                print('Cont negasit!')
        print('Extrasul contului din care s-au tranferat banii:')
        banca[exista].conturi[pozitie_cont_extras].afisare_cont()
        print('Extrasul contului in care s-au tranferat banii:')
        banca[pozitie_client_primitor].conturi[pozitie_cont_primitor].afisare_cont()
    else:
        print('Nu aveti inca un cont deschis!')


def Afisare_Raport(banca,exista):
    banca[exista].afisare_extrase()


def functie_test_user():
    banca = []
    print('Numarul de clienti introdusi: ')
    n = int(input())
    for i in range(n):
        Creare_Profil(banca)
        banca[i].adauga_cont(round(random.uniform(1000.00, 5000.00), 2), id_generator())
    for i in range(n):
        banca[i].afisare_extrase()

    Creare_Profil(banca)
    exista = Autentificare_Cont(banca)
    while exista == -1:
        exista = Autentificare_Cont(banca)
    optiune = 1
    while optiune != 0:
        print('Alegeti o optiune')
        print('1) Deschidere Cont')
        print('2) Inchidere Cont')
        print('3) Depunere bani')
        print('4) Extragere bani')
        print('5) Transfer bani')
        print('6) Afisare raport')
        print('0) Inchidere Meniu')
        optiune = int(input())
        if optiune == 1:
            print('Doriti sa porniti cu o suma initiala? Da-1 Nu-0')
            ok = int(input())
            if ok == 1:
                print("Dati suma:")
                suma= float(input())
                Deschidere_Cont(banca,suma,exista)
            else:
                Deschidere_Cont(banca,0.00,exista)
        elif optiune == 2:
            Inchidere_Cont(banca,exista)
        elif optiune == 3:
            Depunere_Bani(banca)
        elif optiune == 4:
            Extragere_Bani(banca,exista)
        elif optiune == 5:
            Transfer_Bani(banca,exista)
        elif optiune == 6:
            Afisare_Raport(banca,exista)
        elif optiune == 0:
            continue
        else:
            continue


def functie_test_automata():
    banca = []
    print('Numarul de clienti introdusi in baza de date: ')
    n = int(input())
    for i in range(n):
        Creare_Profil(banca)
        banca[i].adauga_cont(round(random.uniform(1000.00, 5000.00), 2), id_generator())
    for i in range(n):
        banca[i].afisare_extrase()
    Creare_Profil(banca)
    exista = Autentificare_Cont(banca)
    while exista == -1:
        exista = Autentificare_Cont(banca)
    print('\n--Deschidere conturi--\n')
    Deschidere_Cont(banca,3000.00,exista)
    Deschidere_Cont(banca,2500.00,exista)
    print('\n--Extragere  bani--\n')
    Extragere_Bani(banca,exista)
    print('\n--Depunere bani--\n')
    Depunere_Bani(banca)
    print('\n--Transfer bani--\n')
    Transfer_Bani(banca,exista)
    print('\n--Afisarea detaliilor conturilor unui client--\n')
    Afisare_Raport(banca,exista)
    print('\n--Inchidere cont--\n')
    Inchidere_Cont(banca,exista)








