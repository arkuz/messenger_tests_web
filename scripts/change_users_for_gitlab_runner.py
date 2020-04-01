import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from helpers.readers import read_yaml
from helpers.writers import write_yaml
import helpers.const as const

config_path = os.path.join(const.PROJECT, 'config.yaml')
config = read_yaml(config_path)

config['users']['user1'] = config['users']['user8']
config['users']['user2'] = config['users']['user9']
config['users']['user3'] = config['users']['user10']
config['users']['user4'] = config['users']['user11']

try:
    write_yaml(config_path, config)
    print('Users changed')
    exit(0)
except Exception:
    print('Error')
    exit(1)

