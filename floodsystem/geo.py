# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):

    result = []

    for station in stations:
        distance = haversine(station.coord, p)

        result.append((station, distance))

    return sorted_by_key(result, 1)

