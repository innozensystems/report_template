import sqlite3

# Define your SQL query with named placeholders
query = """
WITH CustomerOrders AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS TotalOrders,
        SUM(OrderTotal) AS TotalSales
    FROM
        Orders
    WHERE
        OrderDate BETWEEN %(start_date)s AND %(end_date)s
    GROUP BY
        CustomerID
),
HighSpendingCustomers AS (
    SELECT
        CustomerID,
        TotalOrders,
        TotalSales
    FROM
        CustomerOrders
    WHERE
        TotalSales > %(high_spending_threshold)s
)

SELECT
    c.CustomerName,
    c.CustomerEmail,
    hsc.TotalOrders,
    hsc.TotalSales
FROM
    HighSpendingCustomers hsc
JOIN
    Customers c ON hsc.CustomerID = c.CustomerID
WHERE
    c.CustomerName LIKE %(customer_name_pattern)s
ORDER BY
    hsc.TotalSales DESC;
"""

# Define your parameters in a dictionary
params = {
    'start_date': '2022-01-01',
    'end_date': '2022-12-31',
    'high_spending_threshold': 10000,
    'customer_name_pattern': '%John%'
}

# Connect to your SQLite database
conn = sqlite3.connect('exercises.db')
cur = conn.cursor()

# Execute the query using the named parameters
cur.execute(query, params)

# Fetch and print the results
results = cur.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()

