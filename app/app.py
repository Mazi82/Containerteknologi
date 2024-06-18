from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    connection = MySQLdb.connect(
        host='mysql',
        user='root',
        password='root',
        database='flaskdb'
    )
    return connection

@app.route('/persons', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data['name']
    age = data['age']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO persons (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cursor.close()
    conn.close()
    return 'Person added!', 201

@app.route('/persons', methods=['GET'])
def get_persons():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, age FROM persons")
    persons = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(persons)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
