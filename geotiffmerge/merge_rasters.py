import rasterio
import numpy as np
from affine import Affine
import PIL
import os
import matplotlib.pyplot as plt
from .create_merged_array import create_merged_array
from .create_world_file import create_world_file

def search_for_worldfile(path):
    # A function to perform case insensitive search for the matching world file
    
    directory, filename = os.path.split(path)
    filename_worldfile = filename.split('.')[:-1][0] + '.tfw'
    directory, filename_worldfile = (directory or '.'), filename_worldfile.lower()
    for f in os.listdir(directory):
        newpath = os.path.join(directory, f)
        if os.path.isfile(newpath) and f.lower() == filename_worldfile:
            return newpath
        
def merge_rasters(outfile, *infiles):
    # A function to read on-disk input rasters, merge them, and write the output
                     
    # Read the metadata tags into a dict
    raw_tags = dict(PIL.Image.open(infiles[0]).tag.items())

    # Read the colour palette
    col_palette = PIL.Image.open(infiles[0]).getpalette()
    
    #Create the merged array and its transform coefficients
    merged_array, meta, tags = create_merged_array(*infiles)
    new_img = PIL.Image.fromarray(merged_array[0])
    new_img.putpalette(col_palette)
    transform_coeffs_new = [str(i) for i in meta['transform']][0:6]
    
    # Edit the shape tags
    raw_tags[256] = (merged_array.shape[2],)
    raw_tags[257] = (merged_array.shape[1],)

    # Save the new raster and world file
    new_img.save(outfile, tiffinfo=raw_tags)
    out_worldfile = '.'.join(outfile.split('.')[:-1]) + '.tfw'
    create_world_file(out_worldfile, transform_coeffs_new)

    return 