# -*- coding: utf-8 -*-

__all__ = [
    'CATRISKS_BUILDING_COVERAGE_CODE',
    'CATRISKS_CONTENTS_COVERAGE_CODE',
    'CATRISKS_TIME_COVERAGE_CODE',
    'EARTH_RADIUS',
    'fix_locations_by_dictionary',
    'get_area_peril_id',
    'get_area_peril_id_based_on_lonlat',
    'get_area_peril_id_based_on_CRSVG',
    'get_area_peril_id_based_on_CRSL5',
    'get_area_peril_id_based_on_CRSL4',
    'get_area_peril_id_based_on_CRSL3',
    'get_area_peril_id_based_on_CRSL2',
    'get_area_peril_id_based_on_CRSL1',
    'get_area_peril_id_based_on_vrg_areas_grid',
    'get_area_peril_id_builder',
    'get_area_peril_grid_boundary_region_for_location_cell',
    'get_area_peril_grid_coordinates_for_location',
    'get_closest_vrg_area_to_location',
    'get_vrg_areas',
    'get_vrg_areas_lonlat_extrema',
    'get_vrg_area_peril_grid',
    'get_vrg_area_peril_grid_corners',
    'get_vrg_area_peril_grid_corners_from_grid',
    'get_vrg_area_peril_grid_lookup_cells_for_location_cell',
    'get_distance',
    'get_vulnerability_id',
    'get_disaggregation'
]

import collections
import csv
import os
import math
import logging
import itertools
import operator
import sys

#from oasislmf.model_preparation.lookup import UNKNOWN_ID
UNKNOWN_ID=-1

from .values import (
    to_float,
    to_int,
    to_string,
)



# Equatorial radius in kilometres - see
#
#    https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
#
EARTH_RADIUS = 6378.137

CATRISKS_BUILDING_COVERAGE_CODE = "B"
CATRISKS_CONTENTS_COVERAGE_CODE = "C"
CATRISKS_TIME_COVERAGE_CODE = "I"

