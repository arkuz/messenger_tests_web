from locators.create_section_page_loc import CreateSectionPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class CreateSectionPage(BasePage):

    create_section_page_loc = CreateSectionPageLocators()


    # ввести имя участника в поисковое поле
    def invite_member(self, name):
        input_name = self.wait.element_to_be_clickable(*self.create_section_page_loc.INVITE_CONTACT_INPUT)
        input_name.clear()
        input_name.send_keys(name)
        item = self.wait.element_to_be_clickable(*self.create_section_page_loc.DROPDOWN_MEMBER_ITEM)
        item.click()


    # получить текст ошибки
    def get_error_text(self):
        return self.wait.element_to_be_clickable(*self.create_section_page_loc.SECTION_ERROR_MSG).text


    # ввести название секции в попапе
    def input_section_name(self, name):
        input_name = self.wait.element_to_be_clickable(*self.create_section_page_loc.SECTION_NAME)
        input_name.clear()
        input_name.send_keys(name)


    # нажать на кнопку создать секцию
    def create_section_btn_click(self):
        create_section_btn = self.wait.element_to_be_clickable(*self.create_section_page_loc.CREATE_SECTION_BUTTON)
        create_section_btn.click()


    # нажать на кнопку сохранить изменения
    def save_edit_section_btn_click(self):
        create_section_btn = self.wait.element_to_be_clickable(*self.create_section_page_loc.SAVE_EDIT_SECTION_BUTTON)
        create_section_btn.click()


    # нажать на кнопку удалить секцию
    def delete_section_btn_click(self):
        delete_section_btn = self.wait.element_to_be_clickable(*self.create_section_page_loc.DELETE_SECTION_BUTTON)
        delete_section_btn.click()
        confirm_delete_btn = self.wait.element_to_be_clickable(*self.create_section_page_loc.CONFIRM_DELETE_SECTION_BUTTON)
        confirm_delete_btn.click()


    # нажать клавишу "вниз" в окне приоритета секций
    def move_section_to_down(self):
        ActionChains(self.driver).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
