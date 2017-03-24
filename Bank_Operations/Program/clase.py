class Profil:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Cont:
    def __init__(self, sold, id_cont):
        self.sold = sold
        self.id_cont = id_cont
    def afisare_cont(self):
        print('ID: ',self.id_cont)
        print('Sold: ',self.sold,' lei')
    def get_sold(self):
        return self.sold
    def set_sold(self,suma):
        self.sold = suma
    def get_cod(self):
        return self.id_cont


class Client:
    def __init__(self,profil):
        self.profil = profil
        self.conturi = []
    def adauga_cont(self,sold, cod):
        cont = Cont(sold, cod)
        self.conturi.append(cont)
    def inchidere_cont(self,pozitie):
        self.conturi.pop(pozitie)
    def cauta_cont(self,cod):
        pozitie = -1
        nr_cont = len(self.conturi)
        for i in range(nr_cont):
            if cod == self.conturi[i].get_cod():
                pozitie = i
                break
            else:
                pozitie = -1
        return pozitie
    def get_name(self):
        return self.profil.name
    def get_pin(self):
        return self.profil.password
    def afisare_extrase(self):
        print('============================')
        print(self.profil.name)
        for i in range(len(self.conturi)):
            print('---------CONT-----------')
            self.conturi[i].afisare_cont()