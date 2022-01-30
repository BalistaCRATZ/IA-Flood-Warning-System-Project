from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

#Create list of stations
stations = build_station_list()

#Isolate stations with inconsistent typical range data
inconsistent_stations = inconsistent_typical_range_stations(stations)

alphabetical_stations = []

#Generate alphabetically sorted list of inconsistent stations 
for station in inconsistent_stations:
    alphabetical_stations.append(station.name)

print(f"List of inconsistent stations: {sorted(alphabetical_stations)}")
