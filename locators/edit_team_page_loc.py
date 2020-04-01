from selenium.webdriver.common.by import By

class EditTeamPageLocators(object):
    NAME_INPUT = (By.XPATH, "//input[contains(@class,'name-input__input')]")
    DELETE_TEAM_BTN = (By.XPATH, "//button[contains(text(),'Удалить команду')]")
    CANCEL_TEAM_BTN = (By.XPATH, "//button[contains(text(),'Отмена')]")
    SAVE_TEAM_BTN = (By.XPATH, "//button[contains(text(),'Сохранить изменения')]")
    TEAM_ERROR_MSG = (By.XPATH, "//div[contains(@data-error,'Возникли проблемы с изменением команды')]")
    CLOSE_ICON = (By.XPATH, "//*[name()='svg' and contains(@class,'close-icon')]")

    # в попапе подтверждения удаления
    DELETE_TEAM_CONFIRM = (By.XPATH, "//button[contains(text(),'Удалить')]")
