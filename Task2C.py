from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)

at_risk_stations = stations_highest_rel_level(stations, 10)

for s in at_risk_stations:

    print(f"{s.name} {s.relative_water_level()}")