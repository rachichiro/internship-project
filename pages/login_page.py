from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_LOGIN = (By.ID, 'email-2')
    PASSWORD = (By.NAME, 'Password')
    LOGIN_BTN = (By.XPATH, "//a[@wized='loginButton']")


    def open_reelly(self):
        self.open_url('https://soft.reelly.io')

    def login(self):
        self.driver.find_element(*self.EMAIL_LOGIN).send_keys('rachaelmelfi@gmail.com')
        self.driver.find_element(*self.PASSWORD).send_keys('Password123!')
        self.driver.find_element(*self.LOGIN_BTN).click()
