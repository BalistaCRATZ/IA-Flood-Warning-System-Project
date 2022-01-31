# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):

    """ Returns a list of stations arranged in order of 
        increasing distance from a particular geographic location
    """

    result = []

    for station in stations:
        distance = haversine(station.coord, p)

        result.append((station, distance))

    return sorted_by_key(result, 1)

def stations_within_radius(stations, centre, r):

    """Returns a list of stations within a particualr
        radius of a geographic coordinate
    """
    x = stations_by_distance(stations, centre)
    result =[]
    for i in x:
        if i[1] <= r:
            result.append(i[0].name)

    return result

def rivers_with_station(stations):

    """Returns a set with the names of rivers
        that have a monitoring station
    """
    rivers = set()

    for station in stations:
        if station.river != None:
            rivers.add(station.river)

    return rivers

def station_by_river(stations):

    """Returns a dictionary with the names of
        monitoring stations mapped onto the rivers
        they are located on
    """
    
    result = {}

    for station in stations:
        if station.river in result:
            result[station.river].append(station)
        else:
            result[station.river] = [station]

    return result 


