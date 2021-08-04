import rasterio
import numpy as np
from affine import Affine
from rasterio.merge import merge

def create_merged_array(*infiles):
    """Open several raster files and merge them into a new array"""

    raster_list = [rasterio.open(i) for i in infiles]
    
    #merge the rasters
    merged_array, out_trans = rasterio.merge.merge(raster_list)
    
    # find the most north-westerly xy coords in the metadata of the inputs
    new_x = min([i.meta['transform'][2] for i in raster_list])
    new_y = max([i.meta['transform'][5] for i in raster_list])

    # update the metadata with the new xy coords and the height and width
    meta = raster_list[0].meta.copy()
    meta.update({"driver": "GTiff",
                 "height": merged_array.shape[1],
                 "width": merged_array.shape[2],
                 "transform": Affine(meta['transform'][0], meta['transform'][1], new_x, meta['transform'][3], meta['transform'][4], new_y)})

    tags = raster_list[0].tags()
    return merged_array, meta, tags