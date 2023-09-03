import phonenumbers 
from phonenumbers import geocoder
from test import number
import folium
Key = "0ba99c329f3e43e2b8fa1522b121aad2"
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")

print(number_location);

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(number_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)