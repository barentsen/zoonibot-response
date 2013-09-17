#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Zoonibit's response functionality.
"""
from astropy.vo.client import conesearch
from astropy.vo.client.vos_catalog import VOSError
import numpy as np

sdss_typedefs = {0: 'unknowns',
                 1: 'cosmic rays',
                 3: 'galaxies',
                 4: 'ghosts',
                 6: 'stars'}

def count_unique(keys):
    """Identifies unique values and counts their occurences."""
    uniq_keys = np.unique(keys)
    bins = uniq_keys.searchsorted(keys)
    return uniq_keys, np.bincount(bins)

def myconesearch(ra, dec, sr, catname="SDSS DR8 - Sloan Digital Sky Survey Data Release 8 2"):
    try:
        response = conesearch.conesearch(ra, dec, sr, catalog_db=catname)
    except VOSError:
        return None
    return response.array    

def area_response(ra, dec, sr=0.01):
    data = myconesearch(ra, dec, sr)
    if data == None:
        return "There's nothing in this part of the sky."

    mask = (data['mode'] == 1)

    response = "I am Zoonibot. This area contains "

    mytypes, mycounts = count_unique(data[mask]['type'].data)
    contents = []
    for i in np.argsort(mycounts)[::-1]:
        contents.append("{0} {1}".format(mycounts[i],
                                         sdss_typedefs[mytypes[i]]))

    result = response+" and ".join(contents)+"."
    return result

if __name__ == '__main__':
    print zoonibot_area_response(4*15, +50, 0.01)