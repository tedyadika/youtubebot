import time
from selenium import webdriver
import random

driver = webdriver.Chrome(r"C:\Users\New User\OneDrive\Desktop\maichbot\chromedriver.exe")
#driver1 = webdriver.Firefox(r'C:\Users\New User\Downloads\geckodriver-v0.30.0-win32')

videos = ['https://youtu.be/sALZ1C6BlCE',
          'https://youtu.be/K4mlwAcAe4M']


for i in range (10000):
    print('running the video for {} time'.format(i))
    random_video = random.randint(0, 1)
    driver.get(videos[random_video])
    sleep_time = random.randint(150, 200)
    time.sleep(sleep_time)
    
driver.quit()
