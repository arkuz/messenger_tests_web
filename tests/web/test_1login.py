import pytest
import os
from selenium import webdriver
import requests


from helpers.readers import read_yaml
import helpers.const as const
from helpers.browser_setup import config_and_run_browser
from helpers.tools import save_screenshot, generate_random_string

from pages.login_page import LoginPage
from pages.header_page import HeaderPage


class TestsLogin:
    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))

    driver: webdriver
    driver = None

    web = config['web']
    user = config['users']['user1']
    phone = user['phone']
    code = user['code']

    def setup_class(self):
        self.driver = config_and_run_browser(self.web)


    def setup_method(self):
        self.driver.delete_cookie("otvauth")


    def teardown_method(self):
        save_screenshot(self.driver, 'report')


    def teardown_class(self):
        self.driver.close()


    @pytest.mark.positive
    def test_change_country(self):
        country = 'Angola'
        code = '+244'
        login_page = LoginPage(self.driver)
        login_page.change_country(country)
        assert country == login_page.get_country_name()
        assert code == login_page.get_country_code()


    @pytest.mark.positive
    def test_change_country_close_popup(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_main_page()
        country = login_page.get_country_name()
        code = login_page.get_country_code()
        login_page.change_country_and_close_popup('Angola')
        # обход ошибки в gitlab ulr Россия != Russia
        country_after = login_page.get_country_name()
        if country == 'Россия' or country == 'Russia':
            assert country_after == 'Россия' or country_after == 'Russia'
        else:
            assert country == country_after
        assert code == login_page.get_country_code()


    @pytest.mark.negative
    def test_input_invalid_number(self):
        country = 'Russia'
        phone = '123'
        login_page = LoginPage(self.driver)
        #login_page.change_country(country)
        login_page.send_code(phone)
        assert 'Некорректный номер телефона' == login_page.get_invalid_numder_text()


    @pytest.mark.positive
    def test_resend_code(self):
        country = 'Russia'
        phone = self.phone
        login_page = LoginPage(self.driver)
        #login_page.change_country(country)
        login_page.send_code(phone)
        login_page._resend_code_link_click()
        assert 'Повторный запрос кода возможен через' in login_page.get_resend_code_message()


    @pytest.mark.positive
    def test_input_valid_number_back_prev_page(self):
        country = 'Russia'
        phone = self.phone
        code = self.code
        firstname = 'Селен'
        lastname = 'Автотестов'
        login_page = LoginPage(self.driver)
        #login_page.change_country(country)
        user_profile_page = login_page.login(phone, code)
        team_profile_page = user_profile_page.fill_user_fields_and_go_next(firstname, lastname)
        user_profile_page = team_profile_page.back_to_user_profile_page()
        assert 'Сперва, давайте познакомимся!' == user_profile_page.get_hello_text()


    @pytest.mark.positive
    def test_z_input_valid_number(self):
        country = 'Russia'
        phone = self.phone
        code = self.code
        firstname = 'Селен'
        lastname = 'Автотестов'
        team_name = f'login_{generate_random_string(6)}'
        login_page = LoginPage(self.driver)
        #login_page.change_country(country)
        user_profile_page = login_page.login(phone, code)
        team_profile_page = user_profile_page.fill_user_fields_and_go_next(firstname, lastname)
        team_profile_page.create_team_and_enter(team_name)
        header_page = HeaderPage(self.driver)
        assert team_name == header_page.get_team_switcher_name()
