# mjpeg_stream.py
import io
from picamera2 import Picamera2 
from flask import Flask, Response
import cv2

app = Flask(__name__)
#camera = cv2.VideoCapture(0)
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (960, 800)}))
camera.start()
"""
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')"""
               
def generate_frames():
    while True:
        frame = camera.capture_array()
        ret, buffer = cv2.imencode('.jpeg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