# A dictionary mapping raw area record CSV fields to internal Python fields
# used by the model keys lookup.
_AREA_RECORD_META = {
    'area_peril_id': {'csv_header': 'AREA_PERIL_ID', 'csv_data_type': int, 'validator': to_int, 'desc': 'Area peril ID'},
    'area_id': {'csv_header': 'AREA_ID', 'csv_data_type': int, 'validator': to_int, 'desc': 'Area ID'},
    'lon': {'csv_header': 'LON', 'csv_data_type': float, 'validator': to_float, 'desc': 'Longitude'},
    'lat': {'csv_header': 'LAT', 'csv_data_type': float, 'validator': to_float, 'desc': 'Latitude'},
    'population': {'csv_header': 'POPULATION', 'csv_data_type': float, 'validator': to_float, 'desc': 'Population'},
    'area_level_0': {'csv_header': 'AREA_LEVEL_0', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level #0'},
    'area_level_1': {'csv_header': 'AREA_LEVEL_1', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level #1'},
    'area_level_2': {'csv_header': 'AREA_LEVEL_2', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level #2'},
    'area_level_3': {'csv_header': 'AREA_LEVEL_3', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level #3'},
    'area_level_4': {'csv_header': 'AREA_LEVEL_4', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level #4'},
    'area_level_5': {'csv_header': 'AREA_LEVEL_5', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level #5'},
    'area_level_6': {'csv_header': 'AREA_PERIL_ID', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area peril ID'},
    'aggregation_level': {'csv_header': 'AGGREGATION_LEVEL', 'csv_data_type': str, 'validator': to_string, 'desc': 'Aggregation level'}
}

# A dictionary mapping raw vulnerability record CSV fields to internal Python
# fields used by the model keys lookup.
_VULNERABILITY_RECORD_META = {
    'id': {'csv_header': 'VULNERABILITY_ID', 'csv_data_type': int, 'validator': to_int, 'desc': 'Vulnerability ID'},
    'code': {'csv_header': 'REF', 'csv_data_type': str, 'validator': to_string, 'desc': 'Reference code'}
}

# A dictionary mapping location area level mapping record CSV fields to
# internal Python fields used by the model keys lookup.
_LOCATION_AREA_LEVEL_RECORD_META = {
    'area_level_names': {'csv_header': 'AREA_LEVEL_NAMES', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level names'},
    'country_key': {'csv_header': 'COUNTRY_KEY', 'csv_data_type': str, 'validator': to_string, 'desc': 'Country key'},
    'area_level_model_names': {'csv_header': 'AREA_LEVEL_MODEL_NAMES', 'csv_data_type': str, 'validator': to_string, 'desc': 'Area level model names'}
}

# A dictionary mapping occupancy scheme vulnerability record CSV fields to
# internal Python fields used by the model keys lookup.
_OCC_SCHEME_VULNERABILITY_RECORD_META = {
    'ATC': {
        'code': {'csv_header': 'ATC OCCUPANCY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'ATC occupancy code'},
        'risk_code': {'csv_header': 'VULNERABILITY RISK CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability risk code'},
        'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
    },
    'CRS': {
        'code': {'csv_header': 'CRS OCCUPANCY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'CRS occupancy code'},
        'risk_code': {'csv_header': 'VULNERABILITY RISK CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability risk code'},
        'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
    },
    'OED': {
        'code': {'csv_header': 'OED OCCUPANCY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'OED occupancy code'},
        'risk_code': {'csv_header': 'VULNERABILITY RISK CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability risk code'},
        'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
    },
    'IFM': {
        'code': {'csv_header': 'IFM OCCUPANCY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'IFM occupancy code'},
        'risk_code': {'csv_header': 'VULNERABILITY RISK CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability risk code'},
        'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
    },
    'RMS IND': {
        'code': {'csv_header': 'RMS IND OCCUPANCY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'RMS IND occupancy code'},
        'risk_code': {'csv_header': 'VULNERABILITY RISK CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability risk code'},
        'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
    },
    'SIC': {
        'code': {'csv_header': 'SIC OCCUPANCY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'SIC occupancy code'},
        'risk_code': {'csv_header': 'VULNERABILITY RISK CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability risk code'},
        'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
    }
}


# A dictionary mapping construction class record CSV fields to internal Python
# fields used by the model keys lookup.
_CONSTRUCTION_CLASS_RECORD_META = {
    'class': {'csv_header': 'CONSTRUCTION CLASS', 'csv_data_type': str, 'validator': to_string, 'desc': 'Construction class'},
    'structural_type': {'csv_header': 'VULNERABILITY STRUCTURAL TYPE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability structural type'},
    'structural_height': {'csv_header': 'VULNERABILITY STRUCTURAL HEIGHT', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability structural height'},
    'quality_code': {'csv_header': 'VULNERABILITY QUALITY CODE', 'csv_data_type': str, 'validator': to_string, 'desc': 'Vulnerability quality code'}
}

# A dictionary mapping raw location record CSV fields to internal Python fields
# used by the model keys lookup.
_LOCATION_RECORD_META = {
    'loc_id': {'csv_header': 'LocNumber', 'csv_data_type': int, 'validator': to_int, 'desc': 'Locnumber'},
    'geosch_1': {'csv_header': 'GeogScheme1', 'csv_data_type': str, 'validator': to_string, 'desc': 'Geogscheme1'},
    'geoname_1': {'csv_header': 'GeogName1', 'csv_data_type': str, 'validator': to_string, 'desc': 'Geogname1'},
    'latitude': {'csv_header': 'Latitude', 'csv_data_type': float, 'validator': to_float, 'desc': 'Latitude'},
    'longitude': {'csv_header': 'Longitude', 'csv_data_type': float, 'validator': to_float, 'desc': 'Longitude'},
    'country': {'csv_header': 'CountryCode', 'csv_data_type': str, 'validator': to_string, 'desc': 'Country code'},
    'constructioncode': {'csv_header': 'ConstructionCode', 'csv_data_type': str, 'validator': to_string, 'desc': 'Construction Code'},
    'occupancycode': {'csv_header': 'OccupancyCode', 'csv_data_type': str, 'validator': to_string, 'desc': 'Occupancy Code'},
}


def valid_latitude(latitude):
    """
    Validates a latitude value
    """
    return -90 <= latitude <= 90


def valid_longitude(longitude):
    """
    Validates a longitude value
    """
    return -180 <= longitude <= 180


def valid_lonlat(longitude, latitude):
    """
    Validates a longitude-latitude value pair
    """
    return valid_longitude(longitude) and valid_latitude(latitude)


def get_vrg_areas(areas):

    return list(filter(lambda area: area['aggregation_level'] == 'VRG', areas))


def get_vrg_areas_lonlat_extrema(vrg_areas, asdict=False):
    lons = []
    lats = []
    for area in vrg_areas:
        lons.append(area['lon'])
        lats.append(area['lat'])
    min_lon=min(lons)
    min_lat=min(lats)
    max_lon=max(lons)
    max_lat=max(lats)
    #min_lon, min_lat = map(min, ((area['lon'] for area in vrg_areas), (area['lat'] for area in vrg_areas)))
    #max_lon, max_lat = map(max, ((area['lon'] for area in vrg_areas), (area['lat'] for area in vrg_areas)))

    if not asdict:
        return [min_lon, min_lat, max_lon, max_lat]

    return {
        'min_lon': min_lon,
        'min_lat': min_lat,
        'max_lon': max_lon,
        'max_lat': max_lat
    }


def get_area_peril_grid_coordinates_for_location(lon, lat, origin=(0.0,0.0), cell_width=0.1, cell_height=0.1):
    try:
        return int((lon - origin[0]) / cell_width), int((lat - origin[1]) / cell_height)
    except:
        return None


def get_area_peril_grid_boundary_region_for_location_cell(loc_cell, grid_corners):
    
    x, y = loc_cell
    originx, originy = grid_corners[0]
    maxx, maxy = grid_corners[2]

    if x in range(originx, maxx + 1) and y in range(originy, maxy + 1):
        return
    elif x < originx and y < originy:
        return 'A'
    elif x < originx and y == originy:
        return 'AB'
    elif x < originx and y in range(originy + 1, maxy):
        return 'B'
    elif x < originx and y == maxy:
        return 'BC'
    elif x < originx and y > maxy:
        return 'C'
    elif x == originx and y > maxy:
        return 'CD'
    elif x in range(originx + 1, maxx) and y > maxy:
        return 'D'
    elif x == maxx and y > maxy:
        return 'DE'
    elif x > maxx and y > maxy:
        return 'E'
    elif x > maxx and y == maxy:
        return 'EF'
    elif x > maxx and y in range(originy + 1, maxy):
        return 'F'
    elif x > maxx and y == originy:
        return 'FG'
    elif x > maxx and y < originy:
        return 'G'
    elif x == maxx and y < originy:
        return 'GH'
    elif x in range(originx + 1, maxx) and y < originy:
        return 'H'
    elif x == originx and y < originy:
        return 'HA'


def get_vrg_area_peril_grid_neighbours(loc_cell, vrg_areas_grid, cell_distance=1):
    x, y = loc_cell
    dist_range = range(-cell_distance, cell_distance + 1)
    return filter(
        lambda cell: cell in vrg_areas_grid,
        [(x - i, y - j) if not (i == j == 0) else None for i in dist_range for j in dist_range]
    )


def get_vrg_area_peril_grid_corners(vrg_areas, asdict=False):
    
    min_lon, min_lat, max_lon, max_lat = get_vrg_areas_lonlat_extrema(vrg_areas)

    origin = (min_lon, min_lat)

    lonlat_corners = (origin, (min_lon, max_lat), (max_lon, max_lat), (max_lon, min_lat))

    grid_corners = map(
        lambda point: get_area_peril_grid_coordinates_for_location(point[0], point[1], origin),
        lonlat_corners
    )

    if not asdict:
        return grid_corners

    return {
        'minx-miny': grid_corners[0],
        'minx-maxy': grid_corners[1],
        'maxx-maxy': grid_corners[2],
        'maxx-miny': grid_corners[3]
    }


def get_vrg_area_peril_grid_corners_from_grid(vrg_areas_grid):
    xs=[]
    ys=[]
    for k in vrg_areas_grid:
        xs.append(k[0])
        ys.append(k[1])
    minx = min(xs)
    miny = min(ys)
    maxx = max(xs)
    maxy = max(ys)   

    #minx, miny = map(min, [(k[0] for k in vrg_areas_grid), (k[1] for k in vrg_areas_grid)])
    #maxx, maxy = map(max, [(k[0] for k in vrg_areas_grid), (k[1] for k in vrg_areas_grid)])

    return [(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)]


def get_vrg_area_peril_grid(areas, cell_width=0.1, cell_height=0.1):
    
    vrg_areas = get_vrg_areas(areas)

    lonlat_extrema = get_vrg_areas_lonlat_extrema(vrg_areas)
    origin = lonlat_extrema[:2]

    for area in vrg_areas:
        area['xy'] = get_area_peril_grid_coordinates_for_location(area['lon'], area['lat'], origin=origin, cell_width=cell_width, cell_height=cell_height)

    
    vrg_areas = list(vrg_areas)
    vrg_areas.sort(key=operator.itemgetter('xy'))
    #sorted((x for x in vrg_areas), key=operator.itemgetter('xy'))
    vrg_areas_grid = dict(
        (key,list(group)) for key, group in itertools.groupby(vrg_areas, lambda vrg_area: vrg_area['xy'])
    )

    grid_corners = get_vrg_area_peril_grid_corners_from_grid(vrg_areas_grid)
    top_right_corner = grid_corners[2]
    maxx, maxy = top_right_corner[0], top_right_corner[1]

    for x in range(maxx + 1):
        for y in range(maxy + 1):
            if not (x,y) in vrg_areas_grid:
                vrg_areas_grid[(x,y)] = []

    return vrg_areas_grid, grid_corners


def get_vrg_area_peril_grid_lookup_cells_for_location_cell(loc_cell, vrg_areas_grid, vrg_areas_grid_corners):

    x, y = loc_cell
    originx, originy = vrg_areas_grid_corners[0]
    maxx, maxy = vrg_areas_grid_corners[2]
    lookup_cell = None

    if loc_cell in vrg_areas_grid:
        if x in range(originx + 1, maxx) and y in range(originy + 1, maxy):
            lookup_cell = loc_cell
        elif loc_cell == vrg_areas_grid_corners[0]:
            lookup_cell = (x + 1, y + 1)
        elif x == originx and y in range(originy + 1, maxy):
            lookup_cell = (x + 1, y)
        elif loc_cell == vrg_areas_grid_corners[1]:
            lookup_cell = (x + 1, y - 1)
        elif x in range(originx + 1, maxx) and y == maxy:
            lookup_cell = (x, y - 1)
        elif loc_cell == vrg_areas_grid_corners[2]:
            lookup_cell = (x - 1, y - 1)
        elif x == maxx and y in range(originy + 1, maxy):
            lookup_cell = (x - 1, y)
        elif loc_cell == vrg_areas_grid_corners[3]:
            lookup_cell = (x - 1, y + 1)
        elif x in range(originx + 1, maxx) and y == originy:
            lookup_cell = (x, y + 1)
    else:
        boundary_region = get_area_peril_grid_boundary_region_for_location_cell(loc_cell, vrg_areas_grid_corners)

        if boundary_region in ['HA', 'A', 'AB']:
            lookup_cell = (originx + 1, originy + 1)
        elif boundary_region == 'B':
            lookup_cell = (originx + 1, y)
        elif boundary_region in ['BC', 'C', 'CD']:
            top_left_corner = vrg_areas_grid_corners[1]
            lookup_cell = (top_left_corner[0] + 1, top_left_corner[1] - 1)
        elif boundary_region == 'D':
            lookup_cell = (x, maxy - 1)
        elif boundary_region in ['DE', 'E', 'EF']:
            top_right_corner = vrg_areas_grid_corners[2]
            lookup_cell = (top_right_corner[0] - 1, top_right_corner[1] - 1)
        elif boundary_region == 'F':
            lookup_cell = (maxx - 1, y)
        elif boundary_region in ['FG', 'G', 'GH']:
            bottom_right_corner = vrg_areas_grid_corners[3]
            lookup_cell = (bottom_right_corner[0] - 1, bottom_right_corner[1] + 1)
        elif boundary_region == 'H':
            lookup_cell = (x, originy + 1)

    return [lookup_cell] + list(get_vrg_area_peril_grid_neighbours(lookup_cell, vrg_areas_grid))


def get_closest_vrg_area_to_location(record, vrg_areas):
    
    distances = [
        (area['area_peril_id'], area['xy'], get_distance(record, area)) for area in vrg_areas
    ]
    distances.sort(key=lambda t: t[2])
    min_dist_area_dist, min_dist_area_peril_id = distances[0][2], distances[0][0]

    return list(filter(lambda area: area['area_peril_id'] == min_dist_area_peril_id, vrg_areas))[0], min_dist_area_dist


def get_area_peril_id_based_on_CRSVG(record, areas):
    if record['geosch_1']=='CRSVG':
        try:
            area = next(a for a in areas if record['geoname_1'].upper() == a['area_level_6'].upper())
            if record['country'].upper() == area['area_level_1'].upper():
                return area['area_peril_id'], 'Mapped by VRG ID: {} : '.format(area['area_peril_id'])
            return None, "Given VRG ID is in another Country! found AreaPeril_ID '{}' : ".format(area['area_peril_id'])
        except StopIteration:
            return None, "'{}' is not a valid VRG ID / ".format(record['geoname_1'])

def get_area_peril_id_based_on_CRSL5(record, areas):
    if record['geosch_1'] =='CRSL5':
        try:
            area = next(a for a in areas if (record['geoname_1'].upper() == a['area_level_5'].upper()) and (
                        record['country'].upper() == a['area_level_1'].upper()))
            if record['country'].upper() == area['area_level_1'].upper():
                return area['area_peril_id'], 'Mapped by City name:  {} : '.format(area['area_peril_id'])
            return None, "Given City is in another Country! found AreaPeril_ID '{}' : ".format(area['area_peril_id'])
        except StopIteration:
            return None, "'{}' is not a valid City name in '{}' / ".format(record['geoname_1'], record['country'])

def get_area_peril_id_based_on_CRSL4(record, areas):
    if record['geosch_1']=='CRSL4':
        try:
            area = next(a for a in areas if (record['geoname_1'].upper() == a['area_level_4'].upper()) and (
                        record['country'].upper() == a['area_level_1'].upper()))
            if record['country'].upper() == area['area_level_1'].upper():
                return area['area_peril_id'], 'Mapped by Municipality ID: {} : '.format(area['area_peril_id'])
            return None, "Given Municipality is in another Country! found AreaPeril_ID '{}' : ".format(area['area_peril_id'])
        except StopIteration:
            return None, "'{}' is not a valid Municipality name in '{}' / ".format(record['geoname_1'], record['country'])

def get_area_peril_id_based_on_CRSL3(record, areas):
    if record['geosch_1']=='CRSL3':
        try:
            area = next(a for a in areas if (record['geoname_1'].upper() == a['area_level_3'].upper()) and (
                        record['country'].upper() == a['area_level_1'].upper()))
            if record['country'].upper() == area['area_level_1'].upper():
                return area['area_peril_id'], 'Mapped by CRESTA ID: {} : '.format(area['area_peril_id'])
            return None, "Given Cresta ID is in another Country! found AreaPeril_ID '{}' : ".format(area['area_peril_id'])
        except StopIteration:
            return None, "'{}' is not a valid CRESTA name in '{}' / ".format(record['geoname_1'], record['country'])

def get_area_peril_id_based_on_CRSL2(record, areas):
    if record['geosch_1']=='CRSL2':
        try:
            area = next(a for a in areas if (record['geoname_1'].upper() == a['area_level_2'].upper()) and (
                        record['country'].upper() == a['area_level_1'].upper()))
            if record['country'].upper() == area['area_level_1'].upper():
                return area['area_peril_id'], 'Mapped by Province ID: {} : '.format(area['area_peril_id'])
            return None, "Given Province ID is in another Country! found AreaPeril_ID '{} : '".format(area['area_peril_id'])
        except StopIteration:
            return None, " '{}' is not a valid Province name in '{}' / ".format(record['geoname_1'], record['country'])

def get_area_peril_id_based_on_CRSL1(record, areas):

        try:
            area = next(a for a in areas if record['geoname_1'].upper() == a['area_level_1'].upper())
            return area['area_peril_id'], 'Mapped by Country name:  {} : '.format(area['area_peril_id'])
        except StopIteration:
            return None, ' {} is not a valid Country name : '.format(record['country'])



def get_area_peril_id_based_on_lonlat(record, areas):
    # Find minimum distance
    area = min(areas, key=lambda a: get_distance(record, a))
    
    # Return if min distance is greater than 15
    if get_distance(record, area) >= 15:
        return None, ''

    if record['country'] == area['area_level_1']:
        return area['area_peril_id'], "Mapped by Lon/Lat to nearest VRG cell: '{}', with distance of: {1:.14}".format(area['area_peril_id'], get_distance(record, area))
    else:
        return None, "Given Lon/Lat is not in the Country! found AreaPeril_ID '{}'".format(area['area_peril_id'])


def get_area_peril_id_based_on_vrg_areas_grid(record, vrg_areas_grid, vrg_areas_grid_corners):
    
    loc_cell = record['gridxy']
    x, y = loc_cell

    lookup_cells = get_vrg_area_peril_grid_lookup_cells_for_location_cell(
        loc_cell, vrg_areas_grid, vrg_areas_grid_corners
    )
    lookup_areas = []

    for c in lookup_cells:
        lookup_areas += vrg_areas_grid[c]

    # No "closest" VRG areas to given location
    if not lookup_areas:
        return None, ''

    area, distance = get_closest_vrg_area_to_location(record, lookup_areas)

    if record['country'] == area['area_level_1']:
        return area['area_peril_id'], "Mapped by Lon/Lat to nearest VRG cell: '{}', with distance of: {} km".format(area['area_peril_id'], distance)
    else:
        return None, "Given Lon/Lat is not in the Country! found AreaPeril_ID '{}' :".format(area['area_peril_id'])


_AREA_PERIL_LOCATION_MAPPING_META = {
    1: {'agg_level': 'VRG', 'peril_lookup_basis': 'lonlat', 'peril_func': get_area_peril_id_based_on_vrg_areas_grid},
    2: {'agg_level': 'VRG', 'peril_lookup_basis': 'CRSVG', 'peril_func': get_area_peril_id_based_on_CRSVG},
    3: {'agg_level': 'AREA_LEVEL_5', 'peril_lookup_basis': 'CRSL5', 'peril_func': get_area_peril_id_based_on_CRSL5},
    4: {'agg_level': 'AREA_LEVEL_4', 'peril_lookup_basis': 'CRSL4', 'peril_func': get_area_peril_id_based_on_CRSL4},
    5: {'agg_level': 'AREA_LEVEL_3', 'peril_lookup_basis': 'CRSL3', 'peril_func': get_area_peril_id_based_on_CRSL3},
    6: {'agg_level': 'AREA_LEVEL_2', 'peril_lookup_basis': 'CRSL2', 'peril_func': get_area_peril_id_based_on_CRSL2},
    7: {'agg_level': 'AREA_LEVEL_1', 'peril_lookup_basis': 'CRSL1', 'peril_func': get_area_peril_id_based_on_CRSL1}
}



def fix_locations_by_dictionary(record, location_map):
    level = 0
    for i in range(2, 7):
        if record['geosch_1'] == _AREA_PERIL_LOCATION_MAPPING_META[i]['peril_lookup_basis']:
            level =i
            break
    if not level in (0,2):
        for row in location_map[_AREA_PERIL_LOCATION_MAPPING_META[level]['agg_level']]:
            if row['area_level_names'].upper() == record['geoname_1'].upper() and row['country_key'].upper() == record['country'].upper():
                record['geoname_1'] = row['area_level_model_names'].upper()
                break
    if level==0:
        record['geosch_1'] = 'CRSL1'
        record['geoname_1'] = record['country'].upper()

def get_area_peril_id(record, areas, vrg_areas_grid, vrg_areas_grid_corners):
    if not record['country']:
        return UNKNOWN_ID, 'The country code should not be empty!'
    message = ''
    valid_geoshc = 0
    level_priorities = sorted(_AREA_PERIL_LOCATION_MAPPING_META.keys())
    if not no_latlon(record) and valid_lonlat(record['longitude'], record['latitude']):
        peril_func = _AREA_PERIL_LOCATION_MAPPING_META[1]['peril_func']
        area_peril_id, mes = peril_func(record, vrg_areas_grid, vrg_areas_grid_corners)
        message += mes
        if area_peril_id:
            message = mes
            mapping_type = 'GRSVG'
            return area_peril_id, message, mapping_type
        else:
            message= ' No valid Lat/Lon  '
    for priority in level_priorities:
        if priority != 1:
            agg_level = _AREA_PERIL_LOCATION_MAPPING_META[priority]['agg_level']
            peril_func = _AREA_PERIL_LOCATION_MAPPING_META[priority]['peril_func']
            if _AREA_PERIL_LOCATION_MAPPING_META [priority]['peril_lookup_basis'] == record['geosch_1']:
                valid_geoshc=1
                sub_areas = list(filter(lambda area: area['aggregation_level'] == agg_level, areas))
                area_peril_id, mes = peril_func(record, sub_areas)
                if area_peril_id:
                    message += mes
                    mapping_type=record['geosch_1']
                    break
                else:
                    message = mes
                    record['geosch_1'] = 'CRSL1'; record['geoname_1'] = record['country'].upper()
                    peril_func = _AREA_PERIL_LOCATION_MAPPING_META[7]['peril_func']
                    sub_areas = list(filter(lambda area: area['aggregation_level'] == 'AREA_LEVEL_1', areas))
                    area_peril_id, mes = peril_func(record, sub_areas)
                    message += mes
                    mapping_type = 'CRSL1'
                    break
    if valid_geoshc==0:
        record['geosch_1'] = 'CRSL1'; record['geoname_1'] = record['country'].upper()
        peril_func = _AREA_PERIL_LOCATION_MAPPING_META[7]['peril_func']
        sub_areas = list(filter(lambda area: area['aggregation_level'] == 'AREA_LEVEL_1', areas))
        area_peril_id, mes = peril_func(record, sub_areas)
        message = " '{}' is not a valid GeoScheme ".format(record['geosch_1']) + mes
        mapping_type = 'CRSL1'
    return area_peril_id, message, mapping_type


def get_disaggregation(record, areas, mapping_type,ap_id):
    if mapping_type in ('CRSL2','CRSL3','CRSL4', 'CRSL5'):
        sub_areas = filter(lambda area: area['aggregation_level'] == 'VRG' and area['area_level_2']== record['geoname_1'], areas)
        tot_pop= sum(map(lambda a: a['population'], sub_areas))
        if tot_pop > 0.0:
            d_rows = map(lambda r: {
                    'weight': r ['population']/tot_pop,
                    'area_id': r ['area_peril_id']
            }, sub_areas)

            return d_rows
    elif mapping_type in ('CRSVG'):
        return [{'weight': 1, 'area_id': ap_id}]
    return []


def get_vulnerability_id(record, dict_vulnerabilities, vul_mappings, construction_class):
    construction_list = construction_class['OED']
    found_rec = [x for x in construction_list if x['class'] == record['constructioncode']]
    if found_rec:
        vulnerability_quality_code_1 = found_rec[0]['quality_code']
        structural_type = found_rec[0]['structural_type']
        structural_height = found_rec[0]['structural_height']
    else:
        vulnerability_quality_code_1 = 'NO BUILDING CLASS MATCH'
    #logging.exception("vulnerability_quality_code_1: {}".format(str(vulnerability_quality_code_1)))
    occupancyc_list = vul_mappings['OED']
    found_rec = [x for x in occupancyc_list if x['code'] == record['occupancycode']]
    if found_rec:
        RISK_CODE = found_rec[0]['risk_code']
        vulnerability_quality_code_2 = found_rec[0]['quality_code']
    else:
        vulnerability_quality_code_2 = 'NO OCCUPANCY CLASS MATCH'
    #logging.exception("vulnerability_quality_code_2: {}".format(str(vulnerability_quality_code_2)))
    icode = 1
    if vulnerability_quality_code_1 in  ['NO BUILDING CLASS', 'NO BUILDING CLASS MATCH']:
        if vulnerability_quality_code_2 in ['NO OCCUPANCY CLASS', 'NO OCCUPANCY CLASS MATCH']:
            icode = 0
        else:
            QUALITY_CODE = vulnerability_quality_code_2
            structural_type = 'XXX'
            structural_height = 'XX'
        #logging.exception("icode: {}".format(str(icode)))
    else:
        if vulnerability_quality_code_2 in ['NO OCCUPANCY CLASS', 'NO OCCUPANCY CLASS MATCH']:
            QUALITY_CODE = vulnerability_quality_code_1
            RISK_CODE = 'R'
        else:
            QUALITY_CODE = vulnerability_quality_code_1

    if icode != 0:
        code = '%s-EQ-%s-%s-%s-%s-%s' % (record['country'], RISK_CODE, record['coverage_type'],
                                     structural_type, structural_height, QUALITY_CODE)
        result_records = [x for x in dict_vulnerabilities if x['code'] == code]
        if not result_records:
            return -1, '. There is no Vul-ID for %s' % code
    else:
        return -1, '. There is no Building or occupancy class'
    #logging.exception("return: {}".format(str(result_records[0]['id'])))
    return result_records[0]['id'], ''
    

def get_area_peril_id_builder(match_func, found_message, not_found_message):
    def get_area_peril_id_with_match(record, areas):
        try:
            area = next(a for a in areas if match_func())
            return area['area_peril_id'], found_message
        except StopIteration:
            return None, not_found_message
    return get_area_peril_id_with_match


def get_distance(record, area):
    lon1, lat1 = record['longitude'], record['latitude']
    lon2, lat2 = area['lon'], area['lat']

    sPhi, sTeta = map(math.radians, [lat1, lon1])
    ePhi, eTeta = map(math.radians, [lat2, lon2])

    sX = EARTH_RADIUS * math.cos(sPhi) * math.cos(sTeta)
    sY = EARTH_RADIUS * math.cos(sPhi) * math.sin(sTeta)
    sZ = EARTH_RADIUS * math.sin(sPhi)
    eX = EARTH_RADIUS * math.cos(ePhi) * math.cos(eTeta)
    eY = EARTH_RADIUS * math.cos(ePhi) * math.sin(eTeta)
    eZ = EARTH_RADIUS * math.sin(ePhi)

    lengthxyz = math.sqrt((sX - eX)**2 + (sY - eY)**2 + (sZ - eZ)**2)
    return 2 * math.asin(lengthxyz / 2 / EARTH_RADIUS) * EARTH_RADIUS


def no_latlon(record):
    long_valid = math.isnan(record['longitude']) or record['longitude'] in [None, float('nan'), '',]
    lat_valid =  math.isnan(record['latitude']) or record['latitude'] in [None, float('nan'), '', ]
    return lat_valid and long_valid
