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
import uuid
from handle.handle import Handle
import random as r


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
            isFile = Handle.ValidateFile(str(file.filename), 'file')
            if not (isFile):
                basename = "images"
                suffix = datetime.datetime.now().strftime(
                    "%y%m%d_%H%M%S")
                # ext = get_mimetype(file.filename).split('/')
                #  (''.join(random.choice(string.ascii_uppercase)for i in range(10)))
                ext = file.mimetype.split('/')
                filePath = "_".join(
                    [basename, suffix, str(index+1), str(Config.generate_uuid())])+("."+ext[1])
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
            # else:
            #     return Handle.ValidateFile(str(file.filename))
        return data

    def generate_uuid():
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uuid_format = [8, 4, 4, 4, 12]
        for n in uuid_format:
            for i in range(0, n):
                random_string += str(
                    random_str_seq[r.randint(0, len(random_str_seq) - 1)])
            if n != 12:
                random_string += '-'
        return random_string
