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
import datetime
import mimetypes
import random
import string
dbConn = Config.mySqlConnect()


class Service:

    def serviceDB(sql, val):
        data = []
        mySqlConn = dbConn.cursor()
        # try:
        for result in mySqlConn.execute(sql, val, multi=True):
            # print(result.with_rows)
            if result.with_rows:
                for rows in result.fetchall():
                    jsonData = {}
                    for index, row in enumerate(rows, start=0):
                        jsonData = dict(
                            jsonData, **{mySqlConn.column_names[index]: rows[index]})
                    data.append(jsonData)
                print("SQL : '{}'".format(
                    result.statement.encode('utf-8')))
            else:
                print("SQL : '{}'".format(
                    result.statement.encode('utf-8')))
        # except:
        #     pass
        dbConn.commit()
        return data
