from floodsystem.geo import rivers_with_station, station_by_river, stations_by_distance
from floodsystem.stationdata import build_station_list

#Initialise list of station objects
stations = build_station_list()

#Set containing all the names of rivers with stations
rivers = rivers_with_station(stations)

#Dictionary containing stations corresponding to a particular river
stations_by_river = station_by_river(stations)

print(f"{len(rivers)} stations")
print(f"First 10 - {sorted(rivers)[:10]} \n\n")

#Printing the stations corresponding to a particular river in alphabetical order
def print_station_names(river_name):

    station_list = stations_by_river[river_name]

    sorted_station_list = []

    for station in station_list:
        sorted_station_list.append(station.name)
    
    print(f"{river_name}: {sorted(sorted_station_list)} \n")

print_station_names('River Aire')
print_station_names('River Cam')
print_station_names('River Thames')