#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
sql = "SELECT VERSION()"
cursor.execute(sql)
data = cursor.fetchone()
print "Database version : %s " % data



### CREATE TABLE EXAMPLE ###

#sql = "DROP TABLE IF EXISTS EMPLOYEE"
#cursor.execute(sql)
#data = cursor.fetchone()


#sql = """CREATE TABLE EMPLOYEE (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,  
#         SEX CHAR(1),
#         INCOME FLOAT )"""
#cursor.execute(sql)
#data = cursor.fetchone()


### DATA INSERT EXAMPLE ###

#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#try:
#   # Execute the SQL command
#   cursor.execute(sql)
#   # Commit your changes in the database
#   db.commit()
#except:
#   # Rollback in case there is any error
#   db.rollback()

# Fetch a single row using fetchone() method.

# disconnect from server
db.close()
