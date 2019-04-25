import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

import sys
from PIL import Image
import base64
import cStringIO
import PIL.Image

import cloudinary
import cloudinary.uploader

import glob #to get latest added file 

BaseDirectory = '/home/pi/Desktop/azure-faceApi/captured/' # directory where picamera photos are stored


cloudinary.config( 
  cloud_name = "dvey2m05b", 
  api_key = "163722355749348", 
  api_secret = "WYAlWAKzQm75iFEEf5AerCosV1c" 
)

def cloudinaryUpload(imgPath):
        resp =  cloudinary.uploader.upload(imgPath)
        url = resp["secure_url"]
        print(url)
        return url


def latestFile():
        list_of_files = glob.glob(BaseDirectory + '*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print (latest_file)
        return latest_file


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="COMPANY"
)

cursor = connection.cursor(prepared=True)


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as imageFile:
        binaryData = imageFile.read()
        encoded_string = base64.b64encode(binaryData)
    return encoded_string

# def insertBLOB(emp_id, name, photo, biodataFile):
#     print("Inserting BLOB into python_employee table")

#     try:
        

#         sql_insert_blob_query = """ INSERT INTO `python_employee`
#                           (`id`, `name`, `photo`, `biodata`) VALUES (%s,%s,%s,%s)"""

#         empPicture = convertToBinaryData(photo)
#         file = convertToBinaryData(biodataFile)

#         # Convert data into tuple format
#         insert_blob_tuple = (emp_id, name, empPicture, file)

#         result  = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#         connection.commit()
#         print ("Image and file inserted successfully as a BLOB into python_employee table", result)

#     except mysql.connector.Error as error :
#         connection.rollback()
#         print("Failed inserting BLOB data into MySQL table {}".format(error))

#     finally:
#         #closing database connection.
#         if(connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")

# insertBLOB(1, "Eric", "D:\Python\Articles\my_SQL\images\eric_photo.png", "D:\Python\Articles\my_SQL\images\eric_bioData.txt")
# insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png","D:\Python\Articles\my_SQL\images\scott_bioData.txt")


def updateQuery(emp_id, photo):
    # mode = IN_PIC or OUT_PIC
    binPic = convertToBinaryData(photo)
    # sqlQ = "UPDATE ATTENDENCE SET " +str(mode) +"= " + binPic +" WHERE EMP_ID = "+str(emp_id)

    sql = "UPDATE ATTENDENCE SET OUT_PIC = %s WHERE EMP_ID = %s"
    val = (binPic, emp_id)

    cursor.execute(sql, val)
    connection.commit()

updateQuery("512", "/home/akshay/Pictures/aks-manga.png")
