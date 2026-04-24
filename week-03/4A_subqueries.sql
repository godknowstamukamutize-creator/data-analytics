USE northwind;
-- 1. What is the product name(s) of the most expensive products?
SELECT 
	ProductName,
    UnitPrice
FROM products
WHERE UnitPrice = (
	SELECT MAX(UnitPrice) AS ExpensiveProduct
	FROM products);
-- 'Cte de Blaye', '263.5000'

-- 2. What is the product name(s) and categories of the least expensive products?   
SELECT 
	ProductName,
    CategoryName,
    UnitPrice
FROM products p
JOIN categories c	
	ON p.CategoryID = c.CategoryID
WHERE UnitPrice = (
	SELECT MIN(UnitPrice) AS LeastExpensiveProd
    FROM products);
-- 'Geitost', 'Dairy Products', '2.5000'
 
-- 3. What is the order id, shipping name and shipping address of all orders shipped via
-- -- "Federal Shipping"?
SELECT 
	OrderID,
    ShipName,
    ShipAddress,
    ShipVia
FROM orders
WHERE ShipVia = (
	SELECT ShipperID
    FROM shippers
    WHERE CompanyName = 'Federal Shipping');
    
-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID
FROM `order details`
WHERE ProductID = (
	SELECT ProductID 
	FROM products
	WHERE ProductName = 'Sasquatch Ale');

-- 5. What is the name of the employee that sold order 10266?
SELECT CONCAT(FirstName, ' ', LastName) AS EmployeeFullName
FROM employees
WHERE EmployeeID = (
	SELECT EmployeeID
	FROM orders
	WHERE OrderID = 10266);
-- 'Janet Leverling'


-- 6. What is the name of the customer that bought order 10266?
SELECT ContactName AS CustomerName
FROM customers
WHERE CustomerID = (
	SELECT CustomerID
	FROM orders
	WHERE OrderID = 10266);
-- Pirkko Koskitalo
 