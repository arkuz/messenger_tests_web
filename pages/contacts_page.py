from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from locators.contacts_page_loc import ContactsPageLocators
from pages.base_page import BasePage


class ContactsPage(BasePage):

    contacts_page_loc = ContactsPageLocators()


    # выполнить действия, которые открывают попап создания секции
    def open_create_section_popup(self):
        self.plus_btn_click()
        add_section = self.wait.element_to_be_clickable(*self.contacts_page_loc.ADD_SECTION_BTN)
        add_section.click()
        from pages.create_section_page import CreateSectionPage
        return CreateSectionPage(self.driver)


    # нажать "+" в контактах
    def plus_btn_click(self):
        plus_btn = self.wait.element_to_be_clickable(*self.contacts_page_loc.PLUS_BTN)
        plus_btn.click()


    # нажать на секцию
    def click_on_section(self, element):
        element.click()


    # получить список секций
    def get_sections(self):
        return self.driver.find_elements(*self.contacts_page_loc.SECTION_ITEM)


    # получить список контактов в секции
    def get_contacts(self, element):
        return element.find_elements(*self.contacts_page_loc.SECTION_ITEM_MEMBER_NAME)


    # получить список названий контактов
    def get_contacts_names_list(self, contacts):
        names_list = []
        for el in contacts:
            names_list.append(el.text)
        return names_list


    # получить список названий секций
    def get_sections_names_list(self):
        names_list = []
        elems = self.driver.find_elements(*self.contacts_page_loc.SECTION_ITEM_TEXT)
        for el in elems:
            names_list.append(el.text)
        return names_list


    # получить количество секций
    def get_sections_count(self):
        return len(self.get_sections_names_list())


    # ждем пока список секций изменит количество или порядок элементов
    def wait_until_sections_list_updated(self, sec_before, attempt=10):
        at = 0
        while at < attempt:
            if sec_before != self.get_sections_names_list():
                return
            sleep(1)
            at += 1
        raise AssertionError('Sections list is not updated')


    # ждем пока список секций изменит количество или порядок элементов
    def wait_until_sections_elements_updated(self, sec_before, attempt=10):
        at = 0
        while at < attempt:
            sec_after = self.get_sections()
            print(sec_before == sec_after)
            if sec_before != sec_after:
                return
            sleep(1)
            at += 1
        raise AssertionError('Sections elements is not updated')


    # нажать "Редактировать секцию" в меню секции
    def edit_section_click(self, element):
        menu = element.find_element(*self.contacts_page_loc.SECTION_MENU)
        menu.click()
        edit = element.find_element(*self.contacts_page_loc.SECTION_EDIT)
        edit.click()
        from pages.create_section_page import CreateSectionPage
        return CreateSectionPage(self.driver)


    # нажать "Удалить секцию" в меню секции
    def delete_section_click(self, element):
        menu = element.find_element(*self.contacts_page_loc.SECTION_MENU)
        menu.click()
        delete = element.find_element(*self.contacts_page_loc.SECTION_DELETE)
        delete.click()


    # Получить текст в попапе подтверждения удаления секции
    def get_delete_popup_text(self):
        return self.driver.find_element(*self.contacts_page_loc.TEXT_SECTION_POPUP).text


    # Нажать "Удалить" в попапе подтверждения удаления
    def confirm_delete_btn_click(self):
        btn = self.wait.element_to_be_clickable(*self.contacts_page_loc.DELETE_SECTION_POPUP_BTN)
        btn.click()


    # Нажать "Отмена" в попапе подтверждения удаления
    def cancel_delete_btn_click(self):
        btn = self.wait.element_to_be_clickable(*self.contacts_page_loc.CANCEL_SECTION_POPUP_BTN)
        btn.click()


    # Нажать "Переместить" в попапе подтверждения перемещения
    def confirm_move_btn_click(self):
        btn = self.wait.element_to_be_clickable(*self.contacts_page_loc.MOVE_SECTION_POPUP_BTN)
        btn.click()


    # перетащить секцию вниз в списке секций
    def hold_and_move_section_to_down(self, element):
        height = element.size['height']
        #ActionChains(self.driver).click_and_hold(element).move_by_offset(5, 50).release().perform()
        ActionChains(self.driver).click_and_hold(element).perform()
        sleep(1)
        ActionChains(self.driver).move_by_offset(0, 0).perform()
        sleep(2)
        ActionChains(self.driver).move_by_offset(0, 50).perform()
        sleep(1)
        ActionChains(self.driver).release().perform()
