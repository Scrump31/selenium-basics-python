''' 
This is the test configuration file
scope options:
function = applies to every function
session = applies to every function in the module

Note: use pytest --cov=pages tests/ to log test coverage
https://pypi.org/project/pytest-cov/
Note: use pytest --browser firefox  --html=report.html && open report.html
to generat html test report
'''
from selenium import webdriver
import pytest
from config.keys import browserstack_key

@pytest.fixture
def endTest(setDriver):
    yield
    return setDriver.quit()

@pytest.fixture(scope='function')
def setDriver(browser):
    if browser == 'firefox':
        print('Running tests on Firefox')
        driver = webdriver.Firefox()

    elif browser == 'safari':
        '''
        may need to use selenium 3.9 to use Safari browser
        https://stackoverflow.com/questions/49158246/unable-to-start-selenium-safari-webdriver-via-python3
        '''
        print('Running tests on Safari')
        driver = webdriver.Safari()

    elif browser == 'browserstack':
        desired_cap = {
            'browser': 'Safari',
            'browser_version': '11.0',
            'os': 'OS X',
            'os_version': 'High Sierra',
            'resolution': '1024x768'
        }

        driver = webdriver.Remote(
            command_executor=browserstack_key,
            desired_capabilities=desired_cap)
    else:
        print('Running tests on Chrome')
        driver = webdriver.Chrome()
    return driver


# Command-line options to set browser environment
def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
