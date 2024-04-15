from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pyvirtualdisplay import Display

# Setting up a virtual display to run headless Firefox
display = Display(visible=0, size=(1024, 768))
display.start()

# Setting up Firefox options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')  # Bypass OS security model, discouraged
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Setting up WebDriver
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# Accessing the webpage
url = "https://sunrise.net"  # Hardcoded URL
driver.get(url)

# Taking screenshot
driver.save_screenshot('/screen/screen.png')

# Closing the browser
driver.quit()

# Stop the display
display.stop()
