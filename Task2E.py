from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()

#Update data
update_water_levels(stations)

#returns top 5 greatest water level stations
at_risk_stations = stations_highest_rel_level(stations, 5)


#plots water levels of the stations above
dt = 10
for i in at_risk_stations:
    dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(i, dates, levels)
