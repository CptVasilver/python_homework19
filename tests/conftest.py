import pytest
from utils import attach
from selene import browser
import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def mobile_management_android():
    login = os.getenv("login")
    accesskey = os.getenv("accesskey")
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": login,
            "accessKey": accesskey
        }
    })
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    session_id = browser.driver.session_id

    browser.quit()

    attach.add_video(session_id, login, accesskey)
