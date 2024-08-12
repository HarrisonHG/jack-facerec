import cv2, face_recognition
#get webcam
cap = cv2.VideoCapture(0)
while True:
	q , frame = cap.read()
	#detect the faces
	for top,right,bottom,left in face_recognition.face_locations(frame):
		
		#draw rectangle around faces
		cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0), 5) 
	
	
	
	
	#shows the image
	cv2.imshow("window",frame)
	#quit if q is pressed
	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
quit()
