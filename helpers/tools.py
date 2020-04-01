import os
import json
import random
import string
import re
from time import sleep


def get_project_path(path):
    """ Функция возвращает путь до корневой папки проекта """
    proj_name = 'messenger_tests_web'
    while os.path.split(path)[1] != proj_name:
        path = os.path.split(path)[0]
    return path


def generate_random_string(length=17):
    """ Функция генерирует случайный набор букв """
    name = ''
    for _ in range(1, length):
        name += random.choice(string.ascii_letters)
    return name


def is_items_exist_in_list_of_dict(list, key, value):
    """ Функция принимает на вход список словарей
    и ищет пару key, value перебирая все словари в списке"""
    for el in list:
        for k,v in el.items():
            if k == key and v == value:
                return True
    return False


def print_formatted_json(_json, ensure_ascii=True, indent=2):
    """ Функция печатает отформатированный json. Используется для отладки """
    print(json.dumps(_json, ensure_ascii=ensure_ascii, indent=indent))


def delete_all_teams(api_obj):
    """ Функция удаляет все команды юзера. Используется для отладки
     Возвращает True если все команды удалены """
    resp = api_obj.me().json()
    for item in resp['result']['teams']:
        api_obj.delete_team(item['uid'])
    resp = api_obj.me().json()
    return len(resp['result']['teams']) == 0


def get_datetime_iso_string(dt):
    """
    Функция возвращает строку в формате ISO
    dt типа datetime.datetime
    """
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def save_screenshot(driver, path):
    """
    Функция сохраняет скриншот браузера в папку
    """
    fn = os.environ.get('PYTEST_CURRENT_TEST')
    fn = re.findall(r'(.+)(\s\(teardown\))', fn)[0][0]
    fn = prepare_screenshot_name(fn)
    fn = os.path.join(path, os.path.basename(fn))
    driver.get_screenshot_as_file(os.path.join(get_project_path(__file__), fn))


def prepare_screenshot_name(fn):
    """
    Функция модифицирует имя теста для сохранения скриншота
    """
    match = re.findall(r'(.*)(\[.*\])', fn)
    if match:
        name = match[0][0]
        sub_hash = hash(match[0][1])
        fn = name.replace(':', '_') + f'{sub_hash}.png'
    else:
        fn = fn.replace(':', '_') + '.png'
    return fn


def split_phone(phone):
    if phone.find('+7') != -1:
        phone = phone[2:]
    return phone


def get_team_uid_from_url(driver, attempt=10):
    at = 0
    while at < attempt:
        team_uid = re.findall(r'[\w]{8}[-][\w]{4}[-][\w]{4}[-][\w]{4}[-][\w]{12}', driver.current_url)
        if team_uid:
            return team_uid[0]
        sleep(1)
        at += 1
