import urllib.request, urllib.parse, os
import os
google_street_view_api_key = os.environ.get('GOOGLE_STREET_VIEW_API_KEY')

myloc = r"images" #replace with your own location
key = google_street_view_api_key + "" #got banned after ~100 requests with no key

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&heading=300&location="
  MyUrl = base + urllib.parse.quote_plus(Add) + key
  fi = Add + ".jpg"
  urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))


Tests = [
        "Rua Guararapes",
        "Rua Nebraska",
        "Rua Quintana",
        "Rua Florida"
        "Rua Texas",
        "Rua Kansas",
        "Rua Georgia",
        "Rua Luisiania",
        "Rua Pensilvania",
        "Rua Indiana",
        "Rua Michigan",
        "Rua Arizona",
        "Rua Castilho",
        "Av Padre Jose Antonio dos Santos",


        # "Av Santo Amaro",
        # "Av Portugal",
        # "Rua Nova York",
        # "Rua California",
        # "Rua Ribeiro do Vale",
        # "Rua Guaraiuva",
        # "Rua Conceicao de Monte Alegre",
        # "Av Dr Chucri Zaidan",
        # "Av Engenheiro Luis Carlos Berrini",
        # "Av Nova Independencia",
        # "Rua Arandu, Sao Paulo",
        # "Rua Catipara",
        # "Rua Ipurinas",
        # "Rua Hollywood",
        # "Rua Los Angeles",
        # "Rua Tacoma",
        # "Rua George Ohm",
        # "Av Jornalista Roberto Marinho",
        
        ]
enderecos = []
for i in Tests:
    counter = 10
    while counter  < 2500:
        endereco = i + " " + str(counter)+ " , Sao Paulo, SP"
        print(endereco)
        enderecos.append(endereco)
        counter = counter + 100


for i in enderecos:
  GetStreet(Add=i,SaveLoc=myloc)
