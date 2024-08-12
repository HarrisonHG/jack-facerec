def CameraConnection(Camindex = 0):
	try:
		cap = cv2.VideoCapture(CAMINDEX)
		ret,frame = cap.read()
		#check if an image can be formed
		if not ret:
			raise ValueError("camera not responding")
	except ValueError as error:
		print("Camera is not valid, are you sure its plugged in or in use?")
		sys.exit(1)
	return cap
