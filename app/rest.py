import pymysql
from app import app
from db import mysql
from flask import Flask, jsonify, request, abort

@app.route('/persons', methods=['POST'])
def create_person():
    connection = mysql.connect()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    request.method == 'POST'

    cursor.execute('INSERT INTO persons (name, age) values ("Arif", 28) ')
    connection.commit()

    cursor.execute("SELECT * FROM persons")
    connection.commit()

    rows = cursor.fetchall()
    
    resp = jsonify(rows)
    resp.status_code = 200

    return resp

@app.route('/persons', methods=['GET'])
def get_person():
    connection = mysql.connect()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    request.method == 'GET'

    cursor.execute("SELECT * FROM persons")
    connection.commit()

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')
