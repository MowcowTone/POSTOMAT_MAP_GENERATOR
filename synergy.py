import geopy, shelve
import folium as mark
from geopy.geocoders import Nominatim
from style import *

data = shelve.open("adr.suffix")
addrs = data["addrs"][:50]
Apartments = data["Apartments"]

USERAGENT = 'https://www.google.com'

# popups = ['Описание', 'lorem ipsum', 'Ещё описание']
# tooltips = ['First, tooltip, Yartsevskaya Ulitsa, 21']

geolocator = Nominatim(timeout=10, user_agent = f"{USERAGENT}")


# Создаю карту c начальной точкой
map = mark.Map(location=[55.749877, 37.624368], zoom_start=10)
x = 0
y = 0
for i in range(len(addrs)):
    y+=1
    print(f'{x}/{y}')
    location = geolocator.geocode(addrs[i])
    try:
        if "к." in addrs[i]:
            mark.Marker([location.latitude, location.longitude], popup=f'кол-во квартир:{Apartments[i]}', tooltip=addrs[i]).add_to(map)
        else:
            mark.Marker([location.latitude, location.longitude], popup=f'кол-во квартир:{Apartments[i]}', tooltip=addrs[i]).add_to(map)

        x+=1
    except:
        ...

map.save('index.html')
sty()