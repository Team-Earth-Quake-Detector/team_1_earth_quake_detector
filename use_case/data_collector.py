class DataCollector:
    def __init__(self, long:float = 51.2, lat:float = 6.7, radius:float = 1000): #Düsseldorf default -later current location
        self.long = long
        self.lat = lat
        self.radius = radius
        self.refresh()

    def load_data(self):
        """ Get data from API"""
        response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
        global earthquakes = response.json()['features']
    # QUESTION? Is global the right connection?

    def prep_data(self):
        """ Extract relevant features: id, longitude, latitude, time, magnitude"""
        self.load_data()
        earthquake_data = []
        for element in earthquakes:
            time = str(datetime.fromtimestamp(element["properties"]["time"] / 1000))
            dict = {"id": element["id"],
                    "longitude": element["geometry"]["coordinates"][0],
                    "latitude": element["geometry"]["coordinates"][1],
                    "time": time,
                    "magnitude": element["properties"]["mag"]
                    }
            earthquake_data.append(dict)

    def filter_radius(self):
        """ Filter data from API by radius"""
        #
        pass

    def refresh(self):
        # read data from earthquake data source
        self.prep_data()
        # filter data by radius
        self.filter_radius()
        # prepare pandas data frame or dictionary with relevant data
        self.data = {}


# Data Collector und Earthquake verbinden