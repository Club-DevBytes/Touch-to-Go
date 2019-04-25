# import mysql.connector
#Create a table in DB
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="COMPANY"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE ATTENDENCE (EMP_ID VARCHAR(255), EMP_NAME VARCHAR(255), DATE VARCHAR(255), IN_TIME VARCHAR(255), OUT_TIME VARCHAR(255))")


import mysql.connector

#Insert Value
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="COMPANY"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ATTENDENCE (EMP_ID, EMP_NAME, DATE, IN_TIME , OUT_TIME) VALUES (%s, %s, %s, %s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)