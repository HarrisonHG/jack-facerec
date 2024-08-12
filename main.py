import cv2
#get webcam
cap = cv2.VideoCapture(0)
while True:
	q , frame = cap.read()
	
	cv2.imshow("window",frame)
	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
quit()
