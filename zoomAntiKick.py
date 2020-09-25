from selenium import webdriver

url = "https://binus.zoom.us/j/94084323338?pwd=Z1hTRjUwampocmR1VEh4aWkrSkZUdz09#success"

driver = webdriver.Chrome()

while(True):
	try:
		button = driver.find_element_by_xpath('//*[@id="zoom-ui-frame"]/div/div/div[2]/h3/a[1]')
		button.click()
	except:
		driver.delete_all_cookies()
		driver.get(url)
		print("Masuk except")