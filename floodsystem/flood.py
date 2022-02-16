
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):

    stations_over_threshold = []

    for s in stations:
        if s.relative_water_level() is not None:
            if s.relative_water_level() > tol:
                stations_over_threshold.append((s, s.relative_water_level()))
        else:
            pass
    
    return stations_over_threshold

def stations_highest_rel_level(stations, N):

    rel_levels = []
    result = []

    for s in stations:
        if s.relative_water_level() is not None:    
            rel_levels.append((s, s.relative_water_level()))
    
    rel_levels = sorted_by_key(rel_levels, 1)

    highest_stations = rel_levels[-N:]

    for h in highest_stations:
        result.append(h[0])
    
    return reversed(result)

