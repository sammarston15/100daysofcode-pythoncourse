from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

chrome_driver_path = "/Users/smarston/Documents/dev/chromedriver-mac-x64/chromedriver"
# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')


first_name = driver.find_element(By.NAME, value='fname')
first_name.send_keys("Sam")
last_name = driver.find_element(By.NAME, value='lname')
last_name.send_keys("Marston")
email = driver.find_element(By.NAME, value='email')
email.send_keys("sammarston15@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, value='form button')
submit.click()


