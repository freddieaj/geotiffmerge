import os

def create_world_file(savepath, geotrans):
    dir, filename_and_ext = os.path.split(savepath)
    filename, extension = os.path.splitext(filename_and_ext)
    world_file_path = os.path.join(dir, filename) + ".tfw"
    with open(world_file_path, "w") as writer:
        xscale,xskew,xoff,yskew,yscale,yoff = geotrans
        writer.write("\n".join([xscale,yskew,xskew,yscale,xoff,yoff]))
    return