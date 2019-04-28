import easygui
import os


choice = easygui.buttonbox("Hi Admin! what is your wish?",
                           choices = ['Employee Enrollment', 'Employee Attendance', 'Employee Deletion'] )

if choice  == 'Employee Enrollment':
    os.system("python /home/pi/Desktop/GIH/enroll_trial.py")
elif choice  == 'Employee Attendance':
    os.system("python /home/pi/Desktop/GIH/search.py")
elif choice  == 'Employee Deletion':
    os.system("python /home/pi/Desktop/GIH/example_delete.py")
else :
    sys.exit()
