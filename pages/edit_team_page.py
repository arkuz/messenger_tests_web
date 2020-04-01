from locators.edit_team_page_loc import EditTeamPageLocators
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys


class EditTeamPage(BasePage):

    edit_team_page_loc = EditTeamPageLocators


    def save_team_with_new_name(self, name):
        self._input_name(name)
        self._create_team_btn_click()


    def close_popup(self):
        close_popup_btn = self.wait.element_to_be_clickable(*self.edit_team_page_loc.CLOSE_ICON)
        close_popup_btn.click()
        self.wait.invisibility_of_element_located(*self.edit_team_page_loc.CLOSE_ICON)


    def cancel_popup(self):
        close_popup_btn = self.wait.element_to_be_clickable(*self.edit_team_page_loc.CANCEL_TEAM_BTN)
        close_popup_btn.click()
        self.wait.invisibility_of_element_located(*self.edit_team_page_loc.CANCEL_TEAM_BTN)


    def delete_team(self):
        self._delete_team_btn_click()
        self._confirm_delete_team_btn_click()


    def get_error_text(self):
        return self.wait.element_to_be_clickable(*self.edit_team_page_loc.TEAM_ERROR_MSG).get_attribute('data-error')


    # -------------- внутренние методы --------------


    # ввести название команды в попапе
    def _input_name(self, name):
        input_name = self.wait.element_to_be_clickable(*self.edit_team_page_loc.NAME_INPUT)
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(name)


    # нажать на кнопку сохранить
    def _create_team_btn_click(self):
        create_team_btn = self.wait.element_to_be_clickable(*self.edit_team_page_loc.SAVE_TEAM_BTN)
        create_team_btn.click()


    # нажать на кнопку удалить команду
    def _delete_team_btn_click(self):
        create_team_btn = self.wait.element_to_be_clickable(*self.edit_team_page_loc.DELETE_TEAM_BTN)
        create_team_btn.click()


    # нажать на кнопку удалить в попапе подтверждения
    def _confirm_delete_team_btn_click(self):
        create_team_btn = self.wait.element_to_be_clickable(*self.edit_team_page_loc.DELETE_TEAM_CONFIRM)
        create_team_btn.click()


    # закрыть окно по кнопке "Отмена"
    def _close_popup_btn_click(self):
        close_popup_btn = self.wait.element_to_be_clickable(*self.edit_team_page_loc.CLOSE_ICON)
        close_popup_btn.click()
