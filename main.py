from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import string
import random

# initialize webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--disable-translate")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

# repeat the process
while True:
    # go to signup page
    driver.get("https://www.roblox.com/account/signupredir")
    
    # wait for the signup form to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "MonthDropdown")))
    
    # fill in the birthday dropdown
    birthday = driver.find_element_by_id("MonthDropdown")
    birthday.click()
    birthday.send_keys("May")
    
    birthday = driver.find_element_by_id("DayDropdown")
    birthday.click()
    birthday.send_keys("01")
    
    birthday = driver.find_element_by_id("YearDropdown")
    birthday.click()
    birthday.send_keys("2000")
    
    # fill in username field
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    driver.find_element_by_id("signup-username").send_keys(username)
    
    # fill in password field
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    driver.find_element_by_id("signup-password").send_keys(password)
    
    # click signup button
    driver.find_element_by_id("signup-button").click()
    
    # prompt user to restart or quit the program
    print("Press Enter to restart the process or type 'quit' to exit.")
    user_input = input()
    if user_input.lower() == "quit":
        break
    else:
        driver.delete_all_cookies()
        continue
