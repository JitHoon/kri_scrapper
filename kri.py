from bs4 import BeautifulSoup
from selenium import webdriver
# .find_element grap 요소 (By.ID)
from selenium.webdriver.common.by import By
# 키보드 제어
from selenium.webdriver.common.keys import Keys
# 마우스 제어
import pyautogui
# get 시간 벌어주기
import time
import os


def iris_login():
    basic_url = "https://www.kri.go.kr/kri2"
    browser = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
    browser.get(f"{basic_url}")
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 로그인
    browser.find_element(
        By.CLASS_NAME, "show-login").send_keys(Keys.ENTER)
    browser.find_element(By.ID, "uid").send_keys(os.environ.get("USERID"))
    browser.find_element(By.ID, "upw").send_keys(
        os.environ.get("USERPASSWORD") + Keys.ENTER)
    time.sleep(3)

    # 팝업창 제거
    browser.find_element(By.ID, "next_pwd").send_keys(Keys.ENTER)
    browser.find_element(By.CLASS_NAME, "ico-close").send_keys(Keys.ENTER)
    time.sleep(3)

    # 원하는 채널 클릭 방문
    pyautogui.click(720, 400)
    time.sleep(3)
    pyautogui.click(720, 400)
    time.sleep(3)

    # iframe 변경 후 파싱
    frame = browser.find_element(By.CLASS_NAME, "iframePage")
    browser.switch_to.frame(frame)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    time.sleep(3)

    # 원하는 데이터 파싱
    data = soup.find_all("tr", class_="GMDataRow")
    for i in range(len(data)//2):
        tds = data[i].find_all("td")
        thesis_name = tds[-1].string
        print(f"{i}: {thesis_name}")
    while(True):
        pass


iris_login()
