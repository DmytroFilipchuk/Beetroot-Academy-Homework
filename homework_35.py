"""
Task 1

Joins

Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

As a solution to HW, create a file named: task1.sql with all SQL queries:


1)write a query in SQL to display the first name, last name, department number, and department name for each employee

SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees as e
INNER JOIN departments as d
WHERE  e.department_id = d.department_id


2)write a query in SQL to display the first and last name, department, city, and state province for each employee

SELECT e.first_name, e.last_name,  d.depart_name, l.city, l.state_province
FROM employees as e
INNER JOIN departments as d ON e.department_id = d.department_id
INNER JOIN locations as l ON d.location_id=l.location_id


3)write a query in SQL to display the first name, last name, department number, and department name,
for all employees for departments 80 or 40

SELECT e.first_name,e.last_name,e.department_id,d.depart_name
FROM employees as e
INNER JOIN departments as d ON e.department_id = d.department_id
WHERE e.department_id  in  (80, 40)


4) write a query in SQL to display all departments including those where does not have any employee

SELECT d.depart_name
FROM departments as d


5) write a query in SQL to display the first name of all employees including the first name of their manager

SELECT e.first_name as employee, m.first_name as manager
FROM employees as e
INNER JOIN employees as m ON e.manager_id = m.employee_id

6) write a query in SQL to display the job title, full name (first and last name ) of the employee,
and the difference between the maximum salary for the job and the salary of the employee

SELECT j.job_title as job, e.first_name as FirstName, e.last_name as LastName, (j.max_salary - e.salary)
as SalaryDifference
FROM employees as e
INNER JOIN jobs as j ON e.job_id = j.job_id

7) write a query in SQL to display the job title and the average salary of employees

SELECT j.job_title as job, (sum(e.salary)/count(e.employee_id)) as averageSalary
FROM jobs as j
INNER JOIN employees as e ON e.job_id = j.job_id
GROUP BY e.job_id
ORDER BY averageSalary DESC

8) write a query in SQL to display the full name (first and last name), and salary of those
employees who work in any department located in London

SELECT e.first_name as FirstName, e.last_name as LastName, e.salary as Salary
FROM employees as e
INNER JOIN departments as d ON e.department_id = d.department_id
INNER JOIN locations as l ON d.location_id = l.location_id
WHERE l.city = "London"

9) write a query in SQL to display the department name and the number of employees in each department

SELECT d.depart_name as Department, count(e.employee_id) as NumberOfEmployees
FROM departments as d
INNER JOIN employees as e ON d.department_id = e.department_id
GROUP BY e.department_id
ORDER BY NumberOfEmployees DESC

"""