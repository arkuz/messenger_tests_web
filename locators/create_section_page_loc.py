from selenium.webdriver.common.by import By

class CreateSectionPageLocators(object):
    POPUP_CLOSE_ICON = (By.XPATH, "//img[contains(@class,'close-icon')]")
    SECTION_NAME = (By.XPATH, "//input[contains(@placeholder, 'Название секции')]")
    INVITE_CONTACT_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите имя контакта')]")
    DROPDOWN_MEMBER_ITEM = (By.XPATH, "//div[@class='contacts-picker']//li[@class='item selected']")
    TARGET_PRIORITY_SECTION = (By.XPATH, "//li[@class='target']")
    CREATE_SECTION_BUTTON = (By.XPATH, "//button[contains(text(),'Создать')]")
    SAVE_EDIT_SECTION_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить изменения')]")
    CLOSE_SECTION_BUTTON = (By.XPATH, "//button[contains(text(),'Закрыть')]")
    DELETE_SECTION_BUTTON = (By.XPATH, "//button[contains(text(),'Удалить секцию')]")
    CONFIRM_DELETE_SECTION_BUTTON = (By.XPATH, "//button[contains(text(),'Вы уверены')]")
    SECTION_ERROR_MSG = (By.XPATH, "//input[contains(@placeholder, 'Название секции')]/following-sibling::div[contains(@class,'error-message')]")
