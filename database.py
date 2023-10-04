# import sqlite3
# conn=sqlite3.connect('testdb.sqlite3')
# cur=conn.cursor()
# qry='''
# CREATE TABLE Employee (
# EmpID INTEGER PRIMARY KEY AUTOINCREMENT,
# FIRST_NAME TEXT (20),
# LAST_NAME TEXT(20),
# AGE INTEGER,
# SEX TEXT(1),
# INCOME FLOAT
# );
# '''
# try:
#    cur.execute(qry)
#    print ('Table created successfully')
# except:
#    print ('error in creating table')
# conn.close()



import sqlite3
conn=sqlite3.connect('testdb.sqlite3')
cur=conn.cursor()
qry="""INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   cur.execute(qry)
   conn.commit()
   print ('Record inserted successfully')
except:
   conn.rollback()
   print ('error in INSERT operation')
conn.close()