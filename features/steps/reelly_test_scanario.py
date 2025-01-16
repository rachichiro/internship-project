from xml.etree.ElementTree import QName

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Reelly Main Page')
def open_reelly(context):
    context.app.login_page.open_reelly()

@then('Log in to the page')
def login(context):
    context.app.login_page.login()

@then('Click “Off Plan” at the left side menu')
def click_off_plan(context):
   context.app.main_page.click_off_plan()


@then('Verify Correct Page Opened')
def verify_page(context):
    context.app.main_page.verify_page()

@then('Click on Sale Status Filter')
def click_sale_status(context):
    context.app.main_page.click_sale_status()

@when('Change Sale Status to “Out of Stocks”')
def select_oos(context):
    context.app.main_page.select_oos()

@then('Verify Each Product Contains Out Of Stock Tag')
def verify_oos_tag(context):
    context.app.main_page.verify_oos_tag()