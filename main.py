import os
import json
import requests
from http.client import HTTPException
from flask import Flask, jsonify, request, Blueprint, abort, send_file
from werkzeug.utils import secure_filename
import mysql.connector
from flask_expects_json import expects_json
from werkzeug.exceptions import Unauthorized
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv, find_dotenv
from config.config import Config
from handle.handle import Handle
from controller.controller import Controller
import datetime
import mimetypes
import random
import string


load_dotenv(find_dotenv())
app = Flask(__name__)
errors = Blueprint('errors', __name__)
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")  # Change this!
jwt = JWTManager(app)
dbConn = Config.mySqlConnect()

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["email"]
}

app.register_error_handler(405, Handle.method_not_allowed)
app.register_error_handler(404, Handle.page_not_found)
app.register_error_handler(400, Handle.handle_bad_request)


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    error = [str(x) for x in e.args]
    return {
        "status": 500,
        "error":  error
    }, 500


@app.route('/', methods=['GET'])
def index():
    return jsonify(msg="Welcome API")


@app.route('/AddProduct', methods=['POST'])
def AddProduct():
    return Controller.AddProduct(app=app)


# @expects_json(schema, force=False)
@app.route('/GetProductAll', methods=['GET'])
# @jwt_required()
def GetProductAll():
    return Controller.GetProductAll()


@app.route('/Login', methods=['POST'])
def Login():
    return Controller.Login()


@app.route('/Register', methods=['POST'])
def Register():
    return Controller.Register(app=app)


@app.route('/ViewImage/<FileName>', methods=['GET'])
def ViewImage(FileName):
    return Controller.ViewImage(app=app, FileName=FileName)


@app.route('/UploadFile', methods=['POST'])
@jwt_required()
def UploadFile():
    return Controller.UploadFile(app)


if __name__ == "__main__":
    app.run('0.0.0.0')
