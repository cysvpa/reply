"""
    웹 드라이버(chrome)을 사용하여 javascript형식의 페이지를
    끝 까지 스크롤 하여 모든 댓글을 읽을 수 있도록 한다.
    input : 유튜브 url
    output : 전체 펼쳐진 html정보

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scrap(TARGET_URL):
    #웹 드라이버 프로그램 필수 설치, 크롬으로 설정함
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--mute-audio")
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument('disable_infobars')
    driver = webdriver.Chrome(options=options)

    #동적 형식의 유튜브, 마지막까지 자동 스크롤
    driver.get(TARGET_URL)
    driver.get_screenshot_as_file(TARGET_URL+".png")
    time.sleep(2)

    # Get scroll height
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    while True:

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height

        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(3)
    html = driver.page_source
    driver.close()
    return html
