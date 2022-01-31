

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()
centre = (52.2053, 0.1218)
r = 10

print(sorted(stations_within_radius(stations, centre, r)))




