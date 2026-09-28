-- =====================================================
-- Week 3 Assignment : SQL & Excel for Data Analytics
-- File   : schema_and_data.sql   (SQLite / MySQL-compatible)
-- =====================================================
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS products;

CREATE TABLE departments (
    dept_id    INTEGER PRIMARY KEY,
    dept_name  VARCHAR(50) NOT NULL,
    location   VARCHAR(50)
);

CREATE TABLE employees (
    emp_id     INTEGER PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name  VARCHAR(30) NOT NULL,
    dept_id    INTEGER,                 -- foreign key -> departments.dept_id
    job_title  VARCHAR(50),
    salary     INTEGER,
    hire_date  DATE,
    city       VARCHAR(30),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    product_name VARCHAR(50),
    category     VARCHAR(30),
    price        INTEGER,
    stock        INTEGER
);

INSERT INTO departments VALUES
(1,'Sales','Lucknow'),(2,'IT','Noida'),(3,'HR','Kanpur'),
(4,'Finance','Delhi'),(5,'Marketing','Agra'),(6,'Legal','Delhi');

INSERT INTO employees VALUES
(101,'Aarav','Sharma',2,'Software Engineer',65000,'2021-03-15','Noida'),
(102,'Priya','Verma',1,'Sales Executive',42000,'2020-07-01','Lucknow'),
(103,'Rohan','Gupta',2,'Data Analyst',58000,'2022-01-10','Noida'),
(104,'Sneha','Singh',3,'HR Manager',72000,'2019-05-20','Kanpur'),
(105,'Vikram','Yadav',4,'Accountant',48000,'2021-09-12','Delhi'),
(106,'Anjali','Mishra',5,'Marketing Lead',61000,'2020-11-30','Agra'),
(107,'Karan','Tiwari',2,'DevOps Engineer',70000,'2018-02-25','Noida'),
(108,'Neha','Pandey',1,'Sales Manager',80000,'2017-06-18','Lucknow'),
(109,'Amit','Kumar',4,'Financial Analyst',55000,'2022-08-05','Delhi'),
(110,'Pooja','Chauhan',3,'HR Executive',38000,'2023-01-16','Kanpur'),
(111,'Rahul','Saxena',2,'Data Scientist',85000,'2019-10-09','Noida'),
(112,'Simran','Kaur',5,'Content Writer',35000,'2023-04-03','Agra'),
(113,'Deepak','Joshi',1,'Sales Executive',40000,'2021-12-01','Lucknow'),
(114,'Meera','Nair',4,'Finance Manager',90000,'2016-03-14','Delhi'),
(115,'Arjun','Mehta',2,'Software Engineer',62000,'2022-06-21','Noida'),
(116,'Kavya','Rao',5,'SEO Specialist',45000,'2021-05-11','Agra'),
(117,'Sanjay','Dubey',1,'Sales Executive',43000,'2020-02-17','Lucknow'),
(118,'Ritu','Agarwal',3,'Recruiter',41000,'2022-11-28','Kanpur'),
(119,'Manish','Bajpai',2,'QA Engineer',52000,'2021-07-19','Noida'),
(120,'Tanya','Kapoor',NULL,'Intern',15000,'2024-01-08','Delhi');

INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,25),(2,'Smartphone','Electronics',22000,60),
(3,'Headphones','Accessories',1800,120),(4,'Office Chair','Furniture',7500,40),
(5,'Desk','Furniture',12000,18),(6,'Keyboard','Accessories',1200,150),
(7,'Monitor','Electronics',14000,35),(8,'Mouse','Accessories',700,200),
(9,'Bookshelf','Furniture',9000,12),(10,'Tablet','Electronics',30000,28);


-- =====================  TASK 1  =====================
-- 1.1 Display all records
SELECT * FROM employees;

-- 1.2 Select specific columns
SELECT first_name, last_name, job_title, salary
FROM employees;

-- 1.3 Column aliases
SELECT first_name || ' ' || last_name AS full_name,
       salary AS monthly_salary,
       salary * 12 AS annual_salary
FROM employees;


-- =====================  TASK 2  =====================
-- 2.1 WHERE with comparison operator (>)
SELECT emp_id, first_name, job_title, salary
FROM employees
WHERE salary > 60000;

-- 2.2 WHERE with multiple conditions (AND / =)
SELECT emp_id, first_name, city, salary
FROM employees
WHERE city = 'Noida' AND salary >= 60000;

-- 2.3 WHERE with BETWEEN and <>
SELECT emp_id, first_name, salary, city
FROM employees
WHERE salary BETWEEN 40000 AND 50000
  AND city <> 'Agra';

-- 2.4 ORDER BY (descending)
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;

-- 2.5 ORDER BY on two columns
SELECT city, first_name, salary
FROM employees
ORDER BY city ASC, salary DESC;

-- 2.6 Aggregate functions
SELECT COUNT(*)    AS total_employees,
       SUM(salary) AS total_salary,
       ROUND(AVG(salary),2) AS average_salary,
       MIN(salary) AS lowest_salary,
       MAX(salary) AS highest_salary
FROM employees;


-- =====================  TASK 3  =====================
-- 3.1 GROUP BY with aggregates
SELECT dept_id,
       COUNT(*)              AS num_employees,
       SUM(salary)           AS total_salary,
       ROUND(AVG(salary),0)  AS avg_salary,
       MAX(salary)           AS max_salary
FROM employees
GROUP BY dept_id
ORDER BY dept_id;

-- 3.2 GROUP BY city
SELECT city, COUNT(*) AS num_employees, ROUND(AVG(salary),0) AS avg_salary
FROM employees
GROUP BY city
ORDER BY num_employees DESC;

-- 3.3 HAVING - filter groups
SELECT dept_id, COUNT(*) AS num_employees, ROUND(AVG(salary),0) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 55000;

-- 3.4 WHERE + GROUP BY + HAVING together
SELECT dept_id, COUNT(*) AS num_employees, SUM(salary) AS total_salary
FROM employees
WHERE salary > 40000
GROUP BY dept_id
HAVING COUNT(*) >= 3;


-- =====================  TASK 4  =====================
-- 4.1 INNER JOIN
SELECT e.emp_id, e.first_name, e.job_title, d.dept_name, d.location
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- 4.2 LEFT JOIN
SELECT e.emp_id, e.first_name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.emp_id >= 118;

-- 4.3 RIGHT JOIN
SELECT d.dept_id, d.dept_name, e.first_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IN (3, 6)
ORDER BY d.dept_id;

-- 4.4 JOIN + GROUP BY (bonus)
SELECT d.dept_name, COUNT(e.emp_id) AS num_employees, ROUND(AVG(e.salary),0) AS avg_salary
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY num_employees DESC;


-- =====================  TASK 5  =====================
-- 5.1 Employees earning more than the average salary
SELECT emp_id, first_name, job_title, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- 5.2 Products priced higher than the average product price
SELECT product_name, category, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;

-- 5.3 Subquery with IN (employees in Delhi-based departments)
SELECT first_name, job_title
FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'Delhi');

-- 5.4 Highest-paid employee in each department (correlated subquery)
SELECT e.first_name, e.dept_id, e.salary
FROM employees e
WHERE e.salary = (SELECT MAX(salary) FROM employees WHERE dept_id = e.dept_id)
ORDER BY e.dept_id;

