# geotiffmerge
Functions to merge geo-referenced TIF raster files while maintaining the geo-referencing metadata and colour palette.

Functions:
==========
create_merged_array           - Opens several raster files and merge them into a numpy array, storing the metadata/tags
create_world_file             - Takes the geotransformation information and write a .tfw file matching the .tif
search_for_worldfile(path)    - Performs case insensitive search for a matching world file
merge_rasters                 - Reads on-disk input rasters, merge them, and writes the output
plot_disk_raster              - Opens a raster file on disk, prints its metadata, and plots it (doesn't support color palette)
