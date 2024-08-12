import cv2, face_recognition, pickle
#get webcam
cap = cv2.VideoCapture(0)
encodings = []
names = []	
while True:
	ret, frame = cap.read()
	
	
	#shows the image
	cv2.imshow("window",frame)
	#quit if q is pressed
	x = cv2.waitKey(1)
	if  x == ord("q"):
		break
	elif x == ord("p"):
		rgbimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		boxes = face_recognition.face_locations(frame)
		encodings.append(face_recognition.face_encodings(rgbimage,boxes))
		names.append(input("input name"))
cv2.destroyAllWindows()
with open("encodings.pickle","wb") as f:
	pickle.dump(encodings, f)
	f.close()
with open("names.pickle","wb") as f:
	pickle.dump(names, f)
	f.close()
quit()
