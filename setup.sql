CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    OrderTotal REAL,
    OrderDate TEXT
);

INSERT INTO Orders (CustomerID, OrderTotal, OrderDate) VALUES
(1, 150.50, '2023-01-10'),
(1, 200.00, '2023-02-15'),
(2, 50.00, '2023-03-20'),
(2, 300.00, '2023-04-25'),
(3, 100.00, '2023-05-30'),
(3, 400.00, '2023-06-05'),
(4, 250.00, '2023-07-10'),
(4, 150.00, '2023-08-15'),
(5, 600.00, '2023-09-20'),
(5, 350.00, '2023-10-25');

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT,
    CustomerEmail TEXT
);

INSERT INTO Customers (CustomerName, CustomerEmail) VALUES
('John Doe', 'johndoe@example.com'),
('Jane Smith', 'janesmith@example.com'),
('Alice Johnson', 'alicejohnson@example.com'),
('Bob Brown', 'bobbrown@example.com'),
('Charlie Davis', 'charliedavis@example.com');

CREATE TABLE CustomerActivities (
    ActivityID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ActivityDate TEXT
);

INSERT INTO CustomerActivities (CustomerID, ActivityDate) VALUES
(1, '2023-01-10'),
(1, '2023-01-15'),
(1, '2023-02-20'),
(2, '2023-03-25'),
(2, '2023-04-30'),
(3, '2023-05-05'),
(3, '2023-06-10'),
(4, '2023-07-15'),
(5, '2023-09-20'),
(5, '2023-10-25'),
(5, '2023-11-30');

