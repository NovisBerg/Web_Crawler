from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="C:\ProgramData\Anaconda3\Scripts\chromedriver.exe")
wait = WebDriverWait(browser, 10)

def search():
    browser.get('http://www.taobao.com')

    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
    )
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
    )
    input.send_keys('美食')
    submit.click()

def main():
    search()


if __name__ == '__main__':
    main()