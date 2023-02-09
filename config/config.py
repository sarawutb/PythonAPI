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
from handle.handle import Handle
import datetime
import mimetypes
import random
import string

from handle.handle import Handle


class Config:
    def mySqlConnect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shop_product"
        )

    def UploadFile(app):
        filesName = []
        filesPathUrl = []
        data = ""
        files = request.files.getlist('file')
        for index, file in enumerate(files, start=0):
            if not (Handle.ValidateFile(str(file.filename), 'file')):
                basename = "images"
                suffix = datetime.datetime.now().strftime(
                    "%y%m%d_%H%M%S")  # e.g. 'mylogfile_120508_171442'
                # ext = get_mimetype(file.filename).split('/')
                ext = file.mimetype.split('/')
                filePath = "_".join(
                    [basename, suffix, str(index), (''.join(random.choice(string.ascii_lowercase)for i in range(10)))])+("."+ext[1])
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filePath))
                filesName.append(filePath)
                filesPathUrl.append(
                    request.url_root+str("/".join(["ViewImage", filePath])))
                # print(filesPath)
                data = {
                    "filesName": filesName,
                    "UrlPath": filesPathUrl,
                }
            else:
                return Handle.ValidateFile(str(file.filename))
        return data
