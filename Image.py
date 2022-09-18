import cv2
cap0 = cv2.VideoCapture(0)




#assert ret0 # succeeds
ret1, frame1 = cap0.read()
#print(ret0)

cv2.imwrite('./c6.png',frame1)


cap0.release()