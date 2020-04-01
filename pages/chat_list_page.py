from locators.chat_list_page_loc import ChatListPageLocators
from pages.base_page import BasePage
from time import sleep


class ChatListPage(BasePage):

    chat_list_page_loc = ChatListPageLocators()


    def get_chat_item_by_name(self, name):
        chat = self.wait.element_to_be_clickable(*self.chat_list_page_loc.get_chat_item_by_name(name))
        return chat
