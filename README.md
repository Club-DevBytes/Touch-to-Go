# Touch-to-Go
*"Advanced Biometric Enterprise Employee Attendance System with Realtime MySQL Databse and React.js Based Admin Dashboard."*

![enter image description here](https://lh3.googleusercontent.com/H4lpPhO-Tk_rq56K_CeVEeEskAQam8WQZCtuhhMDtu_tZ598GhjxnUT1LR9z4VKS-XMmu1CPsuSMKw)![enter image description here](https://lh3.googleusercontent.com/nhhqOsqknaH2a8Sd1rMouaanuFLUvqu8yGr936gOFcKjY7JgOHd3C6qUX7QivsOqIeIT_L5orDDZ_A)

> A Detailed Installation Blog Post will be Added Soon.

## Working

**Hardware Side - Raspberry pi 3b +**
- First you need to start a server in the Raspberry Pi
So for the Download and install webok server from [chrome store](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en)
- Then Click on Choose folder and select :  `pyscripts/fingerprint`
- Navigate to pyscripts folder
- `$ cd pyscripts`
- `$ python start.py`
## *Working Flow for the Project*
![enter image description here](https://lh3.googleusercontent.com/nVj9aEWrqIC4yc52y1Wjq_VMLfECWkoFscJX60-B8mIBYHTuo0UqVGLlYH91oAYjqqiRYwoPBw9FlQ)
## Enrolling a New Employee

**On your machine/notebook**
Fire up a terminal Navigate to webapp directory

    $ cd webapp
  Head to the server directory
  

    $ cd server
Start nodemon server

    $ nodemon server.js
Fire up another Terminal and Navigate to webapp folder

    $ cd client
 Install all the Dependencies
   

    $ npm i

  Lets Start our Web App
  

    $ npm start
  
This Should Look like this-

![enter image description here](https://lh3.googleusercontent.com/DzIZHKDo9vvvz83iZMogFFI6cHSdbv6muPsNctvooiFPl_bIcU3c4zuLUmPInJo76TwI-ab0Z96v-g)

Now Lets Click on Register a New Employee:

![enter image description here](https://lh3.googleusercontent.com/k0kScwmYhs_LHkNh-Dv9kcaOb4Nqw5iSHBSsMyLbGuEWV1iOJHVZiz5DXiK9saUbg30hkb9_Bndz0g)

**This will Sucessfully register our new employee on our Database.**

## Registering New Employee on Our Fingerprint Scanner

Head to the Raspberry pi terminal to the pyscript folder

    $ cd pyscripts
   Now run the password . py script 

    $ python password.py
- Click on Employee Enrollment
- Enter The Same Enrollment no as Earlier
- Register the Employee's Finger to the machine

***You can Check if the new employee registered or not in the Webapp - Just click on all Employees Button***

## Employee Attendance
Head to the Raspberry pi terminal to the pyscript folder

    $ cd pyscripts
   Now run the password . py script 

    $ python password.py
- Click on Employee Attendance and you are good to go

## Realtime Attendance Dashboard

**Click on the Date Picker in the Home Screen of the Webapp and you are good to Go**

> You can Even  See the Details of the employees IN | OUT Time By clicking the Employee in the webapp

## Deleting the Employee

Head to the Raspberry pi terminal to the pyscript folder

    $ cd pyscripts
   Now run the password . py script 

    $ python password.py
- Click on Employee Deletion
- Enter Employee  Enrollment No and you are Good to Go
