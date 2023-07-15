import numpy as np
import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (80, 25),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Mercury",
    (123, 190),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Venus",
    (195, 175),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Earth",
    (287, 175),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Mars",
    (385, 175),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Jupiter",
    (525, 60),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Saturn",
    (780, 120),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Uranus",
    (960, 140),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)
cv2.putText(
    img,
    "Neptune",
    (1107, 145),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255, 255, 255)
)

# cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.imshow("Display Image", img)
cv2.waitKey(0)
