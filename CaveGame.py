import cv2

print("All you hear is rumbling, you fall into the ground.\n")
titleimg = cv2.imread('title.png')
cv2.imshow('title', titleimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
