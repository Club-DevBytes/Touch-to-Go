import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="COMPANY"
)

mycursor = mydb.cursor()
def sql_extract(positionNumber)

 
sql = "SELECT NAME,EMP_NO FROM EMPLOYEE WHERE SERIAL_NO= %s"

val = (str(positionNumber))


mycursor.execute(sql,val)

myresult = mycursor.fetchall()

print(myresult)

name = myresult[0][0]
emp_no = myresult[0][1]

print(name)
print(emp_no)



