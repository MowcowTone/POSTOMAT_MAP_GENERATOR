import folium as mark

# Создаю карту
map = mark.Map(location=[55.749877, 37.624368], zoom_start=10)

# 55.749877, 37.624368 - Kremlin Embankment
# 55.739705, 37.413482 - Yartsevskaya Ulitsa, 21
# 55.741468, 37.487102 - Ulitsa Alyab'yeva

""" 
API работает таким способом:
mark.Marker([координаты, координаты], popup='описание при клике', tooltip='название при наведении мыши').add_to(map)
"""

mark.Marker([55.739705, 37.413482], popup='Описание', tooltip='Yartsevskaya Ulitsa, 21').add_to(map)


# mark.Marker([55.739705, 37.413482], popup='Описание', tooltip='Yartsevskaya Ulitsa, 21').add_to(map)
# mark.Marker([55.749877, 37.624368], popup='Это центр Москвы', tooltip='Кпемль').add_to(map)

# генерация карты
map.save('index.html')