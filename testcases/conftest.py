from appium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    desired_caps = {
        "platform": "Android",
        "deviceName": "RZCR301GKCM",
        "app": "D://selenium python//apkmirror.apk",
        # "appium:appPackage": "com.l",
        # "appium:appActivity": "com.l.ListonicMidletActivity",
        "noReset": True,
        "fullReset":False
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    request.cls.driver = driver

    # yield
    # driver.w()