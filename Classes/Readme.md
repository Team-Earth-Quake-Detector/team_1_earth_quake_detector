## Class Definition

### 1. DataCollector
- **Purpose**: Access USGS earthquake data and prepare data for further use.
- **Requirements**:
    - *datetime*: Process earthquake timestamp.
    - *geopy.distance*: Calculate distance between the user’s location and the individual earthquakes.
    - *requests*: Set up API to access USGS earthquake data of the last 24 hours (all earth-quakes regardless of magnitude. This presetting can effortlessly be changed by se-lecting another GeoJSON summary format at the USGS website: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
    - *geocoder*: Access the user’s current location.
- **Functions**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| __init__ | **lat** (default = 0), **long** (default = 0) | Uses the user’s current location if no values for longitude and latitude are provided for further data preparation. | - |
| load_data | - | Accesses USGS earthquake data and transfers response to *earthquakes* variable. | - |
| prep_data | - | Loads data with *load_data* function. Extracts relevant earthquake features (id, longitude, latitude, place, time, magnitude) and transfer data to an individual dictionary per earthquake. After that appends earthquake dictionaries to *earthquake_data* list. | earthquake_data |
| filter_radius | **location** (default = None), **user_provided_radius** (default = 250) | Prepares data with *prep_data* function. Uses the user’s current location if no specific location is provided. Calculates the distance between this location and every earthquake in *earthquake_data* list and adds the distance (in km) to the earthquake’s dictionary in *earthquake_data* list. If the calculated distance is smaller than the radius provided by the user, the earthquake is added to *earthquake_data_clean* list. | earthquake_data_clean |


### 2. Map
- **Purpose**: Set up a basic map to be displayed on the web application.
- **Requirements**:
    - *request*: Access the radius provided by the user on the web application for dynamic zoom-in factor.
    - *folium*: Visualize data on interactive map and add features.
    - *geocoder*: Access the user’s current location.
- **Functions**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| __init__ | **lat** (default = 0), **long** (default = 0) | Uses the user’s current location if no values for longitude and latitude are provided for further data preparation. | - |
| set_up_map | **location** (default = None) | Set up a folium map that is centered at the user provided location, highlighted by a marker. By default, the map is centered at the user’s current location. The zoom-in factor adjust dynamically depending on the user provided radius (default = 250 km). OpenStreetMap was chosen as the default layout. | - |
| save_map | **file_name** | Saves the map with the provided file name. | - |



### 3. Overlay
- **Purpose**: Add overlays for geo data visualization on the basic map of class Map.
- **Requirements**:
    - *folium*: Visualize data on interactive map and add features.
    - *folium.Features DivIcon*: Show magnitude markers on the map.
    - *folium.Plugins HeatMap*: Implement a heatmap of earthquake occurrences within the last 24 hours.
    - *branca.colormap*: Dynamically adjust the circle marker’s size according to the earthquake’s magnitude.
    - *geocoder*: Access the user’s current location.
- **Functions**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| __init__ | **lat** (default = 0), **long** (default = 0) | Uses the user’s current location if no values for longitude and latitude are provided for further data preparation. | - |

- Includes superclass Overlay and subclasses EarthquakeOverlay and TectonicOverlay that inherit from class Overlay.
- **Functions - Class EarthquakeOverlay**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| __init__ | **earthquake_data_clean** | Inherit __init__ configurations from superclass Overlay and initialize *earthquake_data_clean* variable. | - |
| apply_circle_markers | **map** | Adds a circle marker for every earthquake in earthquake_data_clean to the map. The circle markers are added to the map as a feature group that allows the user to show or hide the circle markers via layer control. By default, the circle markers are shown on the map. The circle marker’s size and color are dynamically adjusted according to the earthquake’s magnitude. By hovering over the circle marker, the user gets information about the earthquake’s time and magnitude. | - |
| apply_magnitude_markers | **map** | Adds a magnitude marker for every earthquake in earthquake_data_clean to the map. The magnitude markers are added to the map as a feature group that allows the user to show or hide the magnitude markers via layer control. By default, the magnitude markers are shown on the map. | - |
| apply_connective_lines | **map**, **location** (default = None) | Adds a connective line between every earthquake in *earthquake_data_clean* and the user provided location to the map. The connective line are added to the map as a feature group that allows the user to show or hide the connective line via layer control. By default, the connective lines are shown on the map. | - |
| apply_heatmap | **map** | Adds a heatmap of the earthquake occurrence of the last 24 hours within the user provided radius of the user provided location. The heatmap can be shown or hidden via layer control. By default, the heatmap is not shown on the map. | - |

- **Functions - Class TectonicOverlay**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| apply_overlay | **map** | Adds the tectonic plates to the map. The tectonic plates can be shown or hidden via layer control. By default, the tectonic plates are shown on the map. | - |
| add_to_layer_control | **map** | Adds layer control functionality in the top right corner of the map. | - |


### 4. EarthquakeAnalytics
- **Purpose**: Analyse earthquake occurrences and extract relevant KPIs to be included in the dashboard.
- **Requirements**: -
- **Functions**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| __init__ | **earthquake_data**, **earthquake_data_clean** | Initialize *earthquake_data* and *earthquake_data_clean* variables. | - |
| get_total_filtered_earthquakes | **location** (default = None), **radius** (default = 250) | Calculate the number of total earthquake occurrences of the last 24 hours within the user provided radius of the user provided location. | total_filtered_earthquakes |
| get_filtered_minor_earthquakes | **location** (default = None), **radius** (default = 250) | Calculate the number of minor earthquake occurrences of the last 24 hours within the user provided radius of the user provided location. In our case, a minor earthquake is defined as an earthquake with a magnitude below or of 2.5. | filtered_minor_earthquakes |
| get_filtered_moderate_earthquakes | **location** (default = None), **radius** (default = 250) | Calculate the number of moderate earthquake occurrences of the last 24 hours within the user provided radius of the user provided location. In our case, a moderate earthquake is defined as an earthquake with a magnitude between 2.5 and 6.0. | filtered_moderate_earthquakes |
| get_filtered_strong_earthquakes | **location** (default = None), **radius** (default = 250) | Calculate the number of strong earthquake occurrences of the last 24 hours within the user provided radius of the user provided location. In our case, a strong earthquake is defined as an earthquake with a magnitude above 6.0. | filtered_strong_earthquakes |
| get_closest_filtered_earthquake | **location** (default = None), **radius** (default = 250) | Calculate the distance (in km) between the user provided location and the closest earthquake of the last 24 hours. | closest_filtered_earthquake |
| get_place_of_closest_filtered_earthquake | **location** (default = None), **radius** (default = 250) | Get the place of the closest earthquake of the last 24 hours within the user provided radius of the user provided location. The place information is included in the USGS API. | place_of_closest_filtered_earthquake |
| get_strongest_filtered_earthquake | **location** (default = None), **radius** (default = 250) | Get the highest magnitude of all earthquakes of the last 24 hours within the user provided radius of the user provided location. | strongest_filtered_earthquake |
| get_total_earthquakes_worldwide | - | Calculate the number of total earthquake occurrences worldwide of the last 24 hours. | total_earthquakes_worldwide |
| get_minor_earthquakes_worldwide | - | Calculate the number of minor earthquake occurrences worldwide of the last 24 hours. In our case, a minor earthquake is defined as an earthquake with a magnitude below or of 2.5. | minor_earthquakes_worldwide |
| get_moderate_earthquakes_worldwide | - | Calculate the number of moderate earthquake occurrences worldwide of the last 24 hours. In our case, a moderate earthquake is defined as an earthquake with a magnitude between 2.5 and 6.0. | moderate_earthquakes_worldwide |
| get_strong_earthquakes_worldwide | - | Calculate the number of strong earthquake occurrences worldwide of the last 24 hours. In our case, a strong earthquake is defined as an earthquake with a magnitude above 6.0. | strong_earthquakes_worldwide |
| get_strongest_earthquake_worldwide | - | Get the highest magnitude of all earthquakes of the last 24 hours worldwide. | strongest_earthquake_worldwide |
| get_place_of_strongest_earthquake_worldwide | - | Get the place of the strongest earthquake of the last 24 hours worldwide. The place information is included in the USGS API. | place_of_strongest_earthquake_worldwide |


### 5. Location
- **Purpose**: Join a longitude and a latitude value in a format that allows for further use in relevant functions.
- **Requirements**: -
- **Functions**: -


### 6. LocationResolver
- **Purpose**: Resolve a location by a given city or location name.
- **Requirements**:
  - *geocoder*: Access the user’s current location.
  - *geopy.geocoders Nomatim*: Transform longitude and latitude values in address names and vice versa.
- **Functions**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| __init__ | **address** (default = empty string) | Takes the user provided address as an argument. If no user address is provided, takes the user’s current location as an argument. | - |
| get_current_location | - | Accesses the user’s current IP address and extracts longitude and latitude values. These longitude and latitude values are then transformed in address names. | current_location |


### 7. Monitor 
- **Purpose**: Merge functions from different classes to provide a compact and centralized input for flask.
- **Requirements**:
  - *geopy.geocoders Nomatim*: Transform longitude and latitude values in address names and vice versa.
- **Functions**:

| Function | Input parameters | Description | Return |
| ---------------|----------------|---------------|----------------|
| collect_default_data | - | Sets up a DataCollector object and applys the *filter_radius* function. | - |
| relocate | **location** (default = None), **coordinates** (default = None), **radius** (default = 250) | Applies the filter_radius function according to a user provided address. If a string with a location is provided, this location is transformed into longitude and latitude values before applying the filter_radius function. If coordinates are provided, the filter_radius function is applied with these coordinates. | earthquake_data_clean |
| build_map | **location** (default = None), **coordinates** (default = None), **radius** (default = None) | Builds a map to be displayed on the web application. If neither a location nor coordinates are provided (default when webserver is started), the map is built around the user’s current location. If either a location or coordinates are provided (manually entered by the user is the search field), the map is built around this address. In both cases, a base map is built and features (circle markers, magnitude markers, connective lines, a heatmap, tectonic plates and layer control) are added to the map. | map |
| perform_earthquake_analytics | **location** (default = None), **radius** (default = None) | Sets up a DataCollector object and performs all functions of class EarthquakeAnalytics. | total_filtered, minor_filtered, moderate_filtered, strong_filtered, closest_filtered, place_of_closest_filtered, strongest_filtered, total_worldwide, minor_worldwide, moderate_worldwide, strong_worldwide, strongest_worldwide, place_of_strongest_worldwide |


### 8. App
- **Purpose**: Build a flask application to display templates on the webserver.
- **Requirements**:
  - *os*: Save map html file in templates directory.
  - *flask Flask*: Build a flask application.
  - *flask render_template*: Render html templates on the webserver.
  - *flask request*: Access user provided information (location, radius, update frequency) to adapt map html file.
- **app_routes**:
    - */*: Render index.html with customized map and bootstrapped web application layout.
    - *map*: Render map.html to include map on web application.
    - *manual*: Render manual.html to include a website manual.
    - *about_us*: Render about_us.html to include About Us page on web application.



## Class Architecture
![use_case_code/static/images/class_architecture.png](use_case_code/static/images/class_architecture.png)
