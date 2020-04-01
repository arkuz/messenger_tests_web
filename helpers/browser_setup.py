from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def config_and_run_browser(config: dict):
    if config['browser'] == 'Chrome':
        options = ChromeOptions()
        desired_capabilities = DesiredCapabilities.CHROME
        selen_server_url = config['gitlab_chrome_url']

    if config['browser'] == 'Firefox':
        options = FirefoxOptions()
        desired_capabilities = DesiredCapabilities.FIREFOX
        selen_server_url = config['gitlab_firefox_url']

    if config['env'] == 'local':
        selen_server_url = config['local_url']

    if config['browser_mode'] == 'headless':
        options.add_argument('--headless')

    driver = webdriver.Remote(
        command_executor=selen_server_url,
        desired_capabilities=desired_capabilities,
        options=options)

    driver.implicitly_wait(config['implicitly_wait'])
    driver.maximize_window()
    #driver.get(config['site_url'])

    return driver
