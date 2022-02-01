from floodsystem.geo import rivers_with_station, station_by_river, stations_by_distance, rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def run():
    print(rivers_by_station_number(stations, 9))

run()

