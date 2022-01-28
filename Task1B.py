from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()

p = (48.8567, 2.3508)

print(stations_by_distance(stations, p))  
