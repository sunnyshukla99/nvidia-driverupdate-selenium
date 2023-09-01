# import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType

chrome_options = Options()
#  chrome_options.add_argument("--headless")
#  chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(
#     options=chrome_options,
#     service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get("https://www.nvidia.com/Download/index.aspx?")
waitTimer = WebDriverWait(webdriver, 10)  # .until(ec._element_if_visible("Option"))
# function implementation

print("waiting for the website to load completely.")
print("Hello, python user input script here! do your stuff")
print("This is going to print out the product series dropdown list")
productType = driver.find_element(By.ID, "selProductSeriesType")
drop = Select(productType)
element = WebDriverWait(webdriver, 10).until((ec.element_to_be_selected(drop.options[0])))
options = drop.options

dict_options = {}

for index in range(0, len(options)):
    item = options[index]
    dict_options[item.get_attribute('value')] = item.text

print(dict_options)

while True:
    productTypeValue = input("Enter the number corresponding to your product series:")
    if productTypeValue in dict_options:
        break
drop.select_by_value(productTypeValue)

# product Series Type
# productType = driver.find_element(By.ID, "selProductSeriesType")
# drop = Select(productType)
# element = WebDriverWait(webdriver, 10).until((EC.element_to_be_selected(drop.options[0])))
# drop.select_by_value("1")
# options = drop.options
# for index in range(0, len(options)):
#     print(options[index].text)
# product Series
productSeries = driver.find_element(By.ID, "selProductSeries")
drop = Select(productSeries)
element = WebDriverWait(webdriver, 10).until((ec.element_to_be_selected(drop.options[0])))
options = drop.options

dict_options = {}

for index in range(0, len(options)):
    item = options[index]
    dict_options[item.get_attribute('value')] = item.text

print(dict_options)

while True:
    productSeriesValue = input("Enter the number corresponding to your product series:")
    if productSeriesValue in dict_options:
        break
drop.select_by_value(productSeriesValue)
# Product Family

productFamily = driver.find_element(By.ID, "selProductFamily")
drop = Select(productFamily)
element = WebDriverWait(webdriver, 10).until((ec.element_to_be_selected(drop.options[0])))
options = drop.options

dict_options = {}

for index in range(0, len(options)):
    item = options[index]
    dict_options[item.get_attribute('value')] = item.text

print(dict_options)

while True:
    productFamilyValue = input("Enter the number corresponding to your product:")
    if productFamilyValue in dict_options:
        break

drop.select_by_value(productFamilyValue)

# Operating System
operatingSystem = driver.find_element(By.ID, "selOperatingSystem")
drop = Select(operatingSystem)
element = WebDriverWait(webdriver, 10).until((ec.element_to_be_selected(drop.options[0])))
options = drop.options

dict_options = {}

for index in range(0, len(options)):
    item = options[index]
    dict_options[item.get_attribute('value')] = item.text

print(dict_options)

while True:
    productOSValue = input("Enter the number corresponding to your product:")
    if productOSValue in dict_options:
        break

drop.select_by_value(productOSValue)

# Windows Driver Type
driverType = driver.find_element(By.ID, "ddlDownloadTypeCrdGrd")
drop = Select(driverType)
element = WebDriverWait(webdriver, 10).until((ec.element_to_be_selected(drop.options[0])))
options = drop.options

dict_options = {}

for index in range(0, len(options)):
    item = options[index]
    dict_options[item.get_attribute('value')] = item.text

print(dict_options)

while True:
    productDriverValue = input("Enter the number corresponding to your product:")
    if productDriverValue in dict_options:
        break
drop.select_by_value(productDriverValue)

# Select Language
ddLanguage = driver.find_element(By.ID, "ddlLanguage")
drop = Select(ddLanguage)
element = WebDriverWait(webdriver, 10).until((ec.element_to_be_selected(drop.options[0])))
options = drop.options

dict_options = {}

for index in range(0, len(options)):
    item = options[index]
    dict_options[item.get_attribute('value')] = item.text

print(dict_options)

while True:
    productLangValue = input("Enter the number corresponding to your product:")
    if productLangValue in dict_options:
        break
drop.select_by_value(productLangValue)
# for use with NVIDIA Advanced Driver Search
# Recommended Driver
# ddWHQL = driver.find_element(By.ID, "ddWHQL")
# drop = Select(ddWHQL)
# drop.select_by_value("1")
# only selects certified drivers

# click search button
searchButton = driver.find_element(By.XPATH, ".//a[contains(@href, 'GetDriver')]")
searchButton.click()

# click download button 
downloadButton = driver.find_element(By.ID, "lnkDwnldBtn")
downloadButton.click()

driver.implicitly_wait(10)
# final download button
hrefDownload = driver.find_element(By.XPATH, ".//a[contains(@href, 'download')]")
hrefDownload.click()

driver.implicitly_wait(10)


def every_downloads_chrome(cdriver):
    driver.implicitly_wait(5)
    if not cdriver.current_url.startswith("chrome://downloads"):
        cdriver.get("chrome://downloads/")
    return cdriver.execute_script("""
        return document.querySelector('downloads-manager')
            .shadowRoot.querySelector('#downloadsList')
            .items.filter(e => e.state === 'COMPLETE')
            .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
        """)


print("The downloaded location will be updated below: ")
every_downloads_chrome(driver)

paths = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
print(paths)
driver.close()
