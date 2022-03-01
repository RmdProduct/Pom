from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append(r"C:\Users\Ram\Desktop\Selenium\Pom")
from Pages.Testlocatores import Register
class TestLogin(unittest.TestCase):
    username="Admin"
    password="admin123"
    urls="https://opensource-demo.orangehrmlive.com/"
    drivers=webdriver.Chrome(executable_path=r"C:\Users\Ram\Desktop\Selenium\Pom\Drivers\chromedriver.exe")
    @classmethod
    def setUpClass(cls):
        cls.drivers.get(cls.urls)
        cls.drivers.maximize_window()
    def test_login(self):
        Obj=Register(self.drivers)
        Obj.setusername(self.username)
        Obj.setpassword(self.password)
        Obj.button()
    @classmethod
    def tearDownClass(cls):
        cls.drivers.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Ram\Desktop\Selenium\Pom\Reportes"))