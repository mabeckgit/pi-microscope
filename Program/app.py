#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request

from Controller import Controller

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

# Setup motor controller
ctrl = Controller()

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/link1')
def link1():
    """Testing a link"""
    print("Link 1 was clicked")
    return render_template('index.html')


@app.route('/ajax', methods=['POST'])
def ajax():
    """Testing AJAX"""
    print("AJAX received")
    print(request.form["Button"])
    ctrl.readCommand(request.form["Button"])
    return Response("server response")


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
