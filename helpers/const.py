import os

from helpers.tools import get_project_path

# Пути к директориям
PROJECT = get_project_path(os.getcwd()) # корневая папка проекта
EXPECTED_RESULTS = os.path.join(PROJECT, 'expected_results')
TEST_DATA = os.path.join(PROJECT, 'test_data')
TD_FILES = os.path.join(TEST_DATA, 'files')


