from time import sleep

from locators.user_profile_page_loc import UserProfilePageLocators

from pages.base_page import BasePage



class UserProfilePage(BasePage):

    user_profile_page_loc = UserProfilePageLocators()

    # Заполнить имя, фамилию и перейти к созданию команды
    def fill_user_fields_and_go_next(self, firstname, lastname):
        self._input_firstname(firstname)
        self._input_lastname(lastname)
        return self._create_team_btn_click()

    # получить приветственный текст на данной странице
    def get_hello_text(self):
         return self.wait.element_to_be_clickable(*self.user_profile_page_loc.HELLO_DIV).text


    # -------------- внутренние методы --------------


    # ввести имя
    def _input_firstname(self, text):
        firstname = self.wait.element_to_be_clickable(*self.user_profile_page_loc.FIRSTNAME_INPUT)
        self.clear_input_with_keyboard(firstname)
        firstname.send_keys(text)


    # ввести фамилию
    def _input_lastname(self, text):
        lastname = self.wait.element_to_be_clickable(*self.user_profile_page_loc.LASTNAME_INPUT)
        self.clear_input_with_keyboard(lastname)
        lastname.send_keys(text)


    # нажать кнопку для создания команды
    def _create_team_btn_click(self):
        create_team_btn = self.wait.element_to_be_clickable(*self.user_profile_page_loc.CREATE_TEAM_BTN)
        create_team_btn.click()
        from pages.team_profile_page import TeamProfilePage
        return TeamProfilePage(self.driver)
