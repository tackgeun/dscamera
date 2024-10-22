import cv2

from dscamera import DSCamera

for (json_file, img_size) in [("./calibration_zoomin.json", (600, 600)), ("./calibration_zoomout.json", (600,960))]:
    cam = DSCamera(json_file)
    for i in range(0, 3):
        img = cv2.imread(f"sample{i}.png")
        perspective = cam.to_perspective(img, img_size=img_size)
        if 'in' in json_file:
            cv2.imwrite(f'zoomin_perspective{i}.png', perspective)
        else:
            cv2.imwrite(f'zoomout_perspective{i}.png', perspective)

