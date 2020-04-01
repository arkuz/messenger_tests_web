import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from helpers.api import API
from helpers.readers import read_yaml
import helpers.const as const
import helpers.auth as auth


config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))
url = config['api']['url']

def login_user(config, user_number):
    phone = config['users'][f'user{user_number}']['phone']
    code = config['users'][f'user{user_number}']['code']
    auth_cookies = auth.login_with_cookies(url, phone, code)
    return API(url, auth_cookies, is_token_auth=False), phone


def delete_all_teams_for_all_users():
    user_count = 4
    user_index = 1
    while user_index <= user_count:
        api_obj, phone = login_user(config, user_index)
        resp = api_obj.kill_my_own_teams().json()
        if not resp['result']['teams']:
            print(f'Deleted all teams for user{user_index} - {phone}')
        else:
            print(f'Error for user{user_index}')
            exit(1)
        user_index += 1

    print('All teams deleted')
    exit(0)


delete_all_teams_for_all_users()

