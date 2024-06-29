from selenium import webdriver

url="https://kite.zerodha.com/chart/ext/ciq/NSE/GMRINFRA/3463169"
path = 'scrape.png'

driver = webdriver.Chrome(executable_path='/home/pankaj/Documents/stocks/kiteconnect/test_screenshot/chromedriver-linux64/chromedriver')
driver.get(url)
el = driver.find_element_by_tag_name('body')
el.screenshot(path)
driver.quit()
