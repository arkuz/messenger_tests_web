### Описание
Данный репозиторий содержит GUI автотесты для проекта messenger.

### Требования к ПО
- Установленная виртуальная маштна Java - [https://www.java.com/ru/download/](https://www.java.com/ru/download/)
- Установленный Python 3.x - [www.python.org/getit/](https://www.python.org/getit/)
- Установленный инструмент для работы с виртуальными окружениями virtualenv
```bash
pip install virtualenv
```

### Копирование репозитория и установка зависимостей
##### Установка на Linux и MacOS
```bash
git clone https://github.com/arkuz/messenger_tests_web
cd messenger_tests_web
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```

##### Установка на Windows
```bash
git clone https://github.com/arkuz/messenger_tests_web
cd messenger_tests_web
virtualenv env
cd env/scripts
activate.bat
pip install -r requirements.txt
```

#### Копирование необходимых файлов для запуска тестов
Все файлы необходимо скопировать в корневую папку с тестами `messenger_tests_web`.

- Тесты запускаются через `selenium-server-standalone-3.141.59.jar`. Качаем его здесь [https://www.seleniumhq.org/download/](https://www.seleniumhq.org/download/)
- Так же необходимо скачать драйверы для браузеров [Chrome (chromedriver v.78.0.3904.70)](https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.70/) и [Firefox (geckodriver v0.26.0)](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0). 

### Запуск Selenium Server Standalone
```bash
java -jar selenium-server-standalone-3.141.59.jar
```

### Запуск тестов
Перед запуском тестов необходимо перейти в каталог проекта `messenger_tests_web`.

 - В GitLab CI тесты запускаются в браузере Firefox (никакие настройки в репозитории изменять не нужно)
 - Для локального запуска необходимо отредактировать файл `messenger_tests_web/config.yaml`:
   - в ключе `web` изменить параметр `env` на значение `local`
   - так же можно изменять в ключе `web` параметр `browser` на значение `Chrome` и `Firefox`
   - так же можно изменять в ключе `web` параметр `browser_mode` на значение `headless` и `default`, данный параметр определяет режим запуска браузера

Аргументы запуска:
- -s - показывать принты в процессе выпонения
- -v - verbose режим, чтобы видеть, какие тесты были запущены
- --html=report.html --self-contained-html - генерация автономного отчета
##### Запуск всех тестов
```bash
py.test -s -v --html=report/report.html --self-contained-html
```

##### Запуск всех тестов в пакете
```bash
py.test -s -v tests/web
```

##### Запуск помеченных тестов (positive, negative и т.п.)
```bash
py.test -s -v -m positive tests/web
```

##### Запуск тестового модуля
```bash
py.test -s -v tests/web/test_auth.py
```

##### Запуск тестового класса
```bash
py.test -s -v tests/web/test_auth.py::TestAuth
```

##### Запуск конкретного теста
```bash
py.test -s -v tests/web/test_auth.py::TestAuth::test_sms_login_valid_phone
```