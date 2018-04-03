import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#----------- Config ------------------

email = '@supplyszn.co.uk'
firstName = 'Harry'
lastName = 'Potter'
contactNo = '1235'
cityOfresidency = 'Hogwards'
countryOfresidency = 'Muggles'
shoeSize = 7.5
loopCount = 5

#-------------------------------------


#--- Init vars ----
inputList = [email,firstName,lastName,contactNo,cityOfresidency,countryOfresidency]
availShoeSizes =[]
for i in range(3,13) :
	availShoeSizes.append(float(i+0.5))
	availShoeSizes.append(float(i+1))

downPress = availShoeSizes.index(shoeSize)


def automate():
	# Randomize email prefix
	rand_prefix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
	emailNew = rand_prefix+email

	inputList.insert(0,emailNew)
	print('[INFO] Using following data')
	print(inputList,shoeSize)
	 
	driver = webdriver.PhantomJS()
	driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc158NH-zi2UvU6y62PYnTuLAMClsocljviMhB_v1yLrdUyHg/viewform')
	wait = WebDriverWait(driver, 20)

	print('[INFO]Loaded google form content')

	inputs = (driver.find_elements_by_xpath("//input"))

	print('[INFO]Filling the required fields...')
	counter = 0 
	for inputElem in inputs:
		inputElem.send_keys(str(inputList[counter]))
		counter+=1
		if counter==6:
			break

	driver.save_screenshot('screenshots/FilledForm_{0}.png'.format(rand_prefix))
	print('[INFO] Form filled successfully...')
	print('[INFO] Screenshot saved...')


	print('[INFO] Selecting Shoe Size...')
	optionsSelect = driver.find_element_by_class_name("quantumWizMenuPaperselectDropDown")
	optionsSelect.click()

	sleep(5)
	driver.save_screenshot('screenshots/SelectSize_{0}.png'.format(rand_prefix))
	print('[INFO] Screenshot saved...')


	for i in range(0,downPress+1):
		webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
	webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()

	print('[INFO] Shoe Size selected successfully ...')
	sleep(5)
	driver.save_screenshot('screenshots/SizeSeleted_{0}.png'.format(rand_prefix))
	print('[INFO] Screenshot saved...')


	print('[INFO] Clicking checkbox...')
	checkBox = driver.find_element_by_class_name("quantumWizTogglePapercheckboxInnerBox")
	checkBox.click()

	print('[INFO] Checked successfully...')
	sleep(5)
	driver.save_screenshot('screenshots/checkBox_{0}.png'.format(rand_prefix))
	print('[INFO] Screenshot saved...')


	print('[INFO] Clicking checkbox...')
	submitButton = driver.find_element_by_class_name("quantumWizButtonPaperbuttonFocusOverlay")
	submitButton.click()

	print('[INFO] Submit successfully...')

	sleep(5)

	driver.save_screenshot('screenshots/submit_{0}.png'.format(rand_prefix))
	print('[INFO] Screenshot saved...')

print('[INFO] Script will be running for {} times'.format(loopCount))

for i in range(1,loopCount):
	print('[INFO] Iteration {}'.format(i))
	inputList.pop(0)
	automate()
