# United States Geological Surves API

- In order to develop a real-time earthquake map, we needed to included an API from the United States 
       Geological Survey (USGS) website.
- The API delivers our data, which contains all earthquakes from all over the world which occurred within the last 24 hours.  
  
    > If you want to get further information about the USGS, click here:
        https://www.usgs.gov/
  > 
  > If you want to take a look at the data of the API, click here: 
        https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson
- Data Preparation:
  
    For Data Preparation, we extract relevant data from the USGS API & transform it into a usable structure.
    The relevant data contains different features, which are represented in the table below:
  
    | Earthquake ID |  Longitude  | Latitude | Place | Time | Magnitude |   
    | ---:| ---: | ---: | ---: | ---: | ---:
    | 00811746 | -119.4843 | 38.5368,1 | Macquarie Island region | 1625824908214 | 2,0
    | ... | ... | ... | ... | ... | ...
