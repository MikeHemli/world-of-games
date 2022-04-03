from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
chromeOptions.headless = True
# chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
# chrome_driver = webdriver.Chrome(
#    chrome_options=chromeOptions, executable_path="/usr/bin/chromedriver")
# chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)
chrome_driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')


def test_scores_service(url):
    try:
        chrome_driver.get(url)
        scores = chrome_driver.find_element(
            By.XPATH, value='//*[@id="score"]').text
        chrome_driver.quit()
        return 1 < int(scores) < 1000
    except Exception as e:
        print(e)


def main_function():
    if test_scores_service('http://localhost:5001') is True:
        return 0
    return -1


time.sleep(5)
print("This is the result: ", main_function())
