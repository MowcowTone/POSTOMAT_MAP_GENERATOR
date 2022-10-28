from bs4 import BeautifulSoup as bs
import requests
def sty():
    html =  requests.get("http://127.0.0.1:5500/index.html")


    soup = bs(html.text, "lxml")

    # вставка текста

    soup.find('head').find('style').append('.leaflet-popup-content {width: 200px;height: auto;}')

    with open("index.html", "w", encoding="UTF-8") as file:
        file.write(f'{soup.prettify()}')