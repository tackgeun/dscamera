import cv2

from dscamera import DSCamera

for (json_file, img_size) in [("./calibration_zoomin_left.json", (600, 1200)), ("./calibration_zoomin.json", (600,1200)), ("./calibration_zoomin_right.json", (600,1200))]:

    cam = DSCamera(json_file)
    for i in range(0, 3):
        img = cv2.imread(f"sample{i}.png")
        perspective = cam.to_perspective(img, img_size=img_size)
        if 'left' in json_file: # cx = center (1/2 width) - shift (1/8 width)
            cv2.imwrite(f'zoomin_perspective{i}_left.png', perspective)
        elif 'right' in json_file: # cx = center (1/2 width) + shift (1/8 width)
             cv2.imwrite(f'zoomin_perspective{i}_right.png', perspective)
        else: # alined at center cx = center (1/2 width)
            cv2.imwrite(f'zoomin_perspective{i}_center.png', perspective)

