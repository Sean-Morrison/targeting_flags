import importlib.resources as resources
from astropy.table import Table
import os.path as ptt

def get_path(MAPPING_BASENAME='sdss5_target_with_groups.csv'):
    try:  # Python 3.9+
        path = resources.files('sdss_targeting_flags').joinpath('flags').joinpath(MAPPING_BASENAME)
        path = str(path)  # Convert to string if needed
    except AttributeError:  # Python 3.7 and 3.8
        with resources.path('sdss_targeting_flags', f'flags') as path_obj:
            path = ptt.join(str(path_obj),f'{MAPPING_BASENAME}')
    return(path)

def read(path):
    mapping = {}
    for row in Table.read(path):
        row_dict = dict(zip(row.colnames, row))
        mapping[row_dict["bit"]] = row_dict
    return mapping

