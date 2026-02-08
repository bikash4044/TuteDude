 CREATE TABLE Employees (
   EmpID INT PRIMARY KEY,
   Name VARCHAR(50),
   Department VARCHAR(50),
   Email VARCHAR(50)
 );
 INSERT INTO Employees (EmpID, Name, Department, Email) VALUES
   (1, 'Alice Johnson',  'HR',      'alice.johnson@example.com'),
   (2, 'Bob Smith',  	'IT',      'bob.smith@example.com'),
   (3, 'Charlie Brown',  'Finance','charlie.brown@example.com'),
   (4, 'Diana Prince',   'HR',      'diana.prince@example.com'),
   (5, 'Eve Adams',  	'IT',      'eve.adams@example.org');


-- Query 1
SELECT Name, Email FROM Employees WHERE Email LIKE '%@example.com';

-- Query 2
SELECT Name FROM Employees WHERE Name LIKE 'A%';

-- Query 3
 SELECT Name FROM Employees WHERE Name LIKE '%son';

-- Query 4
 SELECT Name FROM Employees WHERE SUBSTRING(Name, 2, 1) = 'v';

-- Query 5
SELECT Name, Department FROM Employees WHERE Department LIKE '%IT%';

-- Query 6
SELECT Name, Department FROM Employees WHERE LOWER(Department) LIKE '%hr%';