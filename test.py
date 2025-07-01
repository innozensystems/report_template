import sqlite3

# Define your SQL query with named placeholders

query = """
WITH CustomerActivity AS (
    SELECT
        CustomerID,
        COUNT(ActivityID) AS ActivityCount
    FROM
        CustomerActivities
    WHERE
        -- ActivityDate BETWEEN %(start_date)s AND %(end_date)s
        ActivityDate BETWEEN ? AND ?
    GROUP BY
        CustomerID
)

SELECT
    c.CustomerName,
    ca.ActivityCount
FROM
    CustomerActivity ca
JOIN
    Customers c ON ca.CustomerID = c.CustomerID
WHERE
    --ca.ActivityCount > %(min_activity_count)s
    ca.ActivityCount > ?
ORDER BY
    ca.ActivityCount DESC;
"""

# Define your parameters in a dictionary
params = [
    '2023-01-01',
    '2023-12-31',
    1
]

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

