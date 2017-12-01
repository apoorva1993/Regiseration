import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

ema= "[^@]+@[^@]+\.[^@]+"
mob= "^[0-9]{10}$"


def validfields(fname, lname, uname, pwd, cpwd, email1, mobile):
    '''
     This function check all validation and check point for user registration form.
     This function validate for first name,last name,username,password,email validation
     and mobile validation.If any validation fail,function return false and error message
     so that we see what type error occured. 
    '''
    email_validation = re.match(ema, email1) # regular expression for email validation
    mobile_validation = re.match(mob, mobile) # regular expression for mobile validation
    
    if len(fname)<=1:
	   # print ("First name should be greater than 2")
	    return False, "First name should have atleast 2"
    elif len(lname)<=1:
	    # print ("Last name should be greater than 2")
	    return False, "Last name should have atleast 2"
    elif len(uname)<8:
	    # print ("Username should be minimum 8")
	    return False, "Username should be minimum 8"
    elif len(pwd)<8:
	    # print ("Password should be minimum 8")
	    return False, "Password should be minimum 8"
    elif (pwd!=cpwd):
	    # print ("Both password is not same")
	    return False, "Your confirm password is not matching with the entered password"
    elif email_validation==None:
	    # print ("Your email-id is not valid")
	    return False, "Your email-id is not valid"
    elif mobile_validation==None:
	    # print ("Mobile number should be 1 digit")
	    return False, "Mobile number should be 10 digit"
    else:	
	    return True, "No Error Found"

#Multiple Entries pass in registration form.
entry = [
{"fname":"", "lname":"", "uname":"", "pwd":"", "cpwd":"", "email1":"", "mobile": ""},
{"fname":"T", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"12345678", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"T", "uname":"testtest", "pwd":"12345678", "cpwd":"12345678", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtes", "pwd":"12345678", "cpwd":"12345678", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"1234567", "cpwd":"12345678", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"1234567", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"123456783213", "cpwd":"123456790", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"123456790", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"12345678", "email1":"ab@c.et", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"12345678", "email1":"abcdtest.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"12345678", "email1":"abcd@test.com", "mobile": "9876543210"},
{"fname":"Test", "lname":"Test", "uname":"testtest", "pwd":"12345678", "cpwd":"12345678", "email1":"abcd@test.com", "mobile": "987654321"}
]

for data in entry:
	fname = data['fname']
	lname = data['lname']
	uname = data['uname']
	pwd = data['pwd']
	cpwd = data['cpwd']
	email1 = data['email1']
	mobile = data['mobile']

        #Chrome driver path
	driverpath= "C:/Users/apoorva.baranwal/Desktop/Py_program/drivers/chromedriver.exe"
	driver =webdriver.Chrome(driverpath)

	#Base URL link
	driver.get("http://adjiva.com/qa-test/")

	#Enter first name
	felem = driver.find_element_by_name("first_name")
	felem.send_keys(fname) # send_keys function used for filling entry in html form 

	#Enter last name
	lelem = driver.find_element_by_name("last_name")
	lelem.send_keys(lname)

	#Select Dropdown option in Department
	driver.find_element_by_name("department").send_keys("Engineering")	

	#Enter username
	uelem = driver.find_element_by_name("user_name")
	uelem.send_keys(uname)

	#Enter password
	pelem = driver.find_element_by_name("user_password")
	pelem.send_keys(pwd)

	#Enter confirm password
	cpelem = driver.find_element_by_name("confirm_password")
	cpelem.send_keys(cpwd)

	#Enter email address
	emelem = driver.find_element_by_name("email")
	emelem.send_keys(email1)

	#Enter contact number
	celem = driver.find_element_by_name("contact_no")
	celem.send_keys(mobile)

	
        # call validfields function for check validation for all entries.
        # this fuction return true or false.  
	status, message = validfields(fname, lname, uname, pwd, cpwd, email1, mobile)
	
	if status == True:
		#Press submit button
		driver.find_element_by_class_name("btn").click()
		driver.execute_script("window.alert('Acknowledgement email has been sent to your registered email')")
	else:
		#error message on submit button
		driver.find_element_by_class_name("btn").click()
		driver.execute_script("window.alert('%s')"%message)
		time.sleep(3)
	    
	time.sleep(10)

	#Close driver
	driver.close()
