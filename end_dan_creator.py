from dannie import *
import shelve
data = shelve.open("adr.suffix")
file_name = 'R_homes_v10.xlsx'
x = dan(file_name)
x.read()
print(len(x.adres))
mat=0
addrs = []
Apartments = []
for i in range(len(x.adres)):
    if str(x.Apartments[i]) == "nan" or str(x.Apartments[i]).lower() == "не указано":
        ...
    else:
        #print(x.adres[i])
        #print(x.Apartments[i])
        mat+=1
        addrs.append(x.adres[i])
        Apartments.append(x.Apartments[i])
print(mat)
data["addrs"] = addrs
data["Apartments"] = Apartments