
import pytest
from selenium import webdriver
@pytest.fixture
def demo_fixture():
    print(f"\nThis is demo fixture, this will run first, after testcases")
    yield #after running the test case before code will run
    print(f"\nThis is demo fixture, this will run first, before testcases")

#Browser-->open--->first
#Browse--->close-->end

# @pytest.fixture
# def browser_setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     print(f"\n Browser is open")
#     yield driver
#     driver.quit()
#     print(f"\n Browser is closed")

#customize browser
#pytest addoption is used for to pass command line argument to pytest

def pytest_addoption(parser):#special name,same you used parser-->to add custome argument
    parser.addoption("--browser")

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def browser_setup(request):
    browser = request.config.getoption("--browser")

    if browser == "edge":
        print("\n\n opening edge browser")
        driver = webdriver.Edge()

    else:
        print(f"\n\n opening {browser if browser else 'chrome'} browser")

        chrome_options = Options()

        # 🔕 Silence Chrome & DevTools logs
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-logging"]
        )

        # 🔐 Disable password & credential popups
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })

        # 🧠 Headless support
        if browser == "headless":
            chrome_options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield driver

    print("\n\n closing browser")
    driver.quit()
#test data
# @pytest.fixture(params=[( "Credence_user_4494@gmail.com","Credence_user_100@124","Pass"),
#                         ( "Credence_user_4494@gmail.com1","Credence_user_100@124","Fail"),
#                         ( "Credence_user_4494@gmail.com","Credence_user_100@127","Fail"),
#                         ( "Credence_user_4494@gmail.com1","Credence_user_100@129","Fail")])
# def credkart_login_data(request):
#     return request.param

def pytest_metadata(metadata):
     metadata["Project_name"]=" Credkart Test Automation"
     metadata["Environment"]="QA"
     del metadata["Platform"]
     metadata["Summary"]="3 Test case Pass"