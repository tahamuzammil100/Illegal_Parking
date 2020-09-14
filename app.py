from detection_video_vinothcopy import task

from flask import Flask, render_template, Response,request,json,jsonify,make_response

app = Flask(__name__)
@app.route('/')
def index():
    task("images/parking.mp4","MobileNetSSD.prototxt.txt","NetSSD.caffemodel")

if __name__ == '__main__':
    app.run(debug=True)