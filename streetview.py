import urllib.request, urllib.parse, os
import os
google_street_view_api_key = os.environ.get('GOOGLE_STREET_VIEW_API_KEY')

myloc = r"/images" #replace with your own location
key = google_street_view_api_key + "" #got banned after ~100 requests with no key

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&heading=90&location="
  MyUrl = base + urllib.parse.quote_plus(Add) + key
  fi = Add + ".jpg"
  urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))


Tests = [
        "Rua Guararapes, Sao Paulo, SP",
        "Rua Nebraska, Sao Paulo, SP"
        ]
enderecos = []
for i in Tests:
    counter = 10
    while counter  < 2200:
        endereco = str(counter) + " " + i
        print(endereco)
        enderecos.append(endereco)
        counter = counter + 100


for i in enderecos:
  GetStreet(Add=i,SaveLoc=myloc)
