from selenium import webdriver
import time

username = input('Enter username/phone_number/email : ')
password = input('Enter password : ')
message = input('Enter the tweet to be posted : ')

driver  = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')

driver.get('https://www.twitter.com/login')

user = driver.find_element_by_name('session[username_or_email]')
user.click()
user.send_keys(username)

login_password = driver.find_element_by_name('session[password]')
login_password.click()
login_password.send_keys(password)

login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
login.click()

driver.implicitly_wait(20)

tweet_btn = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
tweet_btn.click()

driver.implicitly_wait(30)

tweet = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweet.send_keys(message)

time.sleep(12)

post_tweet = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/span/span')
post_tweet.click()
