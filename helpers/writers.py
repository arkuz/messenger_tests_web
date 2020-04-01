import yaml


def write_yaml(path, data):
    """ Функция пишет словарь в yml файл """
    with open(path, 'w', encoding='UTF-8') as f:
       yaml.dump(data, f)