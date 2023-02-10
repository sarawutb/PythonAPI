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
from service.service import Service
from datetime import datetime, timedelta
import mimetypes
import random
import string
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 60 minutes


class Controller():
    def respone(status, data, msg):
        respone = {
            "data": data,
            "status": status,
            "msg": msg,
        }
        return respone, status

    def AddProduct(app):
        flag = Handle.Validate(request.form.get(
            'flag', type=int), "flag")
        sql = ("BEGIN;\
                INSERT INTO product ( name_product, price_product, group_product, star_product, detail_product, qty_product, discount_product) VALUES (%s,%s,%s,%s,%s,%s,%s);\
                SELECT id FROM product ORDER BY id DESC LIMIT 1;\
                COMMIT;")
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
        )
        file = request.files.getlist('file')
        if (len(file) < 1 and file[0].filename == ""):
            Handle.Validate("", "file")
        else:
            data = Service.serviceDB(sql, val)
            id = [i for i in data[0].values()]
            if (flag == 1):
                fileUpload = Config.UploadFile(app)
                imagePaths = [i for i in fileUpload.values()]
                print(imagePaths)
                # path_product_image = Handle.Validate(request.form.get(
                #     'path_product_image', type=str), "path_product_image")
                for index, imagePath in enumerate(imagePaths):
                    sql = ("INSERT INTO image_product ( flag, path_product_image,product_id)"
                           "VALUES"
                           "(%s,%s,%s);")
                    val = (flag, imagePath[index], id[0])
                    Service.serviceDB(sql, val)
            elif (flag == 2):
                url_product_image = Handle.Validate(request.form.get(
                    'url_product_image', type=str), "url_product_image")
                for imagesUrl in url_product_image.split(","):
                    sql = ("INSERT INTO image_product ( flag, url_product_image,product_id)"
                           "VALUES"
                           "(%s,%s,%s);")
                    val = (flag, imagesUrl, id[0])
                    Service.serviceDB(sql, val)
        return Controller.respone(status=200, data=id, msg="success")

    def Login():
        sql = "SELECT * FROM user WHERE email_user = %s AND password_user = %s"
        val = (Handle.Validate(request.form.get('email', type=str), "email"), Handle.Validate(request.form.get(
            'password', type=str), "password"))
        access_token = (
            {
                "token": create_access_token(identity=Handle.Validate(request.form.get('email', type=str), "email"), expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
            })
        jsonData = {}
        data = Service.serviceDB(sql, val)
        jsonData = dict(
            data[0], **access_token)
        if (len(data) > 0):
            return Controller.respone(status=200, data=jsonData, msg="success")
        else:
            return Controller.respone(status=401, data=data, msg="Email or password is incorrect.")

    def Register(app):
        fileUpload = Config.UploadFile(app)
        imagePath = [i for i in fileUpload.values()]
        sql = ("BEGIN;"
               "INSERT INTO user (name_user,lname_user,password_user,email_user)"
               "VALUES"
               "(%s,%s,%s,%s);"
               "INSERT INTO image_user ( url_product_image,user_id)"
               "VALUES"
               "(%s,(SELECT id FROM user ORDER BY id DESC LIMIT 1));"
               "COMMIT;")
        val = (
            Handle.Validate(request.form.get(
                'name_user', type=str), "name_user"),
            Handle.Validate(request.form.get(
                'lname_user', type=str), "lname_user"),
            Handle.Validate(request.form.get(
                'password_user', type=str), "password_user"),
            Handle.Validate(request.form.get(
                'email_user', type=str), "email_user"), str(imagePath[1][0]),
        )
        data = Service.serviceDB(sql, val)
        return Controller.respone(status=200, data=data, msg="success")

    def ViewImage(FileName, app):
        filePath = "/".join([app.config['UPLOAD_FOLDER'], FileName])
        if (os.path.exists(filePath)):
            type = Controller.get_mimetype(FileName)
            print(type)
            return send_file(filePath, mimetype=type)
        else:
            return Controller.respone(404, None, "Not Found Iamges : "+FileName)

    def GetProductAll():
        groupProduct = request.args.get('groupProduct', type=str)
        sql = "SELECT * FROM product a\
        LEFT JOIN image_product b on a.id = b.product_id"
        if (groupProduct != None):
            sql += " WHERE group_product = "+groupProduct
        sql += " ORDER BY RAND()"
        data = Service.serviceDB(sql, None)
        return Controller.respone(status=200, data=data, msg="success")

    def UploadFile(app):
        data = Config.UploadFile(app)
        return Controller.respone(200, data, "Uplaad file success")

    def get_mimetype(filename, buffer=None):
        mimetype, encoding = mimetypes.guess_type(filename)
        if mimetype is None:
            try:
                import magic
                if buffer:
                    mimetype = magic.from_buffer(buffer, mime=True)
                else:
                    mimetype = magic.from_file(filename, mime=True)
            except ImportError:
                pass
        return mimetype
