# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def isThereMyMailAtKMUTTOffice():
    result = None
    try:
        # driver = webdriver.Remote("http://firefox/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
        driver = webdriver.Remote(command_executor="http://firefox/wd/hub",desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
    except Exception as e:
        raise e
    # driver = webdriver.Firefox()
    driver.implicitly_wait(30)
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
