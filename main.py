import requests
from bs4 import BeautifulSoup

codigoICAO = input("Codigo ICAO: ").upper().strip()

print("Caregando")

req = requests.get(f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={codigoICAO}")

try:
    soup = BeautifulSoup(req.text, "html.parser")

    nascer_sol = soup.find('sunrise').text
    por_sol = soup.find('sunset').text

    metar = soup.find('h5', text='METAR').findNextSibling().text
    taf = soup.find('h5', text='TAF').findNextSibling().text

    cartas = soup.findAll(id='cartas')
    cartas = cartas[1].findNextSiblings('h4', attrs={'class': None, 'id': None})

    if len(cartas) != 0:
        print("\nCartas: ", end="")

        for carta in cartas:
            print(f"\n{carta.text}: ", end="")

            links = carta.findNextSibling().children

            for link in links:
                l = link.find('a')

                if l != -1:
                    print(f"{l['href']}, ", end="")


    if nascer_sol != "" and por_sol != "":
        print(f"\nNascer do sol: {nascer_sol}, Por do sol: {por_sol}")
    if metar != "":
        print(f"METAR: {metar}")
    if taf != "":
        print(f"TAF: {taf}")
except:
    print("Algo deu errado")