from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class MainPage(BasePage):

    OFF_PLAN_BTN = (By.XPATH, "//address[@class='menu-twobutton']")
    TOTAL_PRJCT_MSG = (By.XPATH, "//*[(text()='Total projects')]")
    SALE_STATUS_BTN = (By.ID, "Location-2")
    LISTINGS = (By.XPATH,"//div[@wized='projectImage']")
    OOS_LABEL = (By.XPATH, "//div[@wized='projectStatus' and @w-el-text='Status' and text()='Out of stock']")

    def click_off_plan(self):
        self.driver.find_element(*self.OFF_PLAN_BTN).click()

    def verify_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TOTAL_PRJCT_MSG)
        )

    def click_sale_status(self):
       self.driver.find_element(*self.SALE_STATUS_BTN).click()


    def select_oos(self):
      dropdown = Select(self.driver.find_element(*self.SALE_STATUS_BTN))
      dropdown.select_by_value("Out of stock")

    def verify_oos_tag(self):
      listings = self.driver.find_elements(*self.LISTINGS)

      for listing in listings:
        oos_label = listing.find_element(*self.OOS_LABEL)
        assert oos_label.is_displayed()



