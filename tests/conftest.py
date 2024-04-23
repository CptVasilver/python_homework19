import pytest
from selene import browser
import os
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='function', autouse=True)
def mobile_management_android():
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
            "userName": "mike_Z6KI9R",
            "accessKey": "2xS3HkxEMPu8MNUZSVYE"
        }
    })
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '3.0'))

    yield

    browser.quit()
