#import tqdm
import json
import os

image_width = 1024
image_height = 544


# load dataset idxs and mappings
DIR = "../datasets/Durham-Versailles-Maps"
with open(os.path.join(DIR, "labels_idx.json"), "r") as fh:
    labels_idx = json.load(fh)
inv_labels = {v: k for k, v in labels_idx.items()}

with open("preds.json") as fh:
    preds = json.load(fh)

with open("gts.json") as fh:
    gts = json.load(fh)

# create detection files

for img_id, _ in enumerate(preds):
    img_pred = preds[img_id]["pred"][0]
    with open("../Object-Detection-Metrics/detections/" + str(img_id) + ".txt", "a") as fh:
        for pred_n, _ in enumerate(img_pred):
            output = inv_labels[int(img_pred[pred_n][6])].replace(" ", "-") + " " + str(img_pred[pred_n][5]) + " " + str(img_pred[pred_n][0] * image_width) + " " + str(img_pred[pred_n][1] * image_height) + " " + str(img_pred[pred_n][2] * image_width) + " " + str(img_pred[pred_n][3] * image_height)
            fh.write(output + "\n")

for img_id, _ in enumerate(gts):
    img_gt = gts[img_id]
    # x1, y1, w, h
    with open("../Object-Detection-Metrics/groundtruths/" + str(img_id) + ".txt", "a") as fh:
        for gt_n, _ in enumerate(img_gt["boxes"]):
            output = inv_labels[int(img_gt["labels"][gt_n])].replace(" ", "-") + " " + str(img_gt["boxes"][gt_n][0]) + " " + str(img_gt["boxes"][gt_n][1]) + " " + str(img_gt["boxes"][gt_n][0] + img_gt["boxes"][gt_n][2]) + " " + str(img_gt["boxes"][gt_n][1] + img_gt["boxes"][gt_n][3])
            fh.write(output + "\n")

