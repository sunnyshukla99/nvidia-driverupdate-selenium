from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait # will implement in future
import time
import os

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get("https://www.nvidia.com/Download/index.aspx?")
driver.implicitly_wait(10)

#product Series Type
productType = driver.find_element(By.ID, "selProductSeriesType")
drop = Select(productType)
drop.select_by_value("1")

#product Series
productSeries = driver.find_element(By.ID, "selProductSeries")
drop = Select(productSeries)
drop.select_by_value("113")
#Product Family

productFamily = driver.find_element(By.ID, "selProductFamily")
drop = Select(productFamily)
drop.select_by_value("893")

#Operating System
operatingSystem = driver.find_element(By.ID, "selOperatingSystem")
drop = Select(operatingSystem)
drop.select_by_value("135")

#Windows Driver Type
driverType = driver.find_element(By.ID, "ddlDownloadTypeCrdGrd")
drop = Select(driverType)
drop.select_by_value("1")

#Select Language
ddLanguage = driver.find_element(By.ID, "ddlLanguage")
drop = Select(ddLanguage)
drop.select_by_value("1")
#for use with NVIDIA Advanced Driver Search
#Recommended Driver
#ddWHQL = driver.find_element(By.ID, "ddWHQL")
#drop = Select(ddWHQL)
#drop.select_by_value("1")
# only selects certified drivers

#click search button

searchButton = driver.find_element(By.ID, "imgSearch")
searchButton.click()

time.sleep(5)

#click download button 
downloadButton = driver.find_element(By.ID, "lnkDwnldBtn")
downloadButton.click()

driver.implicitly_wait(10)
#final download button
hrefDownload = driver.find_element(By.XPATH, ".//a[contains(@href, 'download')]")  
hrefDownload.click()

driver.implicitly_wait(10)
def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        return document.querySelector('downloads-manager')
        .shadowRoot.querySelector('#downloadsList')
        .items.filter(e => e.state === 'COMPLETE')
        .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
        """)
        
paths = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
print(paths)
driver.close()
