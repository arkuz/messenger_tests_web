from time import sleep
from helpers.tools import split_phone

from locators.login_page_loc import LoginPageLocators

from pages.base_page import BasePage
from pages.user_profile_page import UserProfilePage


class LoginPage(BasePage):

    login_page_loc = LoginPageLocators()


    # выполнить смену страны
    def change_country(self, country):
        self.go_to_main_page()
        self._country_cmb_click()
        self._input_country(country)
        self._country_item_click()

    # выбрать страну и нажать закрыть в попапе
    def change_country_and_close_popup(self, country):
        self.go_to_main_page()
        self._country_cmb_click()
        self._input_country(country)
        self._country_popup_close()


    # ввести и отправить код
    def send_code(self, phone):
        self.go_to_main_page()
        self._input_phone(phone)
        self._send_code_btn_click()

    # ввести номер и отправить код
    def login(self, phone, code):
        self.send_code(phone)
        self._input_code(code)
        return self._login_btn_click()


    # получить текущее имя страны на странице входа
    def get_country_name(self):
        return self.wait.element_to_be_clickable(*self.login_page_loc.COUNTRY_CMB).text


    # получить текущий код телефона страны на странице входа
    def get_country_code(self):
        return self.wait.element_to_be_clickable(*self.login_page_loc.COUNTRY_CODE).text


    # получить текст ошибки при неверном номере телефона на странице входа
    def get_invalid_numder_text(self):
        return self.wait.element_to_be_clickable(*self.login_page_loc.LOGIN_ERROR_MESSAGE).text


    # получить текст сообщения при повторной отправке кода
    def get_resend_code_message(self):
        return self.wait.element_to_be_clickable(*self.login_page_loc.RESEND_CODE_MESSAGE).text


    # -------------- внутренние методы --------------

    # нажать на комбобокс со странами на странице входа
    def _country_cmb_click(self):
        country_cmb = self.wait.element_to_be_clickable(*self.login_page_loc.COUNTRY_CMB)
        country_cmb.click()


    # ввести название страны в попапе
    def _input_country(self, country):
        country_search = self.wait.element_to_be_clickable(*self.login_page_loc.COUNTRY_SEARCH_INPUT)
        country_search.clear()
        country_search.send_keys(country)


    # нажать на страну в попапе
    def _country_item_click(self):
        if self.is_browser_firefox():
            sleep(1)
        country_item = self.wait.element_to_be_clickable(*self.login_page_loc.COUNTRY_ITEM)
        country_item.click()
        sleep(1)


    # закрыть попап выбора страны
    def _country_popup_close(self):
        country_item = self.wait.element_to_be_clickable(*self.login_page_loc.COUNTRY_CLOSE_BTN)
        country_item.click()
        sleep(1)


    # ввести номер телефона
    def _input_phone(self, phone):
        phone_input = self.driver.find_element(*self.login_page_loc.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(split_phone(phone))


    # нажать кнопку отправки кода
    def _send_code_btn_click(self):
        send_code_btn = self.driver.find_element(*self.login_page_loc.SEND_CODE_BTN)
        send_code_btn.click()


    # нажать кнопку повторной отправки кода
    def _resend_code_link_click(self):
        resend_code_link = self.wait.element_to_be_clickable(*self.login_page_loc.RESEND_CODE_LINK)
        resend_code_link.click()


    # ввести код
    def _input_code(self, code):
        code_input = self.wait.element_to_be_clickable(*self.login_page_loc.CODE_INPUT)
        code_input.clear()
        code_input.send_keys(code)


    # нажать кнопку логина
    def _login_btn_click(self):
        login_btn = self.wait.element_to_be_clickable(*self.login_page_loc.LOGIN_BTN)
        login_btn.click()
        return UserProfilePage(self.driver)
