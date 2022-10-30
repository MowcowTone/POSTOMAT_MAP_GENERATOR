import geopy, shelve, time
import folium as mark
from geopy.geocoders import Nominatim
from datetime import datetime
from style import *

data = shelve.open("adr.suffix")
addrs = data["addrs"][:50]
Apartments = data["Apartments"]

USERAGENT = 'https://www.google.com'

# start time
start_time = datetime.now()

def toFixed(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

geolocator = Nominatim(timeout=10, user_agent = f"{USERAGENT}")


# Создаю карту c начальной точкой
map = mark.Map(location=[55.749877, 37.624368], zoom_start=10)
x = 0
y = 0
for i in range(len(addrs)):
    y+=1
    # print(f'Установлено меток: {x}/{y}')
    location = geolocator.geocode(addrs[i])
    try:
        if "к." in addrs[i]:
            mark.Marker([location.latitude, location.longitude], popup=f'кол-во квартир:{Apartments[i]}', tooltip=addrs[i]).add_to(map)
        else:
            mark.Marker([location.latitude, location.longitude], popup=f'кол-во квартир:{Apartments[i]}', tooltip=addrs[i]).add_to(map)

        x+=1
        print([location.latitude, location.longitude])
    except:
        ...

map.save('index.html')
sty()
work_time = datetime.now() - start_time
print(f'Время работы скрипта: {toFixed(work_time, 2)}')