from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pandas
import sys

PAUSE_TIME = 0.5

def get_description(element, text, pause=0.1):
    description = ''
    field = element.find_element_by_css_selector('input')
    field.send_keys(text[:4])
    time.sleep(pause)

    try:
        description = element.find_element_by_css_selector('div.tt-content-up').text
    except:
        print(sys.exc_info()[0])
        input('Hit Enter to continue...')

    for _ in range(4):
        field.send_keys(Keys.BACKSPACE)

    return description


# Read Data
df = pandas.read_csv('computerslist.csv', delimiter=';')
model_numbers = df.Model


# Read Web
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", options=chrome_options)
driver.get('https://pcsupport.lenovo.com/us/en/')
time.sleep(PAUSE_TIME)

# Append Data
descriptions = []
for mn in model_numbers:
    descriptions.append(get_description(driver, mn, PAUSE_TIME))
df['Description'] = descriptions

# Append File
df.to_csv('computerslist.csv')
