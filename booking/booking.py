import booking.constants as const
import os
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Booking(webdriver.Chrome):
    def __int__(self, driver_path='C:\Selenium_Driver'):
        self.driver_path = driver_path
        # self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.teardown:
           self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


