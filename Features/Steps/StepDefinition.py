import time

from behave import *
from behave import given, when, then, step, model
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Library import ConfigReader
from Pages import loginPage
from behave import fixture



# @given(u'user open the url')
# def Open_browser(context):
#     path = "chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#     context.driver.maximize_window()

@given(u'user open the url')
def step_impl(context):
    print('STEP: Given user open the url')
    path = "Drivers/chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.maximize_window()
    # context.driver.get(ConfigReader.read_configData('Details', 'Application_Url'))
    context.driver.get("http://www.google.com/")
    assert "Google" in context.driver.title
    print("title is : " + context.driver.title)


@when(u'user search for python')
def step_impl(context):
    print('STEP: When user search for python')
    'scenario' in context
    context.driver.find_element_by_name("q").click()
    context.driver.find_element_by_xpath("//*[@name='q']").click()
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys("python")
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)


@when(u'user select python.or site link')
def step_impl(context):
    print('STEP: When user select python.or site link')
    context.driver.find_element_by_xpath("//a[@href='https://www.python.org/']").click()


@then(u'user will be on python.or site and the title should be "Welcome to Python.org"')
def step_impl(context):
    print('STEP: Then user will be on python.or site and the title should be "Welcome to Python.org"')
    assert "Welcome to Python.org" in context.driver.title
    print("title is : " + context.driver.title)

@when('user search for "{search_text}"')
def step_impl(context, search_text):
    context.driver.find_element_by_name("q").click()
    context.driver.find_element_by_xpath("//*[@name='q']").click()
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys(search_text)
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)


@step('user select "{link}" site link')
def step_impl(context,link):
    if(link=="wikipedia"):
        context.driver.find_element_by_xpath("//a[@href='https://en.wikipedia.org/wiki/India']").click()
    elif(link=="python.org"):
        context.driver.find_element_by_xpath("//a[@href='https://www.python.org/']").click()


@then('the title should be "{Title}"')
def step_impl(context, Title):
    assert Title in context.driver.title
    print("title is : " + context.driver.title)


@given('user open the second app url')
def step_impl(context):
    print('STEP: Given user open the url')
    # path = "chromedriver.exe"
    # context.driver = webdriver.Chrome(executable_path=path)
    # context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configData('Details', 'Application_Url_2'))
    # context.driver.get("http://127.0.0.1:8000/")
    assert "Home" in context.driver.title
    print("title is : " + context.driver.title)


@when('Enter "{UserID}" and "{Password}"')
def step_impl(context, UserID, Password):
    context.driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
    context.driver.find_element_by_xpath("//input[@placeholder='email@example.com']").send_keys(UserID)
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)
    context.driver.find_element_by_xpath("//button[@class='form-button-submit rounded-pill']").click()


@then("user will be logged into application")
def step_impl(context):
    message = context.driver.find_element_by_xpath("//div[@class='alert alert-success']").text
    assert "Welcome Back!" in message.strip()


@when('Login into application using "{UserID}" and "{Password}"')
def step_impl(context, UserID, Password):
    context.driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
    context.driver.find_element_by_xpath("//input[@placeholder='email@example.com']").send_keys(UserID)
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)
    context.driver.find_element_by_xpath("//button[@class='form-button-submit rounded-pill']").click()


@step('Change password to "{new_Password}"')
def step_impl(context, new_Password):
    context.driver.find_element_by_xpath("//a[contains(text(),'Profile')]").click()
    assert "Profile" in context.driver.title
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(new_Password)
    context.driver.find_element_by_xpath("//input[@placeholder='confirm new password']").send_keys(new_Password)
    context.driver.find_element_by_xpath("//button[@class='form-button-submit rounded-pill']").click()


@then("Password should be changes sucessfully")
def step_impl(context):
    message = context.driver.find_element_by_xpath("//div[@class='alert alert-success']").text
    assert "Profile has been updated successfully!" in message.strip()


@step('Change password back to "{Password}" from "{new_Password}" for "{UserID}"')
def step_impl(context, Password, new_Password, UserID ):
    context.driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
    context.driver.find_element_by_xpath("//input[@placeholder='email@example.com']").send_keys(UserID)
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(new_Password)
    context.driver.find_element_by_xpath("//button[@class='form-button-submit rounded-pill']").click()
    message = context.driver.find_element_by_xpath("//div[@class='alert alert-success']").text
    assert "Welcome Back!" in message.strip()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[contains(text(),'Profile')]").click()
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)
    context.driver.find_element_by_xpath("//input[@placeholder='confirm new password']").send_keys(Password)
    context.driver.find_element_by_xpath("//button[@class='form-button-submit rounded-pill']").click()
    message = context.driver.find_element_by_xpath("//div[@class='alert alert-success']").text
    assert "Profile has been updated successfully!" in message.strip()


@step("user close the browser")
def step_impl(context):
    context.driver.close()