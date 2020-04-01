from selenium.webdriver.common.by import By

class HeaderPageLocators(object):
    NOTOFICATION_DIALOG_CLOSE = (By.XPATH, "//div[@class='notification-bar']/span[@class='nb-close']")
    TEAM_SWITCHER = (By.XPATH, "//div[contains(@class,'team-switcher o-flex-row')]")
    TEAM_SWITCHER_TEXT = (By.XPATH, "//div[contains(@class,'team-switcher o-flex-row')]/span")
    TEAM_SETTINGS_ICON = (By.XPATH, "//div[contains(@class, 'team-item__controls')]//*[name()='svg'][1]")
    CREATE_TEAM_SWITCHER_ITEM = (By.XPATH, "//div[contains(@data-caption, 'Создать новую команду')]")

    TASKS_BTN = (By.XPATH, "//li[@data-key='tasks-block']")
    CONTACTS_BTN = (By.XPATH, "//li[@data-key='contacts']")
    FILES_BTN = (By.XPATH, "//li[@data-key='file-browser']")

