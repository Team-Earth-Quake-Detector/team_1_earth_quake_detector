from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="team_1_earthquake_detector")

# From address
location_1 = geolocator.geocode("175 5th Avenue NYC")
print(location_1.address)
print((location_1.latitude, location_1.longitude))

# From coordinates
location_2 = geolocator.reverse("52.509669, 13.376294")
print(location_2.address)
print((location_2.latitude, location_2.longitude))
