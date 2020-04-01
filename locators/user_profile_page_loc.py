from selenium.webdriver.common.by import By


class UserProfilePageLocators(object):
    HELLO_DIV = (By.XPATH, "//div[contains(text(),'Сперва, давайте познакомимся')]")
    AVATAR_INPUT = (By.XPATH, "//input[@type='file']")
    FIRSTNAME_INPUT = (By.XPATH, "//div[contains(@data-placeholder,'Имя')]/input")
    LASTNAME_INPUT = (By.XPATH, "//div[contains(@data-placeholder,'Фамилия')]/input")
    CREATE_TEAM_BTN = (By.XPATH, "//button[contains(text(),'Перейти к созданию команды')]")
