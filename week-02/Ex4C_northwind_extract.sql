USE northwind;

-- Q4a:Answer: The table that holds the items Northwind sells is called products.

-- Q4b: What is the name of the table that holds the types/categories of items?
-- Answer: The table that holds the categories of items is called categories.

-- Question 5
SELECT * FROM employees;
-- Q5a: Who is the employee whose name makes it look like she's a bird?
-- Answer: Janet Peacock -- her last name "Peacock" is a bird

-- Question 6
SELECT * FROM products;
-- Q6a: How many records does the query return?
-- Answer: The products table contains 77 records.
-- To retrieve only 10 rows using the toolbar: use the row limit
-- dropdown in the toolbar at the top of the query pane and set it to 10,
-- Q6b BONUS: How to limit rows returned in SQL using LIMIT clause:
SELECT * FROM products LIMIT 10;
-- Source: https://www.w3schools.com/mysql/mysql_limit.asp

-- Question 7
SELECT * FROM categories;
-- Q7c: What is the category ID of seafood?
-- Answer: The category ID for Seafood is 8.
USE northwind;

-- ============================================================
-- QUESTIONS ABOUT THE NORTHWIND SCHEMA
-- ============================================================

-- Q4a: What is the name of the table that holds the items Northwind sells?
-- Answer: The table that holds the items Northwind sells is named "products."

-- Q4b: What is the name of the table that holds the types/categories of items?
-- Answer: The table that holds the categories of items is named "categories."


-- ============================================================
-- Q5: SELECT all columns from the employees table
-- ============================================================

SELECT * FROM employees;

-- Q5a: Who is the employee whose name makes it look like she's a bird?
-- Answer: Janet Peacock -- her last name "Peacock" is a bird.


-- ============================================================
-- Q6: SELECT all columns from the products table
-- ============================================================

SELECT * FROM products;

-- Q6a: How many records does the query return?
-- Answer: The products table contains 77 records.
-- To retrieve only 10 rows using the toolbar: use the row limit
-- dropdown in the toolbar at the top of the query pane and set it to 10,
-- then re-run the query.

-- Q6b BONUS: How to limit rows returned in SQL using LIMIT clause:
SELECT * FROM products LIMIT 10;
-- Source: https://www.w3schools.com/mysql/mysql_limit.asp
-- The LIMIT clause is added at the end of a SELECT statement
-- followed by the number of rows you want returned.


-- ============================================================
-- Q7: SELECT all columns from the categories table
-- ============================================================

SELECT * FROM categories;

-- Q7c: What is the category ID of seafood?
-- Answer: The category ID for Seafood is 8.

-- Q8: Top 50 orders with selected columns only
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;

