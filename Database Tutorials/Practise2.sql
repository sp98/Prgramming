# Understanding the tables:
SELECT * FROM customers;
SELECT * FROM employees;
SELECT * FROM offices;
SELECT * FROM orderdetails;
SELECT * FROM orders;
SELECt * FROM payments;
SELECT * FROM productlines;
SELECT * FROM products;


# Get Total Products Types in Each Product Line
SELECT productLine, COUNT(productName) FROM products GROUP BY productline;

# Get Total Product Counts in Each Product Line
SELECT productLine, COUNT(productName), SUM(quantityInStock) FROM products GROUP BY productline;

# Get total Customer Count:
SELECT COUNT(DISTINCT(customerName)) FROM customers;

# Concatenating Strings 
SELECT CONCAT(contactFirstName, ' ', contactLastName) AS Contact FROM customers;

# Get employee details along with office address.
SELECT CONCAT(emp.firstName, ' ', emp.lastName) 
as 'Employee Name' , emp.email, emp.jobTitle, off.city, off.state,off.country 
FROM employees AS emp
INNER JOIN offices AS off	
  ON emp.officeCode = off.officeCode;

#Get All the customers whose order has been shipped:
SELECT customers.customerNumber, customers.customerName, orders.status FROM customers
INNER JOIN orders
ON customers.customerNumber = orders.customerNumber
WHERE orders.status = 'Shipped';

#Get the customername who has mosted shipped products:
SELECT cust.customerName, o.status, COUNT(o.customerNumber) FROM customers AS cust
INNER JOIN orders AS o
ON cust.customerNumber = o.customerNumber
GROUP BY o.customerNumber HAVING o.status = 'Shipped'
ORDER BY COUNT(o.customerNumber) DESC;

# Customer who has paid most 
SELECT pay.customerNumber, cust.customerName, SUM(pay.amount)
 FROM payments as pay
 INNER JOIN customers as cust
 ON pay.customerNumber = cust.customerNumber
GROUP BY pay.customerNumber
ORDER BY SUM(pay.amount) DESC