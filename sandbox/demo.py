from astropy.vo.client import conesearch
import numpy as np

typedefs = {0: 'unknowns',
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
    
    response = conesearch.conesearch(4*15, +50, 0.01, catalog_db=catname)
    return response.array    


data = myconesearch(4*15, +50, 0.01)
mask = (data['mode'] == 1)

response = "Hi bro. I am Zoonibot. This area contains "

mytypes, mycounts = count_unique(data[mask]['type'].data)
contents = []
for i in np.argsort(mycounts)[::-1]:
    contents.append("{0} {1}".format(mycounts[i], typedefs[mytypes[i]]))

print response+" and ".join(contents)+"."
