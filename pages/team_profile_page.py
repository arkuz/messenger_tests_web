from time import sleep

from locators.team_profile_page_loc import TeamProfilePageLocators

from pages.base_page import BasePage



class TeamProfilePage(BasePage):

    team_profile_page_loc = TeamProfilePageLocators()

    # создание команды и вход в нее
    def create_team_and_enter(self, name):
        self._input_name(name)
        self._create_team_bnt_click()


    # вернуться на страницу профидя команды
    def back_to_user_profile_page(self):
        return self._user_profile_link_click()


    # -------------- внутренние методы --------------


    # ввести имя команды
    def _input_name(self, text):
        name = self.wait.element_to_be_clickable(*self.team_profile_page_loc.NAME_INPUT)
        self.clear_input_with_keyboard(name)
        name.send_keys(text)


    # нажать создать команду
    def _create_team_bnt_click(self):
        create_team = self.wait.element_to_be_clickable(*self.team_profile_page_loc.CREATE_TEAM_BTN)
        create_team.click()


    # выполнить переход к странице редактирования профиля
    def _user_profile_link_click(self):
        user_profile = self.wait.element_to_be_clickable(*self.team_profile_page_loc.USER_PROFILE_LINK)
        user_profile.click()
        from pages.user_profile_page import UserProfilePage
        return UserProfilePage(self.driver)
