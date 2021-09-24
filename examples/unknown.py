import cv2


cc1 = cv2.imread('creditcard_digits1.jpg', 0)
cv2.imshow("Digits 1", cc1)
cv2.waitKey(0)
cc2 = cv2.imread('creditcard_digits2.jpg', 0)
cv2.imshow("Digits 2", cc2)
cv2.waitKey(0)
cv2.destroyAllWindows()
