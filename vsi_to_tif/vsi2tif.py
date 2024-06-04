vsi_path="D:\\test\\flow_3096_10ms\\录像_3096.vsi"
SOURCE_DIRECTORY = vsi_path
TARGET_DIRECTORY = vsi_path.split('.vsi')[0] + '\\'
import imagej
from os import listdir 
import numpy as np

ij = imagej.init(headless=False)

def convertImageToTif(image_name): 
    image_url = SOURCE_DIRECTORY + image_name
    save_url = TARGET_DIRECTORY + image_name.split('.vsi')[0] + '.tif'
    jimage = ij.io().open(image_url)
    ij.io().save(jimage, save_url)

files = np.array(listdir(SOURCE_DIRECTORY))
# files in source which contain ".vsi" 
files = files[np.flatnonzero(np.core.defchararray.find(files,'.vsi')!=-1)] 

for file in files: 
    convertImageToTif(file)