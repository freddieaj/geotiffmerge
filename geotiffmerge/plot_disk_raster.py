import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

def plot_disk_raster(raster_path):
    """Open a raster file on disk, print its metadata, and plot it"""
    
    plt.figure(figsize=(32, 16), dpi=80)
    raster = rasterio.open(raster_path)
    print(raster.meta.copy())
    show(raster, cmap='gray_r')
    raster.close()