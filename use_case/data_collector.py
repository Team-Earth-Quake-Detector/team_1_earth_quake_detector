class DataCollector:
    def __init__(self, long:float=51.2, lat:float=7.0, radius:float=1000):
        self.long = long
        self.lat = lat
        self.radius = radius
        self.refresh()


    def refresh(self):
        # read data from earthquake data source
        # filter data by radius
        # prepare pandas data frame or dictionary with relevant data
        self.data = {}
