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

    """Returns a list of stations within a particular
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


def rivers_by_station_number(stations, N):
    """Returns a list of N number of rivers with the 
        greatest number of monitoring stations """

#stations_num is dictionary of rivers with the number of stations on it
    stations_num = {}
    for k,v in station_by_river(stations).items():
        stations_num[k] = len(v)

# returns a list of rivers sorted by descending number of stations
    sorted_stations = sorted(stations_num, key=stations_num.get, reverse=True)

#creates the list with (river name, number of stations) tuple
    result = []
    for sorted_station in sorted_stations:
        result.append((sorted_station, stations_num[sorted_station]))

#First N number of stations gets returned, if there is a tie then all of them gets printed
    for i in range(N, len(result)):
        if result[N][1] == result[i][1]:
            a = result[:N]
            a.append(result[i])
            return a
        else:
            return result[:N]





