from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element_by_name("q")
# 검색하고싶은거 넣는곳
elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 브라우저 스크롤을 끝까지 내리겠다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 로딩될때동안 기다리는시간
    time.sleep(SCROLL_PAUSE_TIME)

    # 스크롤이 끝까지 내려가서 더나올게 없다할때 break
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_css_selector(
            ".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "아이유" + str(count) + ".jpg")
        count += 1
    except:
        pass
    # 사진 다운로드 제한갯수
    if(count == 110):
        break

driver.close()
