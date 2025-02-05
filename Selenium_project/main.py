# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# import undetected_chromedriver as uc
import time


# service = Service(executable_path = "chromedriver.exe")
# driver = uc.Chrome(service = service)

from selenium import webdriver
from selenium_stealth import stealth

# Set up Chrome Options
chrome_options = webdriver.ChromeOptions()
# Set up additional Chrome options for headless mode, window maximization, etc.
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
# Set up the Selenium WebDriver for a specific browser
driver = webdriver.Chrome(options=chrome_options)

# Use Selenium-Stealth to make this browser instance stealthy
stealth(
    driver,
    languages=["en-US", "en"],  # Specify the languages supported by the browser
    vendor="Google Inc.",       # Set the vendor of the browser
    platform="Win32",           # Specify the platform on which the browser is running
    webgl_vendor="Intel Inc.",   # Spoof the WebGL rendering engine vendor
    renderer="Intel Iris OpenGL Engine",  # Spoof the WebGL rendering engine renderer
    fix_hairline=True           # Enable fixing a specific issue related to headless browsing
)

driver.get("https://icp.administracionelectronica.gob.es/icpplus/index.html")

# ... your web automation tasks ...

time.sleep(5)

select = Select(driver.find_element(By.ID, 'form'))
time.sleep(4)

select.select_by_value('/icpplustieb/citar?p=8&locale=es')
time.sleep(2)

driver.find_element(By.ID, "btnAceptar").click()
time.sleep(6)

select= Select(driver.find_element(By.ID, 'tramiteGrupo[0]'))
time.sleep(2)

select.select_by_value("4010")
time.sleep(3)

driver.find_element(By.ID, "btnAceptar").click()
time.sleep(3)

driver.find_element(By.ID, "btnEntrar").click()
time.sleep(5)

driver.find_element(By.ID, "txtIdCitado").send_keys("Z2010354K")
time.sleep(5)

driver.find_element(By.ID, "txtDesCitado").send_keys("Bill Swamp")
time.sleep(6)

select= Select(driver.find_element(By.ID, "txtPaisNac"))
time.sleep(4)

select.select_by_value("258")
time.sleep(2)

driver.find_element(By.ID, "btnEnviar").click()
time.sleep(4)

driver.find_element(By.ID, "btnEnviar").click()

time.sleep(1000)

driver.quit()