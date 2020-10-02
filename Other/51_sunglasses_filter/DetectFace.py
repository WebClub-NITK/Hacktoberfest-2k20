import cv2
import dlib
import numpy as np
import sys


def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


def eye_on_mask(mask, side):
    points = [shape[i] for i in side]
    points = np.array(points, dtype=np.int32)
    mask = cv2.fillConvexPoly(mask, points, 255)
    return mask


def contouring(thresh, mid, img, right=False):
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    try:
        cnt = max(cnts, key=cv2.contourArea)
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        if right:
            cx += mid
        cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
    except:
        pass


detector = dlib.get_frontal_face_detector()
detector_file = 'facial_landmarks_detector.dat'
imgGlasses = cv2.imread('sunglasses.png')
imgGlassesGray = cv2.cvtColor(imgGlasses, cv2.COLOR_BGR2GRAY)
_, orig_mask = cv2.threshold(imgGlassesGray, 10, 255, cv2.THRESH_BINARY)


orig_mask_inv = cv2.bitwise_not(orig_mask)


imgGlasses = imgGlasses[:, :, 0:3]
origGlassesHeight, origGlassesWidth = imgGlasses.shape[:2]


predictor = dlib.shape_predictor(detector_file)

left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]

cap = cv2.VideoCapture(0)
ret, img = cap.read()
thresh = img.copy()

cv2.namedWindow('image')
kernel = np.ones((9, 9), np.uint8)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        mask = eye_on_mask(mask, left)
        mask = eye_on_mask(mask, right)
        mask = cv2.dilate(mask, kernel, 5)
        eyes = cv2.bitwise_and(img, img, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        xs = [v[0] for v in shape[36:48]]
        ys = [v[1] for v in shape[36:48]]
        buffer = 20
        min_x, max_x, min_y, max_y = min(xs)-buffer, max(xs)+buffer, min(ys)-buffer, max(ys)+buffer
#        cv2.rectangle(img, (min_x, min_y), (max_x+buffer, max_y+buffer), (0, 255, 0), 2)
        glassesWidth = max_x - min_x
        glassesHeight = max_y - min_y

        glasses = cv2.resize(imgGlasses, (glassesWidth, glassesHeight), interpolation=cv2.INTER_AREA)
        mask = cv2.resize(orig_mask, (glassesWidth, glassesHeight), interpolation=cv2.INTER_AREA)
        mask_inv = cv2.resize(orig_mask_inv, (glassesWidth, glassesHeight), interpolation=cv2.INTER_AREA)

        roi = img[min_y:max_y, min_x:max_x]

        roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        roi_fg = cv2.bitwise_and(glasses, glasses, mask=mask)

        dst = cv2.add(roi_bg, roi_fg)
        img[min_y:max_y, min_x:max_x] = dst

        # for (x, y) in shape[36:48]:
        #     cv2.circle(img, (x, y), 2, (255, 0, 0), -1)

    cv2.imshow('eyes', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


