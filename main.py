import os
import json
import requests
from http.client import HTTPException
from flask import Flask, jsonify, request, Blueprint
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import mysql.connector
app = Flask(__name__)
errors = Blueprint('errors', __name__)
# app.config['UPLOAD_FOLDER']
app.config['UPLOAD_FOLDER'] = 'static/files'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chullamane_learn"
)


def page_not_found(e):
    return jsonify({
        "message": "Page Not Found"
    }), 404


app.register_error_handler(404, page_not_found)
data = [
    {
        "id": 1,
        "frameworks": "Django",
        "year": 2005
    },
    {
        "id": 2,
        "frameworks": "Flas222k",
        "year": 2010
    },
    {
        "id": 3,
        "frameworks": "Web2Py",
        "year": 2007
    }
]


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    print(e)
    if isinstance(e, HTTPException):
        return e
    message = [str(x) for x in e.args]
    # now you're handling non-HTTP exceptions only
    return {
        "status": 500,
        # "message": message,
        "error":  e.args[0]
    }, 500

# @app.errorhandler(Exception)
# def handle_exception(error):
#     message = [str(x) for x in error.args]
#     # status_code = error.status_code
#     success = False
#     response = {
#         'success': success,
#         'error': {
#             'type': error.__class__.__name__,
#             'message': message
#         }
#     }
#     return jsonify(response), 500

# def handle_bad_request(e):
#     return 'bad request!', 400

# @app.errorhandler(Exception)
# def handle_unexpected_error(error):
#     # print(error.message)
#     status_code = 500
#     success = False
#     response = {
#         'success': success,
#         'error': {
#             'type': 'UnexpectedException',
#             'message': 'An unexpected error has occurred.'
#         }
#     }

#     return jsonify(response), status_code


@app.route('/', methods=['GET'])
def index():

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `manage_std` LIMIT 10")

    myresult = mycursor.fetchall()
    # jsonStr = json.dumps(myresult)

    # print(jsonStr)
    # print(type(myresult['id']))
    # for x in myresult:
    data = []
    for row in myresult:
        data.append(
            {
                "Id": row[0],
                "id_std": row[1],
                "branch": row[2],
                "name": row[3]
            }
        )

    # try:
    # response = requests.get("/", allow_redirects=True)
    test = request.form.get('test', type=int)
    files = request.files.getlist("file")
    for file in files:
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                  app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

    # if request.method == 'GET':
        # return jsonify(q)
    return respone(200, data, "", "")
    # except Exception as e:
    # message = [str(x) for x in e.args]
    # return message;
    # print(str(e))
    # return respone(500,"","",str(e)),500


def respone(status, data, msg, err):
    try:
        if err is None:
            raise Exception("Sorry, no numbers below zero")
        return {
            "data": data,
            "status": status,
            "message": msg,
        }, 200
    except Exception as e:
        return {
            "status": 500,
            "message": msg,
            "error": e
        }, 500


if __name__ == "__main__":
    app.run('0.0.0.0')
