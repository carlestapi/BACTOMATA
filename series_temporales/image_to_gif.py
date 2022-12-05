import glob
from PIL import Image

# filepaths
#fp_in = "/Users/carlestapi/Desktop/series temporales test/m-files/figures/rule30/*.png"
#fp_out = "/Users/carlestapi/Desktop/rule30_50.gif"

fp_in = "/Users/carlestapi/Desktop/ratioPlasmid/*.png"
fp_out = "/Users/carlestapi/Desktop/ratio_Plasmid.gif"


# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
img = next(imgs)  # extract first image from iterator
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=1000, loop=0)
