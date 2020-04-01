from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    COUNTRY_CMB = (By.XPATH, "//*[contains(@class,'onboarding-profile__content')]/*[contains(@class,'login__text--country')]")
    COUNTRY_CODE = (By.XPATH, "//*[contains(@class,'login__text--country-code')]")
    COUNTRY_SEARCH_INPUT = (By.XPATH, "//*[contains(@class,'search-input')]/input")
    COUNTRY_ITEM = (By.XPATH, "//*[contains(@class,'country-code__item')]")
    COUNTRY_CLOSE_BTN = (By.XPATH, "//button[contains(text(),'Закрыть')]")


    PHONE_INPUT = (By.XPATH, "//input[@type='tel']")
    SEND_CODE_BTN = (By.XPATH, "//button[contains(text(),'Выслать пароль')]")
    RESEND_CODE_LINK = (By.XPATH, "//span[contains(text(),'Отправить ещё раз')]")
    RESEND_CODE_MESSAGE = (By.XPATH, "//div[contains(@class,'login__resend-report')]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//div[@class='login__error']")
    CODE_INPUT = (By.XPATH, "//input[contains(@placeholder,'Код из смс')]")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Войти')]")

    def get_country_item_by_name(self, name):
        return (By.XPATH, f"//*[contains(@class,'country-code__item') and contains(@data-name,'{name}')]")
