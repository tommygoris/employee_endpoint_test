## How to run

1. Ensure you have Python installed (I used Python 3.9 for example).
2. Ensure you have Flask installed (pip install Flask)
3. Clone the repository locally
4. Once the repository has been cloned, traverse into the repository locally and double-click
on the run.bat file. This file will start the Flask development server where the endpoints 
   will be served.
 5. Once the Flask server has been started, open up a web browser, such as, Chrome or Firefox
and go to the following link http://127.0.0.1:5000/ to play with the employee endpoints.
    
To retrieve an employee by his id, you can do the following...

http://127.0.0.1:5000/1   will retrieve the employee whose id is 1.

http://127.0.0.1:5000/2   will retrieve the employee whose id is 2.

To retrieve an array of all employees, sorted by highest salary to lowest, you can do the following...

http://127.0.0.1:5000/get_employees   will retrieve an array of all employees sorted by salary

To insert a new employee to the existing array using a JSON object (there are many ways this can be done)

Using the application, Postman, create a new post request to the following endpoint

http://127.0.0.1:5000/add_employee

The endpoint expects an employee's name, age, and salary to be sent with the post request in JSON

