#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/python3-browser-tests-on-a-raspberry-pi-with-firefox-virtualdisplay-selenium-and-pytest/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

profile = webdriver.FirefoxProfile()
profile.native_events_enabled = False
driver = webdriver.Firefox(profile)
driver.set_page_load_timeout(60)

driver.get("http://www.duckduckgo.com")
# print(driver.page_source.encode('utf-8'))

# get the search textbox
search_field = driver.find_element_by_id("search_form_input_homepage")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Running a WordPress blog locally on a Raspberry Pi with WP-Duplicator")
search_field.submit()

result_list = driver.find_elements_by_class_name("result")
results = [tmp.text for tmp in result_list]

assert any(["knight-of-pi" in text for text in results]) == True

driver.quit()