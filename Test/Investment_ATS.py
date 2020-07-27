import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Investment_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def add_investment(self):
        user = "instructor"
        pwd = "maverick1a"
        id = "12345"
        category = "Fund"
        descrip = "Mutual of Omaha Fund"
        acquired_value = 500
        acquired_date = "4/17/2018"
        recent_value = 1700
        recent_date = "05/29/2020"
        driver = self.driver
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_link_text('Login').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[1]/li[3]/a").click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/a/span').click()
        # driver.implicitly_wait(20)
        elem = driver.find_element_by_id('id_customer')
        drp = Select(elem)
        drp.select_by_visible_text(id)
        elem = driver.find_element_by_id('id_category')
        elem.send_keys(category)
        elem = driver.find_element_by_id('id_description')
        elem.send_keys(descrip)
        elem = driver.find_element_by_id('id_acquired_value')
        elem.send_keys(acquired_value)
        elem = driver.find_element_by_id('id_acquired_date')
        elem.send_keys(acquired_date)
        elem = driver.find_element_by_id('id_recent_value')
        elem.send_keys(recent_value)
        elem = driver.find_element_by_id('id_recent_date')
        elem.send_keys(recent_date)
        time.sleep(3)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        time.sleep(3)
        elem = driver.find_element_by_link_text('Logout').click()

    def investment_edit_delete(self):
        driver = self.driver
        user = "instructor"
        pwd = "maverick1a"
        new_category = "Property"
        new_description = "Berkshire Hathaway Property"
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div/div[2]/a").click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a').click()
        elem = driver.find_element_by_id('id_category')
        elem.send_keys(new_category)
        elem = driver.find_element_by_id('id_description')
        elem.send_keys(new_description)
        time.sleep(3)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tbody/tr[4]/td[8]/a').click()
        elem = driver.find_element_by_link_text('Logout').click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
