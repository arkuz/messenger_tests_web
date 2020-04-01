import requests as req

from helpers.api import API
from helpers.tools import generate_random_string
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from pages.tutorial_page import TutorialPage


def __sms_login(url, phone):
    """
    endpoint /sms-login методом POST
    Вход по SMS. Отправляем SMS с кодом на телефон.
    """
    data = {'phone': phone}
    endpoint = '/sms-login'
    url += endpoint
    return req.post(url, data)


def __sms_auth(url, data):
    """
    endpoint /sms-auth методом POST
    Авторизация. Вводим код.
    Обязательные поля: code, device_id, phone, type
    В data передаем json
        data = {
            'phone': user['phone'],
            'code': user['code'],
            'device_id': user['device_id'],
            'type': user['type']
        }
    """
    endpoint = '/sms-auth'
    url += endpoint
    return req.post(url, data)


def __sms_cookieauth(url, phone, code):
    """
    endpoint /sms-cookieauth методом POST
    Авторизация. Отличие от просто sms-auth/: не требуется указывать устройство,
    не выдаётся токен, а просто выставляется кука, с которой можно ходить с запросами к API и коннектиться по ws.
    """
    data = {'phone': phone,
            'code': code}
    endpoint = '/sms-cookieauth'
    url += endpoint
    return req.post(url, data)


def __cookieauth_logout_get(url):
    """
    endpoint /cookieauth-logout методом GET
    Выход для /sms-cookieauth
    """
    endpoint = '/cookieauth-logout'
    url += endpoint
    return req.get(url)


def login_with_cookies(url, phone, code):
    """ Логин по куке """
    __sms_login(url, phone)
    resp = __sms_cookieauth(url, phone, code)
    return resp.cookies['otvauth']


def logout(url):
    """ Логаут для login_with_cookies """
    return __cookieauth_logout_get(url)


def login_with_token(url, data):
    """ Логин по токену
        data = {
            'phone': user['phone'],
            'code': user['code'],
            'device_id': user['device_id'],
            'type': user['type']
        } """
    __sms_login(url, data['phone'])
    resp = __sms_auth(url, data)
    return resp.json()['result']['token']


def login_another_user(url, phone, code):
    auth_cookies = login_with_cookies(url, phone, code)
    return API(url, auth_cookies, is_token_auth=False)


def gui_login(driver, phone, code, country='Russia'):
    login_page = LoginPage(driver)
    #login_page.change_country(country)
    login_page.login(phone, code)


def gui_first_login(driver, phone, code, country='Russia'):
    try:
        login_page = LoginPage(driver)
        #login_page.change_country(country)
        firstname = 'Селен'
        lastname = 'Автотестов'
        user_profile_page = login_page.login(phone, code)
        team_profile_page = user_profile_page.fill_user_fields_and_go_next(firstname, lastname)
        team_profile_page.create_team_and_enter(generate_random_string())
        tutorial_page = TutorialPage(driver)
        tutorial_page.close_tutorial_popup()
    except:
        pass


def add_auth_cookie(driver, url, api_url, phone, code):
    driver.get(url)
    cookie = login_with_cookies(api_url, phone, code)
    cookie_dict = {'name': 'otvauth', 'value': cookie}
    driver.add_cookie(cookie_dict)
    driver.refresh()
