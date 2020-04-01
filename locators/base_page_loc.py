from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOADING_INDICATOR = (By.XPATH,  "//div[@class='loading-indicator']")

