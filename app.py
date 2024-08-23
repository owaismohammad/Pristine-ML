from flask import Flask,render_template,request,flash, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
from models import Model

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='3d6f45a5fc12445dbac2f59c3b6c7cb1'

model=Model()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error":"No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error":"No selected file"})
    if file and allowed_file(file.filename):
        file_bytes = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        prediction= process_data(image)
        return {"success":"successfully recieved", "prediction":prediction}
    elif file and not allowed_file(file.filename):
        return jsonify({"error":"Incorrect Format"})
    
@app.route('/test',methods=["POST"])
def test():
    data = request.json
    return process_test(data)

def process_test(data):
    new_name="new "+data["name"]
    new_age=data["age"]+2
    return jsonify({"name":new_name,"age":new_age}) 

def process_data(file_path):
    model.image_to_feature_vector(image_path=file_path)
    pred=model.image_prediction(image=model.image)
    return pred

if __name__ == '__main__':
    
  app.run(host="0.0.0.0", port=8080, debug=True)


    #In the above you can add ip address with the help of host='<ip_address>', port=8080



