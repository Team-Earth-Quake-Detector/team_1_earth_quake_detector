from bs4 import BeautifulSoup

with open("/Users/aliciahamann/Library/Mobile Documents/com~apple~CloudDocs/MBA/2. Semester/IT Business "
          "Analytics/earthquake project testing/templates/my_map_test.html", "r") as html_map:
    soup = BeautifulSoup(html_map, 'html.parser')
    soup.prettify()

head = soup.find_all('head')
body = soup.find_all('body')
script = soup.find_all("script")[-1]

# /Users/karina/Documents/HSD_Master/2. Semester/4 - IT-Unterstützung von Business Analytics/team_1_earth_quake_detector/use_case/templates/my_map_test.html
