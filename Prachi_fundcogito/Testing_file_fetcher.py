
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver =webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login(self):
        username_get = "prachikolte25@gmail.com"
        password = "MY7NsWfXL2CYPWu!"
        sharefile_company_url = "https://fundcogito.sharefile.com"


        #self.driver.get(sharefile_company_url)
        self.driver.get(sharefile_company_url + "/dashboard")

        self.wait.until(element_to_be_clickable((By.ID, "credentials-email"))).send_keys(username_get)
        self.wait.until(element_to_be_clickable((By.ID, "credentials-password"))).send_keys(
            password)
        self.wait.until(element_to_be_clickable((By.ID, "start-button"))).click()



        text = self.wait.until(presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]/span'))).text
        self.assertEquals(text, "Hello Prachi")


if __name__ == '__main__':
    unittest.main()