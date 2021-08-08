import geopy.distance

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print(geopy.distance.distance(coords_1, coords_2).km)


def calculate_distance(starting_point, earthquake):
    starting_point = (52.2296756, 21.0122287)
    earthquake = (52.406374, 16.9251681)
    return geopy.distance.distance(starting_point, earthquake).km

print(calculate_distance(coords_1, coords_2))


def filter_radius(self):
    """ Filter data from API by radius"""
    for earthquake in earthquake_data:
        starting_point = (self.latitude, self.longitude)
        location = (earthquake["latitude"], earthquake["longitude"])
        distance = geopy.distance.distance(starting_point, location).km
        earthquake_data_clean = []
        if distance <= self.radius:
            earthquake_data_clean.append(earthquake)

