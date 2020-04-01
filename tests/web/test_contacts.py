import pytest
import os
from selenium import webdriver
from time import sleep


from helpers.readers import read_yaml
import helpers.const as const
from helpers.browser_setup import config_and_run_browser
from helpers.tools import save_screenshot, generate_random_string
from helpers.auth import add_auth_cookie, gui_first_login


from pages.header_page import HeaderPage
from pages.contacts_page import ContactsPage


class TestsContacts:
    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))

    driver: webdriver
    driver = None

    api_url = config['api']['url']
    web = config['web']
    user = config['users']['user1']
    phone = user['phone']
    code = user['code']

    def setup_class(self):
        self.driver = config_and_run_browser(self.web)

        gui_first_login(self.driver, self.phone, self.code)

        add_auth_cookie(self.driver,
                        self.web['site_url'],
                        self.config['api']['url'],
                        self.phone,
                        self.code)

     
    def teardown_method(self):
        save_screenshot(self.driver, 'report')
        self.driver.refresh()


    def teardown_class(self):
        self.driver.close()


    # функция добавления новой секции
    def add_section(self, name=''):
        header_page = HeaderPage(self.driver)
        contacts_page = header_page.contacts_click()
        sections_before = contacts_page.get_sections_names_list()
        create_section_page = contacts_page.open_create_section_popup()
        section_name = name if name else generate_random_string(10)
        create_section_page.input_section_name(section_name)
        create_section_page.create_section_btn_click()
        contacts_page.wait_until_sections_list_updated(sections_before)
        created_section_name = contacts_page.get_sections_names_list()[0]
        assert section_name.upper() == created_section_name


    def add_section_with_invite(self, section_name='', member_name='Bot'):
        header_page = HeaderPage(self.driver)
        contacts_page = header_page.contacts_click()
        sections_before = contacts_page.get_sections_names_list()
        create_section_page = contacts_page.open_create_section_popup()
        section_name = section_name if section_name else generate_random_string(10)
        create_section_page.input_section_name(section_name)
        create_section_page.invite_member(member_name)
        create_section_page.create_section_btn_click()
        contacts_page.wait_until_sections_list_updated(sections_before)
        # проверяем, что новая секция появилась
        created_section_name = contacts_page.get_sections_names_list()[0]
        assert section_name.upper() == created_section_name
        # проверяем, что контакт в этой секции
        section = contacts_page.get_sections()[0]
        contacts_page.click_on_section(section)
        contacts = contacts_page.get_contacts(section)
        members = contacts_page.get_contacts_names_list(contacts)
        assert member_name in members


    @pytest.mark.positive
    def test_create_new_section(self):
        self.add_section()


    @pytest.mark.positive
    def test_create_new_section_with_invite(self):
        member_name = 'Bot'
        self.add_section_with_invite(member_name=member_name)


    @pytest.mark.positive
    def test_create_new_section_with_move_position(self):
        header_page = HeaderPage(self.driver)
        contacts_page = header_page.contacts_click()
        sections_before = contacts_page.get_sections_names_list()
        create_section_page = contacts_page.open_create_section_popup()
        section_name = generate_random_string(10)
        create_section_page.input_section_name(section_name)
        create_section_page.move_section_to_down()
        create_section_page.create_section_btn_click()
        contacts_page.wait_until_sections_list_updated(sections_before)
        created_section_name = contacts_page.get_sections_names_list()[1]
        assert section_name.upper() == created_section_name


    @pytest.mark.negative
    @pytest.mark.parametrize('name,msg', [
        ('', 'Обязательное поле'),
        (generate_random_string(210), 'Убедитесь, что это значение содержит не более 200 символов')
    ])
    def test_create_new_section_invalid(self, name, msg):
        header_page = HeaderPage(self.driver)
        contacts_page = header_page.contacts_click()
        create_section_page = contacts_page.open_create_section_popup()
        create_section_page.input_section_name(name)
        create_section_page.create_section_btn_click()
        if self.web['env'] != 'local':
            sleep(2)
        text = create_section_page.get_error_text()
        assert msg in text


    @pytest.mark.positive
    def test_edit_section_name(self):
        # создаем новую секцию
        self.add_section()
        # изменяем секцию
        contacts_page = ContactsPage(self.driver)
        sections_before = contacts_page.get_sections_names_list()
        edit_section = contacts_page.get_sections()[0]
        edit_section_page = contacts_page.edit_section_click(edit_section)
        new_section_name = generate_random_string(10)
        edit_section_page.input_section_name(new_section_name)
        edit_section_page.save_edit_section_btn_click()
        contacts_page.wait_until_sections_list_updated(sections_before)
        edited_section_name = contacts_page.get_sections_names_list()[0]
        assert new_section_name.upper() == edited_section_name


    @pytest.mark.positive
    def test_edit_section_member(self):
        # создаем новую секцию
        self.add_section()
        # изменяем секцию
        contacts_page = ContactsPage(self.driver)
        edit_section = contacts_page.get_sections()[0]
        edit_section_page = contacts_page.edit_section_click(edit_section)
        member_name = 'Bot'
        edit_section_page.invite_member(member_name)
        edit_section_page.save_edit_section_btn_click()
        # ждем для обновления фронтенда
        sleep(3)
        # проверяем, что контакт в этой секции
        section = contacts_page.get_sections()[0]
        contacts_page.click_on_section(section)
        contacts = contacts_page.get_contacts(section)
        members = contacts_page.get_contacts_names_list(contacts)
        assert member_name in members


    @pytest.mark.positive
    def test_delete_section_from_edit_popup(self):
        # создаем новую секцию
        self.add_section()
        # удаляем секцию из попапа изменения секции
        contacts_page = ContactsPage(self.driver)
        sections_before = contacts_page.get_sections_names_list()
        deleted_section_name = contacts_page.get_sections_names_list()[0]
        edit_section = contacts_page.get_sections()[0]
        edit_section_page = contacts_page.edit_section_click(edit_section)
        edit_section_page.delete_section_btn_click()
        contacts_page.wait_until_sections_list_updated(sections_before)
        sections_after = contacts_page.get_sections_names_list()
        assert deleted_section_name not in sections_after


    @pytest.mark.positive
    def test_delete_section_from_menu(self):
        # создаем новую секцию
        self.add_section()
        # удаляем секцию из контекстного меню
        contacts_page = ContactsPage(self.driver)
        sections_before = contacts_page.get_sections_names_list()
        deleted_section_name = sections_before[0]
        contacts_page.delete_section_click(contacts_page.get_sections()[0])
        text = contacts_page.get_delete_popup_text().lower()
        assert deleted_section_name.lower() in text
        contacts_page.confirm_delete_btn_click()
        contacts_page.wait_until_sections_list_updated(sections_before)
        sections_after = contacts_page.get_sections_names_list()
        assert deleted_section_name not in sections_after


    @pytest.mark.negative
    def test_delete_section_with_contacts_from_menu_invalid(self):
        member_name = 'Bot'
        self.add_section_with_invite(member_name=member_name)
        # попытка удалить секцию из контекстного меню
        contacts_page = ContactsPage(self.driver)
        sections_before = contacts_page.get_sections_names_list()
        contacts_page.delete_section_click(contacts_page.get_sections()[0])
        assert 'Для удаления этой секции переместите все контакты в другую' in contacts_page.get_delete_popup_text()
        contacts_page.cancel_delete_btn_click()
        sleep(3)
        sections_after = contacts_page.get_sections_names_list()
        assert sections_before == sections_after


    # Selenium не двигает элемент
    @pytest.mark.skip
    @pytest.mark.positive
    def test_move_section_to_down(self):
        header_page = HeaderPage(self.driver)
        contacts_page = header_page.contacts_click()
        moved_section = contacts_page.get_sections()[0]
        sections_names_before = contacts_page.get_sections_names_list()
        #contacts_page.hold_and_move_section_to_down1(moved_section, contacts_page.get_sections()[1])
        contacts_page.hold_and_move_section_to_down(moved_section)
        contacts_page.confirm_move_btn_click()
        contacts_page.wait_until_sections_elements_updated(sections_names_before)
        sections_names_after = contacts_page.get_sections_names_list()
        assert sections_names_before[0] == sections_names_after[1]
        assert sections_names_before[1] == sections_names_after[0]
