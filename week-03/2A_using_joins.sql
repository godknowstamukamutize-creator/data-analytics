USE northwind;
-- 1. Create a single query to list the product id, product name, unit price and category
-- name of all products. Order by category name and within that, by product name.
SELECT 
	ProductID,
    ProductName,
    UnitPrice,
    CategoryName
FROM products p
JOIN categories c
	ON p.CategoryID = c.CategoryID
ORDER BY CategoryName ASC, ProductName ASC;
    
-- 2. Create a single query to list the product id, product name, unit price and supplier
-- name of all products that cost more than $75. Order by product name
SELECT 
	ProductID,
    ProductName,
    UnitPrice,
    CompanyName
FROM products p
JOIN suppliers s
	ON p.SupplierID = s.SupplierID
ORDER BY ProductName ASC;
    
-- 3. Create a single query to list the product id, product name, unit price, category name,
-- and supplier name of every product. Order by product name.
SELECT 
	ProductID,
    ProductName,
    UnitPrice,
    CategoryName,
    CompanyName AS SupplierName
FROM products p
JOIN categories c
	ON p.CategoryID = c.CategoryID
JOIN suppliers s 
	ON p.SupplierID = s.SupplierID
ORDER BY ProductName;


-- 4. Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- shipped to.
SELECT 
	OrderID,
    ShipName,
    ShipAddress,
    CompanyName AS shipper,
    ShipCountry
FROM orders o
JOIN shippers s
	ON o.ShipVia = s.ShipperID
WHERE ShipCountry = 'Germany'
ORDER BY 4 ASC, ShipName ASC;

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by
-- ship name, with a count of how many orders were shipped for that ship name
SELECT 
    ShipName,
    ShipAddress,
    CompanyName AS shipper,
    ShipCountry,
    COUNT(*)
FROM orders o
JOIN shippers s
	ON o.ShipVia = s.ShipperID
WHERE ShipCountry = 'Germany'
GROUP BY 1, 2, 3
ORDER BY 4 ASC, ShipName ASC;

-- 6. Create a single query to list the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale.
SELECT 
	o.OrderID,
    OrderDate,
    ShipName,
    ShipAddress,
    ProductName
FROM orders o 
JOIN `order details` od
	ON o.OrderID = od.OrderID
JOIN products p
	ON od.ProductID = p.ProductID
WHERE ProductName = 'Sasquatch Ale'
;

