 CREATE TABLE Orders (
   OrderID INT PRIMARY KEY,
   OrderDate DATE,
   Amount DECIMAL(10,2)
 );
 INSERT INTO Orders (OrderID, OrderDate, Amount) VALUES
   (1, '2024-11-01', 250.50),
   (2, '2024-11-02', 300.75),
   (3, '2024-11-03', 150.25);


-- Query 1
 SELECT CAST(Amount AS CHAR(10)) AS AmountText FROM Orders;

-- Query 2
SELECT FORMAT(OrderDate, 'yyyy-MM-dd') AS OrderDateText FROM Orders;

-- Query 3
SELECT CAST('2024-11-05' AS DATE) AS ConvertedDate;

-- Query 4
 SELECT YEAR(OrderDate) AS OrderYear FROM Orders;

-- Query 5
 SELECT CONCAT(FORMAT(OrderDate, 'yyyy-MM-dd'), ' - $', Amount) AS Summary FROM Orders;