import cv2
import numpy as np

camera = cv2.VideoCapture(0)

def dedect():
    min = np.array([22, 50, 50])
    max = np.array([35, 255, 255])

    while True:
        ret, kare = camera.read()
        hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, min, max)
        final_pic = cv2.bitwise_and(kare, kare, mask=mask)
        cv2.imshow("final pic", final_pic)
        cv2.imshow(" mask", mask)
        cv2.imshow(" show", kare)

        kernel = np.ones((15, 15), dtype=np.float32) / 255
        smoothed = cv2.filter2D(final_pic, -1, kernel)
        cv2.imshow(" smothed", smoothed)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    dedect()
