import json
from collections import defaultdict
#from tqdm import tqdm
import os
import sys
import random
import numpy as np

# convert each annotation to file

annotations_path = "../../datasets/cityscapes/Annotations/"
images_path = "../../datasets/cityscapes/images"
output_dir = "../"

# load dataset idxs and mappings
DIR = "../../datasets/cityscapes-maps"
with open(os.path.join(DIR, "labels_idx.json"), "r") as fh:
    labels_idx = json.load(fh)


with open(output_dir + "train.txt", "w") as of:
    for root, dirs, files in os.walk(annotations_path, topdown=False):
        for name in files:
            with open(os.path.join(root, name)) as fh:

                data = json.load(fh)
                data = data["objects"]

                if len(data) > 0:
                    first = True

                    for annotation in data:
                        try:
                            x1 = annotation["x1"]
                            x1 = np.clip(x1,0,2047)
                            y1 = annotation["y1"]
                            y1 = np.clip(y1,0,1023
                            x2 = x1 + annotation["w"]
                            x2 = np.clip(x2,0,2047)
                            y2 = y1 + annotation["h"]
                            y2 = np.clip(y2,0,1023)
                            
                            if x2 > x1 and y2 > y1:
                                label = labels_idx[annotation["label"]]
                                if first:
                                    of.write(name.replace("bounding_boxes.json", "leftImg8bit.png"))
                                    first = False
                                of.write(" " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "," + str(label))
                            else:
                                continue

                        except:
                            # skip this annotation if there is either no bbox or label
                            continue
                    if not first:
                        of.write("\n")
