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
from pages.chat_list_page import ChatListPage


class TestsTeams:
    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))

    driver: webdriver
    driver = None

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


    @pytest.mark.positive
    def test_create_new_team(self):
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        new_team_name = generate_random_string()
        create_team_page.create_team(new_team_name)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name


    @pytest.mark.positive
    def test_create_new_team_with_invite(self):
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        new_team_name = generate_random_string()
        user2 = self.config['users']['user2']
        firstname = 'Invated'
        lastname = 'Man1'
        create_team_page.create_team_with_invite(
            new_team_name,
            user2['phone'],
            firstname,
            lastname)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name
        chat_list_page = ChatListPage(self.driver)
        name = f'{firstname} {lastname}'
        assert chat_list_page.get_chat_item_by_name(name)
    
    
    @pytest.mark.positive
    def test_cancel_create_new_team(self):
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        create_team_page._close_popup_btn_click()
        header_page.team_switcher_click()
        current_name = header_page.get_team_switcher_name()
        assert old_team_name == current_name


    @pytest.mark.negative
    @pytest.mark.parametrize('name,msg', [
        ('', 'Обязательное поле'),
        (generate_random_string(105), 'Убедитесь, что это значение содержит не более 100 символов')
    ])
    def test_team_name_invalid(self, name, msg):
        header_page = HeaderPage(self.driver)
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        create_team_page.create_team(name)
        assert msg in create_team_page.get_error_text()


    @pytest.mark.positive
    def test_change_name_team(self):
        # создаем новую команду
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        new_team_name = generate_random_string()
        create_team_page.create_team(new_team_name)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name
        # изменяем имя команды и сохраняем
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        edit_team_page = header_page.settings_team_switcher_click()
        new_team_name = generate_random_string()
        edit_team_page.save_team_with_new_name(new_team_name)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name


    @pytest.mark.negative
    @pytest.mark.parametrize('name,msg', [
        ('', 'Возникли проблемы с изменением команды'),
        (generate_random_string(105), 'Возникли проблемы с изменением команды')
    ])
    def test_edit_team_name_invalid(self, name, msg):
        # создаем новую команду
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        new_team_name = generate_random_string()
        create_team_page.create_team(new_team_name)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name
        # вводим некорректное имя и пытаемся сохранитьсохраняем
        header_page.team_switcher_click()
        edit_team_page = header_page.settings_team_switcher_click()
        edit_team_page.save_team_with_new_name(name)
        assert msg in edit_team_page.get_error_text()


    @pytest.mark.positive
    def test_delete_team(self):
        # создаем новую команду
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        new_team_name = generate_random_string()
        create_team_page.create_team(new_team_name)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name
        # удаляем команду
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        edit_team_page = header_page.settings_team_switcher_click()
        edit_team_page.delete_team()
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert old_team_name != current_name


    @pytest.mark.positive
    def test_cancel_delete_team(self):
        # создаем новую команду
        header_page = HeaderPage(self.driver)
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        create_team_page = header_page.create_team_switcher_click()
        new_team_name = generate_random_string()
        create_team_page.create_team(new_team_name)
        current_name = header_page.get_team_switcher_name_with_wait(old_team_name)
        assert new_team_name == current_name
        # отмен удаления команды
        old_team_name = header_page.get_team_switcher_name()
        header_page.team_switcher_click()
        edit_team_page = header_page.settings_team_switcher_click()
        edit_team_page._close_popup_btn_click()
        header_page.team_switcher_click()
        current_name = header_page.get_team_switcher_name()
        assert old_team_name == current_name
