import helpers.tools as tools


def add_team(api_obj, name=''):
    """ Функция для быстрого добавления команды """
    data = {'name': name}
    if not name:
        data['name'] = 'team_' + tools.generate_random_string()
    resp = api_obj.add_team(data).json()
    return {
        'name': resp['result']['name'],
        'uid': resp['result']['uid'],
        'owner_jid': resp['result']['contacts'][0]['jid']
    }

def add_team_with_contact(api_obj, name='', phone='', role='member'):
        """ Функция для быстрого добавления команды и добавления в нее участника """
        team_uid = add_team(api_obj, name)['uid']
        data = {'phone': phone,
                'status': role}
        resp = api_obj.add_contacts(team_uid, data).json()
        return {'team_uid': team_uid,
                'member': resp['result']}


def add_contact(api_obj, team_uid, phone='', role='member'):
    """ Функция для быстрого добавления участника в команду """
    data = {'phone': phone,
            'status': role}
    resp = api_obj.add_contacts(team_uid, data).json()
    return {'jid': resp['result']['jid'],
            'status': resp['result']['status']}


def add_section(api_obj, team_uid, name=''):
    """ Функция для быстрого добавления секции """
    data = {'name': name}
    if not name:
        data['name'] = 'section_' + tools.generate_random_string(10)
    resp = api_obj.add_section(team_uid, data).json()
    return {
        'name': resp['result']['name'],
        'uid': resp['result']['uid']
    }


def add_group(api_obj, team_uid, name='', public=False):
        """ Функция для быстрого добавления группы """
        if not name:
            name = 'group_' + tools.generate_random_string(10)
        data = {'display_name': name,
                'public': public}
        resp = api_obj.add_group(team_uid, data).json()
        return {'display_name': resp['result']['display_name'],
                'jid': resp['result']['jid']}


def add_member_to_group(api_obj, team_uid, group_jid, user_jid, status='member'):
    """ Функция для быстрого добавления участника в группу """
    data = {
            'jid': user_jid,
            'status': status
        }
    resp = api_obj.add_members(team_uid, group_jid, data).json()
    return {'jid': resp['result']['jid'],
            'status': resp['result']['status']}


def send_text(api_obj, team_uid, group_jid, text=''):
    """ Функция для быстрой отправки текстового сообщения """
    if not text:
        text = 'msg_' + tools.generate_random_string()
    msg_data = {'text': text}
    resp = api_obj.send_msg_text(team_uid, group_jid, msg_data).json()
    return {'text': resp['result']['content']['text'],
            'message_id': resp['result']['message_id']}


def add_tasklist(api_obj, team_uid, name=''):
    """ Функция для быстрого добавления тасклиста """
    data = {'name': name}
    if not name:
        data['name'] = 'tasklist_' + tools.generate_random_string(10)
    resp = api_obj.add_tasklist(team_uid, data).json()
    for el in resp['result']:
        if el['name'] == data['name']:
            return {
                'name': el['name'],
                'uid': el['uid']
            }


def get_my_jid(api_obj, team_uid):
    """ Функция возвращает jid текущего пользователя """
    resp = api_obj.get_contacts(team_uid).json()['result']
    for item in resp:
        if item['status'] == 'owner':
            return item['jid']
            break


def add_task(api_obj, team_uid, title='', description='', tasklist=''):
    """ Функция для быстрого создания задачи """
    if not title:
        title = 'title_' + tools.generate_random_string(10)
    if not description:
        description = 'desc_' + tools.generate_random_string(10)
    data = {
        'title': title,
        'description': description,
    }
    if tasklist:
        data['tasklist'] = tasklist
    resp = api_obj.add_task(team_uid, data).json()['result']
    return {
        'uid': resp['uid'],
        'title': resp['title'],
        'tasklist': resp['tasklist'],
        'description': resp['description']
    }
