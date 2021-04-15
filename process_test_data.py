import tqdm
import json

image_width = 1024
image_height = 544


with open("classes.json") as fh:
    labels = json.load(fh)

with open("preds.json") as fh:
    preds = json.load(fh)

with open("gts.json") as fh:
    gts = json.load(fh)

# create detection files

for img_id, _ in enumerate(preds):
    img_pred = preds[img_id]
    with open("../Object-Detection-Metrics/detections/" + str(img_id) + ".txt", "a") as fh:
        for pred_n, _ in enumerate(img_pred["boxes"]):
            output = labels_map[img_pred["labels"][pred_n]] + " " + str(img_pred["scores"][pred_n]) + " " + str(img_pred["boxes"][pred_n][0]) + " " + str(img_pred["boxes"][pred_n][1]) + " " + str(img_pred["boxes"][pred_n][2]) + " " + str(img_pred["boxes"][pred_n][3])
            fh.write(output + "\n")

for img_id, _ in enumerate(gts):
    img_gt = gts[img_id]
    with open("../Object-Detection-Metrics/groundtruths/" + str(img_id) + ".txt", "a") as fh:
        for gt_n, _ in enumerate(img_gt["boxes"]):
            output = labels_map[img_gt["labels"][gt_n]] + " " + str(img_gt["boxes"][gt_n][0]) + " " + str(img_gt["boxes"][gt_n][1]) + " " + str(img_gt["boxes"][gt_n][2]) + " " + str(img_gt["boxes"][gt_n][3])
            fh.write(output + "\n")

