import sqlite3

#Connect to Sqlite
connection = sqlite3.connect("student.db")

#Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#Create a table
table_info="""
Create table STUDENT(Name VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# Insert records
cursor.execute("""INSERT INTO STUDENT VALUES('Kristin', 'Data Science', 'A', 98)""")
cursor.execute("""INSERT INTO STUDENT VALUES('John', 'Mathematics', 'B', 85)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Lisa', 'Data Science', 'C', 92)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Anna', 'Chemistry', 'D', 88)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Dipesh', 'Devops', 'A', 35)""")

#Display all the records
print("The inserted records are:")

data = cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)


# Commit changes and close the connection
connection.commit()
connection.close()