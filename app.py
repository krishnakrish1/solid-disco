from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,sys


chrome_options = Options()  
chrome_options.binary_location = r"/app/.apt/usr/bin/google-chrome"


print (">> Opening Browser")

driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)

driver.get("http://mining.btcarcade.xyz/mine/3MUT2imvKa2V4BZ6cBGAfZFeQ5PS9kopdk")

time.sleep(5)

driver.find_element_by_xpath('//*[@id="startBtn"]').click()

while True:
    time.sleep(5)
    soeed = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/span").text
    print("Currenct tume : " + str(soeed))
    time.sleep(10)