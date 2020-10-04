from selenium import webdriver
import time
import pyautogui


browser = webdriver.Firefox()
url = "https://10fastfingers.com/advanced-typing-test/turkish"
while True:
    say = 1
    browser.get(url)
    a = input("Başla ...")
    time.sleep(5)
    try:    
        while True:
        
            word = browser.find_element_by_class_name('highlight')
            yazi = browser.find_element_by_xpath("//*[@id='inputfield']")
            yazi.send_keys(word.text)
            pyautogui.press("space")
            print("{}. Kelime : {}".format(say,word.text))
            say += 1

        
    except:
        print("Easy !")

