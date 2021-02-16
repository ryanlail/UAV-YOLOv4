import json
from collections import defaultdict
from tqdm import tqdm
import os
import sys

# convert each annotation to file

annotations_path = sys.argv[1]
images_path = sys.argv[2]
output_file = sys.argv[3]

for root, dirs, files in os.walk(annotations_path, topdown=False):
    for name in files:
        with open(os.path.join(root, name)) as fh:
            data

