import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Stock_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        user = "instructor"
        pwd = "maverick1a"
        id = "12345"
        symbol = "wal"
        name = "Walmart"
        shares = 500
        price = 1500
        date = "05/18/1991"
        driver = self.driver
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_link_text('Login').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div/div[2]/a").click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/a/span').click()
        # driver.implicitly_wait(20)
        elem = driver.find_element_by_id('id_customer')
        drp = Select(elem)
        drp.select_by_visible_text(id)
        elem = driver.find_element_by_id('id_symbol')
        elem.send_keys(symbol)
        elem = driver.find_element_by_id('id_name')
        elem.send_keys(name)
        elem = driver.find_element_by_id('id_shares')
        elem.send_keys(shares)
        elem = driver.find_element_by_id('id_purchase_price')
        elem.send_keys(price)
        elem = driver.find_element_by_id('id_purchase_date')
        elem.send_keys(date)
        time.sleep(3)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        time.sleep(3)
        elem = driver.find_element_by_link_text('Logout').click()



    def stock_edit_delete(self):
        driver = self.driver
        user = "instructor"
        pwd = "maverick1a"
        new_date = "05/18/1999"
        driver.get("https://efs-site2020.herokuapp.com")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div/div[2]/a").click()
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a').click()
        elem = driver.find_element_by_id('id_purchase_date')
        elem.send_keys(new_date)
        time.sleep(3)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tbody/tr[4]/td[8]/a').click()
        elem = driver.find_element_by_link_text('Logout').click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
