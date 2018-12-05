"""
    유튜브 댓글(영문)을 스크래핑
    txt파일 형태 저장
    형태소 분석

"""

from time import time
from autoscroll_scraping import scrap
from parsing_html import parse_comment
from parsing_html import parse_intro

timmer = time()

TARGET_URL = "https://www.youtube.com/watch?v=BcXwZEbOvpo"

html=scrap(TARGET_URL)
parse_intro(html,"intro.txt")
parse_comment(html,"comment.txt")

print(time()-timmer)