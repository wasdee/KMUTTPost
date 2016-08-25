# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class hello(unittest.TestCase):
    result = None
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hermes.kmutt.ac.th/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_3ini(self):
        driver = self.driver
        driver.get(self.base_url + "/post/")
        driver.find_element_by_id("txtSearch").clear()
        driver.find_element_by_id("txtSearch").send_keys(u"ณัฐชนน")
        driver.find_element_by_css_selector("#lbSearch > b").click()
        try:
            self.assertTrue(self.is_element_present(By.XPATH, "//table[@id='dgLetter']/tbody/tr[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

def isThereMyMailAtKMUTTOffice(remote=None,ip=None,port=None):
    result = None
    # driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    base_url = "http://hermes.kmutt.ac.th/"
    verificationErrors = []
    accept_next_alert = True
    driver.get(base_url + "/post/")
    driver.find_element_by_id("txtSearch").clear()
    driver.find_element_by_id("txtSearch").send_keys(u"ณัฐชนน")
    driver.find_element_by_css_selector("#lbSearch > b").click()
    try:
        result = True
        driver.find_element(By.XPATH, "//table[@id='dgLetter']/tbody/tr[2]//td[2]")
        # a = driver.find_element_by_xpath("//table[@id='dgLetter']/tbody/tr[2]//td[2]")
        # repr(a)
    except NoSuchElementException as e:
        result = False
    finally:
        driver.quit()
    return result

if __name__ == "__main__":
    # unittest.main()
    # hello.run()
    # print(isThereMyMailAtKMUTTOffice())
    print("iloveu")