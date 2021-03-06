import json
from collections import defaultdict
from tqdm import tqdm
import os
import sys
import random

# convert each annotation to file

annotations_path = "../../datasets/Durham-Versailles/Annotations/"
images_path = "../../datasets/Durham-Versailles/images"
output_dir = "../"

tags = dict()
class_count = 0

with open(output_dir + "train.txt", "w") as tr:
    with open(output_dir + "val.txt", "w") as vl:

        for root, dirs, files in os.walk(annotations_path, topdown=False):
            for name in tqdm(files):

                if random.randint(0,10) < 2:
                    of = vl
                else:
                    of = tr

                with open(os.path.join(root, name)) as fh:

                    data = json.load(fh)
                    data = data[0]["annotation"]

                    if len(data) > 0:
                        of.write(name.replace("json", "png"))

                        for annotation in data:
                            try:
                                # x1, y1, w, h
                                x1 = annotation["bbox"][0]
                                y1 = annotation["bbox"][1]
                                x2 = x1 + annotation["bbox"][2]
                                y2 = y1 + annotation["bbox"][3]

                                tag = annotation["tags"][0]
                                
                                if not tags.get(tag):
                                    tags[tag] = class_count
                                    class_count += 1
                                
                                label = tags.get(tag)

                                of.write(" " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "," + str(label))

                            except:
                                pass
                        of.write("\n")
print(len(tags))

with open(output_dir + "classes.json", "w") as fh:
    json.dump(tags, fh)

