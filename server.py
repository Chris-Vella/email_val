from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
@app.route('/')
def index():
    query = "SELECT * FROM emaildb.email"
    email = mysql.query_db(query)
    return render_template('index.html', all_email = email)
@app.route('/email/<email_id>')
def show(email_id):
    query = "SELECT * FROM emaildb.email WHERE id = :specific_id"
    data = {'specific_id': email_id}
    email = mysql.query_db(query, data)
    return render_template('index.html', one_email=email[0])
@app.route('/email', methods=['POST'])
def create():
    query = "INSERT INTO emaildb.email (id,email,created_at,updated_at) VALUES (:id, :email, NOW(), NOW()"
    data = {
        "id": request.form["id"],
        "email": request.form["email"]
        }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
