import time
import selenium
import argparse
from os import system
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--start-maximized')
#options.add_argument('--headless')
options.add_argument("--disable-extensions")
#options.add_argument('--proxy-server=') 

system('clear')

parser = argparse.ArgumentParser()
parser.add_argument('--email', type=str, help='The email you wish to use to login to use to claim a gamertag.')
parser.add_argument('--password', type=str, help='The password for the email you wish to use.')
parser.add_argument('--validation', type=str, help='The validation email for the email that is required to login.')
parser.add_argument('--username', type=str, help='The gamertag you wish to try and claim.')
args = parser.parse_args(rC:\users\cj\chromedriver)

my_chrome_drivers_executable_path = r"chromedriver"
driver = webdriver.Chrome(options=options, executable_path=my_chrome_drivers_executable_path)
username = args.username

# claiming account details
email_id = args.email
password_id = args.password

# (if required) validation account details
validation_email_id = args.validation

# urls
url = "https://www.gamertag.net/check.php"
xbox_login_page = "https://login.live.com/login.srf?"
xbox_change_gamer_tag_page = "https://account.xbox.com/ChangeGamerTag"


def search():
	# switch to the second tab, and begin our search here
	second_window = driver.switch_to.window(driver.window_handles[1])
	second_window
	driver.get(url)
	gamertag_send = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-full"]/div[1]/div/div[2]/div/form/div/div[1]/div[1]/input')))
	gamertag_send.send_keys(username)
	check_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-full"]/div[1]/div/div[2]/div/form/div/div[1]/div[2]/input')))
	check_button.click()
	report = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="report"]')))
	
	if "is available to use!" in str(report.text):
		return True

def looper():
	while True:
		start = time.time()
		if search():
			return
		end = time.time()
		total = str(1.0 / float(end-start))
		print('checks per second: '+total)
		
def signin():
	# create a new tab
	driver.execute_script('''window.open("https://www.google.com","_blank");''')
	
	# switch back to the zeroeth tab
	first_window = driver.switch_to.window(driver.window_handles[0])
	first_window
	
	driver.get(xbox_login_page)
	# email
	email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]')))
	email.clear()
	email.send_keys(email_id)
	next = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]')))
	next.click()

	# password
	password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
	password.clear()
	password.send_keys(password_id)

	# signin
	signin = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]')))
	signin.click()
	
	driver.get(xbox_change_gamer_tag_page)
	
	try:
		# if microsoft requires a validation email...
		send_email_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div')))
		send_email_option.click()
		verify_email_id_by_typing_email_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idTxtBx_SAOTCS_ProofConfirmation"]')))
		verify_email_id_by_typing_email_id.send_keys(validation_email_id)
		send_me_a_code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idSubmit_SAOTCS_SendCode"]')))
		send_me_a_code.click()
		manually_entered_verification_code = str(input('Please enter the code, that you were sent in the verification email.\n I\'ll wait: '))
		verification_code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]')))
		verification_code.send_keys(manually_entered_verification_code)
		click_to_verify = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]')))
		click_to_verify.click()
	except:
		driver.get(xbox_change_gamer_tag_page)
		
	while True:
		if "https://account.xbox.com/" in driver.current_url: # this is so that other countries (like Europe) wont break the code on this line.
			print('Let\'s if we can\'t get that username before anyone else!')
			break
	# switch to the second tab, and begin our search here
	second_window = driver.switch_to.window(driver.window_handles[1])
	second_window

def claim_gamertag():
	type_gamertag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="xbox-changegamertag-9m4a82r"]/div/div[1]/div[3]/input')))
	type_gamertag.send_keys(username)

	check_availability = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkavailability"]')))
	check_availability.click()

	claim_it = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="claimgamertag"]')))
	claim_it.click()
	
	
def main():
	# lets signin to setup our claimer
	signin()
	# after we are signed in, lets start our looper, to find when the gamertag is/has changed.
	looper()
	# looper has found that the gamertag is NOW unclaimed, lets focus the primary tab and claim the gamertag
	first_window = driver.switch_to.window(driver.window_handles[0])
	first_window
	# lets execute the claim_gamertag function, so that the gamertag IS claimed.
	claim_gamertag()
	# now, lets sell this code and make some $$$


if __name__ == "__main__":
	system('clear')
	print('Program initiated.\n')
	main()
	
