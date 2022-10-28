import geopy
from geopy.geocoders import Nominatim

USERAGENT = 'https://www.google.com'
addr = 'ул. Расплетина, д. 21, Москва' # адрес

geolocator = Nominatim(timeout=10, user_agent = f"{USERAGENT}")
location = geolocator.geocode(addr)
# точный адрес
print(location)
# координаты
print(location.latitude, location.longitude)