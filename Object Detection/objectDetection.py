from picamera2 import Picamera2
import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import time
import socket
import os
from PIL import Image
from PIL import ImageFont, ImageDraw
import json

HOST = "192.168.1.4"
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


interpreter = tflite.Interpreter(model_path="detect.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

frame = picam2.capture_array()   
input_data = cv2.resize(frame, (300, 300))
input_data = np.expand_dims(input_data, axis=0).astype(np.uint8)

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

boxes = interpreter.get_tensor(output_details[0]['index'])[0]
classes = interpreter.get_tensor(output_details[1]['index'])[0]
scores = interpreter.get_tensor(output_details[2]['index'])[0]

detections = []
for i in range(len(scores)):
     if scores[i] > 0.5:
        ymin, xmin, ymax, xmax = boxes[i]
        detections.append({
             "class": int(classes[i]),
             "score": int(scores[i]),
             "box": [float(xmin), float(ymin), float(xmax), float(ymax)]
        })
        
print("Detections", detections)

sock.sendall(json.dumps(detections).encode('utf-8'))
sock.close()
