# Get the location/coordinates of the current city

import geocoder
g = geocoder.ipinfo('me')
print(g.ip)

print(g.address)
print(g.latlng)

my_adress =g.latlng

#Print it on a map
import folium
my_map1 = folium.Map(location=my_adress,
                     zoom_start = 12)
#Add Circle
folium.CircleMarker(location=my_adress, radius=50, popup = "Köln").add_to(my_map1)
#Add Marker
folium.Marker(my_adress, popup = "Köln").add_to(my_map1)

my_map1.save("my_map.html")


print(response)

'''
import geocoder
import requests
freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
#geo_json = geo_r.json()

address=input('enter an address: ')
g= geocoder.google(address)
lat_ad=g.latlng[0]
lon_ad=g.latlng[1]

user_position = [geo_json["latitude"], geo_json["longitude"]]

print(user_postition)
'''
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def getLocation():
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return (latitude,longitude)
print(getLocation())
'''

# Request: Get the location of a specific/single ip address
'''
import requests
import requests

response = requests.get("http://ip-api.com/217.246.61.192").json()
print(response)
print(response['lat'])
print(response['lon'])
'''

# Request: Get the location of a batch ip address
'''
import requests
response = requests.post("http://ip-api.com/batch", json=[
    {"query": "217.246.61.192"},
]).json()

print(response)
print(response['lat'])
print(response['lon'])

for ip_info in response:
    print(ip_info)
'''
