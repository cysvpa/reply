"""
    html에서 target을 분리해 내도록 한다.
    target : 댓글
    사용 : beautifulsoup사용
    input : html
    output : txt파일
"""
from bs4 import BeautifulSoup

def parse_comment(html,RESULT_TXT):
    element = BeautifulSoup(html,'lxml')
    txtFile = open(RESULT_TXT,"w",encoding="UTF-8")

    # 댓글만을 추출
    for title in element.find_all("yt-formatted-string",{"id":"content-text"}):
        text = title.get_text()
        txtFile.writelines(text)
        txtFile.writelines('\n')
    txtFile.close()


def parse_intro(html, RESULT_TXT):
    element = BeautifulSoup(html, 'lxml')
    txtFile = open(RESULT_TXT, "w", encoding="UTF-8")

    txtFile.write("영상 제목 :  ")
    text = element.find("yt-formatted-string", {"class": "style-scope ytd-video-primary-info-renderer"})
    txtFile.writelines(text)
    txtFile.writelines('\n')

    txtFile.write("조회수 :  ")
    text = element.find("span", {"class": "view-count style-scope yt-view-count-renderer"})
    txtFile.writelines(text)
    txtFile.writelines('\n')

    txtFile.write("총 댓글 수 :  ")
    text = element.find("yt-formatted-string", {"class": "count-text style-scope ytd-comments-header-renderer"})
    txtFile.writelines(text)
    txtFile.writelines('\n')
    txtFile.close()