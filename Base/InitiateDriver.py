from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Library import ConfigReader

def Open_Browser(context):
    path = "chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.maximize_window()