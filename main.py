import os
import json
import requests
from http.client import HTTPException
from flask import Flask, jsonify, request, Blueprint
from werkzeug.utils import secure_filename
import mysql.connector


app = Flask(__name__)
errors = Blueprint('errors', __name__)
app.config['UPLOAD_FOLDER'] = 'static/files'


dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop_product"
)

def page_not_found(e):
    return jsonify({
        "message": "Page Not Found"
    }), 404

app.register_error_handler(404, page_not_found)
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

@app.route('/', methods=['GET'])
def index():
    return respone(200,None, "Welcome API") 

@app.route('/AddProduct', methods=['POST'])
def AddProduct():
    mySqlConn = dbConn.cursor()
    sql = ("BEGIN;"
	"INSERT INTO product ( name_product, price_product, group_product, star_product, detail_product, qty_product, discount_product)"
	"VALUES"
	"( %s,%s,%s,%s,%s,%s,%s);"
	"INSERT INTO image_product ( flag, url_product_image, path_product_image,product_id)"
	"VALUES"
	"( %s,%s,%s,(SELECT id FROM product ORDER BY id DESC LIMIT 1));"
    "COMMIT;")
    val =  ( 
            request.form.get('name_product', type=str), 
            request.form.get('price_product', type=int), 
            request.form.get('group_product', type=int), 
            request.form.get('star_product', type=int), 
            request.form.get('name_product', type=str), 
            request.form.get('qty_product', type=int),  
            request.form.get('discount_product', type=float),  
            request.form.get('flag', type=int), 
            request.form.get('url_product_image', type=str), 
            request.form.get('path_product_image', type=str), 
        )
    mySqlConn.execute(sql, val, multi=True)
    multiSql = (mySqlConn.statement).split(";")

    check = 0
    for res in multiSql:
        mySqlConn.execute(res)
        if(mySqlConn.rowcount > 0):
            dbConn.commit()
            check = check + 1
    dbConn.commit()
    if (check == 2):
        return respone(200,None, "success")
    else:
        return respone(400,None, "failed")

@app.route('/GetProductAll', methods=['GET'])
def GetProductAll():
    # test = request.form.get('test', type=int)
    mySqlConn = dbConn.cursor()
    mySqlConn.execute("SELECT * FROM product a LEFT JOIN image_product b on a.id = b.product_id ORDER BY RAND()")
    myResult = mySqlConn.fetchall()
    data = []
    for row in myResult:
        data.append(
            {
                mySqlConn.column_names[0]: row[0],
                mySqlConn.column_names[1]: row[1],
                mySqlConn.column_names[2]: row[2],
                mySqlConn.column_names[3]: row[3],
                mySqlConn.column_names[4]: row[4],
                mySqlConn.column_names[5]: row[5],
                mySqlConn.column_names[6]: row[6],
                mySqlConn.column_names[8]: row[8],
                mySqlConn.column_names[9]: row[9],
                mySqlConn.column_names[10]: row[10],
                mySqlConn.column_names[11]: row[11],
            }
        )
    # test = request.form.get('test', type=int)
    return respone(200, data, "")

def respone(status, data, msg):
        return {
                "data": data,
                "status": status,
                "message": msg,
            }


if __name__ == "__main__":
    app.run('0.0.0.0')
