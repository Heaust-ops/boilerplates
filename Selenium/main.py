from selenium import webdriver
from time import sleep
from config import *
from os import path
script_path = path.dirname(path.abspath(__file__))

class generic_bot():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=script_path+r'/geckodriver')




bot = generic_bot()
