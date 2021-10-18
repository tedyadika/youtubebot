import time;
from selenium import webdriver
import random

driver = webdriver.Chrome(r"C:\Users\New User\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver1 = webdriver.Firefox(r'C:\Users\New User\Downloads\geckodriver-v0.30.0-win32')

videos = ['https://youtu.be/xDvixmFpooQ',
          'https://youtu.be/WxRjf4WUFpw',
          'https://youtu.be/jhiBTViX3V8',
          'https://youtu.be/2QE9pX8Je1M',
          'https://youtu.be/bpy6c8fgQwY',
          'https://youtu.be/3kP0oVGnPkU',
          'https://youtu.be/j9q6cF0hnbg',
          'https://youtu.be/hSPxxByIvBE',
          'https://youtu.be/JsJKF7h4ecg',
          'https://youtu.be/Y48LVH8wijY']


for i in range (10000):
    print('running the video for {} time'.format(i))
    random_video = random.randint(0, 5)
    driver.get(videos[random_video])
    sleep_time = random.randint(50, 100)
    time.sleep(sleep_time)
    
driver.quit()