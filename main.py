from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(
    '--user-data-dir=C:\\Users\\symond\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--profile-directory=Default')
# options.add_argument(
#     '--user-data-dir=C:\\Users\\symond\\AppData\\Local\\Google\\Chrome\\User Data\\Dedault')

driver = webdriver.Chrome(options=options)
driver.get('chrome://version/')

print()
# driver.quit()
