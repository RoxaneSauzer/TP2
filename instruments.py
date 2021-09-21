import datetime
import numpy as np

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
thisyear = date.strftime('%Y')




class Instrument:
    def __init__(self, price, brand, year, volume):
        self.price=price
        self.brand=brand
        self.year=year
        self.volume=volume
        self.chars=[self.price, self.brand, self.year, self.volume]

    def __str__(self):
        result= ''
        for i in self.chars:
            if i != self.volume:
                result+=str(i)+','
            else:
                result += str(i)
        return result

    def __eq__(self, other):
        for k in range(len(self.chars)):
            if self.chars[k]==other.chars[k]:
                k+1
                return True
            else:
                return False


    def is_new(self):
       return str(self.year)==thisyear


guitar=Instrument(150, "gibson", 2021, 1)

class Piano(Instrument):

    def __init__(self, price, brand, year, volume, number_of_keys):
        super().__init__(price, brand, year, volume)
        self.number_of_keys=number_of_keys

    def __str__(self):
        result= ''
        for i in self.chars:
            if i != self.number_of_keys:
                result+=str(i)+','
            else:

                result += str(i)
        return result

    def muted_volume(self):
        return np.sqrt(self.volume)



class Store:

    def __init__(self, turnover, list_pianos):
        self.turnover=0
        self.list_pianos=list_pianos
        self.stock_piano=[]

        for i in range(len(self.list_pianos)-1):
                    for k in range(i+1, len(list_pianos)):
                        assert list_pianos[i]!=list_pianos[k]

        for i in range(len(self.list_pianos)):
            self.stock_piano.append(1)


    def add(self,piano):
        for i in range(len(self.list_pianos)):
            if self.list_pianos[i]==piano:
                self.stock_piano[i]+=1
                return
            i+1
            self.list_pianos.append(piano)
            self.stock_piano.append(1)

    def sell(self, piano):
        assert piano in self.list_pianos
        assert self.stock_piano[np.where(piano, self.list_pianos)]>0

        self.stock_piano[np.where(piano, self.list_pianos)]-=1







piano1=Piano(2000, "yamaha", 2005, 25, 88)
piano2=Piano(2100, "yamaha", 2015, 20, 88)
piano3=Piano(1050, "steinway", 2009, 36, 88)



store=Store(0,[piano1,piano2,piano3])

print(store.stock_piano)

print(store.add(piano1))
print(np.where(1, [0,1,2,3])