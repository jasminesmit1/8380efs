import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Customer_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def add_customer(self):
        user = "instructor"
        pwd = "maverick1a"
        id = "12343"
        name = "Richard Smith"
        address = "1111 Wirt St"
        city = "Omaha"
        state = "NE"
        zipcode = "68134"
        email = "rsmith000@gmail.com"
        cell = "531-333-3333"
        driver = self.driver
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_link_text('Login').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[1]/li[2]/a").click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/a/span').click()
        # driver.implicitly_wait(20)
        elem = driver.find_element_by_id('id_cust_number')
        drp = Select(elem)
        drp.select_by_visible_text(id)
        elem = driver.find_element_by_id('id_name')
        elem.send_keys(name)
        elem = driver.find_element_by_id('id_address')
        elem.send_keys(address)
        elem = driver.find_element_by_id('id_city')
        elem.send_keys(city)
        elem = driver.find_element_by_id('id_state')
        elem.send_keys(state)
        elem = driver.find_element_by_id('id_zipcode')
        elem.send_keys(zipcode)
        elem = driver.find_element_by_id('id_email')
        elem.send_keys(email)
        elem = driver.find_element_by_id('id_cell_phone')
        elem.send_keys(cell)
        time.sleep(3)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        time.sleep(3)
        elem = driver.find_element_by_link_text('Logout').click()

    def customer_edit_delete(self):
        driver = self.driver
        user = "instructor"
        pwd = "maverick1a"
        new_cell= "531-222-2222"
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[1]/li[2]/a").click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tbody/tr[2]/td[9]/a').click()
        elem = driver.find_element_by_id('id_cell_phone')
        elem.send_keys(new_cell)
        time.sleep(3)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        time.sleep(2)
        elem = driver.find_element_by_link_text('Logout').click()

    def viewPortfolio(self):
        driver = self.driver
        user = "instructor"
        pwd = "maverick1a"
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[1]/li[2]/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr[3]/td[11]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_link_text('Logout').click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
