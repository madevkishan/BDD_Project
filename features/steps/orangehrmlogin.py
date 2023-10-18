from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Launch Chrome Browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    print('launched')

@when('Open OrangeHRM HomePage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com')
    print('opened')

@then("Enter username '{user}' and password '{pwd}'")
def verifyLogo(context):
    context.driver.find_element(By.NAME,'username').send_keys(user)
    context.driver.find_element(By.NAME, 'password').send_keys(pwd)

@then('click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

@then('User must succuessfully login to the Dashboard page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH,"//h6[text()='Dashboard']")
    assert text == 'Dashboard'
    context.driver.close()

@then('Close Browser')
def closeBrowser(context):
    context.driver.close()
    print('closed')