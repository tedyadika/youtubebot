import time;
from selenium import webdriver
import random

driver = webdriver.Chrome(r"C:\Users\New User\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver1 = webdriver.Firefox(r'C:\Users\New User\Downloads\geckodriver-v0.30.0-win32')

videos = ['put list of videos you want ']


for i in range (10000):
    print('running the video for {} time'.format(i))
    random_video = random.randint(0, 5)
    driver.get(videos[random_video])
    sleep_time = random.randint(50, 100)
    time.sleep(sleep_time)
    
driver.quit()
