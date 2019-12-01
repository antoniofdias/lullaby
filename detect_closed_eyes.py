from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from sys import exit

import paho.mqtt.client as mqtt
import mqtt_methods
import dlib
import time
import argparse
import imutils
import numpy as np
import cv2

host = "192.168.1.102"
port = "1883"
framesPassed = 0

client = mqtt.Client()
client.on_connect = mqtt_methods.on_connect
client.on_disconnect = mqtt_methods.on_disconnect

status = "awake"

try:
    client.connect(host, port)
except:
    print("Error has ocurred!")
    exit()

def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
 
	C = dist.euclidean(eye[0], eye[3])
 
	ear = (A + B) / (2.0 * C)
 
	return ear

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("data/shape_predictor.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 120

COUNTER = 0
TOTAL = 0

vs = VideoStream(src=0).start()

time.sleep(1.0)

client.loop_start()

while True:
    ++framesPassed

    frame = vs.read()
    frame = imutils.resize(frame, width = 450)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)

    for face in faces:    
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESH:
            COUNTER += 1
            
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "OLHOS FECHADOS", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                status = "asleep"
        else:
            COUNTER = 0
            status = "awake"

        cv2.putText(frame, "EAR: {:.2f}".format(ear), (500, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        if (framesPassed >=150):
            client.publish("status", status)


    cv2.imshow("Frame", frame)
 
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

client.loop_stop()

cv2.destroyAllWindows()
vs.stop()