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


class Handle:
    def page_not_found(e):
        return jsonify(msg="Page Not Found"), 404

    def handle_bad_request(e):
        json_str = str(e).split(":")
        if (len(json_str) > 2):
            data = (json_str[1].replace(" ", "")+":" +
                    (json_str[2].replace(" ", "")).replace("'", "")
                    ).replace("'", '"')
            return jsonify(status=400, request=json.loads(data), msg="Validate "+json_str[0]), 400
        return jsonify(msg="400 Bad Request"), 400

    def handle_bad_request(e):
        json_str = str(e).split(":")
        if (len(json_str) > 2):
            data = (json_str[1].replace(" ", "")+":" +
                    (json_str[2].replace(" ", "")).replace("'", "")
                    ).replace("'", '"')
            return jsonify(status=400, request=json.loads(data), msg="Validate "+json_str[0]), 400
        return jsonify(msg="400 Bad Request"), 400

    def method_not_allowed(e):
        return jsonify(msg="Method Not Allowed"), 405

    def Validate(validate, paramsName):
        print(paramsName)
        if validate == None or validate == "" or paramsName == None:
            return abort(400, {
                paramsName: 'null',
            })
        else:
            return validate

    def ValidateFile(validate, paramsName):
        if str(validate) == None or str(validate) == "" or paramsName == None:
            return abort(400, {
                paramsName: 'null',
            })
        else:
            return
