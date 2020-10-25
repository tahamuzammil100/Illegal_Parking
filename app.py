from python_new import task

from flask import Flask, render_template, Response,request,json,jsonify,make_response

app = Flask(__name__)
@app.route('/')
def index():
    
    x=Response(task("images/parking.mp4","MobileNetSSD.prototxt.txt","NetSSD.caffemodel"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    return  x
if __name__ == '__main__':
    app.run(debug=True)