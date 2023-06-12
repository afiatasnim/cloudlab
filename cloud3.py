from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='project';
)

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the request
    username = request.form['username']
    password = request.form['password']

    # Insert the new user into the database
    cursor = db.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return 'Registration successful'

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    username = request.form['username']
    password = request.form['password']

    # Retrieve the user from the database
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()
    cursor.close()

    if user:
        return 'Login successful'
    else:
        return 'Invalid credentials'

if __name__ == '__main__':
    app.run()
