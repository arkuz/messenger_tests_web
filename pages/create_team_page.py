from locators.create_team_page_loc import CreateTeamPageLocators
from pages.base_page import BasePage
from helpers.tools import split_phone
from time import sleep


class CreateTeamPage(BasePage):

    create_team_page_loc = CreateTeamPageLocators()


    def create_team(self, name):
        self._input_name(name)
        self._create_team_btn_click()


    def create_team_with_invite(self, name, phone, firstname, lastname):
        self._input_name(name)
        self._fill_invite_fields(split_phone(phone), firstname, lastname)
        self._create_team_btn_click()

    def close_popup(self):
        close_popup_btn = self.wait.element_to_be_clickable(*self.create_team_page_loc.TEAM_POPUP_CLOSE_ICON)
        close_popup_btn.click()
        self.wait.invisibility_of_element_located(*self.create_team_page_loc.TEAM_POPUP_CLOSE_ICON)


    def get_error_text(self):
        return self.wait.element_to_be_clickable(*self.create_team_page_loc.TEAM_ERROR_MSG).text


    # -------------- внутренние методы --------------


    # ввести название команды в попапе
    def _input_name(self, name):
        input_name = self.wait.element_to_be_clickable(*self.create_team_page_loc.TEAM_NAME)
        input_name.clear()
        input_name.send_keys(name)


    # нажать на кнопку создать команду
    def _create_team_btn_click(self):
        create_team_btn = self.wait.element_to_be_clickable(*self.create_team_page_loc.CREATE_TEAM_BUTTON)
        create_team_btn.click()


    # заполнить поля для приглашения
    def _fill_invite_fields(self, phone, firstname, lastname):
        input_phone = self.wait.element_to_be_clickable(*self.create_team_page_loc.INVITE_PHONE)
        input_firstname = self.wait.element_to_be_clickable(*self.create_team_page_loc.INVITE_FIRSTNAME)
        input_lastname = self.wait.element_to_be_clickable(*self.create_team_page_loc.INVITE_LASTNAME)
        input_phone.clear()
        input_phone.send_keys(phone)
        input_firstname.clear()
        input_firstname.send_keys(firstname)
        input_lastname.clear()
        input_lastname.send_keys(lastname)


    # закрыть окно по кнопке "Отмена"
    def _close_popup_btn_click(self):
        close_popup_btn = self.wait.element_to_be_clickable(*self.create_team_page_loc.TEAM_POPUP_CLOSE_ICON)
        close_popup_btn.click()
