import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome('C:\chromedriver.exe', options=options)
# https://googlechromelabs.github.io/chrome-for-testing/#stable
driver.implicitly_wait(10)
driver.get('https://www.godpia.com/login/login_page.asp?ishref=http://bible.godpia.com/frameindex.asp?url_flag=/index.asp?&ipserver=bible.godpia.com')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'inputID').send_keys('santa6985')
time.sleep(3)
driver.find_element(By.ID, 'inputPW').send_keys('xotjq9180')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/a/img').click()
time.sleep(3)

# driver.get('http://bible.godpia.com/write/sub020101.asp')
# time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[3]/ul/li[2]/div[1]/a/img').click()
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[3]/ul/li[2]/div[4]/div/ul/li[2]/div/h3').click()
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[3]/ul/li[2]/div[4]/div/ul/li[2]/div/ul/li[1]/a').click()
time.sleep(3)

while True:
    line_elements = driver.find_elements(By.CLASS_NAME, "writeSecli")
    start = 0
    end = len(line_elements)

    for i, e in enumerate(line_elements):
        class_name = e.get_attribute('class')
        if 'focustxt' in class_name:
            start = i
            break

    print(f'loop: {start} ~ {end}')

    for _ in range(start, end):
        try:
            target_text = driver.find_element(By.CSS_SELECTOR, "li[class='writeSecli clear focustxt']").find_element(By.CLASS_NAME, 'writeTxt').text
            print(target_text)
        except:
            print('not found, click page')
            driver.find_element(By.CLASS_NAME, 'sub-cont').click()
            break

        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "li[class='writeSecli clear focustxt']").find_element(By.CLASS_NAME, 'writeInput').click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "li[class='writeSecli clear focustxt']").find_element(By.CLASS_NAME, 'writeInput').send_keys(Keys.CONTROL + "a")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "li[class='writeSecli clear focustxt']").find_element(By.CLASS_NAME, 'writeInput').send_keys(Keys.DELETE)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "li[class='writeSecli clear focustxt']").find_element(By.CLASS_NAME, 'writeInput').send_keys([target_text, Keys.BACKSPACE])
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "li[class='writeSecli clear focustxt']").find_element(By.CLASS_NAME, 'writeInput').send_keys([target_text[-1], Keys.ENTER])
        time.sleep(3)
