from locators.tutorial_page_loc import TutorialPageLocators
from pages.base_page import BasePage


class TutorialPage(BasePage):

    tutorial_page_loc = TutorialPageLocators()

    def close_tutorial_popup(self):
        self._tutorial_popup_btn_close_click()


    # -------------- внутренние методы --------------


    def _tutorial_popup_btn_close_click(self):
        tutorial_popup_btn_close = self.wait.element_to_be_clickable(*self.tutorial_page_loc.TUTORIAL_POPUP_CLOSE)
        tutorial_popup_btn_close.click()
