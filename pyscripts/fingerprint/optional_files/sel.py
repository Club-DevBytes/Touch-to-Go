#!/usr/bin/env python


from selenium import webdriver

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

driver.get('http://inventwithpython.com')
browser = webdriver.Firefox()


os.system('fswebcam -r 1280x720 --no-banner ~/pimage/allah.jpg')