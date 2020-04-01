from time import sleep

from locators.header_page_loc import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    header_page_loc = HeaderPageLocators()

    def notification_dialog_close(self):
        notification_dialog_btn = self.wait.element_to_be_clickable(*self.header_page_loc.NOTOFICATION_DIALOG_CLOSE)
        notification_dialog_btn.click()


    def get_team_switcher_name(self):
        return self.wait.element_to_be_clickable(*self.header_page_loc.TEAM_SWITCHER_TEXT).text


    def team_switcher_click(self):
        team_switcher = self.wait.element_to_be_clickable(*self.header_page_loc.TEAM_SWITCHER)
        team_switcher.click()


    def create_team_switcher_click(self):
        team_switcher = self.wait.element_to_be_clickable(*self.header_page_loc.CREATE_TEAM_SWITCHER_ITEM)
        team_switcher.click()
        from pages.create_team_page import CreateTeamPage
        return CreateTeamPage(self.driver)


    def settings_team_switcher_click(self):
        team_switcher = self.wait.element_to_be_clickable(*self.header_page_loc.TEAM_SETTINGS_ICON)
        team_switcher.click()
        from pages.edit_team_page import EditTeamPage
        return EditTeamPage(self.driver)


    # получаем имя элемента на протяжении max_sec и возвращаем его, если оно не равно old_str
    # это хак для обхода перезагрузки страницы
    def get_team_switcher_name_with_wait(self, old_str, max_sec=10):
        return self.get_name_of_elem_with_wait(*self.header_page_loc.TEAM_SWITCHER_TEXT, old_str, max_sec)


    def contacts_click(self):
        contacts = self.wait.element_to_be_clickable(*self.header_page_loc.CONTACTS_BTN)
        contacts.click()
        from pages.contacts_page import ContactsPage
        return ContactsPage(self.driver)
