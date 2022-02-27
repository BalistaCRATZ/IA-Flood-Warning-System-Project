from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
import matplotlib

stations = build_station_list()
update_water_levels(stations)

low_stations = []
moderate_stations = []

#If the relative water level of a station is below 1.5, it should be classed as either moderate or low risk of flooding
for s in stations:
    if s.relative_water_level() is not None:
        if s.relative_water_level() <= 1.5 and s.relative_water_level() > 1:
            moderate_stations.append(s)
        elif s.relative_water_level() <= 1:
            low_stations.append(s)

    else:
        pass




