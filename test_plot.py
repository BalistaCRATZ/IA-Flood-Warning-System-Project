import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
def test_plot_water_levels():
    stations = build_station_list()
    at_risk_stations = stations_highest_rel_level(stations, 5)
    for s in at_risk_stations:
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))
        result = plot_water_levels(station, dates, levels)

        assert type(result) == list and len(result) >= 0

test_plot_water_levels()