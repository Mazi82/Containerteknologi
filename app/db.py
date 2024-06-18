from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

#MySQL Config
app.config ['MYSQL_DATABASE_USER'] = 'root'
app.config ['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config ['MYSQL_DATABASE_DB'] = 'Persons'
app.config ['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)