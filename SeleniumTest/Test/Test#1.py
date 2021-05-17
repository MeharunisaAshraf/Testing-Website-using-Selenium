import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Administrator\PycharmProjects\SeleniumTest\Drivers\chromedriver.exe")
driver.set_page_load_timeout(100)

'''website'''
# Page1-->Home
driver.get("https://www.thesparksfoundationsingapore.org/")
# Title-->1
print(driver.title)
time.sleep(1)
# Logo-->2
logo = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a/img")
if (logo.is_displayed()):
    print("logo is displayed")
else:
    print("logo is not visible")
time.sleep(1)
if (logo.is_enabled()):
    print("logo is enabled")
else:
    print("logo is not enabled")

time.sleep(1)
# Navigation Bar-->3
nav = driver.find_element_by_class_name("navbar")
if (nav.is_displayed()):
    print("Navigation bar is displayed")
else:
    print("Navigation bar is not visible")
time.sleep(1)
# About Us-->4
about = driver.find_element_by_link_text("About Us")
print("About Us page : ", about.is_displayed())
time.sleep(1)
# Drop Down Menu-->5
dropdown = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a/span')
dropdown.click()
print("Clicked Drop Down Menu")
time.sleep(1)
# Page2-->Mission & Vision
mission = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')
mission.click()
print("Mission & Vision page")
time.sleep(1)
# Getting current URL source code
get_source = driver.page_source
# Text you want to search-->6
mission_statement = "Our Mission Statement"
if (mission_statement in get_source):
    print("Statement is displayed")
else:
    print("Statement bar is not visible")
time.sleep(1)
# Scroll to below
driver.execute_script("window.scrollBy(0,2000)", "")
print("Scrolled below")
time.sleep(1)
# Facebook Icon-->7
facebook = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/a')
if (facebook.is_displayed()):
    print("Facebook icon is displayed")
else:
    print("Facebook icon is not visible")
time.sleep(1)
if (facebook.is_enabled()):
    print("Facebook icon is enabled")
else:
    print("Facebook icon is not enabled")
time.sleep(1)
# Page3-->Executive Team
team = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[4]')
team.click()
print("Team page")
time.sleep(1)
# Founder responsive img-->8
founder = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/h3/span')
print("Founder's profile present : ", founder.is_enabled())
time.sleep(1)
# Copyright Reserved Text-->9
copyright = driver.find_element_by_class_name('copyright-wthree')
if (copyright.is_displayed()):
    print("Copyrights Reserved")
else:
    print("Copyrights not Reserved")
time.sleep(1)
# Page4-->AI in Education
driver.get('https://www.thesparksfoundationsingapore.org/links/ai-in-education/')
print("AI in Education")
time.sleep(1)
# Learn More Button-->10
AIinfo = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/a')
print("AI detailed information given : ", AIinfo.is_enabled())

# Page5-->Info
driver.get('https://thesparksfoundation.info')
print("INFO page")
time.sleep(1)
logo1 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/a/img')
if (logo1.is_displayed()):
    print("Logo is displayed on this page too")
else:
    print("Logo is not displayed on other page")

time.sleep(1)
driver.quit()
