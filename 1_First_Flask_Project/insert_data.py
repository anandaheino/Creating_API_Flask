import sqlite3

employees = [
                {'name': 'Val', 'position': 'Analyst', 'pay':5000},
                {'name': 'Eny', 'position': 'Analyst', 'pay':4000},
                {'name': 'Mary', 'position': 'Developer', 'pay':5000},
             ]
# connection with the database
conn = sqlite3.connect('enterprise.db')
# creating and  passing the query
cursor = conn.cursor()

# doing the simple way, iterating through the employee dicts:
for employee in employees:
    cursor.execute("""
                    INSERT INTO employees (name, position, pay)
                    VALUES (?, ?, ?)
                    """,
                   (employee['name'], employee['position'], employee['pay']))

# INSERT INFO "table_name"
print('Data inserted successfully!')
# After inserting the data, we have to commit it
conn.commit()
# closing the connection with the database
conn.close()