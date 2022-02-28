from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
import matplotlib
from Task2G import severity

def test_2G():

    l, m, h, s = severity()

    for i in l:
        assert i.relative_water_level() <= 1
    for i in m:
        assert i.relative_water_level() <= 1.5 and i.relative_water_level() > 1
    for i in h:
        assert i.relative_water_level() > 1.5
    for i in s:
        assert i.relative_water_level() > 1.5 
    
test_2G()