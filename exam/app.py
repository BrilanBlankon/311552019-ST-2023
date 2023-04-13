from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    # Q2-1
    # Go to https://docs.python.org/3/tutorial/index.html.
    driver.get("https://docs.python.org/3/tutorial/index.html")

    # Select the language options on the navigation bar, and choose the Traditional Chinese option.
    # wait = WebDriverWait(driver, 20)
    # element = wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//select[@id='language_select']")))
    # select = Select(element)
    # select_menu.select_by_value("zh-tw") 
    wait = WebDriverWait(driver, 20)
    select_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/ul/li[7]/div[1]/select')))
    select = Select(select_element)
    select.select_by_value('zh-tw')

    # use find_element to get the title and the first paragraph. Print the title and the first paragraph.
    title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="the-python-tutorial"]/h1')))
    print(title.text)
    text = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/section/p[1]')))
    print(text.text)

    
    # Q2-2
    # Find the search box on the navigation bar, and send keys to search for class
    input_box = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/ul/li[11]/div/form/input[1]')))
    input_box.send_keys('class')
    go = driver.find_element(By.XPATH, "//input[@value='Go']")
    go.click()

    # Please use implicit or explicit wait in Selenium to wait for the searching result, and print the top five listed titles
    driver.implicitly_wait(5)
    result = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li[1]/a')))
    print(result.text)
    result = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li[2]/a')))
    print(result.text)
    result = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li[3]/a')))
    print(result.text)
    result = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li[4]/a')))
    print(result.text)
    result = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li[5]/a')))
    print(result.text)


    # close the brower
    driver.close()