from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
https://pcsupport.lenovo.com/us/en/
input
.tt-content-up
'''

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

chrome_options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", options=chrome_options)