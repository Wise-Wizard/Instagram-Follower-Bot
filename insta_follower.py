import os
from dotenv import load_dotenv
load_dotenv(".env")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
DRIVER_PATH = "C:/Users/Saransh/Desktop/Money Tools/Python Projects/chromedriver-win64/chromedriver.exe"

ACCOUNT = "hyuna_inc"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
service = Service(executable_path=DRIVER_PATH)
op = webdriver.ChromeOptions()
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=op, service=service, keep_alive=True)
    def login(self):
        self.driver.get(url="https://www.instagram.com/")
        pass
    def find_followers(self):
        pass
    def follow(self):
        pass   
