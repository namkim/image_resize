#!/usr/bin/python
from PIL import Image
import os
import shutil

path = "original_img/"
dirs = os.listdir( path )

resize_data = [
    {"folder_name": "battle", "width": 132, "length": 176},
    {"folder_name": "boss_battle", "width": 102, "length": 136},
    {"folder_name": "dual", "width": 60, "length": 158},
    {"folder_name": "gashapon", "width": 274, "length": 360},
    {"folder_name": "huge", "width": 648, "length": 853},
    {"folder_name": "large", "width": 274, "length": 365},
    {"folder_name": "levelup", "width": 82, "length": 109},
    {"folder_name": "medium", "width": 210, "length": 280},
    {"folder_name": "rankup", "width": 137, "length": 183},
    {"folder_name": "small", "width": 150, "length": 200},
    {"folder_name": "vertical", "width": 110, "length": 290},
]

for d in resize_data:
    # Delete the existing folder if it exists
    if os.path.isdir(d['folder_name']):
        shutil.rmtree(d['folder_name'])

    # create folder
    os.mkdir(d['folder_name'])

    # img resize
    for item in dirs:
        if os.path.isfile(path+item):
            print(path+item)
            im = Image.open(path+item)
            f, e = os.path.splitext(d['folder_name'] + "/" +item)
            imResize = im.resize((d['width'], d['length']), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
