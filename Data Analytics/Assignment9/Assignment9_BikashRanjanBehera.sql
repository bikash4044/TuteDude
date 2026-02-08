 CREATE TABLE Employees (
   EmpID INT PRIMARY KEY,
   Name VARCHAR(50),
   DateOfBirth DATE,
   JoinDate DATE
 );
 INSERT INTO Employees (EmpID, Name, DateOfBirth, JoinDate) VALUES
   (1, 'Alice Johnson', '1985-05-20', '2010-06-15'),
   (2, 'Bob Smith', 	'1990-08-10', '2015-09-01'),
   (3, 'Charlie Brown', '1988-03-25', '2012-11-12'),
   (4, 'Diana Prince',  '1992-01-30', '2017-07-08'),
   (5, 'Eve Adams', 	'1987-12-05', '2013-03-20');


-- Query 1
 SELECT CURRENT_TIMESTAMP;

-- Query 2
 SELECT Name, FLOOR(DATEDIFF(DAY, DateOfBirth, CURRENT_DATE)/365.25) AS Age FROM Employees;

-- Query 3
 SELECT Name, FLOOR(DATEDIFF(DAY,JoinDate,CURRENT_DATE)/365.25) AS YearsExperience FROM Employees;

-- Query 4
 SELECT Name, YEAR(DateOfBirth) AS BirthYear, MONTH(DateOfBirth) AS BirthMonth, DAY(DateOfBirth) AS BirthDay FROM Employees;

-- Query 5
 SELECT Name FROM Employees WHERE MONTH(DateOfBirth) = 8;

-- Query 6
 SELECT Name FROM Employees WHERE
DATEFROMPARTS(YEAR(GETDATE()), MONTH(DateOfBirth), DAY(DateOfBirth)) 
BETWEEN CAST(GETDATE() AS DATE) AND DATEADD(day, 30, CAST(GETDATE() AS DATE));