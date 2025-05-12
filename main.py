from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-search-engine-choice-screen')

        prefs = {"download.default_directory": os.getcwd()}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, User_Name, Password):
        self.driver.get("https://demoqa.com/login")
        user_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

        user_name.send_keys(User_Name)
        password.send_keys(Password)
        login.click()

    def fill_form(self, full_name, email, current_address, permanent_address):
        Element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        Element.click()

        Text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        Text.click()

        Full_Name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        Email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        Current_Address = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        Permanent_Address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        button = self.driver.find_element(By.ID, 'submit')

        Full_Name.send_keys(full_name)
        Email.send_keys(email)
        Current_Address.send_keys(current_address)
        Permanent_Address.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", button)

    def download(self):
        Upload_and_Download = self.driver.find_element(By.ID, 'item-7')
        self.driver.execute_script("arguments[0].click()", Upload_and_Download)

        Download_file = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", Download_file)

    def close(self):
        self.driver.quit()
