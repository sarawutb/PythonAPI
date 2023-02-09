import os
import json
import requests
from http.client import HTTPException
from flask import Flask, jsonify, request, Blueprint, abort
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
        # "msg": msg,
        "error":  error
    }, 500


@ app.route('/', methods=['GET'])
def index():
    return respone(200, None, "Welcome API")


@ app.route('/AddProduct', methods=['POST'])
def AddProduct():
    sql = ("BEGIN;"
           "INSERT INTO product ( name_product, price_product, group_product, star_product, detail_product, qty_product, discount_product)"
           "VALUES"
           "(%s,%s,%s,%s,%s,%s,%s);"
           "INSERT INTO image_product ( flag, url_product_image, path_product_image,product_id)"
           "VALUES"
           "(%s,%s,%s,(SELECT id FROM product ORDER BY id DESC LIMIT 1));"
           "COMMIT;")
    val = (
        Handle.Validate(request.form.get(
            'name_product', type=str), "name_product"),
        Handle.Validate(request.form.get(
            'price_product', type=str), "price_product"),
        Handle.Validate(request.form.get(
            'group_product', type=int), "group_product"),
        Handle.Validate(request.form.get(
            'star_product', type=int), "star_product"),
        Handle.Validate(request.form.get(
            'name_product', type=str), "name_product"),
        Handle.Validate(request.form.get(
            'qty_product', type=int), "qty_product"),
        Handle.Validate(request.form.get('discount_product',
                                         type=float), "discount_product"),
        Handle.Validate(request.form.get('flag', type=int), "flag"),
        Handle.Validate(request.form.get(
            'url_product_image', type=str), "url_product_image"),
        Handle.Validate(request.form.get(
            'path_product_image', type=str), "path_product_image"),
    )
    return serviceDatabase(sql, val, respone)


# @expects_json(schema, force=False)
@app.route('/GetProductAll', methods=['GET'])
@jwt_required()
def GetProductAll():
    # auth = request.headers.get("Authorization", None)
    # print(auth)
    # if not auth:
    sql = "SELECT * FROM product a LEFT JOIN image_product b on a.id = b.product_id ORDER BY RAND()"
    return serviceDatabase(sql, None, respone)


@app.route('/Register', methods=['POST'])
def Register():
    sql = ("BEGIN;"
           "INSERT INTO user (name_user,lname_user,password_user,email_user,flag_image)"
           "VALUES"
           "(%s,%s,%s,%s,%s);"
           "INSERT INTO image_product ( flag, path_product_image,product_id)"
           "VALUES"
           "(%s,%s,(SELECT id FROM product ORDER BY id DESC LIMIT 1));"
           "COMMIT;")
    val = (
        Handle.Validate(request.form.get('name_user', type=str), "name_user"),
        Handle.Validate(request.form.get(
            'lname_user', type=str), "lname_user"),
        Handle.Validate(request.form.get(
            'password_user', type=str), "password_user"),
        Handle.Validate(request.form.get(
            'email_user', type=str), "email_user"),
        Handle.Validate(request.form.get(
            'flag_image', type=int), "flag_image"),
        Handle.Validate(request.form.get(
            'flag_image', type=int), "flag_image"),
        Handle.Validate(request.form.get('path_product_image',
                        type=str), "path_product_image"),
    )
    return serviceDatabase(sql, val, respone)


@app.route('/UploadFile', methods=['POST'])
@jwt_required()
def UploadFile():
    filesName = []
    filesPath = []
    files = request.files.getlist('file')
    for index, file in enumerate(files, start=0):
        basename = "iamges"
        suffix = datetime.datetime.now().strftime(
            "%y%m%d_%H_%M_%S")  # e.g. 'mylogfile_120508_171442'
        ext = file.mimetype.split('/')
        randName = ''.join(random.choice(string.ascii_lowercase)
                           for i in range(20))
        filename = "_".join([basename, suffix])
        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename+"_"+randName+"_"+str(index)+"."+ext[1]))
        filesName.append
    return ""
    # file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
    #           app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file


# def guess_type(filename, buffer=None):
#     mimetype, encoding = mimetypes.guess_type(filename)
#     if mimetype is None:
#         try:
#             import magic
#             if buffer:
#                 mimetype = magic.from_buffer(buffer, mime=True)
#             else:
#                 mimetype = magic.from_file(filename, mime=True)
#         except ImportError:
#             pass
#     # return mimetype
#     print(mimetype)


def respone(status, data, msg):
    respone = {
        "data": data,
        "status": status,
        "msg": msg,
    }
    return respone


def serviceDatabase(sql, val, respone):
    data = []
    mySqlConn = dbConn.cursor()
    for result in mySqlConn.execute(sql, val, multi=True):
        if result.with_rows:
            for rows in result.fetchall():
                jsonData = {}
                for index, row in enumerate(rows, start=0):
                    jsonData = dict(
                        jsonData, **{mySqlConn.column_names[index]: rows[index]})
                data.append(jsonData)
        print("SQL : '{}'".format(
            result.statement))
    dbConn.commit()
    return respone(200, data, None)


if __name__ == "__main__":
    app.run('0.0.0.0')
