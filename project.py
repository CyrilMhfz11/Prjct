import csv,sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


username=sys.argv[1]
password=sys.argv[2]

path="/Users/cyrilmahfouz/chromedriver_mac_arm64/chromedriver"
service= Service(executable_path=path)
driver=webdriver.Chrome(service=service)

url="https://myportal.lau.edu.lb/Pages/studentPortal.aspx"
driver.get(url)

username_input=driver.find_element("xpath",
                                    "//input[@type='text' and @id='username' and @name='username']")

password_input=driver.find_element("xpath",
                                    "//input[@type='password' and @id='password']")

button_input=driver.find_element("xpath",
                                  "//input[@type='submit' and @value='Log In']")

username_input.send_keys(username)
password_input.send_keys(password)
button_input.click()

print("logged in")

banner=driver.find_element("xpath",
                           "//a[@href='https://banweb.lau.edu.lb/' and @target='_blank']")

banner.click()

print("banner access")
driver.switch_to.window(driver.window_handles[1])

student_services=driver.find_element("xpath", 
                                     "//a[@href='/prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu']")


student_services.click()
print("access to student services")

registration_input=driver.find_element("xpath",
                                       "//a[@href='/prod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu']")
registration_input.click()
print("registration acccessed")

look_up_input=driver.find_element("xpath",
                                  "//a[@href='/prod/bwskfcls.p_sel_crse_search']")
look_up_input.click()
print("look up classes accessed")

dropdown_path=driver.find_element("xpath",
                                  "//select[@name='p_term']")
dropdown_menu=Select(dropdown_path)
dropdown_menu.select_by_value('202410')

dropdown_button=driver.find_element("xpath",
                                    "//input[@type='submit' and @value='Submit']")

dropdown_button.click()
print("selection of the term done")

advance_s_but=driver.find_element("xpath",
                                  "//input[@type='submit' and @name='SUB_BTN' and @value='Advanced Search']")
advance_s_but.click()
print("advanced clicked")

subject_path=driver.find_element("xpath",
                                 "//select[@name='sel_subj' and @size='10']")
subject_menu=Select(subject_path)
subject_menu.select_by_value('CSC')

campus_path=driver.find_element("xpath",
                           "//select[@name='sel_camp']")
campus=Select(campus_path)
campus_option=campus.options[0]
driver.execute_script("arguments[0].setAttribute('disabled','disabled')", campus_option)
campus.select_by_index(2)


selection_search_but=driver.find_element("xpath",
                                         "//input[@type='submit' and @name='SUB_BTN']")
selection_search_but.click()
print("selection completed")

headers=[]
data=[]

#for the headers
heads=driver.find_element("xpath","//table[contains(@class, 'datadisplaytable')]")
head1=heads.find_elements("xpath","//th[contains(@class, 'ddheader')]")

for head in head1:
    headers.append(head.text)
