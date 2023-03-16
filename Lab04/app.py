from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # launch browser, navigate to NYCU home page, and maximize the window
    driver.get("https://www.nycu.edu.tw/")
    driver.maximize_window()

    # click news
    element = driver.find_element(By.XPATH, "//a[@title='新聞']")
    element.click()

    # click first news
    element = driver.find_element(By.CLASS_NAME, "su-post")
    element.click()

    # print title and content
    element = driver.find_element(
        By.XPATH, "//h1[@class='single-post-title entry-title']")
    print(element.text)
    elements = driver.find_elements(By.XPATH, "//p")
    for e in elements:
        print(e.text)

    # open a new tab ,switch to it, and navigate google.com
    driver.execute_script("window.open('https://www.google.com')")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    # type student ID and search it
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('311552019')
    search_box.submit()

    # print the title of second result
    results = driver.find_elements(By.XPATH, "//h3")
    print(results[2].text)

    # close the brower
    driver.close()
