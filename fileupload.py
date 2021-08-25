import os
import urllib.request

from django.contrib.auth.decorators import login_required

from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename


#file restrions add here
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
    '''check if the post request has the file  ,if your not added file method in body it will not work'''
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request , please enter file method'})
        resp.status_code = 400
        return resp
    # json file request calling here
    file = request.files['file']
    '''this condition is used for we are adding form data key but your not uploaded any file in body'''
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp

    '''we are calling extension file here ,config settings file, and once the body will contain varible name (file key)
            	value(pdf ,doc,,) this condition is work'''

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message' : 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        # this block is used for if file not in this format it will show this message
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp

if __name__ == "__main__":
    app.run()