

class loginPage:

    def click_login(self, context):
        context.driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()

    def enter_userId(self, context,UserID):
        context.driver.find_element_by_xpath("//input[@placeholder='email@example.com']").send_keys(UserID)

    def enter_Password(self, context,Password):
        context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)

    def click_login_submit(self, context):
        context.driver.find_element_by_xpath("//button[@class='form-button-submit rounded-pill']").click()