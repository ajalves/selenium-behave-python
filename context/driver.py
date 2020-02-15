from selenium import webdriver
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from context.config import settings


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path
        geckodriver_autoinstaller.install()
        if settings.browser == "chrome":
            self.driver = webdriver.Chrome()
        elif settings.browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Driver.SeleniumDriverNotFound(
                "{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()
