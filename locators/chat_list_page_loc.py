from selenium.webdriver.common.by import By


class ChatListPageLocators(object):

    def get_chat_item_by_name(self, name):
        return (By.XPATH, f"//div[contains(@class,'list-container')]//div[contains(@class,'name') and contains(text(),'{name}')]")
