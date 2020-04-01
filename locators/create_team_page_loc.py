from selenium.webdriver.common.by import By

class CreateTeamPageLocators(object):
    TEAM_POPUP_CLOSE_ICON = (By.XPATH, "//*[name()='svg' and contains(@class,'close-icon')]")
    TEAM_POPUP_HEADER = (By.XPATH, "//div[contains(@data-caption, 'Новая команда')]")
    TEAM_NAME = (By.XPATH, "//div[contains(text(), 'Имя команды')]/following-sibling::input")
    INVITE_PHONE = (By.XPATH, "//input[@type='tel']")
    INVITE_FIRSTNAME = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    INVITE_LASTNAME = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    CREATE_TEAM_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать команду')]")
    TEAM_ERROR_MSG = (By.XPATH, "//div[@class='team-creation__error']")
    LOADER_ICON = (By.XPATH, "//div[@class='v-spinner' and @style!='display: none;']")
