from selenium.webdriver.common.by import By

class ContactsPageLocators(object):
    PLUS_BTN = (By.XPATH, "//div[contains(@class,'contacts__head')]//div[@class='popup-trigger']")
    ADD_SECTION_BTN = (By.XPATH, "//li[@data-content='Добавить секцию']")
    ADD_CONTACT_BTN = (By.XPATH, "//li[@data-content='Добавить контакт']")

    SECTION_ITEM = (By.XPATH, "//div[contains(@class, 'section-wrapper')]")
    SECTION_ITEM_TEXT = (By.XPATH, "//div[@class='section']//div[contains(@class,'name')]")
    SECTION_ITEM_MEMBER_NAME = (By.XPATH, ".//div[contains(@class, 'o-sub-heading')]")

    SECTION_MENU = (By.XPATH, ".//*[name()='svg']")
    SECTION_EDIT = (By.XPATH, ".//li[contains(@data-content,'Редактировать секцию')]")
    SECTION_DELETE = (By.XPATH, ".//li[contains(@data-content,'Удалить секцию')]")

    # кнопки в попапе подтверждения удаления
    TEXT_SECTION_POPUP = (By.XPATH, "//div[@class='modal-question']/div")
    DELETE_SECTION_POPUP_BTN = (By.XPATH, "//button[contains(text(),'Удалить')]")
    CANCEL_SECTION_POPUP_BTN = (By.XPATH, "//button[contains(text(),'Отмена')]")
    MOVE_SECTION_POPUP_BTN = (By.XPATH, "//button[contains(text(),'Переместить')]")
