from flask import Flask, request
import json

app = Flask(__name__)

employee1 = '{ "id":1, "employee_name":"Tiger Nixon", "employee_salary":320800, "employee_age":61 }'
employee2 = '{ "id":2, "employee_name":"Garrett Winters", "employee_salary":170750, "employee_age":63 }'
employee3 = '{ "id":3, "employee_name":"Ashton Cox", "employee_salary":86000, "employee_age":66 }'
employees = [employee1, employee2, employee3]


# Endpoint to retrieve an employee using their id
@app.route('/<int:id>', methods=["GET"])
def employee_id(id):
    for employee in employees:
        employee_json = json.loads(employee)
        if int(employee_json["id"]) == int(id):
            employee_json.pop('id', None)
            return employee_json
    return "Employee ID not found"


# Endpoint to add an employee using a POST request given an employee's name, age, and salary
@app.route("/add_employee/", methods=["POST"])
def add_employee():
    employee_name = request.form["employee_name"]
    employee_age = request.form["employee_age"]
    employee_salary = request.form["employee_salary"]
    new_id = 0
    for employee in employees:
        employee_json = json.loads(employee)
        if new_id <= employee_json["id"]:
            new_id = employee_json["id"] + 1

    employees.append('{ "id":' + str(new_id) + ', "employee_name":' + (
            '"%s"' % employee_name) + ', "employee_salary":' + employee_salary + ', "employee_age":' + employee_age + ' }')
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


#  Sorts the array of employees based on employee salary
def sort_salary(employee):
    try:
        return int(json.loads(employee)["employee_salary"])
    except KeyError:
        return 0


# Endpoint to retrieve all employees
@app.route('/get_employees')
def get_employees():
    data = "["
    data += "<br/>"
    employees.sort(key=sort_salary, reverse=True)
    for employee in employees:
        data += employee + "<br/>"
    data += "]"
    return data


# Main Endpoint
@app.route('/')
def hello():
    return "Welcome to the employees endpoint test"
