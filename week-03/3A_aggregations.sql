USE northwind;
-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price
SELECT MIN(UnitPrice) AS CheapestPrice
FROM products;
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- 2. Write a query to find the average price of all items that Northwind sells.
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM products;

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM products;
SELECT 
	ProductName,
    UnitPrice,
    CompanyName AS SupplierName
FROM products p
JOIN suppliers s
	ON p.SupplierID = s.SupplierID
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries).
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM employees;

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)
SELECT
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM employees;

-- 6. Write a query to find the name and supplier ID of each supplier and the number
-- of items they supply. Hint: Join is your friend here.
SELECT
    s.SupplierID,
    CompanyName AS SupplierName,
    COUNT(ProductID) AS ItemsSupplied
FROM suppliers s
JOIN products p 
	ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY s.CompanyName;

-- 7. Write a query to find the list of all category names and the average price
-- for items in each category.
SELECT
    c.CategoryName,
    ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM categories c
JOIN products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY c.CategoryName;

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind,
-- what is the name of each supplier and the number of items they supply.
SELECT
    s.CompanyName AS SupplierName,
    COUNT(p.ProductID) AS ItemsSupplied
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5
ORDER BY ItemsSupplied DESC;

-- 9. Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (unit price x units on hand). Sort descending by value, then by
-- product name. Exclude products not in stock.
SELECT
    ProductID,
    ProductName,
    ROUND(UnitPrice * UnitsInStock, 2) AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;



