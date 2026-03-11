import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="function")
def driver(request):
    browser = request.param

    project_root = os.path.dirname(__file__)
    download_path = os.path.join(project_root, "downloads")

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    if browser.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()

        prefs = {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        }

        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

    elif browser.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()

        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.dir", download_path)
        firefox_options.set_preference("browser.download.useDownloadDir", True)
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream")
        firefox_options.set_preference("pdfjs.disabled", True)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.alwaysOpenPanel", False)

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://bstackdemo.com")

    yield driver
    driver.quit()