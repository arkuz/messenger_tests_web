from selenium.webdriver.common.by import By


class TeamProfilePageLocators(object):
    AVATAR_INPUT = (By.XPATH, "//input[@type='file']")
    NAME_INPUT = (By.XPATH, "//div[contains(@data-placeholder,'Имя команды')]/input")
    CREATE_TEAM_BTN = (By.XPATH, "//button[contains(text(),'Создать команду')]")
    USER_PROFILE_LINK = (By.XPATH, "//div[contains(@data-caption,'Изменить Ваши данные')]")
