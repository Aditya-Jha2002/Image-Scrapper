import os
import glob
from tqdm import tqdm
from PIL import Image, ImageFile
from joblib import Parallel, delayed

#ImageFile LOAD_TRUNCATED_IMAGES = True


def resize_image(image_path,output_folder, resize):
    base_name = os.path.basename(image_path)
    outpath = os.path.join(output_folder,base_name)
    img = Image.open(image_path)
    img = img.resize(
        (resize[1], resize[0]), resample=Image.BILINEAR
    )
    img.save(outpath)

os.mkdir(os.path.join(os.getcwd(),'instruments224'))

input_folder = os.path.join(os.getcwd(),'instruments')
output_folder = os.path.join(os.getcwd(),'instruments224')

images = glob.glob(os.path.join(input_folder, "*.jpg"))
#Parallel(n_jobs=12)(
    #delayed(resize_image)(
        #i,
        #output_folder,
        #(224, 224),
    #)for i in tqdm(images)
#)
for i in images:
    resize_image(i,output_folder,(224, 224))
