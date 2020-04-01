import requests as req
import json


class API(object):
    """ Класс описывает endpoints API """

    def __init__(self, url, token='', is_token_auth=True):
        """ Если is_token_auth = False, то token это кука,
         иначе token это токен пользователя.
         Дальше этот token подставляется в куки или в заголовок
         в обертках call_post_api и т.п. """
        self.url = url
        self.token = token
        self.is_token_auth = is_token_auth


    def set_token(self, token):
        """ Установить токен """
        self.token = token


    def call_post_api(self, url, data={}, params={}):
        """ Обертка над requests.post """
        headers = {}
        jar={}
        if self.is_token_auth:
            headers = {'Token': self.token}
        else:
            jar = req.cookies.RequestsCookieJar()
            jar.set('otvauth', self.token)
        resp = req.post(
            url,
            data=data,
            params=params,
            headers=headers,
            cookies=jar
        )
        return resp


    def call_post_api_with_file(self, url, path):
        """ Обертка над requests.post с использованием Multipart-Encoded """
        headers = {}
        jar = {}
        if self.is_token_auth:
            headers = {'Token': self.token}
        else:
            jar = req.cookies.RequestsCookieJar()
            jar.set('otvauth', self.token)
        files = {'file': open(path, 'rb')}
        resp = req.post(
            url,
            headers=headers,
            files=files,
            cookies=jar
        )
        return resp


    def call_get_api(self, url, params={}):
        """ Обертка над requests.get """
        headers = {}
        jar = {}
        if self.is_token_auth:
            headers = {'Token': self.token}
        else:
            jar = req.cookies.RequestsCookieJar()
            jar.set('otvauth', self.token)
        resp = req.get(
            url,
            params=params,
            headers=headers,
            cookies=jar
        )
        return resp


    def call_put_api(self, url, data={}, params={}):
        """ Обертка над requests.put """
        headers = {}
        jar = {}
        if self.is_token_auth:
            headers = {'Token': self.token}
        else:
            jar = req.cookies.RequestsCookieJar()
            jar.set('otvauth', self.token)
        resp = req.put(
            url,
            data=data,
            params=params,
            headers=headers,
            cookies=jar
        )
        return resp


    def call_delete_api(self, url, params={}, data={}):
        """ Обертка над requests.delete """
        headers = {}
        jar = {}
        if self.is_token_auth:
            headers = {'Token': self.token}
        else:
            jar = req.cookies.RequestsCookieJar()
            jar.set('otvauth', self.token)
        resp = req.delete(
            url,
            data=data,
            params=params,
            headers=headers,
            cookies=jar
        )
        return resp


    def kill_my_own_teams(self):
        """
        endpoint /kill_my_own_teams методом POST
        Endpoint только для внутренного использования
        Удаляет все команды пользователя
        """
        data = {'magic_phrase': "Take my money take my possession take my obsession. I don't need that shit!"}
        endpoint = '/kill_my_own_teams'
        url = self.url + endpoint
        return self.call_post_api(url, data=data)


    def ping_post(self, delay_sec=0):
        """
        endpoint /ping методом POST
        Просто проверка. Параметров нет.
        """
        if delay_sec <= 0:
            params = {}
        else:
            params = {'delay_sec': delay_sec}
        endpoint = '/ping'
        url = self.url + endpoint
        return self.call_post_api(url, params=params)


    def ping_get(self, delay_sec=0):
        """
        endpoint /ping методом GET
        Просто проверка. Параметров нет.
        """
        if delay_sec <= 0:
            params = {}
        else:
            params = {'delay_sec': delay_sec}
        endpoint = '/ping'
        url = self.url + endpoint
        return self.call_get_api(url, params)


    def time(self):
        """
        endpoint /time методом GET
        Время сервера
        """
        endpoint = '/time'
        url = self.url + endpoint
        return self.call_get_api(url)


    def countries(self):
        """
        endpoint /countries методом GET
        Список стран и кодов городов
        """
        endpoint = '/countries'
        url = self.url + endpoint
        return self.call_get_api(url)


    def sms_login(self, phone):
        """
        endpoint /sms-login методом POST
        Вход по SMS. Отправляем SMS с кодом на телефон.
        """
        data = {'phone': phone}
        endpoint = '/sms-login'
        url = self.url + endpoint
        return req.post(url, data)


    def sms_auth(self, data):
        """
        endpoint /sms-auth методом POST
        Авторизация. Вводим код.
        Обязательные поля: code, device_id, phone, type
        В data передаем json
        """
        endpoint = '/sms-auth'
        url = self.url + endpoint
        return req.post(url, data)


    def sms_cookieauth(self, phone, code):
        """
        endpoint /sms-cookieauth методом POST
        Авторизация. Отличие от просто sms-auth/: не требуется указывать устройство,
        не выдаётся токен, а просто выставляется кука, с которой можно ходить с запросами к API и коннектиться по ws.
        При создании объекта данного класса в этот метод token из конструктора не передается
        """
        data = {'phone': phone,
                'code': code}
        endpoint = '/sms-cookieauth'
        url = self.url + endpoint
        return req.post(url, data)


    def cookieauth_logout_post(self):
        """
        endpoint /cookieauth-logout методом POST
        Выход для /sms-cookieauth
        При создании объекта данного класса в этот метод token из конструктора не передается
        """
        endpoint = '/cookieauth-logout'
        url = self.url + endpoint
        return req.post(url)


    def cookieauth_logout_get(self):
        """
        endpoint /cookieauth-logout методом GET
        Выход для /sms-cookieauth
        При создании объекта данного класса в этот метод token из конструктора не передается
        """
        endpoint = '/cookieauth-logout'
        url = self.url + endpoint
        return req.get(url)


    def me(self):
        """
        endpoint /me методом GET
        Информация о текущем пользователе. То же самое, что возвращает вызов /sms-auth
        """
        endpoint = '/me'
        url = self.url + endpoint
        return self.call_get_api(url)


    def get_ui_settings(self):
        """
        endpoint /ui-settings методом GET
        Получить ui настройки текущего пользователя
        """
        endpoint = '/ui-settings'
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_ui_settings(self, data):
        """
        endpoint /ui-settings методом PUT
        Записать ui настройки текущего пользователя. Не более 16000 байт
        В data передаем json
        """
        endpoint = '/ui-settings'
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def add_device(self, data):
        """
        endpoint /devices методом POST
        Cоздание устройства. Если device_id уже есть, то не создаст новое устройство, а изменит существующее.
        Кроме того, для изменения требуется каждый раз посылать все поля
        В data передаем json
        """
        endpoint = '/devices'
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_devices(self):
        """
        endpoint /devices методом GET
        Cписок устройств без разбивки по страницам.
        То же, что и в вызове /me, только отдельно.
        """
        endpoint = '/devices'
        url = self.url + endpoint
        return self.call_get_api(url)


    def get_device(self, device_id):
        """
        endpoint /devices/{device_id} методом GET
        Информация об устройстве с указанным device_id
        """
        endpoint = '/devices/{device_id}'.format(
            device_id=device_id
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_device(self, device_id, data):
        """
        endpoint /devices/{device_id} методом PUT
        Изменение устройства с указанным device_id
        В data передаем json
        """
        endpoint = '/devices/{device_id}'.format(
            device_id=device_id
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_device(self, device_id):
        """
        endpoint /devices/{device_id} методом DELETE
        Удаление устройства с указанным device_id
        """
        endpoint = '/devices/{device_id}'.format(
            device_id=device_id
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def add_team(self, data):
        """
        endpoint /teams методом POST
        Создание команды (внутри contacts обязательно только одно поле — phone)
        В data передаем json
        """
        endpoint = '/teams'
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_teams(self):
        """
        endpoint /teams методом GET
        Список команд. Без разбивки по страницам
        То же, что отдаётся внутри вызова /me, только отдельно
        """
        endpoint = '/teams'
        url = self.url + endpoint
        return self.call_get_api(url)


    def upload_team_icon(self, team_uid, path):
        """
        endpoint /teams/{team_uid}/icons методом POST
        Загрузка или замена картинки команды
        В теле запроса должен быть multipart/form-data
        """
        endpoint = '/teams/{team_uid}/icons'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api_with_file(url, path)


    def delete_team_icon(self, team_uid):
        """
        endpoint /teams/{team_uid}/icons методом DELETE
        Удаление картинки, если есть
        """
        endpoint = '/teams/{team_uid}/icons'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_team(self, team_uid):
        """
        endpoint /teams/{team_uid} методом GET
        Информация о команде
        """
        endpoint = '/teams/{team_uid}'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_team(self, team_uid, data):
        """
        endpoint /teams/{team_uid} методом PUT
        Изменение команды
        В data передаем json
        """
        endpoint = '/teams/{team_uid}'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_team(self, team_uid):
        """
        endpoint /teams/{team_uid} методом DELETE
        Удаление команды
        """
        endpoint = '/teams/{team_uid}'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_team_usage(self, team_uid):
        """
        endpoint /teams/{team_uid}/usage методом GET
        Информация об использовании места
        """
        endpoint = '/teams/{team_uid}/usage'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def send_help(self, team_uid, email, text):
        """
        endpoint /teams/{team_uid}/help методом POST
        Запрос в поддержку
        """
        data = {'email': email,
                'text': text}
        endpoint = '/teams/{team_uid}/help'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def send_help_upload(self, team_uid, path):
        """
        endpoint /teams/{team_uid}/upload методом POST
        Загрузка файла. Фактически, требуется только для /teams/{team_uid}/help
        В теле запроса должен быть multipart/form-data
        """
        endpoint = '/teams/{team_uid}/upload'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api_with_file(url, path)


    def add_section(self, team_uid, data):
        """
        endpoint /teams/{team_uid}/sections методом POST
        Создание секции. Единственное обязательное поле при создании — name.
        Можно добавить поле move_before / move_after с UIDом другой секции, и секция встанет до / после указанной.
        {"name":"555","sort_ordering":0,"color":"#000","level":0}
        """
        endpoint = '/teams/{team_uid}/sections'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_sections(self, team_uid):
        """
        endpoint /teams/{team_uid}/sections методом GET
        Cписок секций. Без разбивки по страницам, т.к. секции нужны все
        """
        endpoint = '/teams/{team_uid}/sections'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def set_section_move_after(self, team_uid, section_uid, other_section_uid):
        """
        endpoint /teams/{team_uid}/sections/{section_uid}/move-after/{other_section_uid} методом POST
        Поставить секцию ПОСЛЕ указанной
        """
        endpoint = '/teams/{team_uid}/sections/{section_uid}/move-after/{other_section_uid}'.format(
            team_uid=team_uid,
            section_uid=section_uid,
            other_section_uid=other_section_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url)


    def set_section_move_before(self, team_uid, section_uid, other_section_uid):
        """
        endpoint /teams/{team_uid}/sections/{section_uid}/move-before/{other_section_uid} методом POST
        Поставить секцию ДО указанной
        """
        endpoint = '/teams/{team_uid}/sections/{section_uid}/move-before/{other_section_uid}'.format(
            team_uid=team_uid,
            section_uid=section_uid,
            other_section_uid=other_section_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url)


    def edit_section(self, team_uid, section_uid, data):
        """
        endpoint /teams/{team_uid}/sections/{section_uid} методом PUT
        Изменение секции. Возвращает то же, что и GET.
        Изменяемые поля: * name * sort_ordering * level - (не используется) * color
        """
        endpoint = '/teams/{team_uid}/sections/{section_uid}'.format(
            team_uid=team_uid,
            section_uid=section_uid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_section(self, team_uid, section_uid):
        """
        endpoint /teams/{team_uid}/sections/{section_uid} методом DELETE
        Удаление секции. Возвращает null, потому что секции удаляются полностью, без is_archive
        """
        endpoint = '/teams/{team_uid}/sections/{section_uid}'.format(
            team_uid=team_uid,
            section_uid=section_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def add_contacts(self, team_uid, data):
        """
        endpoint /teams/{team_uid}/contacts методом POST
        Cоздание (приглашение) контакта.
        Можно пригласить одного или несколько
        """
        endpoint = '/teams/{team_uid}/contacts'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_contacts(self, team_uid):
        """
        endpoint /teams/{team_uid}/contacts методом GET
        Cписок контактов. Без разбивки по страницам, здесь их может быть много
        """
        endpoint = '/teams/{team_uid}/contacts'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def upload_contact_icon(self, team_uid, contact_jid, path):
        """
        endpoint /teams/{team_uid}/contacts/{contact_jid}/icons методом POST
        Загрузка или замена картинки контакта
        В теле запроса должен быть multipart/form-data
        """
        endpoint = '/teams/{team_uid}/contacts/{contact_jid}/icons'.format(
            team_uid=team_uid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_post_api_with_file(url, path)


    def delete_contact_icon(self, team_uid, contact_jid):
        """
        endpoint /teams/{team_uid}/contacts/{contact_jid}/icons методом DELETE
        Удаление картинки, если есть.
        """
        endpoint = '/teams/{team_uid}/contacts/{contact_jid}/icons'.format(
            team_uid=team_uid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_contact(self, team_uid, contact_jid):
        """
        endpoint /teams/{team_uid}/contacts/{contact_jid} методом GET
        Информация о контакте
        """
        endpoint = '/teams/{team_uid}/contacts/{contact_jid}'.format(
            team_uid=team_uid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_contact(self, team_uid, contact_jid, data):
        """
        endpoint /teams/{team_uid}/contacts/{contact_jid} методом PUT
        Изменение контакта
        """
        endpoint = '/teams/{team_uid}/contacts/{contact_jid}'.format(
            team_uid=team_uid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_contact(self, team_uid, contact_jid):
        """
        endpoint /teams/{team_uid}/contacts/{contact_jid} методом DELETE
        Удаление контакта
        """
        endpoint = '/teams/{team_uid}/contacts/{contact_jid}'.format(
            team_uid=team_uid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def add_group(self, team_uid, data):
        """
        endpoint /teams/{team_uid}/groups методом POST
        Создание группы
        В data передаем json
        """
        endpoint = '/teams/{team_uid}/groups'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_groups(self, team_uid):
        """
        endpoint /teams/{team_uid}/groups методом GET
        Список групп. Без разбивки по страницам, здесь их может быть много
        """
        endpoint = '/teams/{team_uid}/groups'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def add_members(self, team_uid, group_jid, data):
        """
        endpoint /teams/{team_uid}/groups/{group_jid}/members методом POST
        Добавление участника группы, одного или несколько
        В data передаем json
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}/members'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_member_status(self, team_uid, group_jid, contact_jid):
        """
        endpoint /teams/{team_uid}/groups/{group_jid}/members/{contact_jid} методом GET
        Статус участника группы
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}/members/{contact_jid}'.format(
            team_uid=team_uid,
            group_jid=group_jid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_member_status(self, team_uid, group_jid, contact_jid, status):
        """
        endpoint /teams/{team_uid}/groups/{group_jid}/members/{contact_jid} методом PUT
        Изменение статуса участника группы
        """
        data = {'status': status}
        endpoint = '/teams/{team_uid}/groups/{group_jid}/members/{contact_jid}'.format(
            team_uid=team_uid,
            group_jid=group_jid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_member(self, team_uid, group_jid, contact_jid):
        """
        endpoint /teams/{team_uid}/groups/{group_jid}/members/{contact_jid} методом DELETE
        Удаление участника группы
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}/members/{contact_jid}'.format(
            team_uid=team_uid,
            group_jid=group_jid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def upload_group_icon(self, team_uid, group_jid, path):
        """
        endpoint /teams/{team_uid}/groups/{group_jid}/icons методом POST
        Загрузка или замена картинки группы
        В теле запроса должен быть multipart/form-data
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}/icons'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_post_api_with_file(url, path)


    def delete_group_icon(self, team_uid, group_jid):
        """
        endpoint /teams/{team_uid}/groups/{group_jid}/icons методом DELETE
        Удаление картинки, если есть
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}/icons'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_group(self, team_uid, group_jid):
        """
        endpoint /teams/{team_uid}/groups/{group_jid} методом GET
        Информация о группе
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_group(self, team_uid, group_jid, data):
        """
        endpoint /teams/{team_uid}/groups/{group_jid} методом PUT
        Изменение группы
        В data передаем json
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_group(self, team_uid, group_jid):
        """
        endpoint /teams/{team_uid}/groups/{group_jid} методом DELETE
        Удаление группы
        """
        endpoint = '/teams/{team_uid}/groups/{group_jid}'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_public_groups(self, team_uid):
        """
        endpoint /teams/{team_uid}/groups/public методом GET
        Список публичных групп (кроме тех, где запрашивающий и так уже состоит)
        """
        endpoint = '/teams/{team_uid}/groups/public'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def join_public_group(self, team_uid, group_jid):
        """
        endpoint /teams/{team_uid}/groups/public/{group_jid}/join методом POST
        Вступить в публичную группу. Без параметров
        """
        endpoint = '/teams/{team_uid}/groups/public/{group_jid}/join'.format(
            team_uid=team_uid,
            group_jid=group_jid
        )
        url = self.url + endpoint
        return self.call_post_api(url)


    def get_roster(self, team_uid):
        """
        endpoint /teams/{team_uid}/roster методом GET
        Все контакты и доступные группы (включая себя)
        """
        endpoint = '/teams/{team_uid}/roster'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def get_chat(self, team_uid, chat_jid):
        """
        endpoint /teams/{team_uid}/roster/{chat_jid} методом GET
        Информация о чате
        """
        endpoint = '/teams/{team_uid}/roster/{chat_jid}'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def delete_chat(self, team_uid, chat_jid):
        """
        endpoint /teams/{team_uid}/roster/{chat_jid} методом DELETE
        Отметка чата как hidden. Чат сам разотметится, как только в него написать
        """
        endpoint = '/teams/{team_uid}/roster/{chat_jid}'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_botcommands(self, team_uid, chat_jid):
        """
        endpoint /teams/{team_uid}/botcommands/{chat_jid} методом GET
        Список доступных в конкретном чате команд ботов
        Для разных участников этот список может быть разный.
        """
        endpoint = '/teams/{team_uid}/botcommands/{chat_jid}'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def linkscheck(self, team_uid, chat_jid, text):
        """
        endpoint /teams/{team_uid}/messages/{chat_jid}/linkscheck методом POST
        Предварительная проверка ссылок
        """
        data = {'text': text}
        endpoint = '/teams/{team_uid}/messages/{chat_jid}/linkscheck'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def send_msg_text(self, team_uid, chat_jid, data):
        """
        endpoint /teams/{team_uid}/messages/{chat_jid} методом POST
        Отправка текстового сообщения
        В data передаем json
        """
        endpoint = '/teams/{team_uid}/messages/{chat_jid}'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def send_msg_file(self, team_uid, chat_jid, path):
        """
        endpoint /teams/{team_uid}/messages/{chat_jid} методом POST
        Отправка файла
        """
        endpoint = '/teams/{team_uid}/messages/{chat_jid}'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_post_api_with_file(url, path)


    def send_msg_audio(self, team_uid, chat_jid, path):
        """
        endpoint /teams/{team_uid}/messages/{chat_jid} методом POST
        Отправка аудио
        """
        endpoint = '/teams/{team_uid}/messages/{chat_jid}/?type=audiomsg'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_post_api_with_file(url, path)


    # API для галереи


    def get_messages(self, team_uid, chat_jid, params={}):
        """
        endpoint /teams/{team_uid}/messages/{chat_jid} методом GET
        История сообщений. Отдаётся по 200 штук за раз
        """
        endpoint = '/teams/{team_uid}/messages/{chat_jid}'.format(
            team_uid=team_uid,
            chat_jid=chat_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url, params)


    def get_filtered_messages(self, team_uid, params={}):
        """
        endpoint /teams/{team_uid}/messages методом GET
        Поиск сообщений. Используется пагинация limit/offset
        Есть необязательные параметры
        """
        endpoint = '/teams/{team_uid}/messages'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url, params)


    def get_filtered_messages(self, team_uid, params={}):
        """
        endpoint /teams/{team_uid}/messages методом GET
        Поиск сообщений. Используется пагинация limit/offset
        Есть необязательные параметры
        """
        endpoint = '/teams/{team_uid}/messages'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url, params)


    def add_tasklist(self, team_uid, data):
        """
        endpoint /teams/{team_uid}/tasklist методом POST
        Создание списка задач команды. После создания возвращает ВСЕ списки, как при GET
        """
        endpoint = '/teams/{team_uid}/tasklist'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_tasklists(self, team_uid):
        """
        endpoint /teams/{team_uid}/tasklist методом GET
        Cписок задач команды. Без разбивки по страницам, т.к. списки нужны все
        """
        endpoint = '/teams/{team_uid}/tasklist'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def set_tasklist_move_after(self, team_uid, tasklist_uid, other_tasklist_uid):
        """
        endpoint /teams/{team_uid}/tasklist/{tasklist_uid}/move-after/{other_tasklist_uid} методом POST
        Поставить секцию ПОСЛЕ указанной
        """
        endpoint = '/teams/{team_uid}/tasklist/{tasklist_uid}/move-after/{other_tasklist_uid}'.format(
            team_uid=team_uid,
            tasklist_uid=tasklist_uid,
            other_tasklist_uid=other_tasklist_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url)


    def set_tasklist_move_before(self, team_uid, tasklist_uid, other_tasklist_uid):
        """
        endpoint /teams/{team_uid}/tasklist/{tasklist_uid}/move-before/{other_tasklist_uid} методом POST
        Поставить секцию ДО указанной
        """
        endpoint = '/teams/{team_uid}/tasklist/{tasklist_uid}/move-before/{other_tasklist_uid}'.format(
            team_uid=team_uid,
            tasklist_uid=tasklist_uid,
            other_tasklist_uid=other_tasklist_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url)


    def get_tasklist(self, team_uid, tasklist_uid):
        """
        endpoint /teams/{team_uid}/tasklist/{tasklist_uid} методом GET
        Информацию о списке задач
        """
        endpoint = '/teams/{team_uid}/tasklist/{tasklist_uid}'.format(
            team_uid=team_uid,
            tasklist_uid=tasklist_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_tasklist(self, team_uid, tasklist_uid, name):
        """
        endpoint /teams/{team_uid}/tasklist/{tasklist_uid} методом PUT
        Изменение списка задач. Возвращает то же, что и GET
        Изменяемое поле name
        """
        data = {'name': name}
        endpoint = '/teams/{team_uid}/tasklist/{tasklist_uid}'.format(
            team_uid=team_uid,
            tasklist_uid=tasklist_uid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_tasklist(self, team_uid, tasklist_uid):
        """
        endpoint /teams/{team_uid}/tasklist/{tasklist_uid} методом DELETE
        Удаление списка задач. Возвращает null, потому что списки задач удаляются полностью, без is_archive.
        """
        endpoint = '/teams/{team_uid}/tasklist/{tasklist_uid}'.format(
            team_uid=team_uid,
            tasklist_uid=tasklist_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def force_delete_tasklist(self, team_uid, tasklist_uid):
        """
        endpoint /teams/{team_uid}/tasklist/{tasklist_uid} методом DELETE
        Принудительное удаление списка задач
        Возвращает null, потому что списки задач удаляются полностью, без is_archive.
        """
        data = {'force': True}
        data = json.dumps(data)
        endpoint = '/teams/{team_uid}/tasklist/{tasklist_uid}'.format(
            team_uid=team_uid,
            tasklist_uid=tasklist_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url, data=data)


    def add_task(self, team_uid, data={}):
        """
        endpoint /teams/{team_uid}/tasks методом POST
        Создание задачи
        В data передаем json
        """
        endpoint = '/teams/{team_uid}/tasks'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_tasks(self, team_uid, params={}):
        """
        endpoint /teams/{team_uid}/tasks методом GET
        Список задач
        В params передаем словарь с параметрами
        """
        endpoint = '/teams/{team_uid}/tasks'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url, params)


    def add_observer(self, team_uid, task_jid, observer_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/observers методом POST
        Добавление наблюдателя в задачу
        """
        data = {'jid': observer_jid}
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/observers'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_observers(self, team_uid, task_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/observers методом GET
        Только наблюдатели задачи
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/observers'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def delete_observer(self, team_uid, task_jid, contact_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/observers/{contact_jid} методом DELETE
        Удаление наблюдателя из задачи
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/observers/{contact_jid}'.format(
            team_uid=team_uid,
            task_jid=task_jid,
            contact_jid=contact_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_task(self, team_uid, task_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid} методом GET
        Информация о задаче
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_task(self, team_uid, task_jid, data={}):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid} методом PUT
        Изменение задачи
        Поля collapsed, pinned, pinned_sort_order индивидуальные для каждого.
        В data передаем json
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_task(self, team_uid, task_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid} методом DELETE
        Удаление задачи
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def add_points_checklist(self, team_uid, task_jid, data):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/checklist методом POST
        Добавление пунктов чек-листа (одного или нескольких)
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/checklist'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_checklist(self, team_uid, task_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/checklist методом GET
        Получить чек-лист к задаче
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/checklist'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def get_checklist_point(self, team_uid, task_jid, item_uid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/checklist/{item_uid} методом GET
        Получить пункт чек-листа
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/checklist/{item_uid}'.format(
            team_uid=team_uid,
            task_jid=task_jid,
            item_uid=item_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def edit_checklist_point(self, team_uid, task_jid, item_uid, data={}):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/checklist/{item_uid} методом PUT
        Изменение пункта чек-листа
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/checklist/{item_uid}'.format(
            team_uid=team_uid,
            task_jid=task_jid,
            item_uid=item_uid
        )
        url = self.url + endpoint
        return self.call_put_api(url, data)


    def delete_checklist_point(self, team_uid, task_jid, item_uid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/checklist/{item_uid} методом DELETE
        Изменение пункта чек-листа
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/checklist/{item_uid}'.format(
            team_uid=team_uid,
            task_jid=task_jid,
            item_uid=item_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def delete_checklist(self, team_uid, task_jid):
        """
        endpoint /teams/{team_uid}/tasks/{task_jid}/checklist методом DELETE
        Удаление всех пунктов чек-листа и его названия
        """
        endpoint = '/teams/{team_uid}/tasks/{task_jid}/checklist'.format(
            team_uid=team_uid,
            task_jid=task_jid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_tags(self, team_uid):
        """
        endpoint /teams/{team_uid}/tags методом GET
        Список всех тэгов. Без пагинации
        """
        endpoint = '/teams/{team_uid}/tags'.format(
            team_uid=team_uid,
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def add_reminds(self, team_uid, data):
        """
        endpoint /teams/{team_uid}/reminds методом POST
        Создать напоминание
        в data передаем json
        """
        endpoint = '/teams/{team_uid}/reminds'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_post_api(url, data)


    def get_reminds(self, team_uid):
        """
        endpoint /teams/{team_uid}/reminds методом GET
        Информация о напоминаниях
        """
        endpoint = '/teams/{team_uid}/reminds'.format(
            team_uid=team_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def get_remind(self, team_uid, remind_uid):
        """
        endpoint /teams/{team_uid}/reminds/{remind_uid} методом GET
        Информация о напоминании
        """
        endpoint = '/teams/{team_uid}/reminds/{remind_uid}'.format(
            team_uid=team_uid,
            remind_uid=remind_uid
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def delete_remind(self, team_uid, remind_uid):
        """
        endpoint /teams/{team_uid}/reminds/{remind_uid} методом DELETE
        Удалить напоминание в чате
        """
        endpoint = '/teams/{team_uid}/reminds/{remind_uid}'.format(
            team_uid=team_uid,
            remind_uid=remind_uid
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_all_exist_reactions(self):
        """
        endpoint /reactions методом GET
        Список доступных реакций
        """
        endpoint = '/reactions'
        url = self.url + endpoint
        return self.call_get_api(url)


    def add_edit_reaction(self, team_uid, message_id, reaction_name):
        """
        endpoint /teams/{team_uid}/messages/my-reactions/{message_id}/{reaction_name} методом POST
        Добавляет или изменяет реакцию на сообщение
        """
        endpoint = '/teams/{team_uid}/messages/my-reactions/{message_id}/{reaction_name}'.format(
            team_uid=team_uid,
            message_id=message_id,
            reaction_name=reaction_name
        )
        url = self.url + endpoint
        return self.call_post_api(url)


    def get_my_reaction_by_name(self, team_uid, message_id, reaction_name):
        """
        endpoint /teams/{team_uid}/messages/my-reactions/{message_id}/{reaction_name} методом GET
        Информация о реакции на сообщение
        """
        endpoint = '/teams/{team_uid}/messages/my-reactions/{message_id}/{reaction_name}'.format(
            team_uid=team_uid,
            message_id=message_id,
            reaction_name=reaction_name
        )
        url = self.url + endpoint
        return self.call_get_api(url)


    def delete_my_reaction(self, team_uid, message_id, reaction_name):
        """
        endpoint /teams/{team_uid}/messages/my-reactions/{message_id}/{reaction_name} методом DELETE
        Удваляет реакцию на сообщение
        """
        endpoint = '/teams/{team_uid}/messages/my-reactions/{message_id}/{reaction_name}'.format(
            team_uid=team_uid,
            message_id=message_id,
            reaction_name=reaction_name
        )
        url = self.url + endpoint
        return self.call_delete_api(url)


    def get_my_reactions_on_message(self, team_uid, message_id):
        """
        endpoint /teams/{team_uid}/messages/my-reactions/{message_id} методом GET
        Список моих реакций на сообщение
        """
        endpoint = '/teams/{team_uid}/messages/my-reactions/{message_id}'.format(
            team_uid=team_uid,
            message_id=message_id
        )
        url = self.url + endpoint
        return self.call_get_api(url)

