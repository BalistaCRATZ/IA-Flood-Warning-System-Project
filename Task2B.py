from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)

threshold_stations = stations_level_over_threshold(stations, 0.8)

for s in threshold_stations:
    print(f"{s[0].name} {s[1]}")




