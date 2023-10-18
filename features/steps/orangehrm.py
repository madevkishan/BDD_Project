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

@then('Verify that logo is present on page')
def verifyLogo(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@alt,'company-branding')]")))
    print(f"Is displayed: {element.is_displayed()}")
    assert element.is_displayed()
    print('verified')

@then('Close Browser')
def closeBrowser(context):
    context.driver.close()
    print('closed')