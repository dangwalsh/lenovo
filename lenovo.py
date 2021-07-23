from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

PAUSE_TIME = 0.5

def get_model(text):
    field = driver.find_element_by_css_selector('input')
    field.send_keys(text[:4])
    time.sleep(PAUSE_TIME)
    return driver.find_element_by_css_selector('div.tt-content-up').text

def get_model_number(text):
    return text[:4]


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

chrome_options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", options=chrome_options)

driver.get('https://pcsupport.lenovo.com/us/en/')
time.sleep(PAUSE_TIME)
number = get_model_number(get_model('20J7S0QM00'))

pass