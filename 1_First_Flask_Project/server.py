### This is the first example, the requisitions are passed
# directly at the navegator, where we passs '...:5000/req'
# accordingly to the pre-defined @app.route('/req')

# pip install flask

from flask import Flask, request, Response, g
import sqlite3
# creating the app:
app = Flask(__name__)

# path to the database:
DB_URL = 'enterprise.db'

# security step: passing login and password to access the API
# USERS: only users that are allowed to access the data
users = [
            {'username': 'Ananda', 'secret': '@admin1'},
            {'username': 'Math', 'secret': '@admin2'}
        ]

# Adding a flask decorator: before_request
### This means that the first that will be
### executed before any request if the function below!
@app.before_request
def before_request():
    print('Connecting to the database...')
    conn = sqlite3.connect(DB_URL)
    g.conn = conn

# this decorator says that it will execute the
# function below with or without error
@app.teardown_request
def after_request(exception):
    if g.conn is not None:
        g.conn.close()
        print('Closing database connection...')

# creating a method that authenticates the user:
def check_user(username, secret):
    for user in users:
        if user['username'] == username and user['secret'] == secret:
            return True
        else:
            return False

# To make the requisition, we use the decorator:
@app.route("/")
def home():
    return "<h1>Home Page: Ananda Coelho :) </h1>"
    # passing the header that will be at the home page


# This method passes the data from the employees when called
@app.route("/employees")
def get_employees():

    query = """
            SELECT name, position, pay
            FROM employees;
    """
    # g.conn is always created in "after_request" function
    cursor = g.conn.execute(query)
    employers_dict = [
                       {'name': row[0],
                       'position': row[1],
                       'pay': row[2]}
            for row in cursor.fetchall()
    ]

    print(employers_dict)
    return {'employees': employers_dict}


# This method filters the position of the employees depending on the route passed at the URL
@app.route('/employees/<position>')
def get_employees_position(position):
    out_employees = []
    for employee in employees:
        if position.lower() == employee['position'].lower():
            out_employees.append(employee)
    return {'employees': out_employees}


# This last method filters the employees accordingly to some info from the dict
# and a value (e.g. /position/analist)
@app.route('/employees/<info>/<value>')
def get_employees_info(info, value):
    out_employees = []
    for employee in employees:
        if info in employee.keys():
            value_employee = employee[info]
            if type(value_employee) == str:
                if value.lower() == value_employee.lower():
                    out_employees.append(employee)
            elif type(value_employee) == int:
                if int(value) == value_employee:
                    out_employees.append(employee)
    return {'employees': out_employees}

# Using POST method at the decorator:
@app.route('/informations', methods=['POST'])
def get_employees_post():
    username = request.form['username']
    secret = request.form['secret']

    # Checking if the user and password exist:
    if not check_user(username, secret):
        # 'Unauthorized 401 HTTP'
        return Response('Unauthorized', status=401)

    # the parameters will be inside the POST method now
    info = request.form['info']
    value = request.form['value']

    out_employees = []
    for employee in employees:
        if info in employee.keys():
            value_employee = employee[info]
            if type(value_employee) == str:
                if value.lower() == value_employee.lower():
                    out_employees.append(employee)
            elif type(value_employee) == int:
                if int(value) == value_employee:
                    out_employees.append(employee)
    return {'employees': out_employees}


# This condition debugs, so we can edit and use without restarting the app
if __name__ == "__main__":
    app.run(debug=True)
