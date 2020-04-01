import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from helpers.wait import Wait
from helpers.readers import read_yaml
import helpers.const as const

from locators.base_page_loc import BasePageLocators
from locators.login_page_loc import LoginPageLocators


class BasePage(object):

    driver: webdriver
    driver = None
    wait = None

    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))

    base_page_loc = BasePageLocators()
    login_page_loc = LoginPageLocators()


    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)


    def is_browser_firefox(self):
        return self.config['web']['browser'] == 'Firefox'


    def clear_input_with_keyboard(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)


    def go_to_main_page(self):
        self.driver.get(self.config['web']['site_url'])


    # получаем имя элемента на протяжении max_sec и возвращаем его, если оно не равно old_str
    # это хак для обхода перезагрузки страницы
    def get_name_of_elem_with_wait(self, by, loc, old_str, max_sec=10):
        for i in range(1, max_sec + 1):
            current_str = self.wait.element_to_be_clickable(by, loc).text
            if old_str != current_str:
                return current_str
            sleep(1)
        raise ValueError('Текст элемента не изменился')


    def wait_loading_indicator_hide(self):
        self.wait.invisibility_of_element_located(*self.base_page_loc.LOADING_INDICATOR)


    def refresh(self):
        self.driver.refresh()
