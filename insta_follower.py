import os
import time
from dotenv import load_dotenv
load_dotenv(".env")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
DRIVER_PATH = "C:/Users/Saransh/Desktop/Money Tools/Python Projects/chromedriver-win64/chromedriver.exe"

ACCOUNT = "hyuna_inc"
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
service = Service(executable_path=DRIVER_PATH)
op = webdriver.ChromeOptions()
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=op, service=service, keep_alive=True)
    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        login_username = WebDriverWait(self.driver, 10).until\
            (ec.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        login_username.send_keys(USER)

        login_password = WebDriverWait(self.driver, 10).until\
            (ec.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
        login_password.send_keys(PASSWORD)
        WebDriverWait(self.driver, 10).until\
            (ec.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))).click()
        WebDriverWait(self.driver, 20).until\
            (ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()

        WebDriverWait(self.driver, 20).until\
            (ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()
    def find_followers(self):
        self.driver.get(url=f"https://www.instagram.com/{ACCOUNT}/followers")
        # followers = WebDriverWait(self.driver, 10).until\
        #     (ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')))
        # followers.click()
        modal = WebDriverWait(self.driver, 10).until\
            (ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')))
        time.sleep(4)    
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        
    def follow(self):
        all_followers = self.driver.find_elements(By.CSS_SELECTOR, "button")
        for follower in all_followers:
            if follower.text == "Follow":
                webdriver.ActionChains(self.driver).move_to_element(follower).click(follower).perform()
                time.sleep(1)
