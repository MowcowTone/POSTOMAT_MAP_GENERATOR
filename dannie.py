#класс для чтения данных
import pandas
class dan():
    def __init__(self,file_nameascii):
        self.file_nameascii = file_nameascii
    def read(self):
        self.adres = pandas.read_excel(self.file_nameascii)['Адрес']
        #self.m2 = pandas.read_excel(self.file_nameascii)['Площадь м2']
        #self.Floors = pandas.read_excel(self.file_nameascii)['Этажей']
        #self.Entrances = pandas.read_excel(self.file_nameascii)['Подьездов']
        self.Apartments = pandas.read_excel(self.file_nameascii)['Помещений / Квартир']
class rayon():
    def __init__(self,adres,y,data):
        self.adres = adres
        self.data = data
        self.y=y
    def find(self):
        m=True
        for j in self.data["all_adreses"]:
            if j in self.adres and m:
                self.y+=1
                print(self.y)
                m=False