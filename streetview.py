import urllib.request, urllib.parse, os
import os
google_street_view_api_key = os.environ.get('GOOGLE_STREET_VIEW_API_KEY')

myloc = r"" #replace with your own location
key = google_street_view_api_key + "" #got banned after ~100 requests with no key

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
  MyUrl = base + urllib.parse.quote_plus(Add) + key
  fi = Add + ".jpg"
  urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))
#
# Tests = ["457 West Robinwood Street, Detroit, Michigan 48203",
#          "1520 West Philadelphia, Detroit, Michigan 48206",
#          "2292 Grand, Detroit, Michigan 48238",
#          "15414 Wabash Street, Detroit, Michigan 48238",
#          "15867 Log Cabin, Detroit, Michigan 48238",
#          "3317 Cody Street, Detroit, Michigan 48212",
#          "14214 Arlington Street, Detroit, Michigan 48212"]

Tests = [ "469 Rua Guararapes, Sao Paulo, SP, 04561",
          "300 Rua Guararapes, Sao Paulo, SP",
          "100 Rua Guararapes, Sao Paulo, SP"
        ]

for i in Tests:
  GetStreet(Add=i,SaveLoc=myloc)
