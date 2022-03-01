class Register():
    test_username="txtUsername"
    test_password="txtPassword"
    test_button="//*[@id='btnLogin']"
    def __init__(self,drivers):
        self.drivers=drivers
    def setusername(self,username):
        self.drivers.find_element_by_id(self.test_username).send_keys(username)
    def setpassword(self,password):
        self.drivers.find_element_by_id(self.test_password).send_keys(password)
    def button(self):
        self.drivers.find_element_by_xpath(self.test_button).click()