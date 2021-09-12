import sqlite3

### CREATING DATABASE USING SQLITE3

# Choosing the name of our database: enterprise.db
conn = sqlite3.connect('enterprise.db')
# Using cursor to create and access tables
cursor = conn.cursor()
# creating a table passing the query
#### Following the same base from the dict created at the server.py:
# id: it is an int(), not NaN, it`s the primary key
    # and it self incremets whit the addition of new ids
# name: str(), not NaN
# position: str()
# pay: float()
cursor.execute("""
        CREATE TABLE employees (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT,
            pay REAL        
        );
""")

print("Table created successfully!")

#closing the connection with the database
conn.close()