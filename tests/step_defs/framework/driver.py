import os
import pytest
import hashlib
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from tests.step_defs.common_data import CommonData
from tests.step_defs.framework.browser import Browser
from tests.step_defs.login.login_data import login_url

SESSION_COOKIE_NAME = 'DESESSIONID'
NON_ALPHA_RE = re.compile('[^A-Z0-9]')
caps = {}


# Fixtures


@pytest.fixture
def env(request):
    return request.config.getoption("--env")


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser_name, request,env):
    if browser_name == 'grid-chrome':
        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "137.0")
        options.add_argument('--disable-dev-shm-usage')
        d = webdriver.Remote(
            command_executor=CommonData.remote_url,
            options=options)
    elif browser_name == 'chrome':
        # ChromeDriver path - points to chromedriver.exe in project root
        chromedriver_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'chromedriver.exe')
        service = Service(executable_path=chromedriver_path)
        d = webdriver.Chrome(service=service)
    d.set_window_size(CommonData.browser_width, CommonData.browser_height)
    yield d

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            print(f"Test failed on URL: {d.current_url}")
            # Take screenshot on failure (saved locally)
            screenshot_name = f"screenshot_{request.node.name}.png"
            d.save_screenshot(screenshot_name)
            print(f"Screenshot saved: {screenshot_name}")

            cookies = d.get_cookies()
            if env == "qa-us" or env=="qa-ca" or env=="qa-uk":
                desessionids_value = next((cookie['value']
                                           for cookie in cookies if cookie['name'] == 'DESESSIONIDQ'),None)
            elif env == "stage-us" or env=="stage-ca" or env=="stage-uk":
                desessionids_value = next((cookie['value']
                                           for cookie in cookies if cookie['name'] == 'DESESSIONIDS'),None)
            elif env == "prod-us" or env=="prod-ca" or env=="prod-uk":
                desessionids_value = next((cookie['value']
                                           for cookie in cookies if cookie['name'] == 'DESESSIONID'),None)
            elif env == "dev-us" or env=="dev-ca" or env=="dev-uk":
                desessionids_value = next((cookie['value']
                                           for cookie in cookies if cookie['name'] == 'DESESSIONIDD'),None)
            if desessionids_value is None:
                response = requests.get(login_url(env))
                # Check if the request was successful
                if response.status_code == 200:
                    print("Request was successful.")
                    # Fetch the 'Edde-Request-ID' from the response headers
                    request_id = response.headers.get('Edde-Request-ID')
                    if request_id:
                        print(f'Edde-Request-ID: {request_id}')
                    else:
                        print("Edde-Request-ID not found in the response headers.")
                else:
                    print(f"Request failed with status code: {response.status_code}")
            else:
                alpha_num_value = alphanum_only_session_id(desessionids_value)
                compute_log_value = compute_log_session_id(alpha_num_value)
                print("DE log_session_id: " + compute_log_value)
        except:
            print('screenshot could not be captured')  # just ignore
    d.quit()
def alphanum_only_session_id(session_id):
        """
        Converts a session ID to alphanum only form and uppercases it.

        Args:
            session_id: the session ID

        Returns: the uppercase, alphanum only form of session ID

        """
        return NON_ALPHA_RE.sub('', str(session_id).upper())

def compute_log_session_id(session_id):
        """
        Compute a SHA256 hash of the session ID after stripping non-alphanum chars and uppercasing.
        Args:
            session_id: session id

        Returns:
            SHA256 (uppercase hex) hash of processed session ID, prefixed with capital S to mark it.
        """
        if session_id == "NONE":
            return session_id

        return compute_ident(session_id, 'S')

def compute_ident(session_id, ident_prefix):
        """
        Compute a SHA256 hash of the session ID after stripping non-alphanum chars, and uppercasing. The ident_prefix
        is added not to add any security value, but to make these identifiers easier for a human being to identify as
        being for a specific purpose. Otherwise it'd just be hex.

        Args:
            session_id: session id. If None is supplied, None will be returned.

        Returns:
            ident_prefix + SHA256 (uppercase hex) hash of processed session ID, or None if no session ID is set.
        """
        if session_id == "NONE":
            return session_id

        hexdigest = hashlib.sha256((alphanum_only_session_id(session_id)).encode('utf-8')).hexdigest()

        return ident_prefix + hexdigest.upper()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


@pytest.fixture
def browser(driver):
    b = Browser(driver)
    return b


@pytest.fixture()
def context():
    return {}
