from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

# Setting up a virtual display to run headless Chrome
display = Display(visible=0, size=(1024, 768))
display.start()

# Setting up Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')  # Bypass OS security model, discouraged
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
options.add_argument('--disable-gpu')  # GPU hardware acceleration isn't necessary for headless viewing
options.add_argument('--window-size=1920x1080')  # Define window size for screenshots or elements rendering

# Setting up WebDriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Accessing the webpage
url = "https://sunrise.net"  # Hardcoded URL
driver.get(url)

# Taking screenshot
driver.save_screenshot('/screen/screen.png')

# Closing the browser
driver.quit()

# Stop the display
display.stop()
