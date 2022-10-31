import phonenumbers
import opencage
import folium
import rich

from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
from number import phonenumber
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(phonenumber)

location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_pro = phonenumbers.parse(phonenumber)
print(carrier.name_for_number(service_pro, "en"))

# Create a account at https://opencagedata.com and get the APIKEY and use it on the next line.
key = 'API-KEY'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
rich.print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

rich.print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
